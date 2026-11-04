# Chapter 23: Enterprise Risk Management

[Daftar isi](SUMMARY.md) · [Panduan belajar](KAJIAN.md)

Sumber: PDF halaman 948–983. Teks ekstraksi; simbol, tabel, dan rumus belum seluruhnya diverifikasi secara visual.

## Halaman PDF 948

```text
CHAPTER 23
Enterprise Risk Management
On April 13, 2012, JPMorgan Chase CEO Jamie Dimon called rumors of impending
trading losses a “tempest in a teapot.” As time passed, the losses exceeded $6 billion
and led to several criminal charges for hiding losses, making it a pretty big teapot!
Banks make loans to businesses, and JPMorgan is no exception. Many of its
borrowers were exposed to difficult global economic conditions, including the Euro￾zone crises, which in turn exposed JPMorgan to risk. To offset potential losses on
commercial lending, JPMorgan’s Chief Investment Office in London took short posi￾tions on selected indexes that would pay off if some large companies, including some
of their customers, defaulted on bank loans.1 This is a classic hedge—if borrowers
defaulted, JPMorgan’s commercial lending group would lose money, but the London
office would make money, and vice versa.
However, that is not the end of the story. The London office also took long
positions on derivatives based on a broader credit index, the CDX.NA.IG.9. (Long
positions meant that JPMorgan made commitments to buy at a fixed price.) Their
intentions were to reduce expenses but also to hedge their short positions in the
selected indexes, betting that the selected indexes were temporarily mispriced rela￾tive to the IG.9. JPMorgan continued to take long positions on the IG.9 during late
2011 and early 2012, until it became the biggest trader in this segment of the market.
In fact, it is likely that JPMorgan’s own trading activities artificially drove down the
IG.9’s price.
The low price of the IG.9 attracted hedge funds, and what goes down must come
up. As the IG.9 price increased, JPMorgan began to lose money on its long positions
and started liquidating some if its positions to prevent even bigger losses in the
future. Keep this episode in mind as you read the rest of the chapter.
1
These indexes were actually composed of credit default swaps, so JPMorgan was going short in a derivative
based on other derivatives.
911
© Panda3800/Shutterstock.com
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 949

```text
Defining risk management is simple: Identify events that could have adverse consequences
and then take actions to prevent or minimize the damage caused by these events. Applying
risk management is more difficult, but it is vital for a company’s success, and perhaps even
its survival. In this chapter we explain how risk management adds value to a corporation,
describe an enterprise risk management framework, identify different categories of risks,
explain how to measure selected risks, and show how to manage those risks.2 We also
illustrate how companies can use derivatives, which are securities whose values are
determined by the market price of some other asset, to manage certain types of risk.
23-1 Reasons to Manage Risk
Hedging is a risk management technique in which a company can reduce or eliminate its
exposure to a source of risk through the use of derivatives. But will reducing risk make a
company more valuable? Consider Plastic Inc., which manufactures dashboards, interior
door panels, and other plastic components used by auto companies. Petroleum is the key
feedstock for plastic and thus makes up a large percentage of its costs. Plastic has a 3-year
Corporate Valuation and Risk Management
All companies are exposed to risk from volatility in pro￾duct prices, demand, input costs, and other sources of
business risk, such as the risk stemming from the choice
of production technology. Many companies also are
exposed to risk from volatility in exchange rates and
interest rates. Risk management can reduce firm risk, pre￾venting catastrophes and leading to a lower cost of capi￾tal. In some instances, derivatives such as swaps can
reduce the effective interest rate paid by a corporation,
again reducing its cost of capital.
Net operating
profit aer taxes
Free cash flow
(FCF)
Product prices 
and demand
Input costs
Required investments
in operating capital
Foreign exchange rates
Market risk aversion Weighted average
cost of capital
(WACC)
Firm’s business risk
Firm’s debt/equity mix Market interest rates
–
=
Value = + … ++ FCF1 FCF∞
(1 + WACC)1
FCF2
(1 + WACC)2 (1 + WACC)∞
2
For excellent overviews of risk management, see Kenneth A. Froot, David S. Scharfstein, and Jeremy Stein,
“A Framework for Risk Management,” Journal of Applied Corporate Finance, Fall 1994, pp. 22–32; Brian Nocco
and Rene Stultz, “Enterprise Risk Management, Theory and Practice,” Journal of Applied Corporate Finance, Fall
2006, pp. 8–20; Walter Dolde, “The Trajectory of Corporate Financial Risk Management,” Journal of Applied
Corporate Finance, Fall 1993, pp. 33–41; and Marshall Blake and Nelda Mahady, “How Mid-Sized Companies
Manage Risk,” Journal of Applied Corporate Finance, Spring 1991, pp. 59–65.
resource
The textbook’s Web site
contains an Excel file
that will guide you
through the chapter’s
calculations. The file for
this chapter is Ch23 Tool
Kit.xlsx, and we
encourage you to open
the file and follow along
as you read the chapter.
912 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 950

```text
contract with an auto company to deliver 500,000 door panels each year at a price of $20
each. When the company recently signed this contract, oil sold for $100 per barrel and
was expected to stay at that level for the next 3 years. If oil prices fell during this time,
Plastic would have higher than expected profits and free cash flows, but if oil prices rose,
profits would fall. Because Plastic’s value depends on its profits and free cash flows, a
change in the price of oil would cause stockholders to earn either more or less than they
anticipated.
Now suppose that, shortly after signing the contract with its door panel supplier, Plastic
announces that it plans to lock in a 3-year supply of oil at a guaranteed price of $100 per
barrel and that the cost of this guarantee is zero. Would that cause its stock price to rise? At
first glance, it seems the answer should be “yes,” but that might not be correct. Recall that
the value of a stock depends on the present value of its expected future free cash flows,
discounted at the weighted average cost of capital (WACC). Locking in the cost of oil will
cause an increase in Plastic’s stock price if and only if it produces at least one of these two
results: (1) Expected future free cash flows increase. (2) The WACC declines.
Consider first the free cash flows. Before the announcement of guaranteed oil costs,
investors had formed an estimate of the expected future free cash flows based on an
expected oil price of $100 per barrel. Locking in the cost of oil at $100 per barrel will lower
the risk of the expected future free cash flows, but it might not change the expected size of
these cash flows because investors already expected a price of $100 per barrel. Of course,
smaller than expected cash flows can disrupt a firm’s operation and that disruption can, in
turn, adversely affect cash flows.
Now what about the WACC? It will change only if locking in the cost of oil causes a
change either in the cost of debt or equity or in the target capital structure. If the foreseeable
increases in the price of oil are not enough to increase the threat of bankruptcy, then
Plastic’s cost of debt should not change and neither should its target capital structure.
Regarding the cost of equity, recall from Chapter 6 that most investors hold well-diversified
portfolios, which means that the cost of equity should depend only on systematic risk.
Moreover, even though an increase in oil prices would have a negative effect on Plastic’s
stock price, it would not have a negative effect on all stocks. Indeed, oil producers should
have higher than expected returns and stock prices. Assuming that Plastic’s investors hold
well-diversified portfolios that include stocks of oil-producing companies, we should have
little reason to expect its cost of equity to decrease. The bottom line is this: If Plastic’s
expected future cash flows and WACC will not change significantly as a consequence of
eliminating the risk of oil price increases, then neither should the value of its stock.
We discuss futures contracts and hedging in detail in the next section, but for now
let’s assume that Plastic has not locked in oil prices. Therefore, if oil prices increase, its
stock price will fall. However, if its stockholders know this, they can build portfolios that
contain oil futures whose values will rise or fall with oil prices and thus offset changes in
the price of Plastic’s stock. By choosing the correct amount of futures contracts, investors
can thus “hedge” their portfolios and completely eliminate the risk due to changes in oil
prices. There will be a cost to hedging, but that cost to large investors should be about the
same as the cost to Plastic. Because stockholders can hedge away oil price risk themselves,
why should they pay a higher price for Plastic’s stock just because the company itself
hedged away that risk?
The previous points notwithstanding, companies clearly believe that active risk man￾agement is important. A 1998 survey reported that 83% of firms with market values
greater than $1.2 billion engage in risk management.3 A more recent 2005 survey of CFOs
3
See Gordon M. Bodnar, Gregory S. Hayt, and Richard C. Marston, “1998 Wharton Survey of Financial Risk
Management by U.S. Non-Financial Firms,” Financial Management, Winter 1998, pp. 70–91.
Chapter 23 Enterprise Risk Management 913
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 951

```text
reported that 90% of the international and domestic firms responding considered risk in
the planning process. The average of the estimates of the contribution that risk manage￾ment made to the market value of the firm was 3.8%.4 There are many reasons why
companies manage their risks.
1. Debt capacity. Risk management can reduce the volatility of cash flows, which
decreases the probability of bankruptcy. As we discussed in Chapter 15, firms with
lower operating risks can use more debt, and this can lead to higher stock prices due
to the interest tax savings.
2. Maintaining the optimal capital budget over time. Recall from Chapter 15 that firms
are reluctant to raise external equity because of high flotation costs and market
pressure. This means that the capital budget must generally be financed with a
combination of debt and internally generated funds. In bad years, internal cash
flows may be too low to support the optimal capital budget, causing firms to either
slow investment below the optimal rate or else incur the high costs associated with
external equity. By smoothing out the cash flows, risk management can alleviate this
problem. This issue is most relevant for firms with large growth opportunities. A
study by Professors Gerald Gay and Jouahn Nam found that such firms do in fact use
derivatives more than low-growth firms.5 Thus, maintaining an optimal capital
budget is an important determinant of firms’ risk management practices.
3. Financial distress. The stages of financial distress can range from stockholder concern
and higher interest rates on debt to customer defections and bankruptcy. Any serious
level of financial distress causes a firm to have lower cash flows than expected. Risk
management can reduce the likelihood of low cash flows and hence of financial
distress.
4. Comparative advantages in hedging. Most investors cannot hedge as efficiently as a
company. First, firms generally incur lower transaction costs because of their larger
volume of hedging activities. Second, there is the problem of asymmetric information:
Managers know more about the firm’s risk exposure than do outside investors, so
managers can create more effective hedges. And third, effective risk management
requires specialized skills and knowledge that firms are more likely to have.
5. Borrowing costs. As discussed later in the chapter, firms can sometimes reduce input
costs—especially the interest rate on debt—through the use of derivative instruments
called swaps. Any such cost reduction adds value to the firm.
6. Tax effects. The present value of taxes paid by companies with volatile earnings is
higher than the present value of taxes paid by stable companies; this is because of the
treatment of tax credits and the rules governing corporate loss carryforwards and
carrybacks. Moreover, if volatile earnings cause a company to declare bankruptcy,
then the company often will lose the value of its tax loss carryforwards. Therefore,
using risk management to stabilize earnings can reduce the present value of a
company’s tax burden.
7. Compensation systems. Many compensation systems establish “floors” and “ceilings”
on bonuses and also reward managers for meeting targets. To illustrate, suppose a
firm’s compensation system calls for a manager to receive no bonus if net income is
below $1 million, a bonus of $10,000 if income is between $1 million and $2 million,
or a bonus of $20,000 if income is $2 million or more. The manager will also receive
4
See Henri Servaes, Ane Tamayo, and Peter Tufano, “The Theory and Practice of Corporate Risk Management,”
Journal of Applied Corporate Finance, Fall 2009, pp. 60–78.
5
See Gerald D. Gay and Jouahn Nam, “The Underinvestment Problem and Corporate Derivatives Use,” Financial
Management, Winter 1998, pp. 53–69.
914 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 952

