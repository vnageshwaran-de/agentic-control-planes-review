import csv
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
FONT='Arial'

rows=list(csv.DictReader(open('acm_netnew.csv')))  # doi,year,clusters,title

E7_KEYS=['preface','acknowledgments',"authors' biography",'index','epilogue',
         'introduction to the maci','a brief history of ai','session summary podcast']
def presort(r):
    t=r['title'].lower(); y=r['year']
    if y<'2019' or y>'2026': return ('E8','struck','out-of-window (pre-2019 false match)')
    for k in E7_KEYS:
        if k in t: return ('E7','struck','front/back matter or non-contribution')
    if r['doi'].startswith('10.1145/3749421.'): return ('','screen','edited-volume chapter (10.1145/3749421.*) — include book chapters or not?')
    return ('','screen','standalone recent paper — likely in-scope, confirm')

for r in rows:
    code,status,note=presort(r); r['pre_code']=code; r['pre_status']=status; r['pre_note']=note
# order: screen rows first (standalone, then chapters), then struck
def sortkey(r):
    if r['pre_status']=='screen':
        return (0, 0 if 'standalone' in r['pre_note'] else 1, r['clusters'], r['doi'])
    return (1, 0 if r['pre_code']=='E8' else 1, r['doi'])
rows.sort(key=sortkey)
n_screen=sum(1 for r in rows if r['pre_status']=='screen')
n_struck=len(rows)-n_screen

wb=Workbook()
# ---- Instructions ----
ins=wb.active; ins.title='Instructions'; ins.column_dimensions['A'].width=114
def P(ws,cell,v,sz=10,b=False,wrap=True):
    c=ws[cell]; c.value=v; c.font=Font(name=FONT,size=sz,bold=b); c.alignment=Alignment(wrap_text=wrap,vertical='top'); return c
P(ins,'A1','ACM Digital Library net-new — second-rater screening (control-plane mapping review)',14,True)
lines=[
 '',
 'WHAT THIS IS',
 'ACM DL was run as an independent SECOND primary database (same 13 title-scoped clusters as OpenAlex). It returned',
 f'278 unique records; 250 (90%) were already in our OpenAlex set. These {len(rows)} are the NET-NEW records (absent from',
 'OpenAlex and the snowball set). We screen them under the SAME inclusion criteria as every other tier.',
 '',
 'WHAT IS ALREADY DONE (do not re-litigate unless you disagree)',
 f'A pre-sort struck {n_struck} records on structural grounds only: 7 are front/back matter or a podcast summary (E7,',
 'contribution) and 1 is a 2010 paper outside the 2019-2026 window (E8). They sit at the BOTTOM of the Review tab,',
 'greyed, with FINAL already filled. Flip one only if you think the pre-sort is wrong.',
 '',
 f'WHAT NEEDS YOU: the top {n_screen} rows (white) — TITLE + DOI link screening',
 '1. Read the Title; open the DOI link for the abstract/full text (we have no stored abstracts for these ACM items).',
 '2. Fill YOUR columns with the dropdowns: Reviewer 1 -> R1 decision / R1 code; Reviewer 2 -> R2 decision / R2 code.',
 '3. Agree? fills automatically; reconcile every CHECK together into FINAL decision / FINAL code.',
 '',
 'THE ONE REAL JUDGMENT CALL',
 '15 of the net-new are CHAPTERS of a single ACM edited volume, "Multi-LLM Agent Collaborative Intelligence"',
 '(DOI stem 10.1145/3749421.*) — CRIT, SocraSynth, EVINCE, SagaLLM, CoCoMo, the MACI framework, etc. The question is',
 'policy, not per-paper: do we INCLUDE edited-book chapters in the mapping sample, or exclude the whole volume as a',
 'book (E7)? Decide the policy once and apply it to all 15 consistently. The Pre-sort note column flags each one.',
 'The remaining 5 (SensorMCP, PVDetector, SkyMind, Invisible Walls in Cities, Evaluating Kubernetes Performance) are',
 'ordinary recent papers OpenAlex has not indexed yet — screen them as usual.',
 '',
 'DECISION RULE (same as all prior tiers; screen on RELEVANCE)',
 'INCLUDE if the primary contribution is a generalizable control-plane artifact — method, system, benchmark, dataset,',
 'protocol, reference architecture, evaluation, taxonomy, or security analysis — for LLM/agentic systems, addressing',
 '>=1 cluster. EXCLUDE with a code: E6 out-of-scope / single-domain application; E7 not a contribution (book/keynote/',
 'editorial/tutorial/front-matter); E3 duplicate; E8 wrong language/year. ESCALATE only if title+DOI cannot settle it.',
 '',
 f'WORKFLOW: both rate all {n_screen} white rows independently; the Summary tab computes Cohen kappa live over what',
 'scored, and counts the CHECK rows left to reconcile and the FINAL include/exclude tally.',
]
for i,ln in enumerate(lines,start=2):
    P(ins,f'A{i}',ln,10,b=(ln.isupper() and len(ln)>3))

