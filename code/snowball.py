import urllib.request,urllib.parse,json,csv,time
key=open('/home/claude/.openalex_key').read().strip()
seeds=[r['openalex_id'].split('/')[-1] for r in csv.DictReader(open('frozen_primary_final.csv')) if r['decision']=='include']
have=set(r['openalex_id'] for r in csv.DictReader(open('openalex_harvest.csv')))
def get(url):
    req=urllib.request.Request(url,headers={'User-Agent':'systematic-review-harvester/1.0'})
    for a in range(4):
        try:
            with urllib.request.urlopen(req,timeout=50) as r: return json.load(r)
        except Exception:
            if a==3: return {'results':[]}
            time.sleep(2)
# 1) collect referenced works of seeds
refs=set()
for i in range(0,len(seeds),50):
    b='|'.join(seeds[i:i+50])
    d=get('https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':f'openalex_id:{b}','per-page':50,'api_key':key,'select':'id,referenced_works'}))
    for w in d['results']:
        for rw in (w.get('referenced_works') or []): refs.add(rw)
    time.sleep(0.1)
new=[r.split('/')[-1] for r in refs if r not in have]
json.dump({'nrefs':len(refs),'nnew':len(new)},open('snowball_stats.json','w'))
# 2) fetch metadata for new refs, relevance-filter by title cluster terms
CL=['agent','llm','large language model','tool calling','function calling','retrieval-augmented','graphrag','rag',
 'serving','inference','llmops','orchestration','multi-agent','prompt injection','model context protocol','mcp',
 'a2a','interoperability','governance','observability','guardrail','memory','planning']
rows=[]
for i in range(0,len(new),50):
    b='|'.join(new[i:i+50])
    d=get('https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':f'openalex_id:{b}','per-page':50,'api_key':key,'select':'id,doi,title,publication_year,primary_location,cited_by_count'}))
    for w in d['results']:
        t=(w.get('title') or '').lower()
        if not any(k in t for k in CL): continue
        pl=(w.get('primary_location') or {}); src=(pl.get('source') or {})
        rows.append([w['id'],w.get('doi') or '',w.get('publication_year'),w.get('cited_by_count',0),src.get('display_name') or '',w.get('title') or ''])
    if i% 2000==0: 
        import csv as _c; _c.writer(open('snowball_candidates.csv','w',newline='')).writerows([['openalex_id','doi','year','citations','venue','title']]+rows)
    time.sleep(0.1)
import csv as _c
w=_c.writer(open('snowball_candidates.csv','w',newline='')); w.writerow(['openalex_id','doi','year','citations','venue','title']); w.writerows(rows)
print("refs",len(refs),"new",len(new),"relevant_new",len(rows))