```text
an additional $10,000 if actual income is at least 90% of the forecasted level, which is
$1 million. Now consider the following two situations. First, if income is stable at
$2 million each year then the manager receives a $30,000 bonus each year, for a 2-year
total of $60,000. However, if income is zero the first year and $4 million the second, the
manager gets no bonus the first year and gets $30,000 the second, for a 2-year total of
$30,000. So, even though the company has the same total income ($4 million) over the 2
years, the manager’s bonus is higher if earnings are stable. Therefore, even if hedging
does not add much value for stockholders, it may still benefit managers.
There are regulatory and economically driven reasons to manage risk. The following
section describes a typical enterprise risk management framework.
SELF-TEST
Explain why finance theory, combined with well-diversified investors and “homemade
hedging,” might suggest that risk management should not add much value to a company.
List and explain some reasons companies might employ risk management techniques.
23-2 An Overview of Enterprise Risk Management
The practice of enterprise risk management has evolved considerably over the last 20 years,
due to advances in technology and regulatory changes. To better explain the framework for
enterprise risk management, we begin with a brief history of risk management.
One of the earliest used tools in risk management is a futures contract, which is an
agreement in which a buyer pledges to purchase a specific quantity of an item at a specific
price on a specific future date from a seller who has pledged to provide the item at the agreed￾upon terms. Written records show that commodity futures contracts were used and traded
more than 4,000 years ago in India, so risk management has been around a very long time. In
the United States, grain traders used futures contracts as far back as the early 1800s.6
The history of insurance also dates back hundreds of years, with maritime insurance
offered in Genoa in the 1300s and fire insurance offered in London in 1680, not long after
the Great Fire of London. In fact, Benjamin Franklin and the Union Fire Company began
a fire insurance company in 1752.
As the previous examples illustrate, commodity futures contracts and insurance have
been used worldwide for centuries. At the risk of oversimplification, not much new
happened until the 1970s, probably because several sources of risk (interest rates, currency
exchange rates, and oil prices) had been relatively stable, and perhaps because models for
options and other derivatives had not yet been developed. However, the 1970s saw the end
of the monetary gold standard (which dramatically increased foreign exchange rate
volatility), runaway inflation in the United States, and a reversal in bargaining power
between OPEC and oil companies during the Yom Kippur War between Egypt and Israel
in 1973. These events, combined with the acceleration of international competition,
exposed companies to much more risk than in the previous decades. In turn, these
sources of risk made stocks, bonds, and other investments much more volatile.
With the development of pricing models for derivatives, most companies began to
actively manage their exposures to interest rates, exchange rates, and a wide variety of
commodities. However, few companies employed a systematic approach to risk
6
For a thorough treatment of the history of enterprise risk management, see Betty Simkins and Steven A.
Ramirez, “Enterprise-Wide Risk Management and Corporate Governance,” Loyola University Chicago Law
Journal, Vol. 39, 2008, pp. 571–594.
Chapter 23 Enterprise Risk Management 915
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 953

```text
management. Instead, most companies had a risk management group in charge of
insurance-related issues, but different groups in charge of managing each of the other
specific risks. For example, one group might manage foreign exchange risk and another
might manage commodity risk.
The impetus for a more comprehensive and systematic approach to risk management
came from several sources, including corporate bribery scandals in the 1970s, the S&L
crisis in the early 1980s, the accounting scandals in the early 2000s (including Enron and
WorldCom), and the banking crisis in the late 2000s. All of these events had several
common factors, including accounting systems that lacked sufficient controls to identify
improper activities.
Regulators responded to each of these crises in an effort to assign blame and prevent
the next crisis. In 1977, Congress passed the Foreign Corrupt Practices Act (FCPA) to
prevent corporate bribery, and one of its provisions requires companies to have an
accounting system that can identify funds used for bribery. In the mid-1980s, a congres￾sional committee examined the S&L failures and found that some of the failed financial
institutions had fraudulent financial statements. In addition to criticizing accounting
standards, this committee hinted that Congress and the SEC would impose additional
regulatory controls if the accounting profession did not take actions to prevent similar
frauds. In 2002, Congress passed the Sarbanes-Oxley (SOX) Act to prevent accounting
scandals like those that occurred at Enron, Arthur Andersen, and Tyco. Section 404 of
SOX requires senior management to include a section in the annual report that addresses
the internal control system, including the system’s framework and an assessment of its
ability to detect fraud.
In response to stinging criticism from Congress, five major accounting organizations
formed the Committee of Sponsoring Organizations (COSO) and released several reports,
including one in 1992 that provided a framework for an internal control system designed
to prevent fraudulent accounting. The framework for the COSO accounting internal
control system satisfied the reporting requirements made by the Foreign Corrupt Prac￾tices Act (FCPA) and SOX, so many companies adopted the framework. In 2004, COSO
also issued a framework for enterprise risk management, which broadened the scope of
the original internal control framework. Because many companies were already using the
framework for internal controls, some adopted versions of the broader framework for
enterprise risk management. Today, the COSO framework and similar frameworks are
widely used.
COSO defines enterprise risk management (ERM) as follows:
Enterprise risk management is a process, effected by an entity’s board of directors, management
and other personnel, applied in strategy setting and across the enterprise, designed to identify
potential events that may affect the entity, and manage risk to be within its risk appetite, to
provide reasonable assurance regarding the achievement of entity objectives.7
Notice how this definition differs from the traditional compartmentalization of risk
management. The COSO framework is inclusive, starting with the board of directors in
addition to managers and other employees; COSO is broad in defining risk, ranging from
strategic choices to specific events; COSO is unambiguous, with the company explicitly
choosing an acceptable level of risk; and COSO is transparent, requiring monitoring and
reporting.
Before we describe ERM frameworks in more detail, you should know about the Basel
accords, another big regulatory wave that has had an impact on risk management. The Basel
7
We added the italics for emphasis. See page 2 of COSO, “Summary of Enterprise Risk Management—Integrated
Framework,” 2004, www.coso.org/documents/coso_erm_executivesummary.pdf.
916 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 954

```text
Committee, headquartered in Switzerland, is composed of the heads of the central banks
from well-developed economies. In the past 25 years, the Committee has introduced three
major accords designed to control risk in the global financial system, Basel I (1988), Basel II
(2004), and Basel III (introduced in 2010 and revised in 2011). There are similarities in all
three accords, but we focus on Basel III because it is the most recent.
The essence of banking is raising funds (from sales of stock, issuances of debt, borrowing
through short-term loans, and taking deposits) and then investing the funds in assets (such as
business loans and derivatives). A bank experiences financial distress when its assets’ cash
flows and values aren’t sufficient to cover its obligations to its creditors. To prevent a bank
from experiencing financial distress (and then passing its problems on to taxpayers and the
global financial system), Basel III seeks to ensure that a bank is not financed with too much
debt relative to the risk of its assets. In addition to regulations regarding the types and
proportions of capital a bank must maintain relative to its assets’ risks, Basel III also requires
adequate internal control systems to supervise a bank’s risk and goes on to suggest particular
techniques for measuring risk. We will describe several of these measures later in the chapter,
including value at risk and expected shortfall.
SELF-TEST
Describe some regulatory actions that have influenced the evolution of risk management.
Define enterprise risk management.
23-3 A Framework for Enterprise Risk Management
No single framework is applicable to all companies, but the COSO framework (including
modified versions) is widely used, so it provides an excellent example of an ERM framework.8
23-3a The Committee of Sponsoring Organizations’
(COSO) Framework for Enterprise Risk
Management (ERM)
COSO designed its enterprise risk management framework with three dimensions. The first
dimension is the organizational level. The COSO framework applies ERM at all levels of an
organization, including the corporate level, division levels, business units, and subsidiaries.
The second dimension is the category of objectives. Each organizational level should
define its objectives in each of four categories: (1) strategic objectives, which are based on
the company’s mission and overall goals; (2) operating objectives, which focus on the
selection, implementation, and ongoing execution of projects and other applications of
corporate resources; (3) reporting objectives, which seek to disseminate accurate and up￾to-date information to decision makers inside the company and stakeholders outside the
company (such as investors and regulators); and (4) compliance objectives, which seek to
ensure the company complies with laws and regulatory requirements.
8
For more on the COSO framework, see The Committee of Sponsoring Organizations of the Treadway Commission,
Enterprise Risk Management—Integrated Framework, 2004, available at www.coso.org/guidance.htm. A summary
of the framework is available for free at the same Web site. Another widely used framework is ISO 3100:2009,
published by the International Organization for Standardization (ISO), headquartered in Switzerland. For an ERM
framework that is consistent with COSO and ISO, see https://www.theirm.org/knowledge-and-resources/online
-resource-centre/enterprise-risk-management/erm-general/a-structured-approach-to-enterprise-risk-management
-(erm)-and-the-requirements-of-iso-31000,-irm,-2010/ a report that is authored jointly by three major UK
risk management associations.
Chapter 23 Enterprise Risk Management 917
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 955

```text
The third dimension is the process of risk management for an objective at a particular
level within the organization. The risk management process for each objective has eight
components, which we discuss in the following section.
23-3b The Components of the COSO Enterprise Risk
Management Framework
The eight components of the COSO ERM process define the way in which an organiza￾tion approaches and applies risk management.
COMPONENTS 1 AND 2: INTERNAL ENVIRONMENT AND OBJECTIVE
SETTING
The first two components are related to a company’s culture and mission, including the
company’s workplace environment, attitude toward risk, and goal-setting process. An
important part of these processes is the identification of the amount of risk that a
company is willing to take, which often is called the risk appetite.
COMPONENT 3: EVENT IDENTIFICATION
You can’t manage a source of risk if you don’t recognize it. A risky event is defined as any
uncertain outcome that affects a company’s previously defined objectives.9 For example,
risky events include increases in the prices of raw materials, an explosion at a factory, or a
loss of customers to a competitor. To prevent overlooking risky events, ERM systems
typically define categories and then identify the potential events within those categories.
We will take a much closer look at risk categories later.
COMPONENT 4: RISK ASSESSMENT
After identifying a risk, a company should assess the risk. We will describe risk assessment
in more detail later, but it always includes estimating both the probability that the event
will occur and the resulting impact on the company’s objectives. For example, an event
might be an increase in interest rates, which would affect a company’s cost when it issues
debt. To assess this risk, the company would begin by forecasting the probabilities of
different interest rates at the time it plans to issue the debt, and then estimate the cost of
issuing debt at the different interest rates. As another example, an event might be a fire at
a warehouse. In this case, a company would estimate the probability of a fire and the
resulting cost. The insurance industry often uses the terms loss frequency and loss severity
(the dollar value of each loss) for these concepts.
COMPONENT 5: RISK RESPONSE
After identifying and assessing a risky event, the next steps are to choose a response to the
risk and implement that choice. There are several different types of responses, including
the following.
Totally Avoid the Activity That Gives Rise to the Risk For example, a company might
discontinue a product or service line because the risks outweigh the rewards. This often is
the case with pharmaceutical products that have potentially harmful side effects or global
expansion into countries with civil unrest.
9
COSO defines risk as an event that negatively affects an objective, and an opportunity as an event that can
positively affect an objective. We don’t make that distinction—we define risk as uncertainty, which can result in
positive or negative outcomes.
918 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 956