# ---- Review ----
rv=wb.create_sheet('Review')
headers=['#','Year','Clusters','Title','DOI','Pre-sort','Pre-sort note',
         'R1 decision','R1 code','R1 notes','R2 decision','R2 code','R2 notes','Agree?','FINAL decision','FINAL code','Final notes']
widths=[4,6,9,60,10,9,40,11,8,20,11,8,20,9,13,9,22]
hdr=PatternFill('solid',fgColor='1F4E78')
for j,h in enumerate(headers,1):
    c=rv.cell(1,j,h); c.font=Font(name=FONT,size=10,bold=True,color='FFFFFF')
    c.fill=hdr; c.alignment=Alignment(wrap_text=True,vertical='center',horizontal='center')
for j,w in enumerate(widths,1): rv.column_dimensions[get_column_letter(j)].width=w
rv.freeze_panes='A2'
thin=Side(style='thin',color='D9D9D9'); border=Border(left=thin,right=thin,top=thin,bottom=thin)
grey=PatternFill('solid',fgColor='EFEFEF')
last=len(rows)+1
for i,r in enumerate(rows,start=2):
    struck=(r['pre_status']=='struck')
    rv.cell(i,1,i-1).font=Font(name=FONT,size=9,color='808080')
    rv.cell(i,2,r['year']).font=Font(name=FONT,size=10)
    rv.cell(i,3,r['clusters']).font=Font(name=FONT,size=9)
    tc=rv.cell(i,4,r['title']); tc.font=Font(name=FONT,size=10); tc.alignment=Alignment(wrap_text=True,vertical='top')
    doi=r['doi']
    lk=rv.cell(i,5,'DOI'); lk.hyperlink=f'https://doi.org/{doi}'; lk.font=Font(name=FONT,size=10,color='0563C1',underline='single')
    rv.cell(i,6,r['pre_code'] or ('screen' if not struck else '')).font=Font(name=FONT,size=9,bold=struck)
    nc=rv.cell(i,7,r['pre_note']); nc.font=Font(name=FONT,size=9); nc.alignment=Alignment(wrap_text=True,vertical='top')
    if struck:
        # pre-fill FINAL = exclude with code; grey the row
        rv.cell(i,15,'exclude').font=Font(name=FONT,size=10)
        rv.cell(i,16,r['pre_code']).font=Font(name=FONT,size=10)
        rv.cell(i,17,'pre-sort (structural); flip only if wrong').font=Font(name=FONT,size=9,color='808080')
        for j in range(1,18): rv.cell(i,j).fill=grey
    ag=rv.cell(i,14); ag.value=f'=IF(AND(H{i}<>"",K{i}<>""),IF(H{i}=K{i},"yes","CHECK"),"")'
    ag.font=Font(name=FONT,size=10,bold=True); ag.alignment=Alignment(horizontal='center')
    for col in (8,9,10,11,12,13,15,16,17): rv.cell(i,col).border=border
    rv.row_dimensions[i].height=46
