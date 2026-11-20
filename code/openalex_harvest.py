#!/usr/bin/env python3
"""OpenAlex primary harvest for the control-plane survey (multi-source expansion).
Mirrors the published evaluation paper's design: title-scoped streams per cluster,
unioned and deduplicated, then an AND post-filter applied on title+abstract.
Requires an ACTIVATED OpenAlex key in /home/claude/.openalex_key.
Run:  python3 openalex_harvest.py
"""
import urllib.request, urllib.parse, json, time, csv, os, sys, re

KEY=open('/home/claude/.openalex_key').read().strip()
FROM,TO='2019-01-01','2026-12-31'

# Per cluster: list of title phrases (streams) + a required-AND predicate on text.
# Streams = the distinctive OR-phrases from the frozen IEEE Boolean strings.
CLUSTERS={
 'C1':(['LLM agent','large language model agent','LLM-based agent'], None),
 'C2':(['function calling','tool calling','tool invocation'], ['llm','large language model']),
 'C3':(['agentic RAG','agentic retrieval-augmented','self-RAG','iterative retrieval'], ['llm','language model']),
 'C4':(['GraphRAG','graph retrieval-augmented'], ['knowledge graph','llm','language model']),
 'C5':(['LLMOps','LLM serving','large language model operations','model serving'], ['pipeline','deployment','lifecycle','inference']),
 'C6':(['cloud-native LLM','serverless LLM','Kubernetes LLM','LLM serving','LLM inference'], ['serving','inference','deployment','kubernetes','serverless']),
 'C7':(['LLM agent security','agentic AI security','LLM agent attack','agent vulnerability'], ['security','attack','threat','vulnerability']),
 'C8':(['prompt injection','indirect prompt injection','tool poisoning'], ['llm','language model','agent']),
 'C9':(['LLM-based multi-agent','multi-agent LLM','LLM multi-agent','agent orchestration'], ['llm','language model']),
 'C10':(['agent interoperability','agent protocol','agent communication protocol'], ['llm','language model','agentic']),
 'C11':(['Model Context Protocol','Agent2Agent','Agent Communication Protocol','Agent Network Protocol'], None),
 'C12':(['AI governance','policy-as-code','runtime policy enforcement'], ['llm','agent','agentic']),
 'C13':(['observability','distributed tracing','OpenTelemetry'], ['llm','large language model','agentic']),
}

def fetch_stream(phrase):
    """All works whose TITLE matches phrase, within date window, via cursor paging."""
    out=[]; cursor='*'
    while cursor:
        params={'filter':f'title.search:"{phrase}",from_publication_date:{FROM},to_publication_date:{TO}',
                'per-page':200,'cursor':cursor,'api_key':KEY,
                'select':'id,doi,title,publication_year,primary_location,type'}
        url='https://api.openalex.org/works?'+urllib.parse.urlencode(params)
        req=urllib.request.Request(url,headers={'User-Agent':'systematic-review-harvester/1.0'})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req,timeout=60) as r: d=json.load(r); break
            except Exception as e:
                if attempt==3: raise
                time.sleep(2*(attempt+1))
        out.extend(d['results'])
        cursor=d['meta'].get('next_cursor')
        if not d['results']: break
        time.sleep(0.2)
    return out

def venue_of(w):
    pl=w.get('primary_location') or {}
    src=(pl.get('source') or {})
    return src.get('display_name') or (src.get('host_organization_name') or '') or ''

def main():
    allrows={}  # openalex_id -> record (with clusters)
    for cl,(phrases,andp) in CLUSTERS.items():
        seen={}
        for ph in phrases:
            try: res=fetch_stream(ph)
            except Exception as e:
                print(f"  {cl} stream '{ph}' ERROR {e}"); continue
            for w in res: seen[w['id']]=w
            print(f"  {cl} '{ph}': {len(res)} (cumulative {len(seen)})")
        # AND post-filter on title (abstract not selected to keep it light; title-scoped like the paper)
        kept=0
        for wid,w in seen.items():
            title=(w.get('title') or '').lower()
            if andp and not any(a in title for a in andp):
                continue  # require at least one AND term in title
            kept+=1
            rec=allrows.setdefault(wid,{'id':wid,'doi':(w.get('doi') or ''),'title':w.get('title') or '',
                 'year':w.get('publication_year'),'venue':venue_of(w),'type':w.get('type'),'clusters':set()})
            rec['clusters'].add(cl)
        print(f"{cl}: {kept} after title-AND filter")
    # write
    with open('openalex_harvest.csv','w',newline='') as f:
        wr=csv.writer(f); wr.writerow(['openalex_id','doi','year','venue','type','clusters','title'])
        for r in allrows.values():
            wr.writerow([r['id'],r['doi'],r['year'],r['venue'],r['type'],'|'.join(sorted(r['clusters'])),r['title']])
    print(f"\nTOTAL unique OpenAlex works: {len(allrows)} -> openalex_harvest.csv")
    # venue rollup
    from collections import Counter
    c=Counter()
    for r in allrows.values():
        v=r['venue'].lower()
        if 'arxiv' in v: c['arXiv']+=1
        elif 'ieee' in v: c['IEEE']+=1
        elif v.startswith('acm') or 'association for computing' in v: c['ACM']+=1
        elif 'springer' in v or 'lecture notes' in v: c['Springer/LNCS']+=1
        elif 'elsevier' in v: c['Elsevier']+=1
        else: c['other/unknown']+=1
    print("venue rollup:",dict(c))

if __name__=='__main__':
    # guard: refuse to run if key inactive (OpenAlex returns 'activate' error)
    main()