```text
Reduce the Probability of Occurrence of an Adverse Event The expected loss arising
from any risk is a function of both the probability of occurrence and the dollar loss if the
adverse event occurs. In some instances, it is possible to reduce the probability that an
adverse event will occur. For example, the probability that a fire will occur can be reduced
by instituting a fire prevention program, by replacing old electrical wiring, and by using
fire-resistant materials in areas with the greatest fire potential.
Reduce the Magnitude of the Loss Associated with an Adverse Event In some
instances, companies can take actions to reduce losses even if the event occurs. Continu￾ing with the previous example, the dollar cost associated with a fire can be reduced by
such actions as installing sprinkler systems, designing facilities with self-contained fire
zones, and locating facilities close to a fire station.
Transfer the Risk to an Insurance Company Often, it is advantageous to insure against
risk by transferring it to an insurance company. Even though an insured item’s expected loss
is the same for its owner and for the insurance company, the insurance company benefits
from diversification. For example, an insurance company might provide coverage for
tractors, harvesters, and other types of agricultural equipment, which often cost several
hundred thousand dollars or more. If the insurance company has a large number of
customers, it can predict quite accurately the amounts it will pay in claims and then can
set premiums high enough to pay the claims and provide the return required by its investors.
In addition, insurance companies can themselves insure parts of their risk by purchasing
reinsurance from another insurance company. Therefore, the potential loss of a harvester
might be quite risky to a farmer, but it may not be risky to a large insurance company.
However, just because something can be insured does not mean that a company
should insure it. In many instances, it might be better for the company to self-insure,
which means bearing the risk directly rather than paying another party to bear it. In fact,
many large companies choose to self-insure, or to insure only the part of an asset’s loss
that exceeds a certain amount, which is equivalent to an individual who has a large
deductible on car or home insurance.
Insurance typically excludes acts of war or terrorism, but this became a major issue after
the September 11, 2001, attacks on the World Trade Center and the Pentagon. Unless
possible terrorist targets—including large malls, office buildings, oil refineries, airlines, and
ships—can be insured against attacks, lenders may refuse to provide mortgage financing, and
that would crimp the economy. Private insurance companies are reluctant to insure these
projects, at least without charging prohibitive premiums, so the federal government has been
asked to step in and provide terrorist insurance. However, losses due to terrorist attacks are
potentially so large that they could bankrupt even strong insurance companies. Therefore,
Congress passed the Terrorism Risk Insurance Act (TRIA) in 2002 and has extended it until
2020. Under the TRIA, the federal government and private insurers share the cost of benefits
paid on insured losses caused by terrorists.
Transfer the Function That Produces the Risk to a Third Party For example,
suppose a furniture manufacturer is concerned about potential liabilities arising from its
ownership of a fleet of trucks used to transfer products from its manufacturing plant to
various points across the country. One way to eliminate this risk would be to contract
with a trucking company to do the shipping, thus passing the risks to a third party.
Share or Eliminate the Risk by Using Derivative Contracts Many companies use
derivative contracts to reduce or eliminate an event’s risk. For example, a cereal company
may use corn or wheat futures to hedge against increases in grain prices. Similarly,
financial derivatives can be used to reduce risks that arise from changes in interest rates
Chapter 23 Enterprise Risk Management 919
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 957

```text
and exchange rates. As we will describe later, the risk doesn’t disappear—it is just taken on
by the other party in the derivative contract.
Accept the Risk In some instances, a company will decide to accept a risk because the
expected benefits are greater than the expected costs and because the risk doesn’t exceed the
company’s risk appetite. Indeed, accepting risk is the nature of most businesses—if they were
riskless, then investors would expect to receive a return only equal to the risk-free rate. Also,
some stand-alone risks may be quite large, but they may not contribute much to the total
corporate risk if they are not highly correlated with the company’s other risks.
COMPONENTS 6, 7, AND 8: CONTROL ACTIVITIES, INFORMATION AND
COMMUNICATION, AND MONITORING
The last three components focus on ensuring that risky events are in fact being
treated according to the responses that were previously chosen—it doesn’t do much
good to develop strategies and tactics if employees don’t follow them! For example, a
single rogue trader lost €4.9 billion in 2008 at the French bank Societe Generale, and
another lost £1.5 billion in 2011 at the London branch of UBS (headquartered in
Switzerland).
SELF-TEST
Define a risk event.
What are the two stages in risk assessment?
Describe some possible risk responses.
Should a firm insure itself against all of the insurable risks it faces? Explain.
23-4 Categories of Risk Events
Before addressing alternative risk responses to specific risk events, it will be helpful to
describe ways to categorize risk.
23-4a Major Categories
Following is a typical list of major categories that are representative of those at several
organizations.10
1. Strategy and reputation. A company’s strategic choices simultaneously influence and
respond to its competitors’ actions, corporate social responsibilities, the public’s
perception of its activities, and its reputation among suppliers, peers, and customers.
ERM addresses the risk inherent in these strategic choices.
2. Control and compliance. This category includes risk events related to regulatory
requirements, litigation risks, intellectual property rights, reporting accuracy, and
internal control systems.
10To see the way that several organizations have categorized risk and the ways that surveyors categorize risk, see
the following: Mark L. Frigo and Hans Læssøe, “Strategic Risk Management at the LEGO Group,” Strategic
Finance, February 2012, pp. 27–35; Henri Servaes, Ane Tamayo, and Peter Tufano, “The Theory and Practice of
Corporate Risk Management,” Journal of Applied Corporate Finance, Fall 2009, pp. 60–78; Celina Rogers, The
Risk Management Imperative (Boston: CFO Publishing LLC, 2010), http://secure.cfo.com/whitepapers/index
.cfm/download/14521624; Casualty Actuarial Society, Overview of Risk Management, 2003, https://www.casact
.org/area/erm/overview.pdf and the sources cited in footnote 12.
920 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 958

```text
3. Hazards. These include fires, floods, riots, acts of terrorism, and other natural or man￾made disasters. Notice that hazards only have negative outcomes—an earthquake might
destroy a factory, but it isn’t going to build one.
4. Human resources. Success often depends upon a company’s employees. ERM addresses
risk events related to employees, including recruiting, succession planning, employee
health, and employee safety.
5. Operations. A company’s operations include supply chains, manufacturing facilities,
existing product lines, and business processes. Risk events include supply chain
disruptions, equipment failures, product recalls, and changes in customer demand.
6. Technology. Technology changes rapidly and is a major source of risk, including
risk events related to innovations, technological failures, and IT reliability and
security.
7. Financial management. This category includes risk events related to: (1) foreign
exchange risk, (2) commodity price risk, (3) interest rate risk, (4) project selection
risk (including major capital expenditures, mergers, and acquisitions), (5) liquidity
risk, (6) customer credit risk, and (7) portfolio risk (the risk that a portfolio of
financial assets will decrease in value). For the remainder of the chapter, we will
focus on the risk events related to financial management, but first we need to describe
several other ways to think about risk.
23-4b Dimensions of Risk
Sometimes it is helpful to think about risk events based on different dimensions. For
example, several risk management systems classify risk by whether it is driven by external
forces or by internal decisions and activities. This is especially helpful in risk identification
because it forces managers to look at a broader range of risk events.
Sometimes it is useful to classify risk by whether it is a pure risk that only has a
downside (e.g., a hazard, such as a fire) or a speculative risk that has potential positive as
well as negative outcomes (e.g., the exchange rate between dollars and euros can go up or
down, which would have a big impact on the cash flows of U.S. importers). Most pure
risks can be reduced or eliminated with insurance products.
When choosing among different risk responses, it is helpful to determine whether
the source of risk is linear or nonlinear. For example, consider an agricultural
company with access to a low-cost source of water for irrigation. The company grows
corn and can predict its costs and the size of its harvest, but it is exposed to volatility
in the price of corn. Notice that this is a linear risk—the company loses money when
prices are low and makes money when they are high. We discuss the details later, but
the company can enter into derivative contracts that provide positive cash flows when
prices are low but create negative cash flows when prices are high. The derivative also
has a linear payout, but its payouts are opposite those of the company. The combina￾tion of the company’s internally generated cash flows from the harvest and its
externally generated cash flows from the derivative can reduce or eliminate the
company’s risk.
In contrast, consider a company in the oil exploration and extraction industry.11
The company will incur fixed costs and negative cash flows associated with continu￾ing operations when oil prices are too low to justify additional exploration. When oil
prices are high, the company incurs fixed costs and also variable costs associated with
11See Kenneth A. Froot, David S. Scharfstein, and Jeremy Stein, “A Framework for Risk Management,” Journal of
Applied Corporate Finance, Fall 1994, pp. 22–32; also see the paper by Servais et al., cited in footnote 14.
Chapter 23 Enterprise Risk Management 921
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 959

```text
expanded exploration and extraction. However, when oil prices are high, the company
will generate enough positive cash flow to cover its fixed costs and also the new
variable costs associated with the additional exploration and extraction. Therefore, the
company is exposed to nonlinear risk—it needs additional cash flow to support its
ongoing operations only when oil prices are low but not when prices are high. In this
situation, the company might be willing to buy a derivative that pays out only when
oil prices are low. In other words, the company reduces its nonlinear risk with a
nonlinear hedging strategy.
SELF-TEST
List and define the different major categories of risk events.
Should a firm insure itself against all of the insurable risks it faces? Explain.
Explain the difference between a linear risk and a nonlinear risk.
23-5 Foreign Exchange (FX) Risk
Foreign exchange (FX) risk occurs when a company’s cash flows are affected by changes
in currency exchange rates. This can occur if a company imports materials from other
countries or sells its products in other countries. Some smaller companies manage FX risk
for each transaction, but most large companies aggregate their transactions and manage
their exposures centrally. For example, if one division is selling goods denominated in
Canadian dollars and another division is purchasing goods denominated in Canadian
dollars, the company would net out the two transactions and just manage any remaining
exposure.
The primary tool used to manage FX risk is a forward contract, which is an
agreement in which one party agrees to buy an item at a specific price on a specific
future date and another party agrees to sell the item at the agreed-upon terms. Goods are
actually delivered under forward contracts. In the case of foreign exchange, the goods are
the amount of foreign currency specified in the contract, paid for with the other currency
specified in the contract.
Historically, FX trading has been directly between two parties using customized
contracts with unique amounts and dates and no central market. This requires that
both parties be morally and financially strong to minimize the danger that one party
will default on the contract—this is called counterparty risk. In such contracts, major
banks often act as counterparties for their customers. For example, a bank might
agree to buy euros in 30 days at a price of 1.24 dollars per euro from one customer
and agree to sell euros in 30 days at a rate of 1.25 dollars per euro to another
customer. Depending on the change in the euro exchange rate, the bank will make
money on one of the contracts and lose money on the other, netting only the spread
on the difference in prices. This matching of contracts allows banks to reduce their
net exposure to exchange rate volatility, but the bank is still exposed to counterparty
risk from the customers.
The failure to manage counterparty risk was one of the causes of the 2007 global
financial crisis. For example, Lehman Brothers was a counterparty to many other financial
institutions in a variety of derivative contracts, so Lehman’s failure caused distress at
financial institutions throughout the world. In response to this and other causes of the
financial crisis, the Dodd-Frank Consumer Protection Act was passed in 2010. One of its
provisions required the Commodities and Futures Trading Commission (CFTC) to
establish, among other things, a mechanism for centralized clearing of foreign exchange
922 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 960

```text
derivatives contracts, such as forward contracts. The CME Group is one company that
provides this clearing function in the United States and acts as the counterparty to all
trades that it clears. As of mid-2015, the CME Group is able to clear 38 cash-settled
forward contracts involving 33 different currencies.12
Foreign exchange transactions are a big business. Contracts are based on the total
amount of currency to be delivered at expiration, which is called the notional value. At
the beginning of 2015, the notional value of over-the-counter FX derivatives was about
$76 trillion!13 The total is even larger if customized FX contracts between two parties are
considered.
To illustrate how foreign exchange contracts are used, suppose GE arranges to buy
electric motors from a European manufacturer on terms that call for GE to pay 10 million
euros in 180 days. GE would not want to give up the free trade credit, but if the euro
appreciated against the dollar during the next 6 months, then the dollar cost of the
10 million euros would rise. GE could hedge the transaction by buying a forward contract
under which it agreed to buy the 10 million euros in 180 days at a fixed dollar price, which
would lock in the dollar cost of the motors. This transaction would probably be con￾ducted through a money center bank, which would try to find a European company that
needed dollars in 6 months.
SELF-TEST
What is a forward contract?
Explain how a company can use forward contracts to eliminate FX risk.
What is counterparty risk?
23-6 Commodity Price Risk
Many companies use or produce commodities, including agricultural products, energy,
metals, and lumber. Because commodity prices can be quite volatile, many companies
manage their exposure to commodity price risk. Before describing specific ways to
manage commodity price risk, we begin with a brief overview of futures markets in the
United States to illustrate some key concepts.
23-6a An Overview of Futures Markets
As we noted earlier, Midwest farmers in the early 1800s were concerned about the price
they would receive for their wheat when they sold it in the fall, and millers were
concerned about the price they would have to pay. Each party soon realized that the
risks they faced could be reduced if they established a price earlier in the year. Accord￾ingly, mill agents began going out to the Wheat Belt with contracts that called for the
farmers to deliver grain at a predetermined price, and both parties benefited from the
transaction in the sense that their risks were reduced. The farmers could concentrate on
12When a traditional forward for delivery contract expires, the two currencies are exchanged. In a cash-settled
forward contract, however, the currencies are never exchanged. Rather, the difference between the contract price and
the spot price at expiration is converted to U.S. dollars at the prevailing spot price and then these dollars are paid or
received. The clearinghouse would require some form of collateral to reduce the risk that one of the parties didn’t pay.
In addition, cash-settled forward contracts can be “marked to market” every day like a futures contract, and this
further reduces the clearinghouse’s risk. See the CME Group’s Web site, www.CMEGroup.com, for more
information on their clearing mechanism and the products it clears.
13See the Bank for International Settlements, www.bis.org/statistics/derstats.htm.
www
See the CME Group’s
Web site, www
.cmegroup.com, for a
wealth of information on
the operation and
history of the exchange.
Chapter 23 Enterprise Risk Management 923
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 961

```text
growing their crop without worrying about the price of grain, and the millers could
concentrate on their milling operations.
These early agreements were between two parties who arranged the transactions
themselves. Soon, though, intermediaries came into the picture. The Chicago Board of
Trade, founded in 1848, was an early marketplace where futures dealers helped make a
market in futures contracts.
A futures contract is similar to a forward contract in that two parties are involved,
with one party taking a long position (which obligates the party to buy the underlying
asset) and the other party taking a short position (which obligates the party to sell the
asset). However, there are three key differences. First, futures contracts are marked￾to-market on a daily basis, meaning that gains and losses are recognized daily and
money must be put up to cover losses. This greatly reduces the risk of default that
exists with forward contracts because daily price changes are usually smaller than the
cumulative change over the contract’s life. For example, if a corn futures contract has
a price of $4.00 per bushel and the price goes up to $4.10 the next day, a party with a
short position must pay the $0.10 difference, and a party with a long position would
receive the difference. This marking-to-market occurs daily until the delivery date. To
see that this procedure does in fact lock in the price, suppose that the price doesn’t
change again. On the delivery date, the party with the short position would sell corn
at the current price of $4.10. Because the short seller had already paid $0.10 from
daily marking-to-market, the short seller’s net cash flow is $4.00. The party with the
long position would have to buy corn at the current price of $4.10, but because
the purchaser had already received $0.10 from cumulative daily marking-to-market,
the net purchase price would be $4.00.
The second major difference between a forward contract and a futures contract is that
physical delivery of the underlying asset in a futures contract is virtually never taken—the
two parties simply settle up with cash for the difference between the contracted price and
the actual price on the expiration date. The third difference is that futures contracts are
generally standardized instruments that are traded on exchanges, whereas forward con￾tracts are usually tailor-made, negotiated between two parties, and not traded after they
have been signed.
The needs of farmers and millers allowed a natural hedge, defined as a situation
in which aggregate risk can be reduced by derivatives transactions between two
parties. Natural hedges occur when futures are traded between cotton farmers and
cotton mills, copper mines and copper fabricators, importers and foreign manufac￾turers for currency exchange rates, electric utilities and coal mines, and oil producers
and oil users. In such situations, hedging reduces aggregate risk and thus benefits the
economy.
There are two basic types of hedges: (1) long hedges, in which futures contracts are
bought (obligating the hedger to purchase the underlying asset), providing protection against
price increases, and (2) short hedges, where a firm or individual sells futures contracts
(obligating the hedger to sell the underlying asset), providing protection against falling prices.
Not all participants in the futures markets are hedgers. Speculation involves betting
on future price movements, and futures are used instead of the commodities because of
the leverage inherent in the contract. For example, a speculator might buy corn for $4 a
bushel. If corn goes up to $4.40, the speculator has a 10% return (assuming rats don’t eat
the corn before it can be sold).
Now consider a speculator who takes a short position in a futures contract for 5,000
bushels at $4 per bushel. The exchange requires an investor to put up a margin requirement
to ensure that the investor will not renege on the daily marking-to-market. However, the
924 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 962

