import re,csv,sys,os
E=sys.argv[1]; O=sys.argv[2]
MES={m:i+1 for i,m in enumerate(['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'])}
def money(s):
    s=s.replace('R$','').replace(' ','')
    neg=s.startswith('-'); s=s.lstrip('-').replace('.','').replace(',','.')
    return -float(s) if neg else float(s)
rows=[]
# Inter
for f in ['ext_2021_2022.txt','ext_2023_2024.txt','ext_2025_2026.txt']:
    d=None; dayclose={}
    for line in open(os.path.join(E,f),encoding='utf-8'):
        m=re.match(r'\s*(\d{1,2}) de (\w+) de (\d{4}) Saldo do dia: (-?R\$ [\d\.,]+)',line)
        if m:
            d='%04d-%02d-%02d'%(int(m[3]),MES[m[2].lower()],int(m[1])); dayclose[d]=money(m[4]); continue
        m=re.match(r'\s*(\S.*?)\s{2,}(-?R\$ [\d\.,]+)\s{2,}(-?R\$ [\d\.,]+)\s*$',line)
        if m and d:
            rows.append(dict(banco='INTER',data=d,descricao=m[1].strip(),valor=money(m[2]),saldo=money(m[3])))
# Asaas
txt=open(os.path.join(E,'asaas_2025.txt'),encoding='utf-8').read().split('\n')
cur=None
for line in txt:
    m=re.match(r'\s*(\d\d)/(\d\d)/(\d{4})\s+(.*?)\s{2,}(R\$ -?[\d\.,]+)\s*$',line)
    if m:
        v=m[5].replace('R$ ','R$'); v=('-' if '-' in v else '')+v.replace('-','')
        cur=dict(banco='ASAAS',data=f'{m[3]}-{m[2]}-{m[1]}',descricao=m[4].strip(),valor=money(v),saldo='')
        rows.append(cur)
    elif cur and line.strip() and not re.search(r'Data|Movimenta|Saldo|Período|CNPJ|METAVERSO|gerado|Página',line) and line.startswith(' '*15):
        cur['descricao']+=' '+line.strip()
    elif not line.strip(): pass
    else: cur=None
# Cora
for r in csv.DictReader(open(os.path.join(E,'cora_2026.csv'),encoding='utf-8')):
    dd,mm,yy=r['Data'].split('/')
    rows.append(dict(banco='CORA',data=f'{yy}-{mm}-{dd}',descricao=(r['Transação']+' - '+r['Identificação'].strip()),valor=float(r['Valor']),saldo=''))
rows.sort(key=lambda r:(r['banco'],r['data']))
with open(O,'w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=['banco','data','descricao','valor','saldo']); w.writeheader(); w.writerows(rows)
from collections import defaultdict
agg=defaultdict(lambda:[0,0.0])
for r in rows: k=(r['banco'],r['data'][:4]); agg[k][0]+=1; agg[k][1]+=r['valor']
for k in sorted(agg): print(k,agg[k][0],round(agg[k][1],2))
