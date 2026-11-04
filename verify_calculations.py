"""Recompute numerical examples; no network or nonstandard dependencies required."""
from pathlib import Path
import math,json

checks=[]
def check(name,actual,expected,tolerance=1e-5):
    assert abs(actual-expected)<=tolerance,(name,actual,expected)
    checks.append({'name':name,'actual':actual,'expected':expected,'tolerance':tolerance,'status':'PASS'})
def fv(p,r,n):return p*(1+r)**n
def fv_factor(r,n):return ((1+r)**n-1)/r
def pv_factor(r,n):return (1-(1+r)**-n)/r

# Original-source selected self-tests.
check('Ch2 ST1 net income',(5-1)*.6,2.4)
check('Ch2 ST1 NCF',(5-1)*.6+1,3.4)
check('Ch2 ST1 NOPAT',5*.6,3)
check('Ch2 ST1 NOWC',14-4,10)
check('Ch2 ST1 invested capital',14-4+15,25)
check('Ch2 ST1 FCF',3-(25-24),2)
check('Ch2 ST1 ROIC',3/25,.12)
check('Ch2 ST1 EVA',3-25*.1,.5)
check('Ch3 ST1 debt/assets',120/(150+210),1/3)
check('Ch3 ST1 debt/equity',120/210,4/7)
ar=40*14600/365;cl=(400+ar)/2;ca=3*cl;assets=ca+4300;equity=730/.125
check('Ch3 ST2 AR',ar,1600)
check('Ch3 ST2 CL',cl,1000)
check('Ch3 ST2 assets',assets,7300)
check('Ch3 ST2 equity',equity,5840)
check('Ch3 ST2 long-term debt',assets-cl-equity,460)
check('Ch3 ST2 DuPont',(730/14600)*(14600/assets)*(assets/equity),.125)
check('Ch4 ST1a FV',fv(1000,.08,3),1259.712)
check('Ch4 ST1b quarterly FV',fv(1000,.02,12),1268.24179456)
check('Ch4 ST1c FV annuity',250*fv_factor(.08,4),1126.528)
check('Ch4 ST1d PMT',fv(1000,.08,3)/fv_factor(.08,4),279.56,.005)
check('Ch4 ST2 single deposit',1000/1.08**3,793.83224102)
check('Ch4 ST2 PMT',1000/fv_factor(.08,4),221.92080445)
check('Ch4 ST2 year0 PV',1000/1.08**4,735.0298528)
check('Ch4 ST2 lump FV',750*1.08**3,944.784)
check('Ch4 ST2 rate',(1000/750)**(1/3)-1,.1006424163)
ear=(1+.08/4)**4-1;monthly_apr=12*((1+ear)**(1/12)-1)
check('Ch4 ST3 EAR',ear,.08243216)
check('Ch4 ST3 equivalent monthly APR',monthly_apr,.079472485,.000001)
bond=60*pv_factor(.05,50)+1000/1.05**50
check('Ch5 ST1 bond price',bond,1182.5592546)
check('Ch5 ST1 current yield',120/bond,.10147481,.0000001)
beta=sum(w*b for w,b in zip([.6,.25,.1,.05],[.7,.9,1.3,1.5]));newbeta=sum(w*b for w,b in zip([.5,.25,.1,.15],[.7,.9,1.3,1.5]))
check('Ch6 ST2 initial beta',beta,.85)
check('Ch6 ST2 new beta',newbeta,.93)
check('Ch6 ST2 initial CAPM',.06+.05*beta,.1025)
check('Ch6 ST2 new CAPM',.06+.05*newbeta,.1065)
g=(36*.12-2.4)/(36+2.4)
check('Ch7 ST1 growth',g,.05)
check('Ch7 ST1 future price',36*(1+g)**5,45.94613625)

# Additional guide examples, identified separately from textbook questions.
check('Guide WACC',.4*.07*.75+.6*.112,.0882)
check('Guide NPV',-100+sum(40/1.1**t for t in range(1,4)),-.5259203606)
check('Guide terminal PV',103/.07/1.1**5,913.64137536)
check('Guide bond price',80*pv_factor(.1,5)+1000/1.1**5,924.18426461)
check('Guide CCC',60+45-30,75)
check('Guide conversion ratio',1000/25,40)
check('Guide conversion value',(1000/25)*30,1200)

report={'scope':'Selected numerical examples only; not every textbook problem or formula','checks':checks,'passed':len(checks),'all_passed':True,'equivalent_monthly_apr_full_precision':monthly_apr}
target=Path(__file__).parent/'Brigham & Ehrhardt'/'calculation-checks.json'
target.write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({'checks':len(checks),'all_passed':True,'monthly_apr':monthly_apr}))