```text
margin is quite small relative to the size of a contract—the margin is only $1,100, but the total
amount of corn is valued at $20,000 $4 5,000 .
14 If the price goes up to $4.40, the profit
is $2,000 $4 40 $4 00 5,000 . The rate of return on the invested margin is
82% $2,000 $1,100 $1,100. The 82% return on the futures contract is much greater
than the 10% return on the underlying asset. Of course, any losses on the contract also would
be magnified.
At first blush, one might think that the appearance of speculators would increase risk,
but this is not necessarily true. Speculators add capital and players to the market. Thus, to
the extent that speculators broaden the market and make hedging possible, they help
decrease risk for those who seek to avoid it. Unlike the natural hedge, however, risk is not
eliminated. Instead, it is transferred from the hedgers to the speculators.
Today, futures contracts are available on hundreds of real and financial assets traded
on dozens of U.S. and international exchanges, the largest of which are the Chicago Board
of Trade (CBOT) and the Chicago Mercantile Exchange (CME), both of which are now
part of the CME Group. Futures contracts are divided into two classes, commodity
futures and financial futures. Commodity futures include oil, various grains, oilseeds,
livestock, meats, fibers, metals, and wood. Financial futures, which were first traded in
1975, include Treasury bills, notes, bonds, certificates of deposit, Eurodollar deposits,
foreign currencies, and stock indexes. We describe how financial futures can reduce
interest rate risk in a later section.
23-6b Using Futures Contracts to Reduce
Commodity Price Exposure
We will illustrate commodity hedging at Porter Electronics, which uses large quantities
of copper and several precious metals in its manufacturing operations. Suppose that in
May 2016, Porter foresaw a need for 100,000 pounds of copper in March 2017 for use in
fulfilling a fixed-price contract to supply solar power cells to the U.S. government. The
spot price of copper in May is $4.08. Therefore, it would cost Porter $408,000 to
purchase the copper in March if the prices don’t change: 100,000 $4 80 $408,000.
However, Porter’s managers are concerned that a strike by Chilean copper miners might
occur, which would raise the price of copper in world markets and reduce Porter’s
expected profit.
Porter could go ahead and buy the copper it will need to fulfill the contract, but it would
have to borrow money to pay for the copper and then pay for storage. As an alternative,
Porter could hedge against increasing copper prices in the futures market. COMEX, a
division of The New York Commodity Exchange, trades standard copper futures contracts
of 25,000 pounds each. Thus, Porter could buy four contracts (go long) for delivery in March
2017. Suppose these contracts were trading in May 2016 for about $4.10 per pound.
What happens to Porter’s cash flows if copper prices rise to $4.30 by the delivery date?
Porter would have to spend $430,000 to buy the copper it needs. However, Porter would
14The CME requires that an investor make an initial deposit at the time the investor takes a position in a contract.
The dollar value of the initial margin might decline if the investor uses some of it to pay for daily marking-to-market.
However, the investor must not let the amount on deposit drop below a specified amount, which is called the
maintenance margin. The CME specifies the maintenance margin for each contract. For example, if you go to the
CME Web site (www.cmegroup.com) and search for a contract, such as corn futures, you will be directed to a page
with information about the contract, with an option to find the maintenance margin. For corn, it is $1,000 in 2015.
For hedgers, the initial margin is set at 100% of the maintenance margin; for speculators, the initial margin is set at
110% of the maintenance margin (see www.cmegroup.com/clearing/margins/initial-margin-requirements.html).
These margins requirement change over time as the value of the underlying commodity changes. For example, the
corn margin was $3,750 in July of 2012, when corn spot prices where near record highs.
Chapter 23 Enterprise Risk Management 925
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 963

```text
have made a profit on its futures contracts of $0.20 per pound $4 30 $4 10 $0 20 .
15
With contracts for 100,000 pounds, Porter’s profit would be $20,000. Therefore, Porter’s
net cost to purchase the copper would be equal to the $430,000 it actually paid minus the
$20,000 profit on the contract, which is a net cost of $410,000.
Now suppose copper prices fell to $4.00 per pound. Porter would have to pay
$400,000 for the copper, but would have lost $10,000 on the futures contract:
$4 00 $4 10 100,000 $10,000. Porter’s net cost would have been equal to the
$400,000 it paid for the copper minus the loss of $10,000, for a net cost of $410,000.
As this example shows, hedging in the copper futures market locks in Porter’s net cost
of raw materials at $410,000, eliminating any exposure to changes in copper prices.
However, if copper prices had remained at their original spot price of $4.08, Porter would
have paid only $408,000 for copper instead of its net cost of $410,000 with the hedge.
Therefore, the hedge came with a cost: Porter locked in the price it paid for copper, but
that fixed price might have been higher than the expected price.
Many other companies, such as Alcoa with aluminum and Archer Daniels Midland with
grains, routinely use the futures markets to reduce the risks associated with price volatility.
23-6c Options on Futures
Futures contracts and options are similar to one another—so similar that people often confuse
the two. Therefore, it is useful to compare the two instruments. A futures contract is a definite
agreement on the part of one party to buy something on a specific date and at a specific price,
and the other party agrees to sell on the same terms. No matter how low or how high the price
goes, the two parties must settle the contract at the agreed-upon price and the losses of one
party must exactly equal to the gains of the other. In addition, a dollar increase in the futures
price has exactly the opposite effect of a dollar decrease in the futures price. A hedge
constructed using futures contracts is called a symmetric hedge because of this feature—the
payoff from an increase in the futures price is exactly opposite the payoff from a decrease in
the futures price. For this reason, symmetric hedges are typically used to provide a fixed
transaction price at some date in the future and are ideal for managing a risk that is linear.
For example, suppose an agricultural company has access to a source of low-cost water
for irrigation. The company can predict its costs and the size of its harvest but is exposed to
price risk. The company could sell futures contracts (take a short position, which obligates it
to sell corn) for delivery when the corn is harvested in 6 months. If the corn price (and
hence the corn futures price) decreases over the 6 months, then the company will receive
less when selling the corn but will make up the difference when closing out the futures
contract. If instead the corn price increases, then the company will make more money when
selling the corn in 6 months but will lose money when closing out the futures contract. In
this way the ending value of the position doesn’t depend on the corn price in 6 months, and
so the amount received for selling the corn in 6 months is locked in.
An option, on the other hand, gives someone the right to buy (call) or sell (put) an asset, but
the holder of the option does not have to complete the transaction. The payoff from a hedge
constructed using options will be different from a futures hedge because of this option feature.
As discussed in Chapter 8, the payoff from a call option increases as the price of the underlying
asset increases, but if the underlying asset price decreases, then the most the option holder can
lose is the amount invested in the option. That is, upside gains are unlimited but downside
losses are capped at the amount invested in the option. For this reason, an option is said to
create an asymmetric hedge—it hedges price changes in one direction more than price changes
in the other. As such, options are ideal for managing nonlinear risks.
15To focus the example on the primary impact of hedging, we have ignored daily marking-to-market.
926 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 964

