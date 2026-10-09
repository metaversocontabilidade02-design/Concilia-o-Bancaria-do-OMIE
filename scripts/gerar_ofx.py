"""Gera arquivos OFX (SGML 1.02) para importar no Omie em
Finanças > Movimentação de Contas Correntes > Importar Extrato."""
import csv,hashlib,sys,re
from collections import Counter

def ofx(path,bankid,acct,rows,dtstart,dtend,balance=None,org='BANCO'):
    rows=sorted(rows,key=lambda r:r['data'])
    out=['OFXHEADER:100','DATA:OFXSGML','VERSION:102','SECURITY:NONE','ENCODING:UTF-8','CHARSET:NONE',
         'COMPRESSION:NONE','OLDFILEUID:NONE','NEWFILEUID:NONE','','<OFX>','<SIGNONMSGSRSV1>','<SONRS>',
         '<STATUS>','<CODE>0','<SEVERITY>INFO','</STATUS>','<DTSERVER>%s000000[-3:BRT]'%dtend.replace('-',''),
         '<LANGUAGE>POR','<FI>','<ORG>%s'%org,'<FID>%s'%bankid,'</FI>','</SONRS>','</SIGNONMSGSRSV1>',
         '<BANKMSGSRSV1>','<STMTTRNRS>','<TRNUID>1','<STATUS>','<CODE>0','<SEVERITY>INFO','</STATUS>',
         '<STMTRS>','<CURDEF>BRL','<BANKACCTFROM>','<BANKID>%s'%bankid,'<BRANCHID>1','<ACCTID>%s'%acct,
         '<ACCTTYPE>CHECKING','</BANKACCTFROM>','<BANKTRANLIST>',
         '<DTSTART>%s000000[-3:BRT]'%dtstart.replace('-',''),'<DTEND>%s000000[-3:BRT]'%dtend.replace('-','')]
    seen=Counter()
    for r in rows:
        v=float(r['valor']); memo=re.sub(r'[<>&"]','',r['descricao']).strip()[:250]
        key=f"{r['data']}|{v:.2f}|{memo}"; seen[key]+=1
        fitid=r.get('fitid') or hashlib.sha1(f'{acct}|{key}|{seen[key]}'.encode()).hexdigest()[:24]
        out+=['<STMTTRN>','<TRNTYPE>%s'%('CREDIT' if v>0 else 'DEBIT'),
              '<DTPOSTED>%s000000[-3:BRT]'%r['data'].replace('-',''),'<TRNAMT>%.2f'%v,
              '<FITID>%s'%fitid,'<MEMO>%s'%memo,'</STMTTRN>']
    out+=['</BANKTRANLIST>']
    if balance is not None:
        out+=['<LEDGERBAL>','<BALAMT>%.2f'%balance,'<DTASOF>%s000000[-3:BRT]'%dtend.replace('-',''),'</LEDGERBAL>']
    out+=['</STMTRS>','</STMTTRNRS>','</BANKMSGSRSV1>','</OFX>']
    open(path,'w',encoding='utf-8').write('\n'.join(out)+'\n')
    print(path,len(rows),'lançamentos, soma %.2f'%sum(float(r['valor']) for r in rows))

def faltantes(conc_csv):
    """Movimentos do banco que o cruzamento marcou como sem lançamento no Omie."""
    return [dict(data=r['data_banco'],descricao=r['descricao_banco'],valor=r['valor'])
            for r in csv.DictReader(open(conc_csv)) if r['status']=='BANCO_SEM_OMIE']

if __name__=='__main__':
    work,dest=sys.argv[1],sys.argv[2]
    banco=list(csv.DictReader(open(f'{work}/banco.csv')))
    inter=[r for r in banco if r['banco']=='INTER']
    # Inter: só o que falta (evita duplicar os 134 já conciliados), por ano para facilitar a importação
    falt=faltantes(f'{work}/conc_inter.csv')
    for ano in sorted({r['data'][:4] for r in falt}):
        rs=[r for r in falt if r['data'][:4]==ano]
        ofx(f'{dest}/INTER_faltantes_{ano}.ofx','077','83633677',rs,f'{ano}-01-01',max(r['data'] for r in rs),org='Banco Inter')
    # Inter completo (alternativa, caso prefira importar tudo e conciliar os pares na tela)
    ofx(f'{dest}/INTER_completo_2021-01_a_2026-04.ofx','077','83633677',inter,'2021-01-01','2026-04-27',balance=40.32,org='Banco Inter')
    # Cora 2026: só o que falta, mantendo o FITID original do OFX da Cora
    ofx_txt=open(f'{work}/../ext/cora.ofx',encoding='utf-8').read()
    orig=[]
    for b in re.findall(r'<STMTTRN>(.*?)</STMTTRN>',ofx_txt,re.S):
        g=lambda t:re.search(r'<%s>([^<\n]*)'%t,b).group(1).strip()
        d=g('DTPOSTED'); orig.append(dict(data=f'{d[:4]}-{d[4:6]}-{d[6:8]}',valor=g('TRNAMT'),fitid=g('FITID'),descricao=g('MEMO')))
    need=Counter((r['data'],round(float(r['valor']),2)) for r in faltantes(f'{work}/conc_cora_2026.csv'))
    sel=[]
    for o in orig:
        k=(o['data'],round(float(o['valor']),2))
        if need[k]>0: need[k]-=1; sel.append(o)
    assert sum(need.values())==0, need
    ofx(f'{dest}/CORA_faltantes_2026-01_a_2026-07.ofx','403','26371311',sel,'2026-01-01','2026-07-21',org='Cora SCD SA')
