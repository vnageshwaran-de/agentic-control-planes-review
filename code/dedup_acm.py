import csv, re
from collections import defaultdict, Counter
from acm_records import RECORDS

def norm(d):
    if not d: return ""
    d=d.strip().lower()
    d=re.sub(r'^https?://(dx\.)?doi\.org/','',d)
    return d

# --- ACM unique by DOI, aggregate cluster membership ---
acm=defaultdict(lambda:{"clusters":set(),"year":"","title":""})
for cl,doi,yr,title in RECORDS:
    k=norm(doi)
    acm[k]["clusters"].add(cl)
    acm[k]["year"]=yr
    if len(title)>len(acm[k]["title"]): acm[k]["title"]=title
print("ACM raw rows:",len(RECORDS),"| ACM unique DOIs:",len(acm))

# --- OpenAlex DOI set ---
oa=set()
with open("openalex_harvest.csv") as f:
    for row in csv.DictReader(f):
        n=norm(row.get("doi",""))
        if n: oa.add(n)
print("OpenAlex unique DOIs:",len(oa))

overlap=[k for k in acm if k in oa]
netnew=[k for k in acm if k not in oa]
print("ACM∩OpenAlex overlap:",len(overlap))
print("ACM net-new (not in OpenAlex):",len(netnew))

# net-new by cluster (an ACM doi may belong to several clusters)
nn_by_cl=Counter()
for k in netnew:
    for cl in acm[k]["clusters"]:
        nn_by_cl[cl]+=1
print("net-new by cluster:",dict(sorted(nn_by_cl.items(),key=lambda x:(len(x[0]),x[0]))))

# --- write acm_harvest.csv (all unique ACM) ---
def clsort(s): return ",".join(sorted(s,key=lambda c:int(c[1:])))
with open("acm_harvest.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["doi","year","clusters","in_openalex","title"])
    for k in sorted(acm,key=lambda k:(clsort(acm[k]["clusters"]),k)):
        w.writerow([k,acm[k]["year"],clsort(acm[k]["clusters"]),"yes" if k in oa else "no",acm[k]["title"]])

# --- write acm_netnew.csv ---
with open("acm_netnew.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["doi","year","clusters","title"])
    for k in sorted(netnew,key=lambda k:(clsort(acm[k]["clusters"]),k)):
        w.writerow([k,acm[k]["year"],clsort(acm[k]["clusters"]),acm[k]["title"]])
print("wrote acm_harvest.csv and acm_netnew.csv")
