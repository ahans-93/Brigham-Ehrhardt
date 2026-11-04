"""Reproduce curated examples and independent identities. Python standard library only."""
from pathlib import Path
import ast, json, math, sys

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'Brigham & Ehrhardt' / 'kajian-rumus'

def pvaf(r,n): return n if r == 0 else -math.expm1(-n*math.log1p(r))/r
def fvaf(r,n): return n if r == 0 else math.expm1(n*math.log1p(r))/r
def bond(c,f,y,n): return c*pvaf(y,n)+f/(1+y)**n
def pv_stream(cfs,r): return sum(c/(1+r)**t for t,c in enumerate(cfs,1))
def growing_pv_sum(c,g,r,n): return pv_stream([c*(1+g)**t for t in range(n)],r)
def root(fn,lo=-.999,hi=1.):
    flo=fn(lo)
    while flo*fn(hi)>0 and hi<1e6: hi=2*hi+1
    if flo*fn(hi)>0: raise ValueError('No bracketed root; may have no unique financial solution')
    for _ in range(200):
        mid=(lo+hi)/2
        if flo*fn(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2
def ytm(p,c,f,n): return root(lambda y:bond(c,f,y,n)-p)
def irr(cfs): return root(lambda r:sum(c/(1+r)**t for t,c in enumerate(cfs)))
def mirr(cfs,finance,reinvest):
    n=len(cfs)-1
    cost=-sum(c/(1+finance)**t for t,c in enumerate(cfs) if c<0)
    terminal=sum(c*(1+reinvest)**(n-t) for t,c in enumerate(cfs) if c>0)
    if n<1 or cost<=0 or terminal<=0:raise ValueError('MIRR requires positive cost and terminal value')
    return (terminal/cost)**(1/n)-1
def cdf(z):return .5*(1+math.erf(z/math.sqrt(2)))
def bs_call(s,k,r,t,v):
    if t==0:return max(s-k,0)
    if v==0:return max(s-k*math.exp(-r*t),0)
    d1=(math.log(s/k)+(r+v*v/2)*t)/(v*math.sqrt(t));d2=d1-v*math.sqrt(t)
    return s*cdf(d1)-k*math.exp(-r*t)*cdf(d2)
def corr(xs,ys):
    xm=sum(xs)/len(xs);ym=sum(ys)/len(ys)
    return sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/math.sqrt(sum((x-xm)**2 for x in xs)*sum((y-ym)**2 for y in ys))

ENV={k:v for k,v in globals().copy().items() if k in ['pvaf','fvaf','bond','pv_stream','growing_pv_sum','ytm','irr','mirr','cdf','bs_call','corr']}
ENV.update(sqrt=math.sqrt,log=math.log,exp=math.exp,abs=abs,max=max,min=min)
ALLOWED=(ast.Expression,ast.Constant,ast.BinOp,ast.UnaryOp,ast.Call,ast.Name,ast.Load,ast.List,ast.Tuple,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.Pow,ast.USub,ast.UAdd)
def evaluate(expression):
    tree=ast.parse(expression,mode='eval')
    for node in ast.walk(tree):
        if not isinstance(node,ALLOWED):raise ValueError('Disallowed expression syntax')
        if isinstance(node,ast.Name) and node.id not in ENV:raise ValueError('Unknown calculation helper')
        if isinstance(node,ast.Call) and not isinstance(node.func,ast.Name):raise ValueError('Only named helpers allowed')
    return eval(compile(tree,'<curated arithmetic>','eval'),{'__builtins__':{}},ENV)

def verify(notes,locations):
    results=[]
    def check(name,value,expected,rel=1e-7,ab=1e-8):
        ok=math.isfinite(value) and math.isclose(value,expected,rel_tol=rel,abs_tol=ab)
        results.append(dict(name=name,actual=value,expected=expected,status='PASS' if ok else 'FAIL'))
    for entry in notes:
        check(entry['number'],evaluate(entry['calculation']),entry['expected'])
    ids=[x['number'] for x in notes if not x['number'].startswith('U-')]
    expected={x['label'].strip('()') for x in locations}
    coverage=dict(unique_numbered=len(set(ids)),display_locations=len(locations),missing=sorted(expected-set(ids)),unexpected=sorted(set(ids)-expected),duplicates=len(ids)-len(set(ids)))
    # Independent sums, reverse transformations, and limits supplement individual worked cases.
    check('PV annuity vs direct sum',100*pvaf(.08,12),sum(100/1.08**t for t in range(1,13)))
    check('FV annuity vs direct sum',100*fvaf(.08,12),sum(100*1.08**t for t in range(12)))
    check('Zero-interest annuity limit',pvaf(0,12),12)
    check('Due timing vs explicit sum',100*pvaf(.08,12)*1.08,sum(100/1.08**t for t in range(12)))
    check('Bond annuity vs direct cash flows',bond(60,1000,.07,10),pv_stream([60]*9+[1060],.07))
    check('Yield inversion',ytm(bond(60,1000,.07,10),60,1000,10),.07)
    check('IRR NPV residual',sum(c/(1+irr([-100,40,50,60]))**t for t,c in enumerate([-100,40,50,60])),0)
    q=(1.05-.8)/(1.2-.8)
    check('Discounted state prices sum',q/1.05+(1-q)/1.05,1/1.05)
    check('Binomial replication vs risk-neutral value',.5*100-40/1.05,(q*20+(1-q)*0)/1.05)
    call=bs_call(100,100,.05,1,.2);d1=.35;d2=.15
    put=100*math.exp(-.05)*cdf(-d2)-100*cdf(-d1)
    check('Put-call parity',call-put,100-100*math.exp(-.05))
    check('Hamada reverse transformation',(0.8*(1+.75*.5))/(1+.75*.5),.8)
    check('CAPV beta inverse with risky debt',.7*(.8+(.8-.2)*(.3/.7))+.3*.2,.8)
    # Zero growth and fixed debt: MM APV and matching after-tax WACC agree.
    vu=100/.10;d=200;t=.25;vl=vu+t*d;e=vl-d
    re=.10+(.10-.06)*(1-t)*d/e;wacc=e/vl*re+d/vl*.06*(1-t)
    check('MM APV vs WACC same assumptions',100/wacc,vl)
    # Minimum variance first-order condition and neighboring feasible portfolios.
    a,b,rho=.2,.1,0;w=b*b/(a*a+b*b)
    var=lambda x:x*x*a*a+(1-x)**2*b*b+2*x*(1-x)*rho*a*b
    check('Minimum variance derivative',2*w*(a*a+b*b)-2*b*b,0)
    check('Minimum variance beats neighbors',float(var(w)<var(w-.01) and var(w)<var(w+.01)),1)
    check('Printed adjusted beta fixed-point diagnostic',.67*1+.35,1.02)
    check('Convex adjusted beta fixed point',.67*1+.33,1)
    check('Lognormal CV inverse',math.sqrt(math.exp(math.log1p(.47**2))-1),.47)
    passed=all(x['status']=='PASS' for x in results) and not any(coverage[k] for k in ['missing','unexpected','duplicates'])
    return dict(status='PASS' if passed else 'FAIL',checks=len(results),coverage=coverage,results=results)

if __name__=='__main__':
    notes=json.loads((DATA/'formula-review.json').read_text('utf8'))
    locations=json.loads((DATA/'equation-locations.json').read_text('utf8'))
    report=verify(notes,locations)
    print(json.dumps({k:v for k,v in report.items() if k!='results'},ensure_ascii=True))
    for item in report['results']:
        if item['status']=='FAIL': print(json.dumps(item))
    if '--write-report' in sys.argv:(DATA/'verification-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    sys.exit(0 if report['status']=='PASS' else 1)
