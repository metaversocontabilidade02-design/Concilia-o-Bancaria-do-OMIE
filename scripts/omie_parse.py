import json,sys,csv
out=[];hdr=[]
for f in sys.argv[2:]:
    t=open(f).read(); d=json.loads(t[t.index('{'):])['resposta']
    hdr.append((d['cDescricao'],d['dPeriodoInicial'],d['dPeriodoFinal'],d['nSaldoAnterior'],d['nSaldoAtual'],d['nSaldoConciliado']))
    for m in d['listaMovimentos']:
        if not m.get('cSituacao'): continue
        dd,mm,yy=m['dDataLancamento'].split('/')
        out.append(dict(conta=d['cDescricao'],data=f'{yy}-{mm}-{dd}',valor=m['nValorDocumento'],situacao=m['cSituacao'],
          cliente=(m.get('cDesCliente') or m.get('cObservacoes','')[:50]).replace('&amp;','&'),categoria=m.get('cDesCategoria',''),
          origem=m.get('cOrigem',''),tipo=m.get('cTipoDocumento',''),numero=m.get('cNumero',''),cod=m['nCodLancamento'],
          dtconc=m.get('dDataConciliacao',''),obs=m.get('cObservacoes','')[:80]))
for h in hdr: print(h)
w=csv.DictWriter(open(sys.argv[1],'w',newline=''),fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out),Counter(r['situacao'] for r in out))