```text
For example, suppose the agricultural company did not have access to irrigation but
operated many farms in different states. A widespread drought would reduce the size of the
harvest but probably would cause the price of corn to increase due to the lower supply. If this
happened, the company’s revenues would fall but would not be eliminated—the higher corn
price would partially compensate for the smaller harvest. This means the company faces
nonlinear risk with respect to corn prices. Instead of going long in a futures contract, the
company might buy a put option on a corn futures contract, giving the company the right to
sell a futures contract at a fixed price. If the price of corn decreased, the value of the put
option would increase, and the profits on the option would offset the loss from selling the
corn at the lower price. However, if corn prices increased, then the investor would let the put
option expire and simply sell its smaller harvest at the higher price.
SELF-TEST
How does a futures contract differ from a forward contract?
What is a “natural hedge”? Give some examples of natural hedges.
Suppose a company knows the quantity of a commodity that it will produce. Describe how it
might hedge using a futures contract.
23-7 Interest Rate Risk
Interest rates can be quite volatile, exposing a company to interest rate risk, especially if
the company is planning to issue debt or if the company has floating-rate debt. The
following sections describe these two situations.
23-7a Using Futures Contracts to Manage the Risk
of Debt Issuances
To illustrate, assume that it is May and that Carson Foods is considering a plan to issue
$10,000,000 of 20-year bonds in September to finance a capital expenditure program. The
interest rate would be 9% paid semiannually if the bonds were issued today. However, the
market interest rate might be higher when the bonds are actually issued. Carson would
have to issue the bonds with a higher coupon rate than expected, causing Carson’s
financing costs to increase. Carson can protect itself against a rise in rates by hedging
in the futures market using an interest rate futures contract.
INTEREST RATES FUTURES
To illustrate how interest rate futures work, consider the CBOT’s contract on Treasury
bonds. The basic contract is for $100,000 of a hypothetical 6% coupon, semiannual
payment Treasury bond with 20 years to maturity.16 Table 23-1 shows illustrative quotes
for Treasury bond futures.
16The coupon rate on the hypothetical bond was changed to 6% from 8% in March 2000. The CBOT contract
doesn’t specify a 20-year bond but instead allows delivery of any noncallable bond with a remaining maturity
greater than 15 years (or callable bond that is not callable for at least 15 years) and less than 25 years. Rather than
simply deliver a bond, which might have an interest rate other than 6%, the actual bond price is adjusted by a
conversion factor to make it equivalent to a 6% bond that is trading at par. Because the average maturity of bonds
that are eligible for delivery is about 20 years, we use a 20-year maturity for the hypothetical bond in the futures
contract. For even longer maturity hedging, the CBOT also has the Ultra T-Bond contract, which allows for
delivery of a Treasury bond of at least 25 years to maturity.
Chapter 23 Enterprise Risk Management 927
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 965

```text
The first column of Table 23-1 shows the delivery month and year. Column 2 shows the
last price of the day, also called the settlement price, and the next column shows the change in
price from the previous day. For example, the settlement price for the September contract,
127'11, means 127 plus 11/32, or 127.343750%, of par. The change was 0'15, which means the
September 2017 contract’s last price of the day was 15/32 higher than the previous day’s last
trade, which must have been at 126'28. The next three columns show the opening, high, and
low prices for the day. Column 7 shows the day’s estimated trading volume. Notice that most
of the trading occurs in the contract with the nearest delivery date. Finally, Column 8 shows
the “open interest,” which is the number of contracts outstanding.
To illustrate, we focus on the Treasury bonds for September delivery. The settlement
price was 127.343750% of the $100,000 contract value. Thus, the price at which one could
buy $100,000 face value of 6%, 20-year Treasury bonds to be delivered in December was
127 343750% $100,000 $127,343 75.
The contract price increased by 15/32 of 1% of $100,000 from the previous day’s price,
so if you had bought the contract yesterday, you would have made $468.75 = (15/32)
(0.01) ($100,000). There were 95,000 contracts outstanding, representing a total value of
about 95,000 $127,343 75 $12,097,656.
Note that the contract increased by 15/32 of a percent on this particular day. Why
would the value of the bond futures contract increase? Bond prices increase when interest
rates fall, so interest rates must have fallen on that day. Moreover, we can calculate the
implied rate inherent in the futures price. Recall that the contract relates to a hypothetical
20-year, semiannual payment, 6% coupon bond. The settlement price was 127.343750% of
par, so a $1,000 par bond would have a price of 127 343750% $1,000 $1,273 4375. We
can solve for rd by using the following equation:
40
t 1
$30
1 rd 2 t
$1,000
1 rd 2 40 $1,273 4375
Using Excel or a financial calculator, input N 40, PV 1273 4375, PMT 30,
and FV 1000; then solve for I YR 2 0004%. This is the semiannual rate, which is
equivalent to a nominal annual rate of 4.0007%, or approximately 4.00%.
The previous day’s last (settlement) price was 126'28, or 126.87500%, for a bond price
of $1,268 7500 126 87500 $1,000 . Setting N 40, PV 1268 7500, PMT 30, and
FV 1000 and then solving for I YR 2 0150 implies an annual yield of 4.0300%, or
approximately 4.03%. Therefore, interest rates fell from 4.03% to 4.00%. This decline in rates was
only 0.03 percentage points, but that was enough to increase the value of the contract by $468.75.
Rather than discuss changes in percentage points, financial traders use basis points, with 100
basis points equal to 1 percentage point. Therefore, the decline in rates was 3 basis points.
At the time of the quotes in Table 23-1, which was May, the yield on a 20-year T-bond
was about 3.90%. But as we just calculated, the implied yield on the September futures
TABLE 23-1
Example of Futures Prices (Treasury Bonds: $100,000; Pts. 32nds of 100%) in May
Delivery Month/Year
(1)
Settle
(2)
Change
(3)
Open
(4)
High
(5)
Low
(6)
Estimated Volume
(7)
Open Interest
(8)
Jun-17 128'12 0'14 128'06 129'11 127'30 500,000 640,000
Sep-17 127'11 0'15 127'01 127'31 126'28 300,000 95,000
Dec-17 126'16 0'17 126'16 126'16 126'16 0 50
resource
See Ch23 Tool Kit.xlsx
on the textbook’s Web
site for all calculations.
928 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 966

```text
contract was about 4.00%. The September yield reflects investors’ beliefs in May as to
what the interest rate level will be in September: The marginal trader in the futures market
is predicting a 10-basis-point increase in yields between May and September. That
prediction could, of course, turn out to be incorrect.
For example, suppose that the implied yields in the futures market had fallen by 50
basis points from May to August—say, from 4.00% to 3.50%. Inputting N 40,
I YR 3 5 2 1 75, PMT 30, and FV 1000 and then solving for PV
1,357 4279 shows that the September contract would be worth about $1,357.4279 per
bond in August if implied yields fell by 50 basis points. Thus, the contract’s value would
have increased from $127,343.75 to $135,742.79, a gain of about $8,399:
$135,742 79 $127,343 75 ≈ $8 399.
HEDGING WITH TREASURY BOND FUTURES CONTRACTS
Recall that Carson Foods plans to issue $10,000,000 of 9% semiannual 20-year bonds in
September and would like to protect itself from a possible increase in interest rates by
using T-bond futures contracts. Rising interest rates cause bond prices to fall, and thus
decrease the value of bond futures contracts. Therefore, Carson can guard against an
increase in interest rates by taking a short position on a T-bond futures contract—if rates
go up, Carson will receive a cash flow from the futures contract equal to the original
futures price less the now-lower futures price.
Carson would choose a futures contract on the security most similar to the one it
plans to issue, long-term bonds, and so would use the September Treasury bond futures.
In the previous section, we calculated the price of a contract, which was $127,343.75.
Because Carson plans to issue $10,000,000 of bonds and because each contract is worth
$127,343.75, Carson will sell $10,000,000 $127,343 75 78 528≈79 contracts for deliv￾ery in September.17 The total value of the contracts is 79 $127,343 75 $10,060,156,
which is very close to the value of the bonds Carson wants to issue.
Now suppose that in September, when Carson issues its bonds, renewed fears of
inflation push interest rates up by 100 basis points. What would the bond proceeds be if
Carson still tried to issue 9% coupon bonds when the market requires a 10% rate of
return? We can find the total value of the offering with a financial calculator, inputting
N 40, I YR 5, PMT 450000, and FV 10000000 and then solving for
PV 9,142,046. Therefore, bonds with a 9% coupon, based upon its original plans, would
bring proceeds of only $9,142,046, because investors now require a 10% return. Because
Carson would have to issue $10 million worth of bonds at a 10% rate, Carson’s proceeds
would be less than expected: $857,954 $10,000,000 $9,142,046 as a result of delaying
the financing. Therefore, Carson would have to issue additional bonds to raise the
required $10,000,000. In other words, the increase in interest rates resulted in cost to
Carson of $857,954.
Alternatively, we can estimate Carson’s cost of delaying by calculating the present value
of the incremental payments Carson must make. The increase in interest rates from 9% to
10% would cause the semiannual coupon payments to go up from $45 to $50 on a per-bond
basis. For 10,000 bonds, the total incremental semiannual coupon payments are
$50,000 $50 $45 10,000 . We can find the present value of these incremental pay￾ments by inputting N 40, I YR 5, PMT 50000, and FV 0 and then solving for
PV 857954 $857,954, which is the same cost found by the first method. Intuitively,
this is because the first method identifies the difference between an asset’s par value and its
17Carson will have to put up a margin and pay brokerage commissions. To keep the example focused on the
primary issue, which is the impact of changing interest rates, we will ignore margins and commissions.
resource
See Ch23 Tool Kit.xlsx
on the textbook’s Web
site for all calculations.
Chapter 23 Enterprise Risk Management 929
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 967

```text
market value given a change in interest rates. This difference can be thought of as the extra
amount of value that would need to be added to bring the market value up to par. One way to
add value would be to increase the payments, which is what the second approach does.
Either way, Carson incurs a cost of $857,954 due to the increase in rates. However, the
increase in interest rates would also bring about a change in the value of Carson’s short
position in the futures contract. When interest rates increase, the value of the futures
contract will fall. If the interest rate on the futures contract also increased by the same full
percentage point, from 4.0007% to 5.0007%, then the new contract value can be found by
inputting N 40, I YR 5 0007 2 2 50035, PMT 3000, and FV 100000 and
then solving for PV 112,541 86 per contract. With 79 contracts, the total value of the
position is thus $8,890,806 94 79 $112,541 86 . Carson would then close its position in
the futures market by repurchasing for $8,890,806.94 the contracts that it earlier sold for
$10,060,156.00, giving it a profit of $1,169,349.06.
Thus, Carson would offset the loss on the bond issue. In fact, in our example Carson more
than offsets the loss, pocketing an additional $311,395 06 $1,169,349 06 $857,954.18 Of
course, if interest rates had fallen, then Carson would have lost on its futures position, but this
loss would have been offset because Carson could now sell its bonds with a lower coupon.
If futures contracts existed on Carson’s own debt and if interest rates moved identi￾cally in the spot and futures markets, then the firm could construct a perfect hedge in
which gains on the futures contract would exactly offset losses on the bonds. In reality, it
is virtually impossible to construct perfect hedges, because in most cases the underlying
asset is not identical to the futures asset; and even when the assets are identical, prices
(and interest rates) may not move exactly together in the spot and futures markets.19
Observe also that if Carson had been planning an equity offering and if its stock
tended to move fairly closely with one of the stock indexes, then the company could have
hedged against falling stock prices by selling the index future. Even better, if options on
Carson’s stock were traded in the options market, then it could use options rather than
futures to hedge against falling stock prices.
The futures and options markets permit flexibility in the timing of financial transac￾tions: The firm can be protected, at least partially, against changes that occur between the
time a decision is reached and the time the transaction is completed. However, this
protection has a cost—the firm must pay commissions. Whether or not the protection
is worth the cost is a matter of judgment. The decision to hedge also depends on
management’s risk aversion and on the company’s strength and ability to assume the
risk in question.20
18Carson would have to pay taxes on the profit from the futures contract, so the after-tax value of the futures
transaction can be found by multiplying the pre-tax profit by (1 – T). However, Carson would get to deduct the
larger additional coupon payments from its income. To find the present value of the after-tax additional coupon
payments, we multiply the additional pre-tax coupons by (1 – T) and calculate the present value. This gives the
same result as first finding the present value of the additional pre-tax coupons and then multiplying the present
value by (1 – T). In other words, the pre-tax cost of delaying and the pre-tax profit from the futures contract
should be multiplied by (1 – T) to estimate the after-tax effectiveness of the hedge.
19In this example, Carson hedged a 20-year bond with a T-bond futures contract. Rather than simply matching
on maturity, it would be more accurate to match on duration (see Web Extension 5C, available on the textbook’s
Web site, for a discussion of duration). A matching duration in the futures contracts could be accomplished by
taking positions in the T-bond futures contract and in another financial futures contract, such as the 10-Year
Treasury note contract. Because Carson’s bond had a 20-year maturity, matching on maturity instead of duration
provided a good hedge. If Carson’s bond had a different maturity, then it would be essential to match on
duration.
20For additional insights into the use of financial futures for hedging, see Mark G. Castelino, Jack C. Francis, and
Avner Wolf, “Cross-Hedging: Basis Risk and Choice of the Optimal Hedging Vehicle,” The Financial Review,
May 1991, pp. 179–210.
930 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 968