dvd=DataValidation(type='list',formula1='"include,exclude,escalate"',allow_blank=True)
dvc=DataValidation(type='list',formula1='"E3,E6,E7,E8"',allow_blank=True)
rv.add_data_validation(dvd); rv.add_data_validation(dvc)
dvd.add(f'H2:H{last}'); dvd.add(f'K2:K{last}'); dvd.add(f'O2:O{last}')
dvc.add(f'I2:I{last}'); dvc.add(f'L2:L{last}'); dvc.add(f'P2:P{last}')

# ---- Summary ----
sm=wb.create_sheet('Summary'); sm.column_dimensions['A'].width=46
for c in ('B','C'): sm.column_dimensions[c].width=12
def S(cell,v,b=False): sm[cell]=v; sm[cell].font=Font(name=FONT,size=10,bold=b)
S('A1','Live summary - ACM net-new screening',True)
S('A2',f'{len(rows)} net-new records: {n_screen} to screen (white) + {n_struck} pre-struck E7/E8 (grey)')
r1=f'Review!$H$2:$H${last}'; r2=f'Review!$K$2:$K${last}'
S('A4','R1 include'); sm['B4']=f'=COUNTIF({r1},"include")'
S('A5','R1 exclude'); sm['B5']=f'=COUNTIF({r1},"exclude")'
S('A6','R2 include'); sm['B6']=f'=COUNTIF({r2},"include")'
S('A7','R2 exclude'); sm['B7']=f'=COUNTIF({r2},"exclude")'
S('A9','both scored (inc/exc)'); sm['B9']=f'=SUMPRODUCT((({r1}="include")+({r1}="exclude"))*(({r2}="include")+({r2}="exclude")))'
S('A10','agreements'); sm['B10']=f'=SUMPRODUCT((({r1}="include")*({r2}="include"))+(({r1}="exclude")*({r2}="exclude")))'
S('A11','observed Po'); sm['B11']='=IF(B9>0,B10/B9,"")'; sm['B11'].number_format='0.0%'
S('A12','R1 P(include)'); sm['B12']=f'=IF(B9>0,SUMPRODUCT((({r1}="include"))*(({r2}="include")+({r2}="exclude")))/B9,"")'; sm['B12'].number_format='0.0%'
S('A13','R2 P(include)'); sm['B13']=f'=IF(B9>0,SUMPRODUCT((({r2}="include"))*(({r1}="include")+({r1}="exclude")))/B9,"")'; sm['B13'].number_format='0.0%'
S('A14','expected Pe'); sm['B14']='=IF(B9>0,B12*B13+(1-B12)*(1-B13),"")'; sm['B14'].number_format='0.0%'
S('A15',"Cohen's kappa",True); sm['B15']='=IF(AND(B9>0,B14<1),(B11-B14)/(1-B14),"")'; sm['B15'].number_format='0.00'; sm['B15'].font=Font(name=FONT,size=11,bold=True)
S('A17','CHECK rows to reconcile'); sm['B17']=f'=COUNTIF(Review!$N$2:$N${last},"CHECK")'
S('A18','FINAL include (all rows)'); sm['B18']=f'=COUNTIF(Review!$O$2:$O${last},"include")'
S('A19','FINAL exclude (all rows)'); sm['B19']=f'=COUNTIF(Review!$O$2:$O${last},"exclude")'
S('A20','  of which pre-struck E7/E8'); sm['B20']=f'={n_struck}'

wb.save('coauthor_review_acm_netnew.xlsx')
print(f'wrote coauthor_review_acm_netnew.xlsx: {len(rows)} rows ({n_screen} screen + {n_struck} struck)')
