import re,sys,csv
L=[l.rstrip() for l in open(sys.argv[1],encoding='utf-8') if l.strip()]
AM=re.compile(r'R\$ (-?[\d\.]+,\d\d)\s*$'); DT=re.compile(r'^\s*(\d\d)/(\d\d)/(\d{4})')
skip=re.compile(r'Saldo (inicial|final)|^\s*Data\s+Movim|ASAAS Gest|^CNPJ|^\s*CNPJ |Período|METAVERSO CONTABILIDADE$|Agência:')
out=[];used=set()
for i,l in enumerate(L):
    if skip.search(l): continue
    m=AM.search(l)
    if not m: continue
    v=float(m[1].replace('.','').replace(',','.'))
    d=DT.match(l); parts=[AM.sub('',DT.sub('',l)).strip()]
    def free(j): return 0<=j<len(L) and not AM.search(L[j]) and not skip.search(L[j]) and j not in used
    if not d:
        for j in (i+1,i-1):
            if free(j) and DT.match(L[j]): d=DT.match(L[j]); used.add(j); parts.append(DT.sub('',L[j]).strip()); break
    for j in (i-1,i+1):
        if free(j) and not DT.match(L[j]): used.add(j); parts.insert(0 if j<i else len(parts),L[j].strip())
    out.append(dict(banco='ASAAS',data=f'{d[3]}-{d[2]}-{d[1]}',descricao=' '.join(p for p in parts if p),valor=v,saldo=''))
print(len(out),round(sum(r['valor'] for r in out),2))
csv.DictWriter(open(sys.argv[2],'w',newline=''),fieldnames=list(out[0])).writerows(out)
