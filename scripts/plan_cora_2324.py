import csv,re,json,unicodedata
from collections import Counter,defaultdict
CORA=4741279626
def norm(s): return re.sub(r'\s+',' ',re.sub(r'[^A-Z0-9 ]',' ',unicodedata.normalize('NFKD',s.upper()).encode('ascii','ignore').decode())).strip()
STOP=set('LTDA DE DA DO DOS E ME EPP SA EIRELI PIX TRANSF RECEBIDA ENVIADA ENVIADO RECEBIDO PAGAMENTO BOLETO PAGO COM PARA SERVICOS COMERCIO CP QR CODE PGTO TRANSFERENCIA DEBITO CONTA EFETUADO NULL VIA CHAVE API CONC GERADO AUTOMATICAMENTE PELA IMPORTACAO EXTRATO'.split())
def toks(s): return [t for t in norm(s).split() if len(t)>2 and t not in STOP and not t.isdigit()]
def who(desc):
    d=re.sub(r'Cp :\d+-','',desc); d=re.sub(r'\d{3,}[-/. ]?\d*','',d)
    return ' '.join(toks(d)[:3])
# histórico: aprovado pelo usuário (run.jsonl) tem peso maior que o histórico do Omie
hist=defaultdict(Counter)
for h in csv.DictReader(open('lanccc.csv')):
    if h['categ'].startswith('0.01'): continue
    k=who(h['obs'].split('|')[-1])
    if k: hist[(k,h['nat'])][h['categ']]+=1
for l in open('run.jsonl'):
    x=json.loads(l); c=x['detalhes']['cCodCateg']; k=who(x['detalhes']['cObs'].replace('| conc. API',''))
    if k: hist[(k,'R' if c[0]=='1' else 'P')][c]+=5
def classify(desc,v):
    u=norm(desc); nat='R' if v>0 else 'P'
    if 'CORA SCD' in u and nat=='R': return '1.03.26','credito/estorno Cora SCD (conferir)'
    if 'PAGAMENTO DA FATURA' in u or ('FATURA' in u and 'CORA' in u): return '2.01.99','regra usuario: fatura cartao'
    if re.search(r'LUANA PANTOJA|L P SILVA DE FARIAS',u): return ('2.03.99','socia: retirada (como no lote aprovado)') if nat=='P' else ('1.03.26','socia: devolucao (regra usuario)')
    if re.search(r'HAPVIDA',u): return '2.03.10','fornecedor: Hapvida'
    if re.search(r'THOMSON REUTERS',u) and nat=='P': return '2.04.99','fornecedor: sistema'
    k=who(desc.split(' - ',1)[-1])
    if (k,nat) in hist: return hist[(k,nat)].most_common(1)[0][0],'historico: '+k
    for (hk,hn),c in hist.items():
        if hn==nat and k and len(hk)>=8 and (hk.startswith(k[:12]) or k.startswith(hk[:12])): return c.most_common(1)[0][0],'historico (parcial): '+hk
    if re.search(r'MINISTERIO DA ECONOMIA|DAS SIMPLES|DARF',u): return '2.06.99','tabela: imposto (DAS)'
    if re.search(r'TARIFA|CORA PAGAMENTOS|SCFI',u) and nat=='P': return '2.05.04','tabela: tarifa'
    if nat=='R': return '1.01.02','tabela: recebimento de cliente'
    if re.search(r'PIX ENVIADA|PIX ENVIADO',u): return '2.03.97','tabela: pix para pessoa'
    return '?','sem regra'
P=[]
for y in ('2023','2024'):
    for r in csv.DictReader(open(f'conc_cora_{y}.csv')):
        if r['status']!='BANCO_SEM_OMIE': continue
        v=float(r['valor']); c,why=classify(r['descricao_banco'],v)
        P.append(dict(conta='CORA',nCodCC=CORA,data=r['data_banco'],valor=v,descricao=r['descricao_banco'],categoria=c,motivo=why,acao='INCLUIR' if c!='?' else 'REVISAR'))
w=csv.DictWriter(open('plano_cora_2324.csv','w',newline=''),fieldnames=list(P[0])); w.writeheader(); w.writerows(P)
print(len(P),Counter(p['categoria'] for p in P).most_common())
print(Counter(p['motivo'].split(':')[0] for p in P))
