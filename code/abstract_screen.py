#!/usr/bin/env python3
"""Abstract-level relevance screen for the multi-source corpus (Q1 mapping-review).
Applies the inclusion criteria to title+abstract text. Citations are NOT used to exclude.
Output: screening_log_multisource.csv with decision + reason, abstracts retained for audit.
"""
import csv,json,re
from collections import Counter

abs_by=json.load(open('abstracts.json'))
rows=list(csv.DictReader(open('openalex_ranked.csv')))  # has rank/citations/clusters/title

LLM=['llm','large language model','language model','agent','agentic','autonomous agent','multi-agent','foundation model','gpt','chatbot']
CONTRIB=['propose','present','introduce','we design','we build','we develop','framework','benchmark','dataset','system','architecture','protocol','method','approach','evaluation','empirical','taxonomy','survey','study','pipeline','toolkit','platform','analysis']
# cluster relevance vocabulary (control-plane concerns)
CLUSTER=['tool call','function call','tool invocation','tool use','retrieval-augmented','rag','graphrag','knowledge graph',
 'serving','inference','deployment','llmops','kubernetes','serverless','orchestration','multi-agent','coordination',
 'prompt injection','jailbreak','tool poisoning','security','attack','guardrail','model context protocol','mcp','a2a',
 'agent communication','interoperability','governance','policy','observability','tracing','telemetry','memory','planning','reasoning']
DOMAIN=['clinical','patient','medical diagnosis','radiolog','disease','power grid','voltage','distribution network',
 'autonomous driving','traffic signal','agricultur','crop','manufacturing defect','welding','construction site',
 'wireless network','6g','base station','recommender system','e-commerce product','stock trading','credit risk',
 'education','student','classroom','intrusion detection','malware classification','fraud detection','game playing',
 'robot manipulation','drone','uav','vehicle','building energy','water treatment','fault diagnosis']
NONCONTRIB=['editorial','keynote','preface','erratum','retraction','table of contents','call for papers','panel discussion']

def screen(title,abstract):
    t=(title+' '+abstract).lower()
    if any(k in t for k in NONCONTRIB): return ('exclude','E7')
    if not any(k in t for k in LLM): return ('exclude','E8')  # not about LLM/agents
    cluster=any(k in t for k in CLUSTER)
    contrib=any(k in t for k in CONTRIB)
    dom=sum(1 for k in DOMAIN if k in t)
    # domain-dominant: strong vertical signal AND no cross-cutting control-plane method framing
    if dom>=1 and not cluster: return ('exclude','E6')
    if cluster and contrib: return ('include','')
    if cluster or contrib: return ('unsure','')
    return ('unsure','')

out=[]; c=Counter(); noabs=0
for r in rows:
    ab=abs_by.get(r['openalex_id'],'')
    if not ab: noabs+=1
    dec,code=screen(r['title'],ab)
    c[dec]+=1
    out.append([r['openalex_id'],r['doi'],r['year'],r['cited_by_count'],r['venue'],r['clusters'],dec,code,r['title'],'Y' if ab else 'N'])
with open('screening_log_multisource.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['openalex_id','doi','year','citations','venue','clusters','decision','reason_code','title','has_abstract'])
    w.writerows(out)
print("multi-source abstract screen:",dict(c),"| no-abstract:",noabs,"of",len(rows))
