import urllib.request,urllib.parse,json,csv,time
key=__import__('os').environ.get('OPENALEX_KEY','')
ids=[r['openalex_id'].split('/')[-1] for r in csv.DictReader(open('openalex_harvest.csv'))]
def deinvert(inv):
    if not inv: return ''
    pos={}
    for w,ps in inv.items():
        for p in ps: pos[p]=w
    return ' '.join(pos[i] for i in sorted(pos))[:1200]
abs_by={}
for i in range(0,len(ids),50):
    batch='|'.join(ids[i:i+50])
    params={'filter':f'openalex_id:{batch}','per-page':50,'api_key':key,'select':'id,abstract_inverted_index'}
    url='https://api.openalex.org/works?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'User-Agent':'systematic-review-harvester/1.0'})
    for a in range(4):
        try:
            with urllib.request.urlopen(req,timeout=50) as r: d=json.load(r);break
        except Exception:
            if a==3: d={'results':[]}
            else: time.sleep(2)
    for w in d['results']: abs_by[w['id']]=deinvert(w.get('abstract_inverted_index'))
    if i % 1000==0: json.dump(abs_by,open('abstracts.json','w'))
json.dump(abs_by,open('abstracts.json','w'))
print("done",len(abs_by))
