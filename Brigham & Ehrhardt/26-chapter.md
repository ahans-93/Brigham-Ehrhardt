# Chapter 26: Real Options

[Daftar isi](SUMMARY.md) · [Panduan belajar](KAJIAN.md)

Sumber: PDF halaman 1052–1077. Teks ekstraksi; simbol, tabel, dan rumus belum seluruhnya diverifikasi secara visual.

## Halaman PDF 1052

```text
CHAPTER 26
Real Options
Honda Motor Company spent $400 million dollars on something it might not need—
production flexibility. If demand for its vehicles changed in predictable ways, then
Honda would have wasted the $400 million dollars. But as we have seen in the global
economic recession, demand for automobiles is highly volatile, with consumer pre￾ferences swinging wildly every time oil prices change. To prepare for such volatility,
Honda has been building flexibility into its factories and now boasts the most
flexibility of any automaker in the United States.
Honda’s plant in Liberty, Ohio, can stop Civic production, set up for the CR-V
crossover, and start producing CR-Vs in less than 10 minutes, incurring virtually no
additional cost in the process. Many of its other plants have similar capabilities. For
example, Honda has been able to quickly reduce output of its Ridgeline pickup truck
and boost production of more fuel-efficient vehicles. In contrast, Ford will take over a
year to convert a factory now producing gas-guzzling sport utility vehicles, with the
switchover costing over $75 million. GM has similar problems and will spend $370 million
to change models at one of its factories.
Honda’s flexibility stems from several factors, beginning with designs for vehicles
and production processes that share components and assembly techniques. For
example, the assembly process for doors is very similar, no matter what vehicle is
being produced. Honda’s robots also give it flexibility. For example, the same robots
are used to weld different vehicles.
It costs more initially to build in flexibility at a factory, but the payoff can be well
worth the cost. As you read this chapter and learn more about options, think about
how option pricing techniques can lead to better capital budgeting decisions.
Source: Kate Linebaugh, “Honda’s Flexible Plants Provide Edge,” The Wall Street Journal, September 23,
2008, p. B1.
1015
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

## Halaman PDF 1053

```text
Traditional discounted cash flow (DCF) analysis—in which an asset’s cash flows are
estimated and then discounted to obtain the asset’s NPV—has been the cornerstone for
valuing all types of assets since the 1950s. Accordingly, most of our discussion of capital
budgeting has focused on DCF valuation techniques. However, in recent years, academics
and practitioners have demonstrated that DCF valuation techniques do not always tell the
complete story about a project’s value and that rote use of DCF can, at times, lead to
incorrect capital budgeting decisions.1
DCF techniques were originally developed to value securities such as stocks and
bonds. Securities are passive investments: Once they have been purchased, most
investors have no influence over the cash flows the assets produce. However, real assets
are not passive investments, because managerial actions after an investment has been
made can influence its results. Furthermore, investing in a new project often brings
with it the potential for increasing the firm’s future investment opportunities. Such
opportunities are, in effect, options—the right (but not the obligation) to take some
action in the future. As we demonstrate in the next section, options are valuable, so
projects that expand the firm’s set of opportunities have positive option values.
Similarly, any project that reduces the set of future opportunities destroys option value.
A project’s impact on the firm’s opportunities, or its option value, may not be captured
by conventional NPV analysis, so this option value should be considered separately, as
we do in this chapter.
26-1 Valuing Real Options
Recall from Chapter 11 that real options are opportunities for management to change the
timing, scale, or other aspects of an investment in response to changes in market
conditions. These opportunities are options in the sense that management can, if it is in
the company’s best interest, undertake some action; management is not required to
undertake the action. These opportunities are real (as opposed to financial) because they
involve decisions regarding real assets—such as plants, equipment, and land—rather than
financial assets like stocks or bonds. Four examples of real options are investment timing
options, growth options, abandonment options, and flexibility options. This chapter
provides an example of how to value an investment timing option and a growth option.
Web Extension 26A on the textbook’s Web site shows how to value an abandonment
option, which allows a company to reduce a project’s capacity or drop the project entirely
if market conditions deteriorate.
Valuing a real option requires judgment, both to formulate the model and to
estimate the inputs. Does this mean the answer won’t be useful? Definitely not. For
example, the models used by NASA only approximate the centers of gravity for the
moon, the Earth, and other heavenly bodies, yet even with these “errors” in their
models, NASA has been able to put astronauts on the moon. As one professor said,
“All models are wrong, but some are still quite useful.” This is especially true for real
options. We might not be able to find the exact value of a real option, but the value we
find can be helpful in deciding whether or not to accept the project. Equally important,
the process of looking for and then valuing real options often identifies critical issues
that might otherwise go unnoticed.
1
For an excellent general discussion of the problems inherent in discounted cash flow valuation techniques as
applied to capital budgeting, see Avinash K. Dixit and Robert S. Pindyck, “The Options Approach to Capital
Investment,” Harvard Business Review, May/June 1995, pp. 105–115.
resource
The textbook’s Web site
contains an Excel file
that will guide you
through the chapter’s
calculations. The file for
this chapter is Ch26
Tool Kit.xlsx, and we
encourage you to open
the file and follow along
as you read the chapter.
1016 Part 10 Special Topics
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

## Halaman PDF 1054

