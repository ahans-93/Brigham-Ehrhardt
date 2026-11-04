"""Validate curated v2 mapping and independent numerical examples, without network."""
from pathlib import Path
import json,math,re,sys
from urllib.parse import unquote
from verify_formula_review import evaluate

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'Brigham & Ehrhardt';V2=BASE/'kompilasi-v2'
rows=json.loads((V2/'pemetaan-197-rumus.json').read_text('utf8'))
add=json.loads((V2/'tambahan-kajian.json').read_text('utf8'))
assert [r['id'] for r in rows]==[f'V2-{i:03}' for i in range(1,198)]
assert len({r['id'] for r in rows})==197
assert len(add)==12
errors=[]
for r in rows:
    p,anchor=r['review_link'].split('#',1);target=V2/unquote(p)
    if not target.is_file() or f'id="{anchor}"' not in target.read_text('utf8'):
        errors.append({'id':r['id'],'broken_review_link':r['review_link']})

checks=[]
def check(name,value,expected):
    ok=math.isfinite(value) and math.isclose(value,expected,rel_tol=1e-7,abs_tol=1e-8)
    checks.append(dict(name=name,actual=value,expected=expected,status='PASS' if ok else 'FAIL'))
for x in add:check(x['id'],evaluate(x['calculation']),x['expected'])
def growing_pv(c,r,g,n):
    if r==g:return n*c/(1+r)
    return c*(1-((1+g)/(1+r))**n)/(r-g)
def direct(c,r,g,n):return sum(c*(1+g)**(t-1)/(1+r)**t for t in range(1,n+1))
check('Growing annuity PV against direct cash flows',growing_pv(100,.10,.05,3),direct(100,.10,.05,3))
check('Growing annuity FV against direct accumulation',growing_pv(100,.10,.05,3)*1.1**3,sum(100*1.05**(t-1)*1.1**(3-t) for t in range(1,4)))
check('Growing annuity r=g limit',growing_pv(100,.10,.10,3),direct(100,.10,.10,3))
check('Finite growing annuity permits g>r',growing_pv(100,.05,.10,3),direct(100,.05,.10,3))
check('FCF allocations reconciled to operations',15+10+20+30+25,150-50)
check('NAL positive-cost versus signed-cash convention',63.33-60.5,-60.5-(-63.33))
check('EAR differs from inflation-adjusted real rate',(1+.12/12)**12-1,.12682503013197)
check('Real rate applies Fisher to effective rate',(1+.12/12)**12/1.04-1,.083485605896125)
check('Residual distribution cannot be negative',max(0,20-.6*50),0)
check('Merger ownership value and share bases agree',40/140,(40*25)/(140*25))
check('IPO money left differs from spread costs',(12-10)*1000000,2000000)
check('Repurchase total payout yield equivalence',(1+.5)*.03+.04,(3+1.5)/100+.04)
check('Project CV inversion recovers original CV',math.sqrt(math.exp(math.log1p(.47**2))-1),.47)
check('Risk-free mixed-portfolio SD handles short market',abs(1-1.2)*.20,.04)
check('After-tax proceeds with positive basis',50-.25*(50-20),42.5)
check('NCF cash earnings do not subtract capex',60+20,80)
check('FCF subtracts reinvestment from NOPAT',100-30,70)
check('Annualized trade-credit nominal vs effective nonidentity',float((1+.02/.98)**(365/20)-1 > .02/.98*365/20),1)

for p in V2.rglob('*.md'):
    for uri in re.findall(r'\]\(([^)]+)\)',p.read_text('utf8')):
        if uri.startswith(('https:','http:','#')):continue
        if uri=='hasil-verifikasi.json' and '--write-report' in sys.argv:continue
        if not (p.parent/unquote(uri.split('#')[0])).exists():errors.append({'file':str(p.relative_to(ROOT)),'missing_target':uri})
report=dict(status='PASS' if not errors and all(c['status']=='PASS' for c in checks) else 'FAIL',mapped_entries=len(rows),new_supplemental_groups=len(add),annotated_entries=sum(r['integration_status']=='diberi penjelasan/koreksi' for r in rows),numeric_checks=len(checks),mapping_errors=errors,checks=checks)
if '--write-report' in sys.argv:(V2/'hasil-verifikasi.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=True))
for c in checks:
    if c['status']=='FAIL':print(json.dumps(c))
sys.exit(0 if report['status']=='PASS' else 1)
