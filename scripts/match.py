import csv,sys,datetime as dt
from collections import defaultdict
bank_name,omie_file,d0,d1,outp=sys.argv[1:6]
D=lambda s:dt.date.fromisoformat(s)
B=[r for r in csv.DictReader(open(sys.argv[6] if len(sys.argv)>6 else 'work/banco.csv')) if r['banco']==bank_name and d0<=r['data']<=d1]
O=[r for r in csv.DictReader(open(omie_file)) if d0<=r['data']<=d1]
for r in B: r['v']=round(float(r['valor']),2); r['m']=None
for r in O: r['v']=round(float(r['valor']),2); r['m']=None
real=[o for o in O if o['situacao']!='Previsto']; prev=[o for o in O if o['situacao']=='Previsto']
def run(pool,tol):
    idx=defaultdict(list)
    for o in pool:
        if o['m'] is None: idx[o['v']].append(o)
    for b in B:
        if b['m'] is not None: continue
        c=[o for o in idx[b['v']] if o['m'] is None and abs((D(o['data'])-D(b['data'])).days)<=tol]
        if c:
            o=min(c,key=lambda o:abs((D(o['data'])-D(b['data'])).days)); o['m']=b; b['m']=o
for tol in (0,3,10,35): run(real,tol)
for tol in (0,5,35): run(prev,tol)
# summaries
mb=[b for b in B if b['m'] is not None]; ub=[b for b in B if b['m'] is None]
uo=[o for o in real if o['m'] is None]
pm=[o for o in prev if o['m'] is not None]
print(f'{bank_name} {d0}..{d1}: banco {len(B)} tx soma {sum(b["v"] for b in B):.2f} | omie realizados {len(real)} soma {sum(o["v"] for o in real):.2f}')
print(f' casados com realizado: {sum(1 for b in mb if b["m"]["situacao"]!="Previsto")}; casados com PREVISTO (falta baixar): {len(pm)} soma {sum(o["v"] for o in pm):.2f}')
print(f' banco sem lançamento no omie: {len(ub)} soma {sum(b["v"] for b in ub):.2f}')
print(f' omie realizado sem movimento no banco: {len(uo)} soma {sum(o["v"] for o in uo):.2f}')
with open(outp,'w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['status','data_banco','descricao_banco','valor','data_omie','cliente_omie','situacao_omie','categoria_omie','cod_lanc_omie'])
    for b in B:
        o=b['m']
        if o is None: w.writerow(['BANCO_SEM_OMIE',b['data'],b['descricao'],b['v'],'','','','',''])
        else: w.writerow(['PREVISTO_A_BAIXAR' if o['situacao']=='Previsto' else ('OK_CONCILIADO' if o['situacao']=='Conciliado' else 'OK_A_CONCILIAR'),b['data'],b['descricao'],b['v'],o['data'],o['cliente'],o['situacao'],o['categoria'],o['cod']])
    for o in uo: w.writerow(['OMIE_SEM_BANCO','','',o['v'],o['data'],o['cliente'],o['situacao'],o['categoria'],o['cod']])