```text
23-7b Using Interest Rate Swaps: Managing
Floating versus Fixed Rates
Suppose that Company S has a 20-year, $100 million floating-rate bond outstanding and
that Company F has a $100 million, 20-year, fixed-rate issue outstanding. Thus, each
company has an obligation to make a stream of interest payments, but one payment
stream is fixed while the other will vary as interest rates change in the future. This
situation is shown in Panel A of Figure 23-1.
FIGURE 23-1
Cash Flows under a Swap
Company S: 
Has Floating-Rate
Obligations
Company S:
Has Floating-Rate
Obligations
Company F: 
Has Fixed-Rate
Obligations
Floating-Rate
Bondholders
Floating￾Rate
Payments
Floating￾Rate
Payment
Fixed￾Rate
Payment
A. Before the Swap
B. After the Swap
Company F: 
Has Fixed-Rate
Obligations
Fixed-Rate
Bondholders
Floating-Rate
Bondholders
Fixed-Rate
Bondholders
Fixed￾Rate
Payments
Floating￾Rate
Payments
Fixed￾Rate
Payments
Note: In Panel A, Company S must make floating-rate payments out of its own internal cash flows; but in Panel B, it uses the floating payments
from Company F to pay its bondholders. Company F has a reversed position. After the swap, S has de facto fixed payments, which are consistent with
its stable internal flows, and F has floating payments, which are consistent with its fluctuating flows.
Chapter 23 Enterprise Risk Management 931
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 969

```text
Now suppose that Company S has stable cash flows and wants to lock in its cost of
debt. Company F has cash flows that fluctuate with the economy, rising when the
economy is strong and falling when it is weak. Recognizing that interest rates also move
up and down with the economy, Company F has concluded it would be better off with
variable-rate debt. Suppose the companies agreed to swap their payment obligations.
Panel B of Figure 23-1 shows that the net cash flows for Company S are at a fixed rate
and those for Company F are based on a floating rate. Company S would now have to
make fixed payments, which are consistent with its stable cash inflows, and Company F
would have a floating obligation, which for it is less risky.
In practice, the two companies would not deal with one another directly; instead, each
company would enter into a swap with a large bank. For example, a bank might offer to
swap LIBOR for a fixed payment of 2.5%. In this example, Company S would pay the
bank a fixed payment equal to 2.5% of the amount Company S borrowed at a floating rate
and the bank would pay Company S an amount equal to the current LIBOR rate multi￾plied by the amount Company S borrowed. Company F would enter into a similar
contract with a bank, except Company F would make a floating rate payment to the bank
(based on LIBOR) and the bank would make a fixed payment to Company F. Of course,
the bank will charge a fee for this service.
A swap is just what the name implies—two parties agree to swap something, generally
obligations to make specified payment streams.
The previous example, which is an interest rate swap, illustrates how swaps can
reduce risks by allowing each company to match the variability of its interest payments
with that of its cash flows. However, there are also situations in which swaps can reduce
both the risk and the effective cost of debt. For example, Antron Corporation, which has a
high credit rating, can issue either floating-rate debt at LIBOR 1% or fixed-rate debt at
10%.21 Bosworth Industries is less creditworthy, so its cost for floating-rate debt is
LIBOR 1 5% and its fixed-rate cost is 10.4%. Owing to the nature of Antron’s opera￾tions, its CFO has decided that the firm would be better off with fixed-rate debt; mean￾while, Bosworth’s CFO prefers floating-rate debt. Paradoxically, both firms can benefit by
issuing the type of debt they do not want and then swapping their payment obligations.
First, each company will issue an identical amount of debt, which is called the
notional principal. Even though Antron wants fixed-rate debt, it issues floating-rate debt
at LIBOR 1%, and Bosworth issues fixed-rate debt at 10.4%. Next, the two companies
enter into an interest rate swap.22 Assume the debt maturities are 5 years, which means
the length of this swap will also be 5 years. By convention, the floating-rate payments of
most swaps are based on LIBOR, with the fixed rate adjusted upward or downward to
reflect credit risk and the term structure. The riskier the company that will receive the
floating-rate payments, the higher the fixed-rate payment it must make. In our example,
Antron will be receiving floating-rate payments from Bosworth, and those payments will
be set at LIBOR multiplied by the notional principal. Then, payments will be adjusted
every 6 months to reflect changes in the LIBOR rate.
The fixed payment that Antron must make to Bosworth is set (that is, “fixed”) for the
duration of the swap at the time the contract is signed, and it depends primarily on two
21LIBOR stands for the London Interbank Offered Rate, the rate charged on interbank dollar loans in the
Eurodollar market.
22Such transactions are generally arranged by large money center banks, and payments are made to the bank,
which in turn pays the interest on the original loans. The bank assumes the credit risk and guarantees the
payments should one of the parties default. For its services, the bank receives a percentage of the payments as its
fee. In addition, the CME clears swaps similar to these.
932 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 970

```text
factors: (1) the level of fixed interest rates at the time of the agreement and (2) the relative
creditworthiness of the two companies.
In our example, assume interest rates and creditworthiness are such that 8.95% is the
appropriate fixed swap rate for Antron, so it will make 8.95% fixed-rate payments to
Bosworth. In turn, Bosworth will pay the LIBOR rate to Antron. Table 23-2 shows the net
rates paid by each participant, and Figure 23-2 graphs the flows. Note that Antron ends
up making fixed payments, which it desires, but because of the swap, the rate paid is
9.95% versus the 10% rate it would have paid had it issued fixed-rate debt directly. At the
same time, the swap leaves Bosworth with floating-rate debt, which it wants, but at a rate
of LIBOR 1 45% versus the LIBOR 1 50% it would have paid on directly issued
floating-rate debt. As this example illustrates, swaps can sometimes lower the interest
rate paid by each party.
Currency swaps are special types of interest rate swaps. To illustrate, suppose Com￾pany A, an American firm, had issued $100 million of dollar-denominated bonds in the
The Game of Truth or LIBOR
LIBOR stands for the London Interbank Offered Rate, the
rate banks charge one another for loans in the Eurodollar
market. LIBOR might possibly be the most important num￾ber reported in financial markets because many derivative
contracts base payments on LIBOR. Some analysts esti￾mate that there are over $300 trillion of derivatives linked
to LIBOR. Because LIBOR is such a widely used rate, you
might think that it is reported with the utmost care and
accuracy. Wrong!
The largest banks in London report to Thomson Reu￾ters the rates they charge one another on loans. Each day
Thomson Reuters collects these rates, throws out the high￾est and lowest percentiles, and uses the middle 50% to
calculate the average rate, which it reports to the rest of
the world. That part of the process is clear, but how do the
banks define the rates that they report? It turns out that
some of them just pick a number. On June 27, 2012,
Barclays admitted that it had been fined £290 million by
U.S. and UK regulators for knowingly reporting untrue
rates. Barclays reported low rates at times to disguise
how risky other banks viewed Barclays, according to its
own e-mails. In addition, some e-mails suggest that Bar￾clays manipulated LIBOR to profit on trades. In the wake of
this news, Barclays’s CEO and other senior executives were
forced to resign.
The Barclays case was just the beginning of a much
bigger scandal. In 2013 Deutsche Bank, Société Générale,
and Royal Bank of Scotland admitted fixing reported inter￾est rates on the euro version of LIBOR, the EURIBOR, and
Citigroup, HSBC, JPMorgan, and Crédit Agricole are being
investigated. As of mid-2014, $5.8 billion in fines have been
assessed in the combined LIBOR and EURIBOR scandals,
with more likely to come.
Note: For more information on the LIBOR and EURIBOR scandal, see http://
topics.nytimes.com/top/reference/timestopics/subjects/l/london
_interbank_offered_rate_libor/index.html and www.ft.com/intl/indepth
/libor-scandal.
TABLE 23-2
Anatomy of an Interest Rate Swap
Antron’s Payments: Borrows Floating, Swaps for Fixed Bosworth’s Payments: Borrows Fixed, Swaps for Floating
Payment to lender (LIBOR 1%) Payment to lender 10.40% fixed
Payment from Bosworth LIBOR Payment from Antron 8.95% fixed
Payment to Bosworth 8.95% fixed Payment to Antron LIBOR
Net payment by Antron 9.95% fixed Net payment by Bosworth (LIBOR 1.45%)
Chapter 23 Enterprise Risk Management 933
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 971

```text
United States to fund an investment in Germany. Meanwhile, Company G, a German
firm, had issued $100 million of euro-denominated bonds in Germany to make an
investment in the United States. Company A would earn euros but be required to make
payments in dollars, and Company G would be in the opposite situation. Thus, both
companies would be exposed to exchange rate risk. However, both companies’ risks would
be eliminated if they swapped payment obligations.
Originally, swaps were arranged between companies by money center banks, which
would match up counterparties. Such matching still occurs, but today most swaps are
between companies and banks, with the banks then taking steps to ensure that their own
risks are hedged. For example, Citibank might arrange a swap with Company A. Com￾pany A would agree to make specified payments in euros to Citibank, while Citibank
made dollar payments to Company A. Citibank would charge a fee for setting up the
swap, and those charges would reflect the creditworthiness of Company A. To protect
itself against exchange rate movements, the bank would hedge its position, either by lining
up a European company that needed to make dollar payments or else by using currency
futures.23
Major changes have occurred over time in the swaps market. First, standardized
contracts have been developed for the most common types of swaps, which has had
two effects: (1) Standardized contracts lower the time and effort involved in arranging
swaps, and this lowers transactions costs. (2) The development of standardized contracts
has led to a secondary market for swaps, which has increased the liquidity and efficiency
of the swaps market. A number of international banks now make markets in swaps and
offer quotes on several standard types. The second major change is due to a provision in
FIGURE 23-2
The Antron/Bosworth Swap
Antron Bosworth
LIBOR
8.95%
Floating-Rate
Bondholders
Fixed-Rate
Bondholders
LIBOR
+ 1% 
10.4%
Fixed
23For more information on swaps, see Keith C. Brown and Donald J. Smith, “Default Risk and Innovations in the
Design of Interest Rate Swaps,” Financial Management, Summer 1993, pp. 94–105; Robert Einzig and Bruce
Lange, “Swaps at Transamerica: Applications and Analysis,” Journal of Applied Corporate Finance, Winter 1990,
pp. 48–58; John F. Marshall, Vipul K. Bansal, Anthony F. Herbst, and Alan L. Tucker, “Hedging Business Cycle
Risk with Macro Swaps and Options,” Journal of Applied Corporate Finance, Winter 1992, pp. 103–108; and
Laurie S. Goodman, “The Uses of Interest Rate Swaps in Managing Corporate Liabilities,” Journal of Applied
Corporate Finance, Winter 1990, pp. 35–47.
934 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 972

```text
the Dodd-Frank Act mandating that certain standardized interest rate swaps be centrally
cleared rather than managed by banks. The Chicago Mercantile Group (CME) is one of
these clearing houses and as of October, 2014 the notional principal of the swaps out￾standing with CME totaled $23 trillion.
Most swaps today involve either interest payments or currencies, but just about
anything can be swapped, including equity swaps, credit spread swaps, and commodity
swaps.24
23-7c Inverse Floaters
A floating-rate note has an interest rate that rises and falls with some interest rate index.
For example, if the prime rate were currently 8.5%, then the interest rate on a $100,000
note at prime plus 1% would be 9.5% and the note’s rate would move up and down with
the prime rate. Because both the cash flows associated with the note and the discount rate
used to value it would rise and fall together, the market value of the note would be
relatively stable.
With an inverse floater, the rate paid on the note moves counter to market rates.
Thus, if interest rates in the economy rise, the interest rate paid on an inverse floater will
fall, reducing its cash interest payments. At the same time, the discount rate used to
value the inverse floater’s cash flows will rise along with other rates. The combined
effect of lower cash flows and a higher discount rate would lead to a large decline in the
value of the inverse floater. Thus, inverse floaters are exceptionally vulnerable to
increases in interest rates. Of course, if interest rates fall then the value of an inverse
floater will soar.
Could an inverse floater be used for hedging purposes? The answer is “yes, perhaps
quite effectively.” These securities have a magnified effect, so not many are required to
hedge a given position. However, because they are so volatile, they could make what is
supposed to be a hedged position quite risky.
SELF-TEST
Explain how a company can use Treasury bond futures to hedge against rising interest rates.
What is an interest rate swap? Describe the mechanics of a fixed-rate to floating-rate swap.
A Treasury bond futures contract is selling for 94ʹ16. What is the implied annual yield? (6.5%)
Messman Corporation issues fixed-rate debt at a rate of 9.00%. Messman agrees to an interest
rate swap in which it pays LIBOR to Moore Inc. and Moore pays 8.75% to Messman. What is
Messman’s resulting net payment? (LIBOR + 0.25%)
23-8 Project Selection Risks
A project is any corporate undertaking that uses corporate assets such as cash,
factories, buildings, equipment, IT infrastructure, intellectual property, and people.
A successful project creates value by generating a return that is commensurate with
the size and risk of the assets invested in the project. Perhaps the most important
factor for a company’s success is its ability to select value-adding projects and avoid
value-destroying projects.
24In an equity swap, the cash flow based on an equity index is swapped for some other cash flow. In a commodity
swap, the swapped cash flow is based on commodity prices. In a credit swap, the cash flow usually is based on the
spread between a risky bond and a U.S. Treasury bond.
Chapter 23 Enterprise Risk Management 935
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 973

```text
23-8a Using Monte Carlo Simulation to Evaluate
Project Risk
When evaluating a potential project, a company should assess the project qualitatively and
quantitatively using the three-step approach we described in Chapters 10 and 11: (1)
Forecast the project’s future cash flows. (2) Estimate the value of the cash flows. (3)
Analyze the risk of the cash flows.25 Small projects, such as the replacement of a single
machine, require less analysis than large projects, which include major capital expendi￾tures, product line extensions, new products, geographic expansion, acquisitions, and
mergers.
For larger projects, it is absolutely vital to conduct a thorough risk analysis, including
sensitivity analysis and scenario analysis, as described in Chapter 11. Very large projects
require even more risk analysis, including Monte Carlo simulation, which is widely used
in enterprise risk management—you can’t manage a risk very well if you can’t measure it!
We repeat here some of the results from the simulation analysis in Chapter 11, and we
include some new results. Recall that the analysis in Chapter 11 was for the application of
a radically new liquid nano-coating technology to a new type of solar water heater
module. We projected cash flows for the project, calculated NPV and other evaluation
measures, performed a sensitivity analysis, and did a scenario analysis; see Section 11-2 for
the basic analysis and Sections 11-5 and 11-6 for the sensitivity and scenario analyses.
We conducted a Monte Carlo simulation analysis in Section 11-7. Recall that in a
simulation analysis, a probability distribution is assigned to each input variable—sales in
units, the sales price, the variable cost per unit, and so on. The computer begins by picking
a random value for each variable from its probability distribution. Those values are then
entered into the model, the project’s NPV (and any other measures) is calculated, and the
NPV is stored in the computer’s memory. This is called a trial. After completing the first
trial, a second set of input values is selected from the input variables’ probability
distributions, and a second NPV is calculated. This process is repeated until there are
enough observations that the estimated NPV and any other outcome measures are stable.
We replicated the simulation analysis from Chapter 11 with 10,000 iterations; see
Ch23 Tool Kit.xlsx and look in the worksheet Simulation. Figure 23-3 reports the
estimated evaluation measures from Chapter 11 and some additional measures.26 The
measures from Chapter 11 for NPV include its average, standard deviation, max￾imum, minimum, median, and the probability that the NPV will be positive. Based on
these measures, the project has a positive expected NPV and will break even about
57% of the time.
In addition to the evaluation measures from Chapter 11, enterprise risk management
systems often use another measure called value at risk (VaR). Using the trials from the
simulation analysis, the company specifies a threshold, such as the bottom 1% or 5% of
outcomes. The basic idea is to measure the value of the project if things go badly.
For example, Figure 23-3 shows that there is a 5% chance that the project will lose
$6.626 million or more (the values are reported in thousands) and a 1% chance that the
project will lose $9.472 million or more.
The VaR measures are helpful, but they don’t measure the extent of possible losses if things
go badly. A measure that many companies now apply is the conditional value at risk (CVaR); it
25Recall from Chapter 10 that cash flow evaluation methods include the net present value (NPV), the internal
rate of return (IRR), the modified internal rate of return (MIRR), the profitability index (PI), the payback period,
and the discounted payback period.
26The values of the measures will be different in this figure than in Figure 11-7 since these results are from
another run of 10,000 trials for the simulation. Each new run of the simulation will give slightly different results.
936 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 974