```text
Five possible procedures can be used to deal with real options. Starting with the
simplest, they are as follows:
1. Use discounted cash flow (DCF) valuation and ignore any real options by assuming
their values are zero.
2. Use DCF valuation and include a qualitative recognition of any real option’s value.
3. Use decision-tree analysis.
4. Use a standard model for a financial option.
5. Develop a unique, project-specific model using financial engineering techniques.
The following sections illustrate these procedures.
SELF-TEST
List the five possible procedures for dealing with real options.
26-2 The Investment Timing Option: An Illustration
There is frequently an alternative to investing immediately—the decision to invest or not
can be postponed until more information becomes available. By waiting, a better￾informed decision can be made, and this investment timing option adds value to the
project and reduces its risk.
Murphy Systems is considering a project for a new type of handheld device that
provides wireless Internet connections. The cost of the project is $50 million, but the
future cash flows depend on the demand for wireless Internet connections, which is
uncertain. Murphy believes there is a 25% chance that demand for the new device will
be high, in which case the project will generate cash flows of $33 million each year for
3 years. There is a 50% chance of average demand, with cash flows of $25 million per year,
and a 25% chance that demand will be low and annual cash flows will be only $5 million.
A preliminary analysis indicates that the project is somewhat riskier than average, so it has
been assigned a cost of capital of 14% versus 12% for an average project at Murphy
Systems. Here is a summary of the project’s data:
Demand Probability Annual Cash Flow
High 0.25 $33 million
Average 0.50 25 million
Low 0.25 5 million
Expected annual cash flow $22 million
Project’s cost of capital 14%
Life of project 3 years
Required investment, or cost of project $50 million
Murphy could accept the project and implement it immediately; however, because the
company has a patent on the device’s core modules, it could also choose to delay the
decision until next year, when more information about demand will be available. The cost
will still be $50 million if Murphy waits, and the project will still be expected to generate
the indicated cash flows, but each flow will be pushed back 1 year. However, if Murphy
waits, then it will know which of the demand conditions—and hence which set of cash
flows—will occur. If Murphy waits, then it will, of course, make the investment only if
demand is sufficient to yield a positive NPV.
resource
All calculations for the
analysis of the
investment timing option
are shown in Ch26 Tool
Kit.xlsx on the
textbook’s Web site.
Chapter 26 Real Options 1017
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

## Halaman PDF 1055

```text
Observe that this real timing option resembles a call option on a stock. A call gives its
owner the right to purchase a stock at a fixed strike price, but only if the stock’s price is
higher than the strike price will the owner exercise the option and buy the stock. Similarly,
if Murphy defers implementation, then it will have the right to “purchase” the project by
making the $50 million investment if the NPV as calculated next year, when new
information is available, is positive.
26-2a Approach 1: DCF Analysis Ignoring the
Timing Option
Based on probabilities for the different levels of demand, the expected annual cash flows
are $22 million per year:
Expected cash flow per year 0 25 $33 0 50 $25 0 25 $5
$22 million
Ignoring the investment timing option, the traditional NPV is $1.08 million, found as
follows:
NPV $50 $22
1 0 14 1
$22
1 0 14 2
$22
1 0 14 3 $1 08
The present value of the cash inflows is $51.08 million while the cost is $50 million,
leaving an NPV of $1.08 million.
Based just on this DCF analysis, Murphy should accept the project. Note, however,
that if the expected cash flows had been slightly lower—say, $21.5 million per year—then
the NPV would have been negative and the project would have been rejected. Also, note
that the project is risky: There is a 25% probability that demand will be weak, in which
case the NPV will turn out to be a negative $38.4 million.
26-2b Approach 2: DCF Analysis with a Qualitative
Consideration of the Timing Option
The discounted cash flow analysis suggests that the project should be accepted, but just
barely, and it ignores the existence of a possibly valuable real option. If Murphy imple￾ments the project now, it gains an expected (but risky) NPV of $1.08 million. However,
accepting now means that it is also giving up the option to wait and learn more about
market demand before making the commitment. Thus, the decision is this: Is the option
Murphy would be giving up worth more or less than $1.08 million? If the option is worth
more than $1.08 million, then Murphy should not give up the option, which means
deferring the decision—and vice versa if the option is worth less than $1.08 million.
Based on the discussion of financial options in Chapter 8, what qualitative assessment
can we make regarding the option’s value? Put another way: Without doing any additional
calculations, does it appear that Murphy should go forward now or wait? In thinking
about this decision, first note that the value of an option is higher if the current value of
the underlying asset is high relative to its strike price, other things held constant. For
example, a call option with a strike price of $50 on a stock with a current price of $50 (an
at-the-money call) is worth more than if the current price were $20 (an out-of-the-money
call). The strike price of the project is $50 million, and our first guess at the value of its
cash flows is $51.08 million. We will calculate the exact value of Murphy’s underlying
asset later, but the DCF analysis does suggest that the underlying asset’s value will be close
to the strike price, so the option should be valuable. We also know that an option’s value
1018 Part 10 Special Topics
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

## Halaman PDF 1056

