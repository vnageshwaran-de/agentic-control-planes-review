import csv, sys
DOMAIN = [
 'tax','withholding','real estate','food ordering','taxi','hotel','guest experience',
 'power grid','grid dispatch','distribution network','voltage','hydropower','wildfire',
 'water network','non-revenue water','optical network','6g network','telecom','base station',
 'vehicle','automotive','uav','ardupilot','aircraft','space habitat','orbit','satellite',
 'ecg','surgical','surgeon','cardiovascular','clinical','chest x-ray','cxr','medical','mental health','biomedical','iomt','diagnosis','disease','patient','drug','radiolog','patholog','cancer','healthcare','health care','nurs','psych',
 'bridge','phage','mineral','agricultur','crop','farming','geospatial','remote sensing','bidding','procurement',
 'game content','table tennis','sports','fake news','inventory management','erp','booking','restaurant',
 'intrusion detection','penetration testing','pentest','red-team','red team','threat hunt','blue team','malware','phishing','fraud detection',
 'smart contract','electromagnetic','gas turbine','gas path','parenting','tourism','travel',
 'readme generation','scrum','manufacturing','welding','construction','traffic','urban','transportation',
 'education','student','teaching','classroom','e-learning','curriculum','legal','court','law ','judicial','contract review',
 'finance','financial','investment','stock','trading','banking','accounting','insurance',
 'power system','energy system','battery','photovoltaic','solar','wind power','smart grid','microgrid',
 'water quality','environment','climate','weather','earthquake','flood','disaster',
 'robot','robotic','drone','autonomous driving','self-driving','navigation','manipulation',
 'recommendation system','recommender','e-commerce','advertis','marketing','sentiment',
 'speech','emotion recogn','face recogn','image classification','object detection','segmentation',
]
GENERIC_INCLUDE = [
 'function calling','function-calling','tool calling','tool-calling','tool invocation','tool use','tool-use',
 'tool execution','tool-augmented','tool definition','tool-maker','tool selection','multi-tool',
 'benchmark','evaluation framework','empirical evaluation','empirical study','taxonomy','dependability','reliability',
 'verification','runtime verification','guardrail','authorization','access control','protocol',
 'model context protocol',' mcp','mcp ','mcp-','a2a','agent-to-agent','agent2agent','specification framework',
 'caching','orchestration','planning','scheduling','reasoning framework','failure mode','failure taxonomy',
 'fuzzing','testing','prompt injection','poisoning','threat model','defense','jailbreak',
 'reference architecture','architecture for','design pattern','in-context learning',
 'observability','distributed tracing','opentelemetry','telemetry','monitoring framework',
 'governance','policy enforcement','policy-as-code','compliance','audit',
 'serving','inference serving','llmops','deployment','lifecycle','pipeline','mlops',
 'multi-agent','multiagent','agent orchestration','coordination','collaboration framework',
 'memory','context management','interoperability','survey','systematic review',
]
BOOK = ['building production ai agents','architectural patterns for building','proven design patterns','hands-on','o\'reilly','packt',': design and']
WORKSHOP = ['workshop','proceedings','front matter','keynote','special issue','table of contents']

def make_classify(extra_include):
    inc_terms = GENERIC_INCLUDE + [e.lower() for e in extra_include]
    def classify(title):
        t=title.lower()
        if any(b in t for b in BOOK): return ('exclude','E7','book')
        if any(w in t for w in WORKSHOP): return ('exclude','E7','frontmatter')
        inc=any(k in t for k in inc_terms)
        dom=any(d in t for d in DOMAIN)
        if inc and not dom: return ('include','inc','kw-include')
        if dom and not inc: return ('exclude','E6','kw-domain')
        if inc and dom: return ('unsure','U','method-in-domain')
        return ('unsure','U','no-signal')
    return classify

if __name__=='__main__':
    cluster=sys.argv[1]; infile=sys.argv[2]
    extra={'C4':['graphrag','graph retrieval','graph-based retrieval','knowledge graph','kg-rag','graph rag','retrieval-augmented','rag '],
           'C5':['llmops','llm serving','model serving','inference','deployment','pipeline','lifecycle','scaling','latency','throughput','gpu','quantization','batching'],
           'C8':['prompt injection','indirect prompt','tool poisoning','jailbreak','adversarial','attack','defense','injection','safety'],
           'C9':['multi-agent','multiagent','orchestration','coordination','collaboration','role','debate','workflow','planning','communication'],
           'C11':['model context protocol','mcp','a2a','agent2agent','agent communication','agent network protocol','protocol','interoperability','acp','anp'],
           'C12':['governance','policy','compliance','audit','guardrail','access control','authorization','accountability','regulation','risk management','assurance'],
           'C13':['observability','distributed tracing','opentelemetry','telemetry','monitoring','logging','metrics','debugging','trace','instrumentation'],
           'C1':['llm agent','agentic','autonomous agent','agent framework','agent architecture','reasoning','planning','tool','memory','react'],
           }.get(cluster,[])
    classify=make_classify(extra)
    rows=[r for r in csv.reader(open(infile),delimiter='\t') if len(r)>=3]
    from collections import Counter
    c=Counter();out=[]
    for docid,yr,title in [(r[0],r[1],r[2]) for r in rows]:
        d,code,why=classify(title); c[d]+=1; out.append([docid,yr,d,code,why,title])
    csv.writer(open(cluster+'_proposed.tsv','w',newline=''),delimiter='\t').writerows(out)
    print(cluster,'proposed:',dict(c),'total',len(out))