```text
is also called the expected shortfall, the expected tail loss (ETL), and the average
value at risk (AVaR). The CVaR measures the average NPV of all outcomes below
the threshold—it is the average NPV conditional upon the NPV being less than the
threshold value.27 For example, the CVaR for the 1% threshold is −$10.950 million,
which means that if the worst 1% of outcomes occur, the expected loss is $10.950 million.
Notice that the VaR calculation is not affected by the size of the losses below the
threshold—it just tells you size of the loss at the threshold percentile. In contrast, the
CVaR takes into account the size of the losses below the threshold—it shows the expected
loss if things go badly.
Many companies now are applying simulation when they analyze mergers and
acquisition. In addition to the quantitative output from a simulation analysis, the process
of identifying sources of risk can help companies avoid costly mistakes.
FIGURE 23-3
An Example of Monte Carlo Simulation Applied to Project Analysis (Thousands of Dollars)
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
A B C D E FG
Number of T rials: 10,000
NPV
A 612,1$egarev VPN at 5th percentile $6,626
Standard deviation $5,162 Average NPV below 5th percentile $8,343
M 215,52$mumixa VPN at 1st percentile $9,472
Minimum $16,775 Average NPV below 1st percentile $10,950
naideM 458$ 94.0ssenwekS
Probability of NPV > 0 57.0%
Coefficient of variation 4.25
Summary Statistics for
Simulated Results
–25,512 –12,756 0 12,756 25,512
Probability
NPV ($) 193
194
27This definition is correct when applying CVaR to the outcomes from a Monte Carlo simulation because there is
an equal probability of each outcome. It is a little more complicated to calculate CVaR from a given probability
distribution than it is from the outcomes of a simulation.
Chapter 23 Enterprise Risk Management 937
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 975

```text
23-8b Using Monte Carlo Simulation to Evaluate
Financing Risks
Companies use simulation for purposes other than project analysis. For example, the
Danish maker of the popular plastic building-brick toys, the LEGO Group, also uses
simulation in its budgeting process to show the possible outcomes. CFO Hans Læssøe
reports that simulation analysis revealed that sales volatility has a much bigger impact
than top managers previously understood.28
Simulation also is helpful when a company prepares a cash budget such as the one we
described in Chapter 16. Rather than just showing the expected short-term financing
requirements, simulation can show the probabilities of a larger financing requirement,
allowing companies to plan for previously unexpected credit needs.
23-8c Using Monte Carlo Simulation to Evaluate
Portfolio Risks
Many companies are exposed to portfolio risk, which is the risk that a portfolio of
financial assets will decrease in value. For example, many companies offer pension plans
to their employees. Defined benefit plans have a portfolio of stocks, bonds, and other
financial assets that is used to support promised pension benefits to its employees. Such
companies are exposed to significant portfolio risk—if the value of the pension assets
portfolio drops too much relative to the value of the promised pension benefits, then the
company will have to use its other resources to make additional contributions to the plan.
Most financial institutions are also exposed to portfolio risk because they own
financial assets and have financial liabilities. Simulation is a widely used tool for measur￾ing a bank’s portfolio risk. In fact, the Basel II and III accords require banks to report their
VaR and the Basel Committee is presently (2015) considering requiring banks to also
report the expected shortfall (the CVaR).
When the trading and risk management groups at financial institutions use VaR (or
CVaR), they usually measure it over a very short time horizon because they want to know
how much they might lose overnight or within a couple of days.
SELF-TEST
What is Monte Carlo simulation?
What is value at risk, VaR? What is conditional value at risk, CVaR?
23-9 Managing Credit Risks
Nonfinancial companies are exposed to risk if they extend credit to their customers, and
financial institutions are exposed to credit risk when they lend to their customers.
Following are some key concepts in the management of credit risk.
23-9a Managing Credit Risk at Nonfinancial
Companies
As we described in Chapter 16, when a company sells a product to a customer but does
not require immediate payment, an account receivable is created. There are three primary
tools that companies use to manage this credit risk.
28See the paper by Mark Frigo and Hans Læssøe cited in footnote 10.
938 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 976

```text
First, a company evaluates its customers before extending credit. The company can do
its own evaluation or purchase an evaluation from a third party. If the customer is an
individual, credit evaluations are available from several companies, including as Equifax,
Experian, and TransUnion. Each of these companies provides a numerical score, with the
FICO score being the most widely used. The score ranges from 300 to 850, with lower
scores indicating that the customer is more likely to default.
When the customer is another company, the evaluation is conducted using many of
the same ratios and analyses we described in Chapter 3. In addition, some companies
create their own credit scoring models based on past experience or statistical models (such
as multiple discriminant analysis).
A company can mitigate its credit risk by selling its accounts receivable to a third
party in a process called factoring. Of course, the price a company receives from selling its
receivables depends on the receivables’ risk, with riskier receivables purchased for much
less than their nominal value. A company can also buy insurance for some or all of its
receivables. Many companies, including the LEGO Group, use simulation to estimate the
risk of their receivables so that they can better negotiate with insurers.
23-9b Managing Credit Risk at Financial
Institutions
In addition to the same techniques used at nonfinancial corporations (credit scoring
models and simulation), many financial institutions use credit default swaps (CDS). Even
though CDS are called swaps, they are like insurance. For example, an investor (which
might be a financial institution) might purchase a CDS by making an annual payment to a
counterparty to insure a particular bond or other security against default; if the bond
defaults, the counterparty pays the purchaser the amount of the defaulted bond that was
insured.
The CDS “price” is quoted in basis points and is called the CDS spread. For
example, the spread on Unitymedia KabelBW GmbH, a German cable operator, was
about 271 basis points in May 2014. An easy way to interpret the reported basis point
spread is that it would be the annual fee in dollars (or euros) to protect $10,000 (or
euros) of the bond. Therefore, it would cost €271 per year to insure €10,000 of
Unitymedia’s bonds.
To protect €10 million of Unitymedia’s debt, a buyer would pay €271,000
0 0271 €10 million per year. In contrast, the spread on the automobile manufacturer
BMW’s bonds was only 42 basis points, so insuring €10 million of BMW’s debt would
cost only €42,000 per year. If the investors owned the bonds, then the purchase of the
CDS would reduce the investor’s risk.
There is an active secondary market for CDS, and it is not necessary to own the underlying
security. In fact, most participants in the CDS market don’t own the underlying securities. For
example, a speculator might purchase a CDS on Unitymedia for 271 basis points but only
purchase coverage for 1 month, which would be a payment of €22,583 €271,000 12. Now
suppose the Eurozone’s problems immediately worsened and drove Unitymedia’s CDS spread
up to 300 basis points. The investor could liquidate the position by selling 1-month credit
protection for €25,000 €300,000 12 and use the previously purchased CDS to offset the
newly sold CDS. The investor’s profit would be €2,417.
In addition to CDS for individual securities, there are CDS for indices. For example,
the CDX.NA.IG is an index of 125 CDS for North American investment-grade debt. The
index’s movements are positively correlated with the overall level of default for many
commercial loans—the index goes up when defaults increase. Therefore, a U.S. bank can
www
See the Markit Group
Limited’s Web site for
updates on CDS data.
Free registration allows
access to a variety of
current data, including
indexes: www.markit
.com/en.
Chapter 23 Enterprise Risk Management 939
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 977

```text
protect itself from increasing default rates in its loan portfolio by taking a short position in
the CDX.NA.IG. If defaults increase, then the index goes up, which means a short investor
can profit by selling the now higher priced index at the lower price specified in the
original short position. This is a situation in which the CDS help reduce a financial
institution’s risk—when defaults increase, the institution loses money on it loans but
makes money on the index. Of course, if the index falls, then the bank loses on the short
position but wins on its own loan portfolio because there are fewer defaults.
Recall from the opening vignette that JPMorgan took long positions in a particular
series of the CDX.NA.IG, which certainly wasn’t to hedge its loan portfolios. JPMorgan
explained that it was to hedge other derivatives that were hedging its loan portfolio, which
sounds very complicated—no wonder it didn’t work!
When banks and other major financial institutions take positions in swaps and CDS,
they are themselves exposed to various risks, especially if their counterparties cannot meet
their obligations. Furthermore, swaps are off–balance sheet transactions, making it
impossible to tell just how large the swap market is or who has what obligation. The
Bank of International Settlements estimates that as of the end of 2014 the notional value
of all CDS was $16 trillion. As we write this in the summer of 2015, the SEC and the
Commodity Futures Trading Commission (CFTC) continue implementation of provi￾sions in Title VII of the 2010 Dodd-Frank Act to improve transparency in the swaps
markets. Standardized interest-rate and credit-default swaps must now be centrally
cleared and the market is working to develop new products that provide the same benefits
as these swaps, but with lower counterparty risk.29
Credit default swaps are traded on government debt as well as corporate debt. Before
2008, a CDS on a 5-year U.S. Treasury bond was trading at less than 7 basis points, which
would be a $7 annual fee to protect $10,000 of the bond. The CDS price increased to
almost 100 basis points in 2009, and is currently (May 2015) trading around 20 basis
points. Figure 23-4 shows the prices for the U.S. and selected European countries, some
that have adopted the euro (Germany, France, Italy, Spain, and Portugal) and some that
have not. The extremely high prices for Eurozone debt indicate the problems facing these
countries.
SELF-TEST
Describe some ways to manage credit risk at a nonfinancial company.
What are credit default swaps?
23-10 Risk and Human Safety
Risk management decisions, like all corporate decisions, should begin with a cost–benefit
analysis for each feasible alternative. For example, suppose it would cost $50,000 per year
to conduct a comprehensive fire safety training program for all personnel in a high-risk
plant. Presumably, this program would reduce the expected value of future fire losses. An
alternative to the training program would be to place $50,000 annually in a reserve fund
set aside to cover future fire losses. Both alternatives involve expected cash flows, and
from an economic standpoint the choice should be made on the basis of the lowest
present value of future costs.
29See the presentation “Swaps Regulation under Dodd-Frank’s Title VII: Recent Developments” given March 6,
2014, by David Kaufman, Anna Pinedo, James Schwartz, and Michael Sefton at www.mofo.com/files/Uploads/
Images/140306-Swaps-Regulation-under-Dodd-Franks-Title-VII.pdf.
940 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 978