```text
is higher the longer its time to expiration. Here the option has a 1-year life, which is fairly
long for an option, and this also suggests that the option is probably valuable. Finally, we
know that the value of an option increases with the risk of the underlying asset. The data
used in the DCF analysis indicate that the project is quite risky, which again suggests that
the option is valuable.
Thus, our qualitative assessment indicates that the option to delay might well be more
valuable than the expected NPV of $1.08 if we undertake the project immediately. This
conclusion is subjective, but the qualitative assessment suggests that Murphy’s manage￾ment should go on to make a quantitative assessment of the situation.
26-2c Approach 3: Scenario Analysis and
Decision Trees
Part 1 of Figure 26-1 presents a scenario analysis and decision tree similar to the
examples in Chapter 11. Each possible outcome is shown as a “branch” on the tree.
Each branch shows the cash flows and probability of a scenario laid out as a time line.
Thus, the top line, which gives the payoffs of the high-demand scenario, has positive
cash flows of $33 million for the next 3 years, and its NPV is $26.61 million. The average￾demand branch in the middle has an NPV of $8.04 million, while the NPV of the low￾demand branch is a negative $38.39 million. Because Murphy will suffer a $38.39 million
loss if demand is weak, and there is a 25% probability of weak demand, the project is
clearly risky.
The expected NPV is the weighted average of the three possible outcomes, where the
weight for each outcome is its probability. The weighted sum in the last column in
Part 1 shows that the expected NPV is $1.08 million, the same as in the original DCF
analysis. Part 1 also shows a standard deviation of $24.02 million for the NPV and a
coefficient of variation (defined as the ratio of standard deviation to the expected NPV)
of 22.32, which is extremely large. Clearly, the project is quite risky under the analysis
thus far.
Part 2 is set up similarly to Part 1 except that it shows what happens if Murphy delays
the decision and then implements the project only if demand turns out to be high or
average. No cost is incurred now at Year 0—here, the only action is to wait. Then, if
demand is average or high, Murphy will spend $50 million at Year 1 and receive either
$33 million or $25 million per year for the following 3 years. If demand is low, as shown
on the bottom branch, Murphy will spend nothing at Year 1 and will receive no cash flows
in subsequent years. The NPV of the high-demand branch is $23.35 million and that of
the average-demand branch is $7.05 million. Because all cash flows under the low￾demand scenario are zero, the NPV in this case will also be zero. The expected NPV if
Murphy delays the decision is $9.36 million.
This analysis shows that the project’s expected NPV will be much higher if Murphy
delays than if it invests immediately. Also, because there is no possibility of losing money
under the delay option, this decision also lowers the project’s risk. This plainly indicates
that the option to wait is valuable; hence, Murphy should wait until Year 1 before deciding
whether to proceed with the investment.
Before we conclude the discussion of decision trees, note that we used the same cost of
capital, 14%, to discount cash flows in the “proceed immediately” scenario analysis in Part 1
and under the “delay 1 year” scenario in Part 2. However, this is not appropriate for three
reasons. First, because there is no possibility of losing money if Murphy delays, the
investment under that plan is clearly less risky than if Murphy charges ahead today. Second,
the 14% cost of capital might be appropriate for risky cash flows, yet the investment in the
project at Year 1 in Part 2 is known with certainty. Perhaps, then, we should discount it at
Chapter 26 Real Options 1019
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

## Halaman PDF 1057

```text
the risk-free rate.2 Third, the project’s cash inflows (excluding the initial investment) are
different in Part 2 than in Part 1 because the low-demand cash flows are eliminated. This
suggests that if 14% is the appropriate cost of capital in the “proceed immediately” case,
then some lower rate would be appropriate in the “delay decision” case.
FIGURE 26-1
DCF and Decision-Tree Analysis for the Investment Timing Option (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision.
Thus, intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The WACC is 14%.
b
The expected value and standard deviation are calculated as explained in Chapter 6.
c
The coefficient of variation is the standard deviation divided by the expected value.
d
The NPV in Part 2 is as of Year 0. Therefore, each of the project cash flows is discounted back 1 more year than in Part 1.
2
For a more detailed explanation of the rationale behind using the risk-free rate to discount the project cost, see
Timothy A. Luehrman, “Investment Opportunities as Real Options: Getting Started on the Numbers,” Harvard
Business Review, July/August 1998, pp. 51–67. This paper also provides a discussion of real option valuation.
Professor Luehrman also wrote a follow-up paper that provides an excellent discussion of the ways real options
affect strategy:“Strategy as a Portfolio of Real Options,” Harvard Business Review, September/October 1998, pp. 89–99.
1020 Part 10 Special Topics
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

## Halaman PDF 1058

```text
In Figure 26-2, Part 1, we repeat the “delay decision” analysis but with one exception.
We continue to discount the operating cash flows in Year 2 through Year 4 at the 14%
WACC, but now we discount the project’s cost at Year 1 using the risk-free rate of 6%. This
increases the PV of the cost, which lowers the NPV from $9.36 million to $6.88 million. Yet
we really don’t know the precise WACC for this project—the 14% we used might be too
high or too low for the operating cash flows in Year 2 through Year 4.3 Therefore, in Part 2
FIGURE 26-2
Decision-Tree and Sensitivity Analysis for the Investment Timing Option (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The operating cash flows in Year 2 through Year 4 are discounted at the WACC of 14%. The cost in Year 1 is discounted at the risk-free rate of 6%.
b
The expected value and standard deviation are calculated as explained in Chapter 6.
c
The coefficient of variation is the standard deviation divided by the expected value.
3
Murphy might gain information by waiting, which could reduce risk, but if a delay would enable others to enter
and perhaps preempt the market, this could increase risk. In our example, we assumed that Murphy has a patent
on critical components of the device, precluding the entrance of a competitor that could preempt its position in
the market.
Chapter 26 Real Options 1021
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

## Halaman PDF 1059

```text
of Figure 26-2 we show a sensitivity analysis of the NPV in which the discount rates
used for both the operating cash flows and for the project’s cost vary. This sensitivity
analysis shows that, under all reasonable WACCs, the NPV of delaying is greater than
$1.08 million. This confirms that the option to wait is more valuable than the $1.08
million NPV resulting from immediate implementation. Therefore, Murphy should wait
rather than implement the project immediately.
26-2d Approach 4: Valuing the Timing Option with
the Black-Scholes Option Pricing Model
The decision-tree approach, coupled with a sensitivity analysis, may provide enough
information for a good decision. However, it is often useful to obtain additional insights
into the real option’s value, which means using the fourth procedure, an option pricing
model. To do this, the analyst must find a standard financial option that resembles the
project’s real option.4 As noted earlier, Murphy’s option to delay the project is similar to a
call option on a stock. Hence, the Black-Scholes option pricing model can be used. This
model requires five inputs: (1) the risk-free rate, (2) the time until the option expires,
(3) the strike price, (4) the current price of the stock, and (5) the variance of the stock’s
rate of return. Therefore, we need to estimate values for those five inputs.
First, if we assume that the rate on a 52-week Treasury security is 6%, then this rate
can be used as the risk-free rate. Second, Murphy must decide within a year whether or
not to implement the project, so there is 1 year until the option expires. Third, it will cost
$50 million to implement the project, so $50 million can be used for the strike price.
Fourth, we need a proxy for the value of the underlying asset, which in Black-Scholes is
the current price of the stock. Note that a stock’s current price is the present value of its
expected future cash flows. For Murphy’s real option, the underlying asset is the project
itself, and its current “price” is the present value of its expected future cash flows.
Therefore, as a proxy for the stock price we can use the present value of the project’s
future cash flows. And fifth, the variance of the project’s return can be used to represent
the variance of the stock’s return in the Black-Scholes model.
Figure 26-3 shows how to estimate the present value of the project’s cash inflows. We need
to find the current value of the underlying asset—that is, the project. For a stock, the current
price is the present value of all expected future cash flows, including those that are expected
even if we do not exercise the call option. Note also that the strike price for a call option has no
effect on the stock’s current price.5 For our real option, the underlying asset is the delayed
project, and its current “price” is the present value of all its future expected cash flows. Just as
the price of a stock includes all of its future cash flows, so should the present value of the project
include all of its possible future cash flows. Moreover, because the price of a stock is not affected
by the strike price of a call option, we ignore the project’s “strike price,” which is its
implementation cost, when we find its present value. Figure 26-3 shows the expected cash
flows if the project is delayed. The PV of these cash flows as of now (Year 0) is $44.80 million,
and this is the input we should use for the current price in the Black-Scholes model.
The last required input is the variance of the project’s return. Three different approaches
could be used to estimate this input. First, we could use judgment—an educated guess. Here,
we would begin by recalling that a company is a portfolio of projects (or assets), with each
project having its own risk. Because returns on the company’s stock reflect the diversification
4
In theory, financial option pricing models apply only to assets that are continuously traded in a market. Even
though real options usually don’t meet this criterion, financial option models often provide a reasonably accurate
approximation of the real option’s value.
5
The company itself is not involved with traded stock options. However, if the option were a warrant issued by
the company, then the strike price would affect the company’s cash flows and hence its stock price.
1022 Part 10 Special Topics
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

## Halaman PDF 1060

```text
gained by combining many projects, we might expect the variance of the stock’s returns to be
lower than the variance of one of its average projects. The variance of an average company’s
stock return is about 0.12, so we might expect the variance for a typical project to be
somewhat higher, say, 0.15 to 0.25. Companies in the Internet infrastructure industry are
riskier than average, so we might subjectively estimate the variance of Murphy’s project to be
in the range of 0.18 to 0.30.
The second approach, called the direct method, is to estimate the rate of return for
each possible outcome and then calculate the variance of those returns. First, Part 1 in
Figure 26-4 shows the PV for each possible outcome as of Year 1, the time when the
option expires. Here, we simply find the present value of all future operating cash flows
discounted back to Year 1, using the WACC of 14%. The Year-1 present value is
$76.61 million for high demand, $58.04 million for average demand, and $11.61 million
for low demand. Then, in Part 2, we show the percentage return from the current time until
the option expires for each scenario, based on the $44.80 million starting “price” of the
project at Year 0 as calculated in Figure 26-3. If demand is high, we will obtain a return of
71.0%: $76 61 $44 80 $44 80 0 710 71 0%. Similar calculations show returns of
29.5% for average demand and 74.1% for low demand. The expected percentage return is
14%, the standard deviation is 53.6%, and the variance is 0.287.6
The third approach for estimating the variance of the annual rate of return is also
based on the scenario data, but the data are used in a different manner. First, we know
FIGURE 26-3
Estimating the Input for Stock Price in the Option Analysis of the Investment Timing Option (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
Here we find the PV, not the NPV, because the project’s cost is ignored. The WACC is 14%. All cash flows in this scenario are discounted back to Year 0.
b
The expected value and standard deviation are calculated as explained in Chapter 6.
c
The coefficient of variation is the standard deviation divided by the expected value.
6
Two points should be made about the percentage return. First, for use in the Black-Scholes model, we need a
percentage return calculated as shown, not an IRR return. The IRR is not used in the option pricing approach.
Second, the expected return comes to 14%, the same as the WACC. This is because the Year-0 price and the
Year-1 PVs were all calculated using the 14% WACC and because we measured return over only 1 year. If we
measure the compound return over more than 1 year, then the average return generally will not equal 14%.
Chapter 26 Real Options 1023
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

## Halaman PDF 1061

```text
FIGURE 26-4
Estimating the Input for Variance in the Option Analysis of the Investment Timing Option (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The WACC is 14%. The Year-2 through Year-4 cash flows are discounted back to Year 1.
b
The expected value, variance, and standard deviation are calculated as explained in Chapter 6.
c
The coefficient of variation is the standard deviation divided by the expected value.
d
The Year-0 price is the expected PV from Figure 26-3.
e
The Year-1 PVs are from Part 1.
f
The returns for each scenario are calculated as PVYear 1 Price Year 0 Price Year 0.
g
The expected “price” at the time the option expires is taken from Part 1.
h
The standard deviation of expected “price” at the time the option expires is taken from Part 1.
1024 Part 10 Special Topics
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

## Halaman PDF 1062

```text
that demand is not really limited to three scenarios, which means the direct approach in
Figure 26-4 isn’t necessarily reliable. We could overcome this problem by estimating
thousands of scenarios, but that would require a lot of effort. Fortunately, there is a simple
shortcut we can use. From Part 1 of Figure 26-4, we have estimates of the expected value
of the project and its standard deviation at the time the option expires. Using this
information (and a lot of complicated mathematics), we can estimate the variance of
the project’s annual rate of return, σ2, with this formula:7
σ2 ln CV2 1
t
(26-1)
Here CV is the coefficient of variation of the underlying asset’s price at the time the
option expires, and t is the time until the option expires. Although the three outcomes
in the scenarios represent a small sample of the many possible outcomes, we can
still use the scenario data to estimate the variance that the project’s rate of return
would have if there were an infinite number of possible outcomes. For Murphy’s
project, this indirect method produces the following estimate of the variance of the
project’s return:
σ2 ln 0 472 1
1
0 20 (26-1a)
Which of the three approaches is best? Obviously, they all involve judgment, so an analyst
might want to consider all three. In our example, all three methods produce similar
estimates, but for illustrative purposes we will simply use 0.20 as our initial estimate for
the variance of the project’s rate of return.
In Part 1 of Figure 26-5, we calculate the value of the option to defer investment in the
project based on the Black-Scholes model, and the result is $7.04 million. Because this is
significantly higher than the $1.08 million NPV under immediate implementation and
because the option would be forfeited if Murphy goes ahead right now, we conclude as
before that the company should defer the final decision until more information is
available.
Many inputs were based on subjective estimates, so it is important to determine how
sensitive the final outcome is to key inputs. Therefore, in Part 2 of Figure 26-5 we show
the sensitivity of the option’s value to different estimates of the variance. It is reassuring to
see that, for all reasonable estimates of variance, the option to delay remains more
valuable than immediate implementation.
26-2e Approach 5: Financial Engineering
Sometimes an analyst might not be satisfied with the results of a decision-tree analysis and
cannot find a standard financial option that corresponds to the real option. In such a
situation the only alternative is to develop a unique model for the specific real option being
analyzed, a process called financial engineering. When financial engineering is applied on
7
For a more detailed discussion of the relationship between the variance of a stock’s price and the variance of its
return, see David C. Shimko, Finance in Continuous Time (Miami, FL: Kolb Publishing, 1992).
Chapter 26 Real Options 1025
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

## Halaman PDF 1063

```text
Wall Street, where it was developed, the result is a newly designed financial product.8 When it
is applied to real options, the result is the value of a project that contains embedded options.
Although financial engineering was originally developed on Wall Street, many financial
engineering techniques have been applied to real options during the last 20 years. We expect
this trend to continue, especially in light of the rapid improvements in computer processing
speed and spreadsheet software capabilities. One financial engineering technique is called risk￾neutral valuation. This technique uses simulation, and we discuss it in Web Extension 26B.
Most other financial engineering techniques are too complicated for a course in financial
management, so we leave a detailed discussion of them to a specialized course.
FIGURE 26-5
Estimating the Value of the Investment Timing Option Using a Standard Financial Option (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The current value of the project is taken from Figure 26-3.
b
The variance of the project’s rate of return is taken from Part 2 of Figure 26-4.
8
Financial engineering techniques are widely used for the creation and valuation of derivative securities.
1026 Part 10 Special Topics
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

## Halaman PDF 1064

```text
SELF-TEST
What is a decision tree?
In a qualitative analysis, what factors affect the value of a real option?
26-3 The Growth Option: An Illustration
As we saw with the investment timing option, there is frequently an alternative to merely
accepting or rejecting a static project. Many investment opportunities, if successful, lead to
other investment opportunities. The production capacity of a successful product line can
later be expanded to satisfy increased demand, or distribution can be extended to new
geographic markets. A company with a successful name brand can capitalize on its success
by adding complementary or new products under the same brand. These opportunities
are growth options, which add value to a project and explain, for example, why compa￾nies are flocking to make inroads into the very difficult business environment in China.
Kidco Corporation designs and manufactures products aimed at the preteen market.
Most of its products have a very short life, given the rapidly changing tastes of preteens.
Kidco is now considering a project that will cost $30 million. Management believes there
is a 25% chance that the project will “take off” and generate operating cash flows of
$34 million in each of the next 2 years, after which preteen tastes will change and the
project will be terminated. There is a 50% chance of average demand, in which case cash
flows will be $20 million annually for 2 years. Finally, there is a 25% chance that preteens
won’t like the product at all, and it will generate cash flows of only $2 million per year.
The estimated cost of capital for the project is 14%.
Based on its experience with other projects, Kidco believes it will be able to launch a
second-generation product if demand for the original product is average or above. This
second-generation product will cost the same as the first-generation product, $30 million,
and the cost will be incurred at Year 2. However, given the success of the first-generation
product, Kidco believes that the second-generation product would be just as successful as
the first-generation product.
This growth option resembles a call option on a stock, because it gives Kidco the
opportunity to “purchase” a successful follow-on project at a fixed cost if the value of the
project is greater than the cost. Otherwise, Kidco will let the option expire by not
implementing the second-generation product.
The following sections apply the first four valuation approaches: (1) DCF, (2) DCF
and qualitative assessment, (3) decision-tree analysis, and (4) analysis with a standard
financial option.
26-3a Approach 1: DCF Analysis Ignoring the
Growth Option
Based on probabilities for the different levels of demand, the expected annual operating
cash flows for the project are $19 million per year:
0 25 $34 0 50 $20 0 25 $2 $19 00
Ignoring the growth option, the traditional NPV is $1.29 million:
NPV $30 $19
1 0 14 1
$19
1 0 14 2 $1 29
Based on this DCF analysis, Kidco should accept the project.
Chapter 26 Real Options 1027
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

## Halaman PDF 1065

```text
26-3b Approach 2: DCF Analysis with a Qualitative
Consideration of the Growth Option
Although the DCF analysis indicates that the project should be accepted, it ignores a
potentially valuable real option. The option’s time to maturity and the volatility of the
underlying project provide qualitative insights into the option’s value. Kidco’s growth
option has 2 years until maturity, which is a relatively long time, and the cash flows of the
project are volatile. Taken together, this qualitative assessment indicates that the growth
option should be quite valuable.
26-3c Approach 3: Decision-Tree Analysis of the
Growth Option
Part 1 of Figure 26-6 shows a scenario analysis for Kidco’s project. The top line, which
describes the payoffs for the high-demand scenario, has operating cash flows of
$34 million for the next 2 years. The NPV of this branch is $25.99 million. The NPV
of the average-demand branch in the middle is $2.93 million, and it is $26.71 million
for the low-demand scenario. The sum in the last column of Part 1 shows the expected
NPV of $1.29 million. The coefficient of variation is 14.54, indicating that the project is
very risky.
Part 2 of Figure 26-6 shows a decision-tree analysis in which Kidco undertakes the
second-generation product only if demand is average or high. In these scenarios, shown
on the top two branches of the decision tree, Kidco will incur a cost of $30 million at
Year 2 and receive operating cash flows of either $34 million or $20 million for the next
2 years, depending on the level of demand. If the demand is low, shown on the bottom
branch, Kidco has no cost at Year 2 and receives no additional cash flows in subsequent
years. All operating cash flows (which do not include the cost of implementing the
second-generation project at Year 2) are discounted at the WACC of 14%. Because the
$30 million implementation cost is known, it is discounted at the risk-free rate of 6%. As
shown in Part 2 of Figure 26-6, the expected NPV is $4.70 million, indicating that the
growth option is quite valuable.
The option itself alters the risk of the project, which means that 14% is probably not
the appropriate cost of capital. Figure 26-7 presents the results of a sensitivity analysis in
which the cost of capital for the operating cash flows varies from 8% to 18%. The
sensitivity analysis also allows the rate used to discount the implementation cost at Year 2
to vary from 3% to 9%. The resulting NPV is positive for all reasonable combinations of
discount rates.
26-3d Approach 4: Valuing the Growth Option with
the Black-Scholes Option Pricing Model
The fourth approach is to use a standard model for a corresponding financial option. As
we noted earlier, Kidco’s growth option is similar to a call option on a stock, so we will use
the Black-Scholes model to find the value of the growth option. The time until the growth
option expires is 2 years. The rate on a 2-year Treasury security is 6%, and this provides a
good estimate of the risk-free rate. Implementing the project will cost $30 million, which
is the strike price.
The input for stock price in the Black-Scholes model is the current value of the under￾lying asset. For the growth option, the underlying asset is the second-generation project, and
its current value is the present value of its cash flows. The calculations in Figure 26-8 show
that this value is $24.07 million. Because the strike price of $30 million is greater than the
current “price” of $24.07 million, the growth option is currently out-of-the-money.
1028 Part 10 Special Topics
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

## Halaman PDF 1066

```text
Figure 26-9 shows the estimates for the variance of the project’s rate of return using
the two methods described earlier in the chapter for the analysis of the investment timing
option. The direct method, shown in Part 2 of the figure, produces an estimate of 0.179
FIGURE 26-6
Scenario Analysis and Decision-Tree Analysis for the Kidco Project (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision.
Thus, intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The operating cash flows are discounted by the WACC of 14%.
b
The expected value, standard deviation, and variance are calculated as in Chapter 6.
c
The coefficient of variation is the standard deviation divided by the expected value.
d
The total cash flows at Year 2 are equal to the operating cash flows for the first-generation product minus the $30 million cost to implement the
second-generation product, if the firm chooses to do so. For example, the Year-2 cash flow in the high-demand scenario is $34 $30 $4 million.
Based on Part 1, it makes economic sense to implement the second-generation product only if demand is high or average.
e
The operating cash flows in Year 1 through Year 2, which do not include the $30 million cost of implementing the second-generation project at
Year 2 for the high-demand and average-demand scenarios, are discounted at the WACC of 14%. The $30 million implementation cost at Year 2 for
the high-demand and average-demand scenarios is discounted at the risk-free rate of 6%.
Chapter 26 Real Options 1029
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

## Halaman PDF 1067

```text
FIGURE 26-7
Sensitivity Analysis of the Kidco Decision-Tree Analysis in Figure 26-6 (Millions of Dollars)
$4.70 3% 4% 5% 6% 7% 8% 9%
8% $11.0 $11.4 $11.8 $12.1 $12.5 $12.9 $13.2
9% $9.6 $10.0 $10.4 $10.8 $11.2 $11.5 $11.9
10% $8.3 $8.7 $9.1 $9.5 $9.9 $10.2 $10.6
11% $7.0 $7.4 $7.8 $8.2 $8.6 $9.0 $9.3
12% $5.8 $6.2 $6.6 $7.0 $7.4 $7.7 $8.1
13% $4.7 $5.1 $5.5 $5.8 $6.2 $6.6 $6.9
14% $3.5 $3.9 $4.3 $4.7 $5.1 $5.4 $5.8
15% $2.4 $2.8 $3.2 $3.6 $4.0 $4.3 $4.7
16% $1.4 $1.8 $2.2 $2.5 $2.9 $3.3 $3.6
17% $0.3 $0.7 $1.1 $1.5 $1.9 $2.3 $2.6
18% $0.7 $0.3 $0.1 $0.5 $0.9 $1.3 $1.6
Cost of Capital Used to
Discount the Year 1 through
Year 4 Operating Cash Flowsa
Cost of Capital Used to Discount the $30 Million Implementation
Cost in Year 2 of the Second Generation Project
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Note:
a
The operating cash flows do not include the $30 million implementation cost of the second-generation project in Year 2.
FIGURE 26-8
Estimating the Input for Stock Price in the Growth Option Analysis of the Investment Timing Option (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The WACC is 14%. All cash flows in this scenario are discounted back to Year 0.
b
The expected value, standard deviation, and variance are calculated as in Chapter 6.
c
The coefficient of variation is the standard deviation divided by the expected value.
1030 Part 10 Special Topics
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

## Halaman PDF 1068

```text
FIGURE 26-9
Estimating the Input for Stock Return Variance in the Growth Option Analysis (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The WACC is 14%. The Year-3 through Year-4 cash flows are discounted back to Year 2.
b
The standard deviation, variance, and expected value are calculated as in Chapter 6.
c
The coefficient of variation is the standard deviation divided by the expected value.
d
The Year-0 price is the expected PV from Figure 26-8.
e
The Year-2 PVs are from Part 1.
f
The annualized returns for each scenario are calculated as PVYear 2 Price Year 0 0 5 1.
g
The expected annualized return is not equal to the cost of capital, 14%. However, if you do the calculations, then you’ll see that the expected 2-year
return is 29.26%, which is equal to the 2-year compounded cost of capital: 1 14 2 1 29 26%.
h
The expected “price” at the time the option expires is taken from Part 1.
i
The standard deviation of the expected “price” at the time the option expires is taken from Part 1.
Chapter 26 Real Options 1031
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

## Halaman PDF 1069

```text
for the variance of return. The indirect method, in Part 2, estimates the variance as 0.153.
Both estimates are somewhat higher than the 0.12 variance of a typical company’s stock
return, which is consistent with the idea that a project’s variance is higher than a stock’s
because of diversification effects. Thus, an estimated variance of 0.15 to 0.20 seems
reasonable. We use an initial estimate of 0.153 in our initial application of the Black￾Scholes model, shown in Part 1 of Figure 26-10.
Using the Black-Scholes model for a call option, Figure 26-10 shows a $4.34 million
value for the growth option. The total NPV is the sum of the first-generation project’s
NPV and the value of the growth option: Total NPV $1 29 $4 34 $5 63 million,
which is much higher than the NPV of the first-generation project alone. As this analysis
FIGURE 26-10
Estimating the Value of the Growth Option Using a Standard Financial Option (Millions of Dollars)
Source: See the file Ch26 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a
The current value of the project is taken from Figure 26-8.
b
The variance of the project’s rate of return is taken from Part 3 of Figure 26-9.
1032 Part 10 Special Topics
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

## Halaman PDF 1070

```text
shows, the growth option adds considerable value to the original project. In addition, the
sensitivity analysis in Part 2 of Figure 26-10 indicates that the growth option’s value is
large for all reasonable values of variance. Kidco should therefore accept the project.
For an illustrative valuation of an abandonment option, see Web Extension 26A.
SELF-TEST
Explain how growth options are like call options.
26-4 Concluding Thoughts on Real Options
We don’t deny that real options can be complicated. Keep in mind, however, that
60 years ago very few companies used NPV because it seemed too complicated. Now
NPV is a basic tool used by virtually all companies and taught in all business schools.
A similar but more rapid pattern of adoption is occurring with real options. Twenty years
ago very few companies used real options, but a survey of CFOs reported that more than
26% of companies now use real option techniques when evaluating projects.9 Just as with
NPV, it’s only a matter of time before virtually all companies use real option techniques.
We have provided you with some basic tools for evaluating real options, starting with
the ability to identify real options and make qualitative assessments regarding a real
option’s value. Decision trees are another important tool, because they facilitate an explicit
identification of the embedded options, which is critical in the decision-making process.
However, keep in mind that the decision tree should not use the original project’s cost of
capital. Although finance theory has not yet provided a way to estimate the appropriate
cost of capital for a decision tree, sensitivity analysis can identify the effect that different
costs of capital have on the project’s value.
Many real options can be analyzed using a standard model for an existing financial
option, such as the Black-Scholes model for calls and puts. There are also other financial
models for a variety of options. These include the option to exchange one asset for
another, the option to purchase the minimum or the maximum of two or more assets,
the option on an average of several assets, and even an option on an option.10 In fact,
there are entire textbooks that describe even more options.11 Given the large number of
standard models for existing financial options, it is often possible to find a financial option
that resembles the real option being analyzed.
Sometimes there are some real options that don’t resemble any financial options. But
the good news is that many of these options can be valued using techniques from financial
engineering. This is frequently the case if there is a traded financial asset that matches the
risk of the real option. For example, many oil companies use oil futures contracts to price
the real options that are embedded in various exploration and leasing strategies. With the
explosion in the markets for derivatives, there are now financial contracts that span an
9
See John R. Graham and Campbell R. Harvey, “The Theory and Practice of Corporate Finance: Evidence from
the Field,” Journal of Financial Economics, May 2001, pp. 187–243.
10See W. Margrabe, “The Value of an Option to Exchange One Asset for Another,” Journal of Finance, March
1978, pp. 177–186; R. Stulz, “Options on the Minimum or Maximum of Two Risky Assets: Analysis and
Applications,” Journal of Financial Economics, Vol. 10, 1982, pp. 161–185; H. Johnson, “Options on the
Maximum or Minimum of Several Assets,” Journal of Financial and Quantitative Analysis, September 1987,
pp. 277–283; P. Ritchken, L. Sankarasubramanian, and A. M. Vijh, “Averaging Options for Capping Total Costs,”
Financial Management, Autumn 1990, pp. 35–41; and R. Geske, “The Valuation of Compound Options,” Journal
of Financial Economics, March 1979, pp. 63–81.
11See John C. Hull, Options, Futures, and Other Derivatives, 9th ed. (Boston: Pearson, 2015).
Chapter 26 Real Options 1033
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

## Halaman PDF 1071

```text
incredible variety of risks. This means that an ever-increasing number of real options
can be valued using these financial instruments. Most financial engineering techniques
are beyond the scope of this book, but Web Extension 26B on the textbook’s Web site
describes one particularly useful financial engineering technique called risk-neutral
valuation.12
SELF-TEST
How widely used is real option analysis?
What techniques can be used to analyze real options?
SUMMARY
In this chapter we discussed some topics that go beyond the simple capital budgeting
framework, including the following:
• Investing in a new project often brings with it a potential increase in the firm’s future
opportunities. Opportunities are, in effect, options—the right but not the obligation to
take some future action.
• A project may have an option value that is not accounted for in a conventional NPV
analysis. Any project that expands the firm’s set of opportunities has positive option
value.
• Real options are opportunities for management to respond to changes in market
conditions and involve “real” rather than “financial” assets.
• There are five possible procedures for valuing real options: (1) DCF analysis only, and
ignore the real option; (2) DCF analysis and a qualitative assessment of the real option’s
value; (3) decision-tree analysis; (4) analysis with a standard model for an existing
financial option; and (5) financial engineering techniques.
• Many investment timing options and growth options can be valued using the Black￾Scholes call option pricing model.
• See Web Extension 26A on the textbook’s Web site for an illustration of valuing the
abandonment option.
• See Web Extension 26B on the textbook’s Web site for a discussion of risk-neutral
valuation.
12For more on real options, see Martha Amram, Value Sweep: Mapping Corporate Growth Opportunities
(Boston: Harvard Business School Press, 2002); Martha Amram and Nalin Kulatilaka, Real Options:
Managing Strategic Investment in an Uncertain World (Boston: Harvard Business School Press, 1999);
Michael Brennan and Lenos Trigeorgis, Project Flexibility, Agency, and Competition: New Developments in
the Theory and Application of Real Options (New York: Oxford University Press, 2000); Eduardo Schwartz and
Lenos Trigeorgis, Real Options and Investment Under Uncertainty (Cambridge, MA: MIT Press, 2001); Han
T. J. Smit and Lenos Trigeorgis, Strategic Investment: Real Options and Games (Princeton, NJ: Princeton
University Press, 2004); Lenos Trigeorgis, Real Options in Capital Investment: Models, Strategies, and
Applications (Westport, CT: Praeger, 1995); and Lenos Trigeorgis, Real Options: Managerial Flexibility and
Strategy in Resource Allocation (Cambridge, MA: MIT Press, 1996).
1034 Part 10 Special Topics
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

## Halaman PDF 1072

```text
QUESTIONS
(26-1) Define each of the following terms:
a. Real option; managerial option; strategic option; embedded option
b. Investment timing option; growth option; abandonment option; flexibility option
c. Decision tree
(26-2) What factors should a company consider when it decides whether to invest in a project
today or to wait until more information becomes available?
(26-3) In general, do timing options make it more or less likely that a project will be accepted
today?
(26-4) If a company has an option to abandon a project, would this tend to make the company
more or less likely to accept the project today?
SELF-TEST PROBLEM Solution Shown in Appendix A
(ST-1) Katie Watkins, an entrepreneur, believes that consolidation is the key to profit in the
fragmented recreational equine industry. In particular, she is considering starting a
business that will develop and sell franchises to other owner-operators, who will then
board and train hunter-jumper horses. The initial cost to develop and implement the
franchise concept is $8 million. She estimates a 25% probability of high demand for the
concept, in which case she will receive cash flows of $13 million at the end of each year for
the next 2 years. She estimates a 50% probability of medium demand, with annual cash
flows of $7 million for 2 years, and a 25% probability of low demand, with annual cash
flows of $1 million for 2 years. She estimates the appropriate cost of capital is 15%. The
risk-free rate is 6%.
a. Find the NPV of each scenario, and then find the expected NPV.
b. Now assume that the expertise gained by taking on the project will lead to an
opportunity at the end of Year 2 to undertake a similar venture that will have the
same cost as the original project. The new project’s cash flows would follow
whichever branch resulted for the original project. In other words, there would be
an $8 million cost at the end of Year 2 and then cash flows of $13 million, $7 million,
or $1 million for Years 3 and 4. Use decision-tree analysis to estimate the combined
value of the original project and the additional project (but implement the additional
project only if it is optimal to do so). Assume that the $8 million cost at Year 2 is
known with certainty and should be discounted at the risk-free rate of 6%. (Hint: Do
one decision tree that discounts the operating cash flows at the 15% cost of capital
and another decision tree that discounts the costs of the projects—that is, the costs at
Year 0 and Year 2—at the risk-free rate of 6%; then sum the two decision trees to find
the total NPV.)
c. Instead of using decision-tree analysis, use the Black-Scholes model to estimate the
value of the growth option. Assume that the variance of the project’s rate of return is
0.15. Find the total value of the project with the option to expand—that is, the sum of
the original expected value and the growth option. (Hint: You will need to find the
expected present value of the additional project’s operating cash flows in order to
estimate the current price of the option’s underlying asset.)
Real Options
Chapter 26 Real Options 1035
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

## Halaman PDF 1073

```text
PROBLEMS Answers Are in Appendix B
INTERMEDIATE PROBLEMS 1–5
Kim Hotels is interested in developing a new hotel in Seoul. The company estimates that
the hotel would require an initial investment of $20 million. Kim expects the hotel will
produce positive cash flows of $3 million a year at the end of each of the next 20 years.
The project’s cost of capital is 13%.
a. What is the project’s net present value?
b. Kim expects the cash flows to be $3 million a year, but it recognizes that the cash
flows could actually be much higher or lower, depending on whether the Korean
government imposes a large hotel tax. One year from now, Kim will know whether
the tax will be imposed. There is a 50% chance that the tax will be imposed, in which
case the yearly cash flows will be only $2.2 million. At the same time, there is a 50%
chance that the tax will not be imposed, in which case the yearly cash flows will be
$3.8 million. Kim is deciding whether to proceed with the hotel today or to wait a
year to find out whether the tax will be imposed. If Kim waits a year, the initial
investment will remain at $20 million. Assume that all cash flows are discounted at
13%. Use decision-tree analysis to determine whether Kim should proceed with the
project today or wait a year before deciding.
The Karns Oil Company is deciding whether to drill for oil on a tract of land the company
owns. The company estimates the project would cost $8 million today. Karns estimates
that, once drilled, the oil will generate positive net cash flows of $4 million a year at the
end of each of the next 4 years. Although the company is fairly confident about its
cash flow forecast, in 2 years it will have more information about the local geology and
about the price of oil. Karns estimates that if it waits 2 years then the project would cost
$9 million. Moreover, if it waits 2 years, then there is a 90% chance that the net cash flows
would be $4.2 million a year for 4 years and a 10% chance that they would be $2.2 million
a year for 4 years. Assume all cash flows are discounted at 10%.
a. If the company chooses to drill today, what is the project’s net present value?
b. Using decision-tree analysis, does it make sense to wait 2 years before deciding
whether to drill?
Hart Lumber is considering the purchase of a paper company, which would require an
initial investment of $300 million. Hart estimates that the paper company would provide
net cash flows of $40 million at the end of each of the next 20 years. The cost of capital for
the paper company is 13%.
a. Should Hart purchase the paper company?
b. Hart’s best guess is that cash flows will be $40 million a year, but it realizes that the
cash flows are as likely to be $30 million a year as $50 million. One year from now, it
will find out whether the cash flows will be $30 million or $50 million. In addition,
Hart could sell the paper company at Year 3 for $280 million. Given this additional
information, does decision-tree analysis indicate that it makes sense to purchase the
paper company? Again, assume that all cash flows are discounted at 13%.
Utah Enterprises is considering buying a vacant lot that sells for $1.2 million. If the
property is purchased, the company’s plan is to spend another $5 million today t 0 to
build a hotel on the property. The after-tax cash flows from the hotel will depend critically
on whether the state imposes a tourism tax in this year’s legislative session. If the tax is
imposed, the hotel is expected to produce after-tax cash inflows of $600,000 at the end of
each of the next 15 years, versus $1,200,000 if the tax is not imposed. The project has
(26-1)
Investment Timing
Option: Decision￾Tree Analysis
(26-2)
Investment Timing
Option: Decision￾Tree Analysis
(26-3)
Investment Timing
Option: Decision￾Tree Analysis
(26-4)
Real Options:
Decision-Tree
Analysis
1036 Part 10 Special Topics
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

## Halaman PDF 1074

```text
a 12% cost of capital. Assume at the outset that the company does not have the option to
delay the project. Use decision-tree analysis to answer the following questions.
a. What is the project’s expected NPV if the tax is imposed?
b. What is the project’s expected NPV if the tax is not imposed?
c. Given that there is a 50% chance that the tax will be imposed, what is the project’s
expected NPV if the company proceeds with it today?
d. Although the company does not have an option to delay construction, it does have
the option to abandon the project 1 year from now if the tax is imposed. If it
abandons the project, it would sell the complete property 1 year from now at an
expected price of $6 million. Once the project is abandoned, the company would no
longer receive any cash inflows from it. If all cash flows are discounted at 12%, would
the existence of this abandonment option affect the company’s decision to proceed
with the project today?
e. Assume there is no option to abandon or delay the project but that the company
has an option to purchase an adjacent property in 1 year at a price of $1.5 million.
If the tourism tax is imposed, then the net present value of developing this property
(as of t 1) is only $300,000 (so it wouldn’t make sense to purchase the property
for $1.5 million). However, if the tax is not imposed, then the net present value of
the future opportunities from developing the property would be $4 million (as of
t 1). Thus, under this scenario it would make sense to purchase the property for
$1.5 million. Given that cash flows are discounted at 12% and that there’s a 50-50
chance the tax will be imposed, how much would the company pay today for the
option to purchase this property 1 year from now for $1.5 million?
Fethe’s Funny Hats is considering selling trademarked, orange-haired curly wigs for
University of Tennessee football games. The purchase cost for a 2-year franchise to sell the
wigs is $20,000. If demand is good (40% probability), then the net cash flows will be
$25,000 per year for 2 years. If demand is bad (60% probability), then the net cash flows
will be $5,000 per year for 2 years. Fethe’s cost of capital is 10%.
a. What is the expected NPV of the project?
b. If Fethe makes the investment today, then it will have the option to renew the
franchise fee for 2 more years at the end of Year 2 for an additional payment of
$20,000. In this case, the cash flows that occurred in Years 1 and 2 will be repeated
(so if demand was good in Years 1 and 2, it will continue to be good in Years 3 and 4).
Write out the decision tree and use decision-tree analysis to calculate the expected
NPV of this project, including the option to continue for an additional 2 years.
Note: The franchise fee payment at the end of Year 2 is known, so it should be
discounted at the risk-free rate, which is 6%.
CHALLENGING PROBLEMS 6–8
Rework Problem 26-1 using the Black-Scholes model to estimate the value of the option.
Assume that the variance of the project’s rate of return is 6.87% and that the risk-free rate
is 8%.
Rework Problem 26-2 using the Black-Scholes model to estimate the value of the option.
Assume that the variance of the project’s rate of return is 0.111 and that the risk-free rate
is 6%.
Rework Problem 26-5 using the Black-Scholes model to estimate the value of the option.
Assume that the variance of the project’s rate of return is 0.2025 and that the risk-free rate
is 6%.
(26-5)
Growth Option:
Decision-Tree
Analysis
(26-6)
Investment Timing
Option: Option
Analysis
(26-7)
Investment Timing
Option: Option
Analysis
(26-8)
Growth Option:
Option Analysis
Chapter 26 Real Options 1037
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

## Halaman PDF 1075

```text
SPREADSHEET PROBLEM
(26-9) Start with the partial model in the file Ch26 P09 Build a Model.xlsx on the textbook’s
Web site. Bradford Services Inc. (BSI) is considering a project with a cost of $10 million
and an expected life of 3 years. There is a 30% probability of good conditions, in which
case the project will provide a cash flow of $9 million at the end of each of the next
3 years. There is a 40% probability of medium conditions, in which case the annual cash
flows will be $4 million, and there is a 30% probability of bad conditions with a cash flow
of $1 million per year. BSI uses a 12% cost of capital to evaluate projects like this.
a. Find the project’s expected present value, NPV, and the coefficient of variation of the
present value.
b. Now suppose that BSI can abandon the project at the end of the first year by selling it
for $6 million. BSI will still receive the Year-1 cash flows, but will receive no cash
flows in subsequent years.
c. Now assume that the project cannot be shut down. However, expertise gained by
taking it on would lead to an opportunity at the end of Year 3 to undertake a venture
that would have the same cost as the original project, and the new project’s cash flows
would follow whichever branch resulted for the original project. In other words, there
would be a second $10 million cost at the end of Year 3 followed by cash flows of
either $9 million, $4 million, or $1 million for the subsequent 3 years. Use decision￾tree analysis to estimate the value of the project, including the opportunity to
implement the new project at Year 3. Assume that the $10 million cost at Year 3 is
known with certainty and should be discounted at the risk-free rate of 6%.
d. Now suppose the original project (no abandonment option or additional growth
option) could be delayed a year. All the cash flows would remain unchanged, but
information obtained during that year would tell the company exactly which set of
demand conditions existed. Use decision-tree analysis to estimate the value of the
project if it is delayed by 1 year. (Hint: Discount the $10 million cost at the risk-free
rate of 6% because the cost is known with certainty.)
e. Go back to part c. Instead of using decision-tree analysis, use the Black-Scholes
model to estimate the value of the growth option. The risk-free rate is 6%, and the
variance of the project’s rate of return is 0.22.
MINI CASE
Assume you have just been hired as a financial analyst by Tropical Sweets Inc., a mid-size
California company that specializes in creating exotic candies from tropical fruits such as
mangoes, papayas, and dates. The firm’s CEO, George Yamaguchi, recently returned from
an industry corporate executive conference in San Francisco, and one of the sessions he
attended addressed real options. Because no one at Tropical Sweets is familiar with the
basics of real options, Yamaguchi has asked you to prepare a brief report that the firm’s
executives can use to gain a cursory understanding of the topic.
To begin, you gathered some outside materials on the subject and used these materials
to draft a list of questions that need to be answered. Now that the questions have been
drafted, you must develop the answers.
a. What are some types of real options?
b. What are five possible procedures for analyzing a real option?
Build a Model:
Real Options
1038 Part 10 Special Topics
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

## Halaman PDF 1076

```text
c. Tropical Sweets is considering a project that will cost $70 million and will generate
expected cash flows of $30 million per year for 3 years. The cost of capital for this
type of project is 10%, and the risk-free rate is 6%. After discussions with the
marketing department, you learn that there is a 30% chance of high demand with
associated future cash flows of $45 million per year. There is also a 40% chance of
average demand with cash flows of $30 million per year as well as a 30% chance of
low demand with cash flows of only $15 million per year. What is the expected NPV?
d. Now suppose this project has an investment timing option, because it can be delayed
for a year. The cost will still be $70 million at the end of the year, and the cash flows
for the scenarios will still last 3 years. However, Tropical Sweets will know the level of
demand and will implement the project only if it adds value to the company. Perform
a qualitative assessment of the investment timing option’s value.
e. Use decision-tree analysis to calculate the NPV of the project with the investment
timing option.
f. Use a financial option pricing model to estimate the value of the investment timing
option.
g. Now suppose that the cost of the project is $75 million and the project cannot be
delayed. However, if Tropical Sweets implements the project, then the firm will have
a growth option: the opportunity to replicate the original project at the end of its life.
What is the total expected NPV of the two projects if both are implemented?
h. Tropical Sweets will replicate the original project only if demand is high. Using
decision-tree analysis, estimate the value of the project with the growth option.
i. Use a financial option model to estimate the value of the project with the growth
option.
j. What happens to the value of the growth option if the variance of the project’s return
is 0.142? What if it is 0.50? How might this explain the high valuations of many start￾up high-tech companies that have yet to show positive earnings?
Chapter 26 Real Options 1039
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

## Halaman PDF 1077

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

