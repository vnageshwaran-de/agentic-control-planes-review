import urllib.request,urllib.parse,json,csv,time
key=open('/home/claude/.openalex_key').read().strip()
ids=[r['openalex_id'].split('/')[-1] for r in csv.DictReader(open('openalex_harvest.csv'))]
cc={}
for i in range(0,len(ids),50):
    batch='|'.join(ids[i:i+50])
    params={'filter':f'openalex_id:{batch}','per-page':50,'api_key':key,'select':'id,cited_by_count'}
    url='https://api.openalex.org/works?'+urllib.parse.urlencode(params)
    req=urllib.request.Request(url,headers={'User-Agent':'systematic-review-harvester/1.0'})
    for a in range(4):
        try:
            with urllib.request.urlopen(req,timeout=40) as r: d=json.load(r);break
        except Exception as e:
            if a==3: d={'results':[]}
            else: time.sleep(2)
    for w in d['results']: cc[w['id']]=w['cited_by_count']
    if i % 1000==0:
        json.dump(cc,open('citations.json','w'))
json.dump(cc,open('citations.json','w'))
print("done",len(cc))