```text
However, suppose a fire occurs and a life is lost. In situations involving safety and
health, the trade-off between expected profits and expected losses is not sufficient for
making sound decisions. Companies must always consider the impact their decisions have
on the safety of their employees and customers. Ignoring safety and health is an ethical
mistake, but it also is a business mistake because many companies have been forced out of
business or suffered debilitating losses when they produced unsafe products.
SELF-TEST
Describe a situation in risk management that involves ethical as well as financial issues.
SUMMARY
The key concepts in enterprise risk management are listed here.
• Enterprise risk management (ERM) includes risk identification, risk assessment, and
risk responses.
• A derivative is a security whose value is determined by the market price or interest rate
of some other security.
• Risk management allows corporations: (1) to increase their use of debt, (2) to maintain
their capital budget over time, (3) to avoid costs associated with financial distress, (4) to
utilize their comparative advantages in hedging relative to the hedging ability of
individual investors, (5) to reduce both the risks and costs of borrowing by using swaps,
and (6) to reduce the higher taxes that result from fluctuating earnings. Managers may
also want to stabilize earnings in order to boost their own compensation.
FIGURE 23-4
Credit Default Swap Spreads for Sovereign Debt (April 13, 2015)
Basis Points
Sweden
UK
U.S.
Japan
Spain
Hungary
Portugal
China
India
Dubai
Egypt
0
50
100
150
200
250
300
350
Source: CNBC News, www.cnbc.com/id/38451750.
Chapter 23 Enterprise Risk Management 941
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 979

```text
• Risk responses include: (1) avoiding the activity, (2) reducing the probability of
occurrence of an adverse event, (3) reducing the magnitude of the loss associated with
an adverse event, (4) transferring the risk to an insurance company, (5) transferring the
function that produces the risk to a third party, and (6) sharing the risk by purchasing a
derivative contract.
• Major categories of risk include: (1) strategy and reputation, (2) control and
compliance, (3) hazards, (4) human resources, (5) operation, (6) technology, and (7)
financial management.
• Types of financial risk include: (1) foreign exchange risk, (2) commodity price risk, (3)
interest rate risk, (4) project selection risk, (5) liquidity risk, (6) customer credit risk,
and (7) portfolio risk.
• A hedge is a transaction that lowers risk. A natural hedge is a transaction between two
counterparties whose risks are mirror images of each other.
• A futures contract is a standardized contract that is traded on an exchange and is
marked-to-market daily, although physical delivery of the underlying asset usually does
not occur.
• Under a forward contract, one party agrees to buy a commodity at a specific price and
a specific future date and the other party agrees to make the sale; delivery does occur.
• A swap is an exchange of cash payment obligations. Swaps occur because the parties
involved prefer the other’s payment stream.
• Financial futures permit firms to create hedge positions to protect themselves against
fluctuating interest rates, stock prices, and exchange rates.
• Commodity futures can be used to hedge against input price increases.
• Long hedges involve buying futures contracts to guard against price increases.
• Short hedges involve selling futures contracts to guard against price declines.
• Symmetric hedges protect against price increases and price decreases. Futures contracts
are frequently used for symmetric hedges.
• Asymmetric hedges protect against price movements in one direction more than
movements in another. Options are frequently used for asymmetric hedges.
• A perfect hedge occurs when the gain or loss on the hedged transaction exactly offsets
the loss or gain on the unhedged position.
QUESTIONS
(23-1) Define each of the following terms:
a. Derivatives
b. Enterprise risk management
c. Financial futures; forward contract
d. Hedging; natural hedge; long hedge; short hedge; perfect hedge; symmetric hedge;
asymmetric hedge
e. Swap; structured note
f. Commodity futures
942 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 980

```text
(23-2) Give two reasons why stockholders might be indifferent between owning the stock of a
firm with volatile cash flows and that of a firm with stable cash flows.
(23-3) List six reasons why risk management might increase the value of a firm.
(23-4) Discuss some of the techniques available to reduce risk exposures.
(23-5) Explain how the futures markets can be used to reduce interest rate risk and input
price risk.
(23-6) How can swaps be used to reduce the risks associated with debt contracts?
SELF-TEST PROBLEM Solution Shown in Appendix A
(ST-1) It is now March, and the current cost of debt for Wansley Construction is 12%. Wansley
plans to issue $5 million in 20-year bonds (with coupons paid semiannually) in Septem￾ber, but it’s afraid that rates will climb even higher before then. The following data are
available:
a. What is the implied interest rate on the September contract?
b. Construct a hedge for Wansley.
c. Assume all interest rates rise by 1 percentage point. What is the dollar value of Wansley’s
increased cost of issuing debt? What is Wansley’s gain from the futures contract?
PROBLEMS Answers Are in Appendix B
EASY PROBLEMS 1–2
Zhao Automotive issues fixed-rate debt at a rate of 7.00%. Zhao agrees to an interest rate
swap in which it pays LIBOR to Lee Financial and Lee pays 6.8% to Zhao. What is
Zhao’s resulting net payment?
A Treasury bond futures contract has a settlement price of 89'08. What is the implied
annual yield?
INTERMEDIATE PROBLEMS 3–4
What is the implied interest rate on a Treasury bond ($100,000) futures contract that
settled at 100'16? If interest rates increased by 1%, what would be the contract’s new
value?
Carter Enterprises can issue floating-rate debt at LIBOR 2% or fixed-rate debt at 10%.
Brence Manufacturing can issue floating-rate debt at LIBOR 3 1% or fixed-rate debt at 11%.
Futures Prices: Treasury Bonds—$100,000; Pts. 32nds of 100%
Delivery Month
(1)
Open
(2)
High
(3)
Low
(4)
Settle
(5)
Change
(6)
Mar 96'28 97'13 97'22 98'05 7
June 98'03 98'03 97'13 97'25 8
Sept 97'03 97'17 97'03 97'13 8
Hedging
(23-1)
Swaps
(23-2)
Futures
(23-3)
Futures
(23-4)
Swaps
Chapter 23 Enterprise Risk Management 943
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 981

```text
Suppose Carter issues floating-rate debt and Brence issues fixed-rate debt. They are
considering a swap in which Carter makes a fixed-rate payment of 7.95% to Brence and
Brence makes a payment of LIBOR to Carter. What are the net payments of Carter and Brence
if they engage in the swap? Would Carter be better off if it issued fixed-rate debt or if it issued
floating-rate debt and engaged in the swap? Would Brence be better off if it issued floating-rate
debt or if it issued fixed-rate debt and engaged in the swap? Explain your answers.
CHALLENGING PROBLEM 5
The Zinn Company plans to issue $10,000,000 of 20-year bonds in June to help finance a
new research and development laboratory. The bonds will pay interest semiannually. It is
now November, and the current cost of debt to the high-risk biotech company is 11%.
However, the firm’s financial manager is concerned that interest rates will climb even
higher in coming months. The following data are available:
a. Use the given data to create a hedge against rising interest rates.
b. Assume that interest rates in general increase by 200 basis points. How well did your
hedge perform?
c. What is a perfect hedge? Are any real-world hedges perfect? Explain.
SPREADSHEET PROBLEM
(23-6) Start with the partial model in the file Ch23 P06 Build a Model.xlsx on the textbook’s
Web site. Use the following information and data.
F. Pierce Products Inc. is financing a new manufacturing facility with the issue in
March of $20,000,000 of 20-year bonds with semiannual interest payments. It is now
October, and if Pierce were to issue the bonds now, the yield would be 10% because of
Pierce’s high risk. Pierce’s CFO is concerned that interest rates will climb even higher in
coming months and is considering hedging the bond issue. The following data are
available:
Futures Prices: Treasury Bonds—$100,000; Pts. 32nds of 100%
Delivery
Month
(1)
Open
(2)
High
(3)
Low
(4)
Settle
(5)
Change
(6)
Open
Interest
(7)
Dec 93'28 94'13 93'22 94'05 0'06 723,946
Mar 95'03 95'03 94'13 94'25 0'07 97,254
a. Create a hedge with the futures contract for Pierce’s planned March debt offering of
$20 million using the March Treasury bond futures contract. What is the implied
yield on the bond underlying the futures contract?
Futures Prices: Treasury Bonds—$100,000; Pts. 32nds of 100%
Delivery
Month
(1)
Open
(2)
High
(3)
Low
(4)
Settle
(5)
Change
(6)
Open
Interest
(7)
Dec 94'28 95'13 94'22 95'05 0'07 591,944
Mar 96'03 96'03 95'13 95'25 0'08 120,353
June 95'03 95'17 95'03 95'17 0'08 13,597
(23-5)
Hedging
Build a Model:
Hedging
resource
944 Part 9 Strategic Finance in a Dynamic Environment
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 982

```text
b. Suppose that interest rates fall by 300 basis points. What are the dollar savings from
issuing the debt at the new interest rate? What is the dollar change in value of the
futures position? What is the total dollar value change of the hedged position?
c. Create a graph showing the effectiveness of the hedge if the change in interest rates,
in basis points, is −300, −200, −100, 0, 100, 200, or 300. Show the dollar cost (or
savings) from issuing the debt at the new interest rates, the dollar change in value of
the futures position, and the total dollar value change.
MINI CASE
Assume you have just been hired as a financial analyst by Tennessee Sunshine Inc. (TS), a
mid-sized Tennessee company that specializes in creating exotic sauces from imported
fruits and vegetables. The firm’s CEO, Bill Stooksbury, recently returned from an industry
corporate executive conference in San Francisco, and one of the sessions he attended was
on the pressing need for companies to institute enterprise risk management programs.
Because no one at Tennessee Sunshine is familiar with the basics of enterprise risk
management, Stooksbury has asked you to prepare a brief report that the firm’s executives
could use to gain at least a cursory understanding of the topics.
To begin, you gathered some outside materials on derivatives and risk management
and used these materials to draft a list of pertinent questions that need to be answered. In
fact, one possible approach to the paper is to use a question-and-answer format. Now that
the questions have been drafted, you have to develop the answers.
a. Why might stockholders be indifferent to whether or not a firm reduces the volatility
of its cash flows?
b. What are six reasons risk management might increase the value of a corporation?
c. What is COSO? How does COSO define enterprise risk management?
d. Describe the eight components of the COSO ERM framework.
e. Describe some of the risks events within the following major categories of risk:
(1) strategy and reputation, (2) control and compliance, (3) hazards, (4) human
resources, (5) operations, (6) technology, and (7) financial management.
f. What are some actions that companies can take to minimize or reduce risk
exposures?
g. What are forward contracts? How can they be used to manage foreign exchange risk?
h. Describe how commodity futures markets can be used to reduce input price risk.
i. It is January, and Tennessee Sunshine is considering issuing $5 million in bonds in
June to raise capital for an expansion. Currently, the firm can issue 20-year bonds
with a 7% coupon (with interest paid semiannually), but interest rates are on the rise
and Stooksbury is concerned that long-term interest rates might rise by as much as
1% before June. You looked online and found that June T-bond futures are trading at
111'25. What are the risks of not hedging, and how might TS hedge this exposure? In
your analysis, consider what would happen if interest rates all increased by 1%.
j. What is a swap? Suppose two firms have different credit ratings. Firm Hi can borrow
fixed at 11% and floating at LIBOR 1%. Firm Lo can borrow fixed at 11.4% and
floating at LIBOR 1 5%. Describe a floating versus fixed interest rate swap between
firms Hi and Lo in which Lo also makes a “side payment” of 45 basis points to Firm L.
Chapter 23 Enterprise Risk Management 945
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

## Halaman PDF 983

```text
Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.

`Ìi`ÊÜÌ
ÊÌ
iÊ`iÊÛiÀÃÊvÊ
vÝÊ*ÀÊ*
Ê
`ÌÀ
/ÊÀiÛiÊÌ
ÃÊÌVi]ÊÛÃÌ\Ê
ÜÜÜ°Vi°VÉÕV°
Ì
```

