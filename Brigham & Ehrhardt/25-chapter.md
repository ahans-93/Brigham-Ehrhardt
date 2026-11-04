# Chapter 25: Portfolio Theory and Asset Pricing Models

[Daftar isi](SUMMARY.md) · [Panduan belajar](KAJIAN.md)

Sumber: PDF halaman 1018–1051. Teks ekstraksi; simbol, tabel, dan rumus belum seluruhnya diverifikasi secara visual.

## Halaman PDF 1018

```text
CHAPTER 25
Portfolio Theory and Asset
Pricing Models
Americans love mutual funds. By 1985, they had invested about $495 billion in mutual
funds, which is not exactly chicken feed. By December 2014, however, they had
invested more than $12.03 trillion in mutual funds! Not only has the amount of
money invested in mutual funds skyrocketed, but the variety of funds is astounding.
You can buy funds that specialize in virtually any type of asset: funds that specialize in
stocks from a particular industry, a particular continent, or a particular country. There
are money market funds that invest only in Treasury bills and other short-term
securities, and there are even funds that hold municipal bonds from a specific state.
For those with a social conscience, there are funds that refuse to own stocks of
companies that pollute, sell tobacco products, or have workforces that are not
culturally diverse. For others, there are “vice” funds, which invest only in brewers,
defense contractors, tobacco companies, and the like.
You can buy an index fund, which simply holds a portfolio of stocks in an index
such as the S&P 500. Index funds don’t try to beat the market. Instead, they try to
keep their expenses low and pass the savings on to investors. An exchange-traded
fund, or ETF, has its own stock that is traded on a stock exchange. Different ETFs hold
widely varied portfolios, ranging from the S&P 500 to gold-mining companies to
Middle Eastern oil companies, and their fees to long-term investors are quite low.
At the other extreme, hedge funds, which are pools of money provided by institutions
and wealthy individuals, are very actively managed—even to the extent of taking over
and then operationally managing firms in the portfolio—and they have relatively high
expenses.
As you read this chapter, think about how portfolio theory, which became widely
understood about 30 years ago, has influenced the mutual fund industry.
Sources: The Investment Company Institute publishes a Fact Book containing updated information on
mutual funds. See www.ici.org/research/stats/factbook.
981
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

## Halaman PDF 1019

```text
In Chapter 6, we presented the key elements of risk and return analysis. There we saw that
much of a stock’s risk can be eliminated by diversification, so rational investors should
hold portfolios of stocks rather than shares of a single stock. We also introduced the
Capital Asset Pricing Model (CAPM), which links risk and required rates of return and
uses a stock’s beta coefficient as the relevant measure of risk. In this chapter, we extend
these concepts and explain portfolio theory. We then present an in-depth treatment of the
CAPM, including a more detailed look at how betas are calculated. We also describe the
Arbitrage Pricing Theory model.
25-1 Efficient Portfolios
Recall from Chapter 6 the important role in portfolio risk that is played by the
correlation between assets. One important use of portfolio risk concepts is to select
efficient portfolios, defined as those portfolios that provide the highest expected return
for any specified level of risk—or the lowest degree of risk for any specified level of
return. We begin with the two-asset case and then extend it to the general case of
N assets.
25-1a The Two-Asset Case
Consider two assets, A and B. Suppose we have estimated the expected returns (r^
Aand r^
B),
the standard deviations (σA and σB) of returns, and the correlation coefficient ρAB
Intrinsic Value, Risk, and Return
In Chapter 1, we told you that managers should strive to
make their firms more valuable and that the value of a firm
is determined by the size, timing, and risk of its free cash
flows (FCF). In Chapter 6, we discussed risk, which affects
WACC and value. Now we provide additional insights into
how to manage a portfolio’s risk and measure a firm’s risk.
Required investments
in operating capital
Net operating
profit aer taxes –
= Free cash flow
(FCF)
Weighted
average cost of
capital (WACC)
Cost of debt
Cost of equity
Market interest rates
Market risk aversion
Firm’s debt/equity mix
Firm’s business risk
Value = + … ++ FCF1
(1 + WACC)1
FCF2
(1 + WACC)2
FCF∞
(1 + WACC)∞
resource
The textbook’s Web site
contains an Excel file
that will guide you
through the chapter’s
calculations. The file for
this chapter is Ch25 Tool
Kit.xlsx, and we
encourage you to open
the file and follow along
as you read the chapter.
982 Part 10 Special Topics
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

## Halaman PDF 1020

```text
for returns.1 The expected return and standard deviation (SD) for a portfolio contain￾ing these two assets are:
r
^
p wAr
^
A 1 wA r
^
B (25-1)
and
Portfolio SD σp w2
Aσ2
A 1 wA 2
σ2
B 2wA 1 wA ρABσAσB (25-2)
Here wA is the fraction of the portfolio invested in Security A, so 1 wA is the fraction
invested in Security B.
To illustrate, suppose we can allocate our funds between A and B in any proportion.
Suppose Security A has an expected rate of return of r^
A 5% and a standard deviation of
returns of σA 4%, while r^
B 8% and σB 10%. Our first task is to determine the set of
feasible portfolios, which are the ones that are attainable given the risk and expected
return of Securities A and B. The second step is to examine the attainable portfolios and
select the efficient subset.
To construct the attainable set, we need data on the degree of correlation between the
two securities’ expected returns, ρAB. Let us work with three different assumed degrees of
correlation—namely, ρAB 1 0, ρAB 0, and ρAB 1 0—and use them to develop the
portfolios’ expected returns, r^
p, and standard deviations, σp. (Of course, only one correlation
can exist; our example simply shows three alternative situations that could occur.)
To calculate r^
p, we use Equation 25-1: Substitute the given values for r^
A and r^
B, and
then calculate r^
p for different values of wA. For example, if wA 0 75, then r^
p 5 75%:
r
^
p wAr
^
A 1 wA r
^
B
0 75 5% 0 25 8% 5 75%
Other values of r^
p are found similarly and are shown in the third column of Figure 25-1.
Next, we use Equation 25-2 to find σp. Substitute the given values for σA, σB, and ρAB,
and then calculate σp for different values of wA. For example, if ρAB 0 and wA 0 75,
then σp 3 9%:
σp w2
Aσ2
A 1 wA 2
σ2
B 2wA 1 wA ρABσAσB
0 752 0 042 1 0 75 2 0 102 2 0 75 1 0 75 0 0 04 0 10
0 0009 0 000625 0 0 001525 0 039 3 9%
Figure 25-1 gives r^
p and σp values for several different value of wA; Figure 25-2 plots
r
^
p and σp for each set of weights and correlations. For any given set of weights, the graphs
show the feasible set of portfolios. Note the following points:
1. Panel A shows the feasible expected portfolio returns for three different values of
correlation: (1) Case 1, with ρAB 1; (2) Case 2, with ρAB 0; and (3) Case 3, with
ρAB 1. Notice that these graphs are identical for each of the three cases: The
1
See Chapter 6 for definitions using historical data to estimate the expected return, standard deviation,
covariance, and correlation.
resource
See Ch25 Tool Kit.xlsx
on the textbook’s Web
site for all calculations.
Chapter 25 Portfolio Theory and Asset Pricing Models 983
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

## Halaman PDF 1021

```text
portfolio return, r^
p, is a linear function of wA, and it does not depend on the correlation
coefficients. This is also seen from the r^
p column in Figure 25-1. This should not be
surprising, because Equation 25-1 shows that a portfolio’s expected return is a weighted
average of the individual expected returns.
2. Panel B shows how risk is affected by the asset mix in the portfolio. For Case 1, where
ρAB 1, portfolio risk σp changes linearly as the portfolio weights change. In
other words, portfolio risk is a weighted average of the individual standard deviations.
However, the graphs for Cases 2 and 3 paint a very different picture. Portfolio risk is a
nonlinear function of the weights, with the risk for these cases being lower than the
risk for Case 1. This shows that if the stocks are not perfectly positively correlated
(i.e., ρAB 1), then combining stocks in a portfolio can diversify away some of its risk.
In fact, if ρAB 1, then risk can be completely diversified away! Thus, a portfolio’s risk
σp , unlike a portfolio’s expected return r
^
p , does depend on correlation.
3. Panel C has graphs plotting a portfolio’s expected return versus its risk. Unlike the
other Panels, which plotted return and risk versus the portfolio’s composition, each of
these three graphs in Panel C is plotted from pairs of r^
p and σp. For example, Point A
(in the first graph of Panel C) is the point r^
p 5% and σp 4%, corresponding to
wA 100% from Panels A and B for Case 1 (i.e., ρAB 1). Notice that the
relationship between risk and return is linear for Case 1, but not for Cases 2 and 3
in which correlation is not equal to 1.
4. Are all portfolios in the feasible set equally good? The answer is “no.” Only that part
of the feasible set from Y to B in Cases 2 and 3 is defined as efficient. The part from A
to Y is inefficient because, for any degree of risk on the line segment AY, a higher
return can be found on segment YB. Thus, no rational investor would hold a portfolio
that lies on segment AY. In Case 1, however, the entire feasible set is efficient—no
combination of the securities can be ruled out.
5. We rarely encounter ρAB 1 0, 0 0, or 1.0. Generally, ρAB is in the range of 0.3
to 0.6 for most stocks. Case 2 (zero correlation) produces graphs that, pictorially,
most closely resemble real-world examples.
From these examples we see that in one extreme case ρ 1 0 , risk can be diversified
away completely, while in the other extreme case ρ 1 0 , higher expected returns always
FIGURE 25-1
r
^
p and σp under Various Assumptions
Source: See the file Ch25 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
984 Part 10 Special Topics
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

## Halaman PDF 1022

```text
have higher risk. In between these extremes, combining two stocks into a portfolio reduces
but does not eliminate the risk inherent in the individual stocks.
Panel C of Figure 25-2 shows that there exists a minimum possible risk portfolio (Y)
for Cases 2 and 3 (i.e., for ρ 1 0). How can we determine the weights for the
minimum risk portfolio? Differentiate Equation 25-2 with respect to wA, set the derivative
equal to zero, and then solve for wA. This identifies the fraction of the portfolio that
should be invested in Security A if we wish to form the least-risky portfolio. Here is the
equation:
Minimum risk portfolio wA
σB σB ρABσA
σ2
A σ2
B 2ρABσAσB
(25-3)
A value of wA that is negative means that Security A is sold short; if wA is greater than
1, B is sold short. In a short sale, you borrow shares of stock from a broker and then sell
them, expecting to buy shares of stock back later (at a lower price) in order to repay the
person from whom you borrowed the stock. If you sell short and the stock price rises, then
you lose, but you win if the price declines. If the stock pays a dividend, you must pay the
FIGURE 25-2
Illustrations of Portfolio Returns, Risk, and the Feasible Set of Portfolios
100%A Portfolio 100%B
Allocation
rA = 5
rB = 8 rp
rp(%) rp(%) rp(%)
rp(%) rp(%) rp(%)
sp(%) sp(%)
Portfolio
Allocation
100%A 100%B
rA = 5
rB = 8 rp
Portfolio
Allocation
100%A 100%B
rA = 5
rB = 8 rp
100%A Portfolio 100%B
Allocation
sA = 4
sB = 10
sp
Portfolio
Allocation
100%A 100%B
sA = 4 sp
sB = 10
Portfolio
Allocation
100%A 100%B
sA = 4 sp
sB = 10
Case 1: rAB = + 1 Case 2: rAB = 0
Case 2: rAB = 0
Case 2: rAB = 0 Case 3: rAB = –1
sp(%)
Case 3: rAB = –1
Case 3: rAB = –1
5
8
4 10
Risk, sp(%)
A
B
0
Risk, sp(%)
5
8
4 10
A
B
Y
0
Risk, sp(%)
5
8
4 10
A
B
Y
0
Panel A: Expected Returns (rp)
Panel B: Risk (Standard Deviation of Returns, sp)
Case 1: rAB = + 1
Case 1: rAB = + 1
Panel C: Risk versus Return for Feasible Portfolios (rp versus sp)
Chapter 25 Portfolio Theory and Asset Pricing Models 985
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

## Halaman PDF 1023

```text
dividend to the broker, who passes it on to the client who provided the shares. Therefore,
selling a share short is like owning a negative share of stock.
To find the minimum risk portfolio if short sales are not used, limit wA to the range 0
to 1.0; that is, if the solution value is wA 1 0, set wA to 1.0, and if wA is negative, set
wA to 0.0.
25-1b The N-Asset Case
The same principles from the two-asset case also apply when the portfolio is composed of
N assets. Here is the notation for the N-asset case: The percentage of the investment in
asset i (the portfolio weight) is wi, the expected return for asset i is r^
i
, the standard
deviation of asset i is σi, and the correlation between asset i and asset j is ρij. The expected
return for a portfolio with N assets is then:
r
^
p
N
i 1
wir
^
i (25-4)
And the variance of the portfolio is:
σ2
p
N
i 1
N
j 1
wiwjσiσjρij (25-5)
For the case in which i j, the correlation is ρij ρii 1. Notice also that when i j, the
product σiσj σiσi σ2
i .
One way to apply Equation 25-5 is to set up a table with a row and column for each
asset. Give the rows and columns labels showing the assets’ weights and standard
deviations. Then fill in each cell in the table by multiplying the values in the row and
column headings by the correlation between the assets, as shown here:
w1σ1 (1) w2σ2 (2) w3σ3 (3)
w1σ1 (1) w1σ1w1σ1ρ11 w2
1σ2
1 w1σ1w2σ2ρ12 w1σ1w3σ3ρ13
w2σ2 (2) w2σ2w1σ1ρ21 w2σ2w2σ2ρ22 w2
2σ2
2 w2σ2w3σ3ρ23
w3σ3 (3) w3σ3w1σ1ρ31 w3σ3w2σ2ρ32 w3σ3w3σ3ρ33 w2
3σ2
3
The portfolio variance is the sum of the nine cells. For the diagonal, we have substituted
the values for the case in which i j. Notice that some of the cells have identical values. For
example, the cell for Row 1 and Column 2 has the same value as the cell for Column 1 and
Row 2. This suggests an alternative formula:
σ2
p
N
i 1
w2
i σ2
i
N
i 1
N
j 1
j i
wi σi wj σj ρij (25-5a)
The main thing to remember when calculating portfolio standard deviations is simply
this: Do not leave out any terms. Using a table like the one shown here can help.
986 Part 10 Special Topics
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

## Halaman PDF 1024

```text
SELF-TEST
What does the term “attainable set” mean?
Within the attainable set, which portfolios are “efficient”?
Stock A has an expected return of 10% and a standard deviation of 35%. Stock B has an
expected return of 15% and a standard deviation of 45%. The correlation coefficient between
Stocks A and B is 0.3. What are the expected return and standard deviation of a portfolio
invested 60% in Stock A and 40% in Stock B? (12.0%; 31.5%)
25-2 Choosing the Optimal Portfolio
With only two assets, the feasible set of portfolios is a line or curve, as shown in Figure 25-2,
Panel C. However, by increasing the number of assets, we obtain an area, such as the shaded
region in Figure 25-3. Points A, H, G, and E represent single securities (or portfolios containing
only one security). All the other points in the shaded area and its boundaries, which comprise
the feasible set, represent portfolios of two or more securities. Each point in this area represents
a particular portfolio with a risk of σp and an expected return of r^
p. For example, Point X
represents one such portfolio’s risk and expected return, as do each of Points B, C, and D.
Given the full set of potential portfolios that could be constructed from the available
assets, which portfolio should actually be held? This choice involves two separate deci￾sions: (1) determining the efficient set of portfolios and (2) choosing from the efficient set
the single portfolio that is best for the specific investor.
25-2a The Efficient Frontier
In Figure 25-3, the boundary line BCDE defines the efficient set of portfolios, which is also
called the efficient frontier.
2 Portfolios to the left of the efficient set are not possible
FIGURE 25-3
The Efficient Set of Investments
A
B
C
D
E
G
H
Efficient Set (BCDE)
Feasible, or
Attainable, Set
Risk, sp
Expected Portfolio
Return, rp
X
2
A computational procedure for determining the efficient set of portfolios was developed by Harry Markowitz
and first reported in his article “Portfolio Selection,” Journal of Finance, March 1952, pp. 77–91. In this article,
Markowitz developed the basic concepts of portfolio theory, and he later won the Nobel Prize in economics for
his work.
Chapter 25 Portfolio Theory and Asset Pricing Models 987
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

## Halaman PDF 1025

```text
because they lie outside the attainable set. Portfolios to the right of the boundary line
(interior portfolios) are inefficient because some other portfolio would provide either a
higher return for the same degree of risk or a lower risk for the same rate of return. For
example, Portfolio X is dominated in this sense by all portfolios on the curve CD.
25-2b Risk–Return Indifference Curves
Given the efficient set of portfolios, which specific portfolio should an investor
choose? To determine the optimal portfolio for a particular investor, we must know
the investor’s attitude toward risk as reflected in his or her risk–return trade-off function,
or indifference curve.
An investor’s risk–return trade-off function is based on the standard economic
concepts of utility theory and indifference curves, which are illustrated in Figure 25-4.
The curves labeled IY and IZ represent the indifference curves of two individuals, Ms. Y
and Mr. Z. Ms. Y’s curve indicates indifference between the riskless 5% portfolio, a
portfolio with an expected return of 6% but a risk of σp 1 4%, and so on. Mr. Z’s curve
indicates indifference between a riskless 5% return, an expected 6% return with risk of
σp 3 3%, and so on.
Note that Ms. Y requires a higher expected rate of return as compensation for any given
amount of risk; thus, Ms. Y is said to have more risk aversion than Mr. Z. Her higher risk
aversion causes Ms. Y to require a higher risk premium—defined here as the difference
between the 5% riskless return and the expected return required to compensate for any
FIGURE 25-4
Risk–Return Indifference Curves
0
1
2
3
4
5
6
7
8
9
10
123456789 Risk, sp(%)
I
Y I
Z
Y’s Risk Premium (RP) for
Risk = sp = 3.3%; RPY = 2.5%
Z’s Risk Premium (RP) for
Risk = sp = 3.3%; RPZ = 1.0%
Expected Rate
of Return, rp
(%)
988 Part 10 Special Topics
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

## Halaman PDF 1026

```text
specific amount of risk—than Mr. Z requires. Thus, Ms. Y requires a risk premium RPY of
2.5% to compensate for a risk of σp 3 3%, whereas Mr. Z’s risk premium for this degree
of risk is only RPz 1 0%. In general, an indifference curve with a steeper slope means that
the investor is more risk averse. Thus, Ms. Y is more risk averse than Mr. Z.
Each individual has a “map” of indifference curves; the indifference maps for Ms. Y
and Mr. Z are shown in Figure 25-5. The higher curves denote a greater level of
satisfaction (or utility). Thus, IZ2 is better than IZ1 because, for any level of risk, Mr. Z
has a higher expected return and hence greater utility. An infinite number of indiffer￾ence curves could be drawn in the map for each individual, and each individual has a
unique map.
25-2c The Optimal Portfolio for an Investor
Figure 25-5 also shows the feasible set of portfolios for the two-asset case, under the
assumption that ρAB 0, as it was developed in Figure 25-2. The optimal portfolio for
each investor is found at the tangency point between the efficient set of portfolios and
one of the investor’s indifference curves. This tangency point marks the highest level of
FIGURE 25-5
Selecting the Optimal Portfolio of Risky Assets
0 2
Expected Rate
of Return, rp
(%)
Risk, sp(%)
I
Y3 I
Y2 I
Y1
I
Z2
4 6 810
4.2 7.1
4
5
6
7
8
7.2
I
Z1
I
Z3
B
A
Chapter 25 Portfolio Theory and Asset Pricing Models 989
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

## Halaman PDF 1027

```text
satisfaction the investor can attain. Ms. Y, who is more risk averse than Mr. Z, chooses
a portfolio with a lower expected return (about 6%) but a risk of only σp 4 2%. Mr. Z
picks a portfolio that provides an expected return of about 7.2% but has a risk of about
σp 7 1%. Ms. Y’s portfolio is more heavily weighted with the less risky security, while
Mr. Z’s portfolio contains a larger proportion of the more risky security.3
SELF-TEST
What is the efficient frontier?
What are indifference curves?
Conceptually, how does an investor choose his or her optimal portfolio?
25-3 The Basic Assumptions of the Capital
Asset Pricing Model
The Capital Asset Pricing Model (CAPM), which was introduced in Chapter 6, specifies
the relationship between risk and required rates of return on assets when they are held in
well-diversified portfolios. The assumptions underlying the CAPM’s development are
summarized in the following list.4
1. All investors focus on a single holding period, and they seek to maximize the
expected utility of their terminal wealth by choosing among alternative portfolios
on the basis of each portfolio’s expected return and standard deviation.
2. All investors can borrow or lend an unlimited amount at a given risk-free rate of
interest, rRF, and there are no restrictions on short sales of any asset.
3. All investors have identical estimates of the expected returns, variances, and
covariances among all assets (that is, investors have homogeneous expectations).
4. All assets are perfectly divisible and perfectly liquid (that is, marketable at the going
price).
5. There are no transaction costs.
6. There are no taxes.
7. All investors are price takers (that is, all investors assume that their own buying and
selling activity will not affect stock prices).
8. The quantities of all assets are given and fixed.
Theoretical extensions in the literature have relaxed some of these assumptions, and,
in general, these extensions have led to conclusions that are reasonably consistent with the
basic theory. However, the validity of any model can be established only through
empirical tests, which we discuss later in the chapter.
SELF-TEST
What are the key assumptions of the CAPM?
3
Ms. Y’s portfolio would contain 67% of Security A and 33% of Security B, whereas Mr. Z’s portfolio would
consist of 27% of Security A and 73% of Security B. These percentages can be determined with Equation 25-1 by
simply seeing what percentage of the two securities is consistent with r^
p 6 0% and 7.2%. For example,
wA 5% 1 wA 8% 7 2%, and solving for wA, we obtain wA 0 27 and 1 wA 0 73.
4
The CAPM was originated by William F. Sharpe in his article “Capital Asset Prices: A Theory of Market
Equilibrium under Conditions of Risk,” Journal of Finance, September 1964, pp. 425–442. Professor Sharpe won
the Nobel Prize in economics for his work on capital asset pricing. The assumptions inherent in Sharpe’s model
were spelled out by Michael C. Jensen in “Capital Markets: Theory and Evidence,” Bell Journal of Economics and
Management Science, Autumn 1972, pp. 357–398.
990 Part 10 Special Topics
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

## Halaman PDF 1028

```text
25-4 The Capital Market Line and the
Security Market Line
Figure 25-5 showed the set of portfolio opportunities for the two-asset case, and it
illustrated how indifference curves can be used to select the optimal portfolio from the
feasible set. In Figure 25-6, we show a similar diagram for the many-asset case, but here
we also include a risk-free asset with a return rRF. The riskless asset by definition has zero
risk, σ 0%, so it is plotted on the vertical axis.
The figure shows both the feasible set of portfolios of risky assets (the shaded area)
and a set of indifference curves I1, I2, I3 for a particular investor. Point N, where
indifference curve I1 is tangent to the efficient set, represents a possible portfolio choice;
it is the point on the efficient set of risky portfolios where the investor obtains the highest
possible return for a given amount of risk and the smallest degree of risk for a given
expected return.
However, the investor can do better than Portfolio N by reaching a higher indifference
curve. In addition to the feasible set of risky portfolios, we now have a risk-free asset that
provides a riskless return, rRF. Given the risk-free asset, investors can create new portfolios
that combine the risk-free asset with a portfolio of risky assets. This enables them to
achieve any combination of risk and return on the straight line connecting rRF with M, the
point of tangency between that straight line and the efficient frontier of risky asset
FIGURE 25-6
Investor Equilibrium: Combining the Risk-Free Asset with the Market Portfolio
A
Z
E
G
H
Expected Rate
of Return, rp
Risk, sp
R
0 sM
rp
rRF
r M
I1 I2 I
3
Increasing
Utility
B
N
M
Chapter 25 Portfolio Theory and Asset Pricing Models 991
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

## Halaman PDF 1029

```text
portfolios.5 Some portfolios on the line rRFMZ will be preferred to most risky portfolios
on the efficient frontier BNME, so the points on the line rRFMZ now represent the best
attainable combinations of risk and return.
Given the new opportunities along line rRFMZ, our investor will move from Point N
to Point R, which is on her highest attainable risk–return indifference curve. Note that any
point on the old efficient frontier BNME (except the point of tangency M) is dominated
by some point along the line rRFMZ. In general, because investors can purchase some of
the risk-free security and some of the risky portfolio (M), it will be possible to move to a
point such as R. In addition, if the investor can borrow as well as lend (lending is
equivalent to buying risk-free debt securities) at the riskless rate rRF, then it is possible
to move out on the line segment MZ; an investor would do so if his or her indifference
curve were tangent to rRFMZ, to the right of Point M.6
All investors should hold portfolios lying on the line rRFMZ under the conditions
assumed in the CAPM. This implies that they should hold portfolios that are combina￾tions of the risk-free security and the risky Portfolio M. Thus, the addition of the risk-free
asset totally changes the efficient set: The efficient set now lies along line rRFMZ rather
5
The risk–return combinations between a risk-free asset and a risky asset (a single stock or a portfolio of stocks)
will always be linear. To see this, consider the following equations, which were developed earlier, for return r
^
p
and risk σp for any combination wRF and 1 wRF :
r
^
p wRFrRF 1 wRF rM
^ (25-1a)
and
σP w2
RFσ2
RF 1 wRF 2
σ2
M 2wRF 1 wRF ρRF, MσRF σM (25-2a)
Equation 25-1a is linear. As for Equation 25-2a, we know that rRF is the risk-free asset, so σRF 0; hence, σ2
RF is
also zero. Using this information, we can simplify Equation 25-2a as follows:
σp 1 wRF 2
σ2
M 1 wRF σM (25-2b)
Thus, σp is also linear when a riskless asset is combined with a portfolio of risky assets.
If expected returns, as measured by r^
p, and risk, as measured by σp, are both linear functions of wRF, then
the relationship between r^
p and σp, when graphed as in Figure 25-6, must also be linear. For example, if 100% of
the portfolio is invested in rRF with a return of 8%, then the portfolio return will be 8% and σp will be 0. If 100%
is invested in M with rM 12% and σM 10%, then σp 1 0 10% 10% and r^
p 0 8% 1 0 12% 12%.
If 50% of the portfolio is invested in M and 50% in the risk-free asset, then σp 0 5 10% 5% and
r
^
p 0 5 8% 0 5 12% 10%. Plotting these points will reveal the linear relationship given as rRFMZ in
Figure 25-6.
6
An investor who is highly risk averse will have a steep indifference curve and will end up holding only the
riskless asset or perhaps a portfolio at a point such as R (i.e., holding some of the risky market portfolio and some
of the riskless asset). An investor who is only slightly averse to risk will have a relatively flat indifference curve,
which will cause her to move out beyond M toward Z, borrowing to do so. This investor might buy stocks on
margin, which means borrowing and using the stocks as collateral. If individuals’ borrowing rates are higher than
rRF, then the line rRFMZ will tilt down (i.e., be less steep) beyond M. This condition would invalidate the basic
CAPM, or at least require it to be modified. Therefore, the assumption of being able to borrow or lend at the
same rate is crucial to CAPM theory.
992 Part 10 Special Topics
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

## Halaman PDF 1030

```text
than along the curve BNME. Note also that if the capital market is to be in equilibrium,
then M must be a portfolio that contains every risky asset in exact proportion to that
asset’s fraction of the total market value of all assets. In other words, if Security i is
X percent of the total market value of all securities, then X percent of the market portfolio
M must consist of Security i. (That is, M is the market value–weighted portfolio of all
risky assets in the economy.) Thus, all investors should hold portfolios that lie on the line
rRFMZ, with the particular location of a given individual’s portfolio being determined by
the point at which his indifference curve is tangent to the line.
The line rRFMZ in Figure 25-6 is called the Capital Market Line (CML). It has an
intercept of rRF and a slope of r
^
M rRF σM.
7 The equation for the Capital Market Line
may be expressed as follows:
CML r
^
p rRF
r
^
M rRF
σM
σp (25-6)
The expected rate of return on an efficient portfolio is equal to the riskless rate plus a risk
premium that is equal to r
^
M rRF σM multiplied by the portfolio’s standard deviation,
σp. Thus, the CML specifies a linear relationship between an efficient portfolio’s
expected return and risk, where the slope of the CML is equal to the expected return
on the market portfolio of risky stocks r
^
M minus the risk-free rate rRF , which is called
the market risk premium, all divided by the standard deviation of returns on the
market portfolio, σM:
Slope of the CML r
^
M rRF σM
For example, suppose rRF 10%, r^
M 15%, and σM 15%. In this case, the slope of
the CML would be 15% 10% 15% 0 33, and if a particular efficient portfolio had
σp 10%, then its r^
p would be:
r
^
p 10% 0 33 10% 13 3%
A (riskier) portfolio with σp 20% would have r^
p 10% 0 33 20% 16 6%.
The CML is graphed in Figure 25-7. It is a straight line with an intercept at rRF and a
slope equal to the market risk premium rM rRF divided by σM. The slope of the CML
reflects the aggregate attitude of investors toward risk.
Recall that an efficient portfolio is well diversified; hence, all of its unsystematic risk
has been eliminated and its only remaining risk is market risk. Therefore, unlike indivi￾dual stocks, the risk of an efficient portfolio is measured by its standard deviation, σp. The
CML equation specifies the relationship between risk and return for such efficient
portfolios—that is, for portfolios that lie on the CML—and in the CML equation and
graph risk is measured by portfolio standard deviation.
The CML specifies the relationship between risk and return for an efficient portfolio,
but investors and managers are more concerned about the relationship between risk and
return for individual assets. To develop the risk–return relationship for individual secu￾rities, note in Figure 25-6 that all investors are assumed to hold Portfolio M, so M must be
the market portfolio (i.e., the one that contains all stocks). Note also that M is an efficient
portfolio. Thus, the CML defines the relationship between the market portfolio’s expected
7
Recall that the slope of any line is measured as ΔYΔX, or the change in height associated with a given change in
horizontal distance. Here, rRF is at 0 on the horizontal axis, so ΔX σM 0 σM. The vertical axis difference
associated with a change from rRF to r^
M is r^
M rRF. Therefore, slope ΔYΔX r
^
M rRF σM.
Chapter 25 Portfolio Theory and Asset Pricing Models 993
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

## Halaman PDF 1031

```text
return and its standard deviation. Equations 25-4 and 25-5 show the formulas for the
expected return and standard deviation for a multi-asset portfolio, including the market
portfolio. It is possible to take the equations for the expected return and standard
deviation of a multi-asset portfolio and show that the required return for each individual
Stock i must conform to the following equation in order for the CML to hold for the
market portfolio:8
ri rRF
rM rRF
σM
Cov ri, rM
σM
rRF rM rRF
Cov ri, rM
σ2
M
(25-7)
The CAPM defines Company i’s beta coefficient, bi, as follows:
bi
Covariance between Stock i and the market
Variance of market returns
Cov ri, rM
σ2
M
ρiMσiσM
σ2
M
ρiM
σi
σM
(25-8)
FIGURE 25-7
The Capital Market Line (CML)
sp
Expected Rate
of Return, rp
0 sM
rRF
rM
rM – rRF CML: rP = rRF + sM
Risk, sp
M
Note: We did not draw it in, but you can visualize the shaded space shown in Figure 25-6 in this graph and the
CML as the line formed by connecting rRF with the tangent to the shaded space.
8
For consistency with most investment textbooks, we let Cov ri,rM denote the covariance between the returns of
assets i and M. Using the notation in Chapter 6, we would have denoted the covariance as COVi,M.
994 Part 10 Special Topics
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

## Halaman PDF 1032

```text
Recall that the risk premium for the market, RPM, is rM rRF. Using this definition
and substituting Equation 25-8 into Equation 25-7 gives the Security Market Line (SML):
SML ri rRF rM rRF bi
rRF RPM bi
(25-9)
The SML tells us that an individual stock’s required return is equal to the risk-free rate
plus a premium for bearing risk. The premium for risk is equal to the risk premium for
the market, RPM, multiplied by the risk of the individual stock, as measured by its beta
coefficient. The beta coefficient measures the amount of risk that the stock contributes to
the market portfolio.
Unlike the CML for a well-diversified portfolio, the SML tells us that the standard
deviation σi of an individual stock should not be used to measure its risk, because some
of the risk as reflected by σi can be eliminated by diversification. Beta reflects risk after
taking diversification benefits into account, and so beta, rather than σi, is used to measure
individual stocks’ risks to investors. Be sure to keep in mind the distinction between the
SML and the CML and why that distinction exists.
SELF-TEST
Draw a graph showing the feasible set of risky assets, the efficient frontier, the risk-free asset,
and the CML.
Write out the equation for the CML and explain its meaning.
Write out the equation for the SML and explain its meaning.
What is the difference between the CML and the SML?
The standard deviation of stock returns of Park Corporation is 60%. The standard deviation of
the market return is 20%. If the correlation between Park and the market is 0.40, what is Park’s
beta? (1.2)
25-5 Calculating Beta Coefficients
Equation 25-8 defines beta, but recall from Chapter 6 that this equation for beta is also the
formula for the slope coefficient in a regression of the stock return against the market return.
Therefore, beta can be calculated by plotting the historical returns of a stock on the y-axis of a
graph versus the historical returns of the market portfolio on the x-axis and then fitting the
regression line. In his 1964 article that set forth the CAPM, Sharpe called this regression line
the characteristic line. Thus, a stock’s beta is the slope of its characteristic line.
In Chapter 6, we estimated General Electric’s beta using 4 years of monthly returns.
In this chapter, we estimate betas using 1 year of weekly returns because this is another
often-used approach. In addition to estimating the beta of a company in this chapter
(Apple), we also estimate the beta of a mutual fund (Fidelity’s Magellan Fund) to illustrate
the impact that portfolio diversification has on confidence intervals for estimated betas.
In addition, we examine a modified estimation approach using excess returns, which are
the assets’ returns in excess of the risk-free rate.
25-5a Calculating the Beta Coefficient for a Single
Stock: Apple
Table 25-1 shows a summary of the data used in this analysis; the full data set is in the file
Ch25 Tool Kit.xlsx and has weekly returns for each week in 2014. Table 25-1 shows the
Chapter 25 Portfolio Theory and Asset Pricing Models 995
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

## Halaman PDF 1033

```text
market returns (defined as the percentage price change of the S&P 500), the stock returns
for Apple, and the returns on the Magellan Fund (which is a well-diversified portfolio).
The table also shows the risk-free rate, defined as the yield on a short-term (3-month) U.S.
Treasury bill, which we will use later in this analysis.
As Table 25-1 shows, Apple had an average annual return of 39.9% during 2014, while
the market had an average annual return of 13.2%. As we noted before, it is usually
unreasonable to think that the future expected return for a stock will equal its average
historical return over a relatively short period, such as 52 weeks. However, we might well
expect past volatility to be a reasonable estimate of future volatility, at least during the
next year. Observe that the standard deviation for Apple’s return during this period was
21.7%, versus 11.2% for the market. Thus, the market’s volatility is much less than that of
Apple. This is what we would expect, because the market is a well-diversified portfolio and
thus much of its risk has been diversified away. The correlation between Apple’s stock
returns and the market returns is about 0.47, which is a little higher than the correlation
for a typical stock.
Skill or Luck?
That’s the question The Wall Street Journal’s Investment
Dartboard Contest sought to answer by comparing the actual
investment results of professional analysts against amateurs
and dart throwers. Here’s how the contest worked. First, The
Wall Street Journal (WSJ) picked four professional analysts, and
each of those pros formed a portfolio by picking four stocks.
Second, amateurs could enter the contest by e-mailing their
pick of a single stock to the WSJ, which then picked four
amateurs at random and combined their choices to make a
four-stock portfolio. Third, a group of WSJ editors formed a
portfolio by throwing four darts at the stock tables. At the
beginning of each contest, the WSJ announced the six resulting
portfolios, and at the end of 6 months, the paper announced the
results. The top two pros were invited back for the next contest.
In 142 contests, the pros beat the darts 87 times and lost
55 times. The pros also beat the Dow Jones Industrial Average
(DJIA) in 54% of the contests. The pros had an average return
higher than that of the DJIA, the darts, and the amateurs.
Do these results mean that skill is more important than
luck when it comes to investing in stocks? Not necessarily,
according to Burton Malkiel, an economics professor at
Princeton and the author of the widely read book A Ran￾dom Walk Down Wall Street. Because the dart-selected
portfolios consist of randomly chosen stocks, they should
have average risk. However, the pros consistently picked
high-risk stocks. Because there was a bull market during
most of the contests, one would expect high-risk stocks to
outperform the average stock. According to Malkiel, the
pros’ performance could be due as much to a rising market
as to superior analytical skills. The WSJ discontinued that
contest in 2002, so we can’t know for sure whether Malkiel
was right or wrong.
Until early 2013, the WSJ ran a contest pitting six amateurs
against six darts. Overall, readers won 19 contests and the darts
won 30. The WSJ now offers a number of different investment
games at www.marketwatch.com/game.
TABLE 25-1
Summary of Data for Calculating Beta (Weekly Returns during the Year 2014)
rM, Market Return
(S&P 500 Index) ri, Apple Return
rp, Fidelity Magellan
Fund Return
rRF, Risk-Free Rate
(Yield on 3-Month T-Bill)
Average return (annualized) 13.2% 39.9% 15.5% 0.034%
Standard deviation (annual) 11.2% 21.7% 12.2% 0.002%
Correlation with market return, ρ 0.47 0.97 0.12
Source: See the file Ch25 Tool Kit.xlsx. Returns are based on adjusted prices from Yahoo! Finance and T-bill yields are from the Federal Reserve Bank of
St. Louis’s FRED® Economic Data.
resource
See Ch25 Tool Kit.xlsx
on the textbook’s
Web site.
996 Part 10 Special Topics
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

## Halaman PDF 1034

```text
Figure 25-8 shows a plot of Apple’s returns against the market’s returns. We used the
Excel Trendline feature to plot the trendline and show the estimated regression equation on
the chart. We also used Excel’s regression analysis feature (Data, Data Analysis, Regression)
to estimate the regression equation. Table 25-2 reports some of these regression results for
Apple. Its estimated beta, which is the slope coefficient in the regression, is about 0.90.
As with all regression results, Apple’s estimated beta of 0.90 is just an estimate, not
necessarily the true value of beta. Table 25-2 also shows the t-statistic and the probability
that the true beta is zero. For Apple, this probability is approximately equal to zero. This
means that there is virtually a zero chance that the true beta is equal to zero. Because this
probability is less than 5%, statisticians would say that the slope coefficient, beta, is
“statistically significant.” The output of the regression analysis also gives us the 95%
confidence interval for the estimate of beta. For Apple, the results tell us that we can be
95% confident that the true beta is between 0.42 and 1.39. This is an extremely wide
range, but it is typical for most individual stocks. Therefore, the regression estimate for the
beta of any single company is highly uncertain.
Observe also that the points in Figure 25-8 are not clustered very tightly around the
regression line. Sometimes Apple does much better than the market; other times, it does
much worse. The R2 value shown in the chart measures the degree of dispersion about the
regression line. (Statistically speaking, it measures the proportion of variation that is
explained by the regression equation.) An R2 of 1.0 indicates that all points lie exactly on
the line; in this case, all of the variation in the y variable is explained by the x variable. The
R2 for Apple is about 0.22, which is typical of individual stocks. This indicates that about
78% of the variation in Apple’s returns is not explained by the overall market return.
FIGURE 25-8
Calculating a Beta Coefficient for Apple
Source: See the file Ch25 Tool Kit.xlsx.
Chapter 25 Portfolio Theory and Asset Pricing Models 997
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

## Halaman PDF 1035

```text
Finally, note that the intercept shown in the regression equation displayed on the
chart is about 0.0054. Because the regression equation is based on weekly data, this
means that Apple had a 28% annual return that was not explained by the CAPM
model: 0 0054 52 0 28 28%. However, the regression results in Table 25-2 also
show that the probability of the t-statistic is 16% (which is much greater than 5%),
meaning that the “true” intercept might be zero even though the estimated intercept
was 0.0054. Therefore, most statisticians would say that this intercept is not statisti￾cally significant—the returns of Apple are so volatile that we cannot be sure the true
intercept is not equal to zero. Translating statistician-speak into plain English, this
means that the part of Apple’s average weekly return that is not explained by the
CAPM could, in fact, be zero. Thus, the CAPM might very well explain all of Apple’s
average weekly returns.
25-5b The Market Model versus the CAPM
When we estimated beta, we used the following regression equation:
ri,t ai birM,t ei,t (25-10)
where
ri,t Historical realized rate of return on Stock i in period t
rM,t Historical realized rate of return on the market in period t
ai Vertical axis intercept term for Stock i
bi Slope, or beta coefficient, for Stock i
ei,t Random error, reflecting the difference between the actual return on Stock i
in a given period and the return as predicted by the regression line
TABLE 25-2
Regression Results for Calculating Beta
Regression
Coefficient t-Statistic
Probability of
t-Statistic
Lower 95%
Confidence Interval
Upper 95%
Confidence Interval
Panel A: Apple (Market model)
Intercept 0.0054 1.43 15.97% 0.002 0.013
Slope (beta) 0.9024 3.75 0.05% 0.419 1.386
Panel B: Magellan Fund (Market model)
Intercept 0.0003 0.51 61.55% 0.001 0.001
Slope (beta) 1.0526 28.57 0.00% 0.979 1.127
Panel C: Apple (CAPM: Excess returns)
Intercept 0.0054 1.43 15.97% 0.002 0.013
Slope (beta) 0.9025 3.75 0.05% 0.419 1.386
Source: See the file Ch25 Tool Kit.xlsx.
Note: The market model uses actual historical returns; the CAPM model uses returns in excess of the risk-free rate.
998 Part 10 Special Topics
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

## Halaman PDF 1036

```text
Equation 25-10 is called the market model, because it regresses the stock’s return
against the market’s return. However, the SML of the CAPM for realized returns is a little
different from Equation 25-10:
SML for realized returns ri,t rRF,t bi rM,t rRF,t ei,t (25-11)
where rRF,t is the historical (realized) risk-free rate in period t.
In order to use the CAPM to estimate beta, we must rewrite Equation 25-11 as a
regression equation by adding an intercept, ai. The result is:
ri rRF,t ai bi rM,t rRF,t ei,t (25-12)
Therefore, to be theoretically correct when estimating beta, we should use the stock’s
return in excess of the risk-free rate as the y variable and use the market’s return in excess
of the risk-free rate as the x variable. We did this for Apple using the data in Ch25 Tool
Kit.xlsx (which are summarized in Table 25-1); the results are reported in Panel C of
Table 25-2. Note that there are no appreciable differences between the results in Panel A,
the market model, and in Panel C, the CAPM model. This typically is the case, so we will
use the market model in the rest of the book.
25-5c Calculating the Beta Coefficient for a
Portfolio: The Magellan Fund
Let’s calculate beta for Fidelity’s Magellan Fund, which is a well-diversified portfolio.
Figure 25-9 shows the plot of Magellan’s weekly returns versus the market’s weekly returns.
Note the differences between this chart and the one for Apple shown in Figure 25-8. The
points for Magellan are tightly clustered around the regression line, indicating that the vast
majority of Magellan’s variability is explained by the stock market. The R2 of over 0.94
confirms this visual conclusion. We can also see from Table 25-1 that the Magellan Fund
has a standard deviation of 12.2%, which is similar to the 11.2% standard deviation of
the market.
As Table 25-2 shows, Magellan’s estimated beta is 1.05 and the 95% confidence
interval is from 0.979 to 1.127, which is much tighter than the confidence interval for
Apple’s estimated beta. Magellan’s intercept is virtually zero, and the probability of the
intercept’s t-statistic is much greater than 5%. Therefore, the intercept is statistically
insignificant, indicating that the CAPM explains the average weekly return of the Magel￾lan Fund very well.
25-5d Performance Measures
Mutual fund managers are often evaluated by their risk-adjusted performance. The three
most widely used measures are Jensen’s alpha, Sharpe’s reward-to-variability ratio, and
Treynor’s reward-to-volatility ratio.
JENSEN’S ALPHA
Consider the intercept in the CAPM regression of excess returns, shown in Equation 25-12
and repeated here for convenience:
ri rRF,t ai bi rM,t rRF,t ei,t
resource
See Ch25 Tool Kit.xlsx
on the textbook’s Web
site for all calculations
for these performance
measures.
Chapter 25 Portfolio Theory and Asset Pricing Models 999
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

## Halaman PDF 1037

```text
For regression equations that have an intercept, the error terms eit have an average value
of zero Therefore, the estimated intercept, ai, is the average return that is not explained by
the excess market return. In the context of portfolio performance, this intercept is called
Jensen’s alpha.
For the Magellan Fund, the intercept is 1.52% per year (see Ch25 Tool Kit.xlsx for all
calculations). This indicates that the Magellan Fund had slightly better performance than
can be explained by the CAPM. However, statistically, this intercept is not significantly
different from zero. Its t-statistic is 0.51, which is so low a value that it could happen
about 62% of the time by chance even if the intercept were truly zero. When this
probability is greater than 5%, as is the case for Magellan, then most statisticians would
be reluctant to conclude that Magellan’s estimated excess return of 1.52% is not actually
equal to zero.
SHARPE’S REWARD-TO-VARIABILITY RATIO
Sharpe’s reward-to-variability ratio is defined as the portfolio’s average return (in excess
of the risk-free rate) divided by its standard deviation:
Sharpe ratio rp,Avg rRF,Avg
σ of rp,Avg rRF,Avg
(25-13)
FIGURE 25-9
Calculating a Beta Coefficient for Fidelity’s Magellan Fund
Source: See the file Ch25 Tool Kit.xlsx.
1000 Part 10 Special Topics
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

## Halaman PDF 1038

```text
The Sharpe ratio measures the amount of return per unit risk. For performance
evaluation, compare the Sharpe ratio of a portfolio with the Sharpe ratio of a benchmark
asset. For example, suppose the S&P 500 is benchmark for the Magellan Fund. Sharpe’s
ratio for Magellan is 1.26, which is a little greater than the S&P’s measure of 0.95. This
indicates that the Magellan Fund earned a higher return per unit risk than the S&P 500
earned.
TREYNOR’S REWARD-TO-VOLATILITY RATIO
Treynor’s reward-to-volatility ratio is defined as the portfolio’s average return (in excess
of the risk-free rate) divided by its beta:
Treynor ratio
rp,Avg rRF,Avg
bp
(25-14)
The Treynor ratio measures the return per unit of risk as measured by beta. For
Magellan, the Treynor ratio is 14.6%, which is a little better than the S&P 500’s ratio of
13.3%. All in all, the Magellan Fund seems to have slightly overperformed the market, but
perhaps not by a statistically significant amount. Although it’s not clear whether Magellan
“beat the market,” it did dramatically reduce the risk faced by investors as compared with
the risk inherent in a randomly chosen individual stock.
25-5e Additional Insights into Risk and Return
The CAPM provides some additional insights into the relationship between risk and return.
1. The relationship between a stock’s total risk, market risk, and diversifiable risk can be
expressed as follows:
Total risk Variance Market risk Diversifiable risk
σ2
i b2
i σ2
M σ2
ei
(25-15)
Here σ2
i is the variance (or total risk) of Stock i, σ2
M is the variance of the market, bi is
Stock i’s beta coefficient, and σ2
ei is the variance of Stock i’s regression error term.
2. If all the points in Figure 25-8 had plotted exactly on the regression line, then the
variance of the error term, σ2
ei
, would have been zero, and all of the stock’s total risk
would have been market risk. On the other hand, if the points were widely scattered
about the regression line, then much of the stock’s total risk would be diversifiable. The
shares of a large, well-diversified mutual fund will plot very close to the regression line.
3. Beta is a measure of relative market risk, but the actual market risk of Stock i is b2
i σ2
M.
Market risk can also be expressed in standard deviation form, biσM. Therefore, stocks
with higher betas have greater market risk. If beta were zero, the stock would have no
market risk, whereas if beta were 1.0, then the stock would be exactly as risky as the
market—assuming the stock is held in a diversified portfolio—and the stock’s market
risk would be σM.
25-5f Modifying the Historical Beta
Betas are generally estimated from the stock’s characteristic line by running a linear
regression between past returns on the stock in question and past returns on some
Chapter 25 Portfolio Theory and Asset Pricing Models 1001
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

## Halaman PDF 1039

```text
market index. We define betas developed in this manner as historical betas. However,
in most situations, it is the future beta that is needed. This has led to the development of
two different types of betas: (1) adjusted betas and (2) fundamental betas.
Adjusted betas grew largely out of the work of Marshall E. Blume, who showed that
true betas tend to move toward 1.0 over time.9 Therefore, we can begin with a firm’s pure
historical statistical beta, make an adjustment for the expected future movement toward
1.0, and produce an adjusted beta that will, on average, be a better predictor of the future
beta than the unadjusted historical beta would be. Value Line publishes betas based on
approximately this formula:
Adjusted beta 0 67 Historical beta 0 35 1 0 (25-16)
Consider American Camping Corporation (ACC), a retailer of supplies for outdoor
activities. ACC’s historical beta is 1.2. Therefore, its adjusted beta is
Adjusted beta 0 67 1 2 0 35 1 0 1 15
Other researchers have extended the adjustment process to include such fundamental
risk variables as financial leverage, sales volatility, and the like. The end product here is a
fundamental beta, which is constantly adjusted to reflect changes in a firm’s operations
and capital structure. In contrast, with historical betas (including adjusted ones), such
changes might not be reflected until several years after the company’s “true” beta had
changed.
Adjusted betas obviously are heavily dependent on unadjusted historical betas, and so
are fundamental betas as they are actually calculated. Therefore, the plain old historical
beta, calculated as the slope of the characteristic line, is important even if one goes on to
develop a more exotic version.
25-5g Choice of Estimation Period, Holding Period,
and Market Index
When calculating betas from past returns, you must choose the sample estimation period,
which is the amount of calendar time over which you gather past returns. You must also
choose the holding period over which you measure returns, such as weekly returns.
Finally, you must choose an index to represent the market portfolio. Following is a
discussion of each choice.
LENGTH OF ESTIMATION PERIOD
Betas can be based on historical periods of different lengths. For example, data for the
past 1 year, 3 years, 5 years, or even 10 years may be used. Estimated betas can vary
significantly for different choices of estimation periods. For example, the beta esti￾mated from 1 year of data might be very different from the beta estimated from
5 years of data, especially if the company has undergone operating changes or shifts
in capital structure during the 5-year period. Because changes in a company’s opera￾tions or financing can change its beta, most analysts use only 1 to 3 years of past data
to estimate beta.
9
See Marshall E. Blume, “Betas and Their Regression Tendencies,” Journal of Finance, June 1975, pp. 785–796;
and Marshall E. Blume, “On the Assessment of Risk,” Journal of Finance, March 1971, pp. 1–10.
1002 Part 10 Special Topics
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

## Halaman PDF 1040

```text
HOLDING PERIOD FOR MEASURING RETURNS
Returns may be calculated over holding periods of different lengths—a day, a week, a
month, a quarter, a year, and so on. For example, if data on NYSE stocks are analyzed
over a 2-year period, then we might obtain 52 2 104 weekly returns for a stock and for
the market index. Alternatively, we could use monthly returns, which would provide 24
observations in the sample period: 12 2 24. Or we could use daily returns, which
would provide about 524 observations in the 2-year period (there are about 252 trading
days in a year).
Given the choice of holding period for returns and length of the estimation period, the
stock returns would be regressed on the corresponding market returns to obtain the
stock’s beta. In statistical analysis, it is generally better to have more rather than fewer
observations, because using more observations generally leads to greater statistical con￾fidence. This suggests the use of weekly returns and, say, 5 years of data for a sample size
of 260, or even daily returns for a still larger sample size. However, the shorter the holding
period, the more likely the data are to exhibit random “noise.” Also, the greater the
number of years of data, the more likely the company’s basic risk position has changed.
Thus, the choice of both the number of years of data and the length of the holding period
for calculating rates of return involves trade-offs between the preference for many
observations and a desire to rely on more recent and thus more relevant data.
CHOICE OF MARKET INDEX
The value used to represent “the market” is also an important consideration, because the
index that is used can have a significant effect on the calculated beta. Many analysts today
use the New York Stock Exchange Composite Index (based on more than 2,000 common
stocks, weighted by the value of each company), but others use the S&P 500 Index. In
theory, a broader index yields a more theoretically correct estimate of beta. Indeed, the
theoretical index should include returns on all stocks, bonds, leases, private businesses,
real estate, and even “human capital.” As a practical matter, however, we cannot get
accurate returns data on most other types of assets, so measurement problems largely
restrict us to stock indexes.
OUR RECOMMENDATION
Where does this leave financial managers regarding the proper beta? We recommend
estimating your own beta using daily returns for 1 to 2 years. This seems to be the “sweet”
spot that provides the tightest confidence intervals for the estimated betas. Shorter
estimation periods don’t have enough observations, whereas longer estimation periods
have problems associated with betas changing during the estimation period. We also
recommend adjusting the estimated beta using Equation 25-15.
If you don’t estimate your own betas, we recommend Value Line because it estimates
betas similarly to the way we recommend. Alternatively, you could get betas from several
online sources and average them together for a final estimate.
SELF-TEST
Explain the meaning and significance of a stock’s beta coefficient. Illustrate your explanation
by drawing, on one graph, the characteristic lines for stocks with low, average, and high risk.
(Hint: Let your three characteristic lines intersect at ri rM 6%, the assumed risk-free rate.)
What is a typical R2 for the characteristic line of an individual stock? For a portfolio?
What is the market model? How is it different from the SML for the CAPM?
How are total risk, market risk, and diversifiable risk related?
Chapter 25 Portfolio Theory and Asset Pricing Models 1003
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

## Halaman PDF 1041

```text
25-6 Empirical Tests of the CAPM
Does the CAPM’s SML produce reasonable estimates for a stock’s required return? The
literature dealing with empirical tests of the CAPM is quite extensive, so we can give here
only a synopsis of some of the key work.
25-6a Tests of the Stability of Beta Coefficients
According to the CAPM, the beta used to estimate a stock’s market risk should reflect
investors’ estimates of the stock’s future variability in relation to that of the market.
Obviously, we do not know now how a stock will be related to the market in the future,
nor do we know how the average investor views this expected future relative variability.
All we have are data on past variability, which we can use to plot the characteristic line
and to calculate historical betas. If historical betas have been stable over time, then there
would seem to be reason for investors to use past betas as estimators of future variability.
For example, if Stock i’s beta had been stable in the past, then its historical bi would
probably be a good proxy for its ex ante, or expected, beta. By “stable” we mean that if bi
were calculated with data from the period of, say, 2012 to 2016, then this same beta
(approximately) should be found from 2017 to 2021.
Robert Levy, Marshall Blume, and others have studied in depth the question of beta
stability.10 Levy calculated betas for individual securities, as well as for portfolios of
securities, over a range of time intervals. He reached two conclusions: (1) The betas of
individual stocks are unstable and hence past betas for individual securities are not good
estimators of their future risk. (2) Betas of portfolios of ten or more randomly selected
stocks are reasonably stable and hence past portfolio betas are good estimators of future
portfolio volatility. In effect, the errors in individual securities’ betas tend to offset one
another in a portfolio. The work of Blume and others supports this position.
The conclusion that follows from the beta stability studies is that the CAPM is a better
concept for structuring investment portfolios than it is for estimating the required return
for individual securities.11
25-6b Tests of the CAPM Based on the Slope of the SML
The CAPM states that a linear relationship exists between a security’s required rate of
return and its beta. Moreover, when the SML is graphed, the vertical axis intercept should
be rRF, and the required rate of return for a stock (or portfolio) with b 1 0 should be rM,
the required rate of return on the market. Various researchers have attempted to test the
validity of the CAPM by first calculating betas and then plotting subsequent realized rates
of return in graphs such as that in Figure 25-10. Second, researchers then determine
whether the results conform to three CAPM implications: (1) Is the intercept equal to rRF?
(2) Is the plot is linear or curved? (3) Is the slope of the line equal to, rM rRF? Monthly
or daily historical rates of return are generally used for stocks, and both 30-day Treasury
bill rates and long-term Treasury bond rates have been used to estimate the value of rRF.
Also, most of the studies actually analyzed portfolios rather than individual securities
because security betas are so unstable.
10See Robert A. Levy, “On the Short-Term Stationarity of Beta Coefficients,” Financial Analysts Journal,
November/December 1971, pp. 55–62; and Marshall E. Blume, “Betas and Their Regression Tendencies,”
Journal of Finance, June 1975, pp. 785–796.
11For more on beta stability, see Robert W. Kolb and Ricardo J. Rodriguez, “The Regression Tendencies of Betas:
A Reappraisal,” The Financial Review, May 1989, pp. 319–334. Also see Robert Kolb, “Is the Distribution of Betas
Stationary?” Journal of Financial Research, Winter 1990, pp. 279–283.
1004 Part 10 Special Topics
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

## Halaman PDF 1042

```text
Before discussing the results of the tests, it is critical to recognize that although the
CAPM is an ex ante, or forward-looking, model, the data used to test it are entirely
historical. This presents a problem, for there is no reason to believe that realized rates of
return over past holding periods are necessarily equal to the rates of return to expect in
the future. Also, historical betas may or may not reflect expected future risk. This lack of
ex ante data makes it extremely difficult to test the CAPM, but here is a summary of the
key results.
1. The evidence generally shows a significant positive relationship between realized
returns and beta. However, the intercept usually is a bit higher than predicted by
the CAPM and the slope usually is smaller than that predicted by the CAPM.
2. The relationship between risk and return appears to be linear. Empirical studies give
no evidence of significant curvature in the risk–return relationship.
3. Tests that attempt to assess the relative importance of market- and company-specific
risk do not yield conclusive results. The CAPM implies that company-specific risk
should not be relevant, yet both kinds of risk appear to be positively related to security
returns; that is, higher returns seem to be required to compensate for diversifiable as
well as market risk. However, it may be that the observed relationships reflect statistical
problems rather than the true nature of capital markets.
4. Richard Roll has questioned whether it is even conceptually possible to test the
CAPM.12 Roll showed that the linear relationship that prior researchers had
observed in graphs like Figure 25-10 resulted from the mathematical properties of
the models being tested; therefore, a finding of linearity would prove nothing
whatsoever about the CAPM’s validity. Roll’s work did not disprove the CAPM,
FIGURE 25-10
Tests of the CAPM
0 0.5 1.0 1.5 2.0 Risk, bi
Theoretical SML
Fitted SML
Required
Rate of Return
(% )
rRF = 6
rM = 12
12See Richard Roll, “A Critique of the Asset Pricing Theory’s Tests,” Journal of Financial Economics, March 1977,
pp. 129–176.
Chapter 25 Portfolio Theory and Asset Pricing Models 1005
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

## Halaman PDF 1043

```text
but it did demonstrate the virtual impossibility of proving that investors behave in
accordance with its predictions.
5. If the CAPM were completely valid, then it should apply to all financial assets,
including bonds. In fact, when bonds are introduced into the analysis, they do not
plot on the SML. This is worrisome, to say the least.
25-6c Current Status of the CAPM
The CAPM is extremely appealing on an intellectual level: It is logical and rational, and
once someone works through and understands the theory, his or her reaction is usually to
accept it without question. However, doubts begin to arise when one thinks about the
assumptions upon which the model is based, and these doubts are as much reinforced as
reduced by the empirical tests. Our own views on the CAPM’s current status are as
follows.
1. The CAPM framework, with its focus on market as opposed to stand-alone risk, is
clearly a useful way to think about the risk of assets. Thus, as a conceptual model, the
CAPM is fundamentally important.
2. When applied in practice, the CAPM appears to provide neat, precise answers to
important questions about risk and required rates of return. However, the answers
are less clear than they seem. The simple truth is that we do not know precisely how
to measure any of the inputs required to implement the CAPM. These inputs should
all be ex ante, yet only ex post data are available. Furthermore, historical data on rM,
rRF, and betas vary greatly depending on the time period studied and the methods
used to estimate them. Thus, even though the CAPM appears to be precise, estimates
of ri found through its use are subject to potentially large errors.13
3. Because the CAPM is logical in the sense that it represents the way risk-averse people
ought to behave, the model is a useful conceptual tool.
4. It is appropriate to think about many financial problems in a CAPM framework.
However, it is also important to recognize the limitations of the CAPM when using it
in practice.
SELF-TEST
What are the two major types of tests that have been performed to test the validity of the
CAPM? (beta stability; slope of the SML) Explain their results.
Are there any reasons to question the validity of the CAPM? Explain.
25-7 Arbitrage Pricing Theory
The CAPM is a single-factor model. That is, it specifies risk as a function of only one factor,
the security’s beta coefficient. Perhaps the risk–return relationship is more complex, with a
stock’s required return a function of more than one factor. For example, what if investors,
because personal tax rates on capital gains are lower than those on dividends, value capital
gains more highly than dividends? Then, if two stocks had the same market risk, the stock
paying the higher dividend would have the higher required rate of return. In that case,
required returns would be a function of two factors: market risk and dividend policy.
13For an article supporting a positive link between market risk and expected return, see Felicia Marston and
Robert S. Harris, “Risk and Return: A Revisit Using Expected Returns,” The Financial Review, February 1993,
pp. 117–137.
1006 Part 10 Special Topics
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

## Halaman PDF 1044

```text
Further, what if many factors are required to specify the equilibrium risk–return
relationship rather than just one or two? Stephen Ross has proposed an approach called
the Arbitrage Pricing Theory (APT).
14 The APT can include any number of risk
factors, so the required return could be a function of two, three, four, or more factors.
We should note at the outset that the APT is based on complex mathematical and
statistical theory that goes far beyond the scope of this text. Also, although the APT
model is widely discussed in academic literature, practical usage to date has been
limited. However, such use may increase, so students should at least have an intuitive
idea of what the APT is all about.
The SML states that each stock’s required return is equal to the risk-free rate plus the
product of the market risk premium times the stock’s beta coefficient. If stocks are in
equilibrium, then the required return will be equal to the expected return:
r
^
i ri rRF rM rRF bi
The historical realized return, ri, which will generally be different from the expected
return, can be expressed as follows:15
ri r
^
i rM r
^
M bi ei (25-17)
Thus, the realized return, ri, will be equal to the expected return, r^
i
, plus a positive or
negative increment, rM r
^
M bi, which depends jointly on the stock’s beta and on
whether the market did better or worse than was expected, plus a random error term, ei.
The market’s realized return, rM, is in turn determined by a number of factors,
including domestic economic activity as measured by gross domestic product (GDP),
the strength of the world economy, the level of inflation, changes in tax laws, and so forth.
Further, different groups of stocks are affected in different ways by these fundamental
factors. So, rather than specifying a stock’s return as a function of one factor (return on
the market), one could specify required and realized returns on individual stocks as a
function of various fundamental economic factors. If this were done, we would transform
Equation 25-17 into 25-18:
ri r
^
i r1 F
^
1 bi1 Fj F
^
j bij ei (25-18)
Here,
ri Realized rate of return on Stock i
r
^
i Expected rate of return on Stock i
Fj Realized value of economic Factor j
F
^
j Expected value of Factor j
bij Sensitivity of Stock i to economic Factor j
ei Effect of unique events on the realized return of Stock i
14See Stephen A. Ross, “The Arbitrage Theory of Capital Asset Pricing,” Journal of Economic Theory, December
1976, pp. 341–360.
15To avoid cluttering the notation, we have dropped the subscript t to denote a particular time period.
Chapter 25 Portfolio Theory and Asset Pricing Models 1007
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

## Halaman PDF 1045

```text
Equation 25-18 shows that the realized return on any stock is the sum of: (1) the
stock’s expected return; (2) increases or decreases that depend on unexpected changes in
fundamental economic factors, multiplied by the sensitivity of the stock to these changes;
and (3) a random term that reflects changes unique to the firm.
Certain stocks or groups of stocks are most sensitive to Factor 1, others to Factor 2, and
so forth, and every portfolio’s returns depend on what happened to the different funda￾mental factors. Theoretically, one could construct a portfolio with these two properties:
(1) The portfolio is riskless. (2) The net investment in it is zero (some stocks would be sold
short, with the proceeds from the short sales being used to buy the stocks held long). Such a
zero-investment portfolio must have a zero expected return, or else arbitrage operations
would occur and cause the prices of the underlying assets to change until the portfolio’s
expected return became zero. Using this key insight and the hypothesized risk–return
relationship for actual returns in Equation 25-18, the APT determines the risk–return
relationship for required returns (i.e., equivalent of the CAPM’s Security Market Line):16
ri rRF r1 rRF bi1 rj rRF bij (25-19)
Here, rj is the required rate of return on a portfolio that is sensitive only to economic Factor j
bpj 1 0 and has zero sensitivity to all other factors. Thus, for example, r2 rRF is the
risk premium on a portfolio with bp2 1 0 and all other bpj 0 0. Note that Equation 25-16
is identical in form to the SML, but it permits a stock’s required return to be a function of
multiple factors.
To illustrate the APT concept, assume that all stocks’ returns depend on only three
risk factors: inflation, industrial production, and the aggregate degree of risk aversion (the
cost of bearing risk, which we assume is reflected in the spread between the yields on
Treasury and low-grade bonds). Further, suppose that: (1) The risk-free rate is 8.0%.
(2) The required rate of return is 13% on a portfolio with unit sensitivity b 1 0 to
inflation and zero sensitivities b 0 0 to industrial production and degree of risk
aversion. (3) The required return is 10% on a portfolio with unit sensitivity to industrial
production and zero sensitivities to inflation and degree of risk aversion. (4) The required
return is 6% on a portfolio (the risk-bearing portfolio) with unit sensitivity to the degree
of risk aversion and zero sensitivities to inflation and industrial production. Finally,
assume that Stock i has factor sensitivities (betas) of 0.9 to the inflation portfolio, 1.2 to
the industrial production portfolio, and 0.7 to the risk-bearing portfolio. Stock i’s
required rate of return, according to the APT, would be 16.3%:
ri 8% 13% 8% 0 9 10% 8% 1 2 6% 8% 0 7
16 3%
Note that if the required rate of return on the market were 15.0% and if Stock i had a
CAPM beta of 1.1, then its required rate of return, according to the SML, would be 15.7%:
ri 8% 15% 8% 1 1 15 7%
The primary theoretical advantage of the APT is that it permits several economic
factors to influence individual stock returns, whereas the CAPM assumes that the effect of
all factors, except those that are unique to the firm, can be captured in a single measure:
the variability of the stock with respect to the market portfolio. Also, the APT requires
16See Thomas E. Copeland, J. Fred Weston, and Kuldeep Shastri, Financial Theory and Corporate Policy, 4th ed.
(Reading, MA: Addison-Wesley, 2005).
1008 Part 10 Special Topics
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

## Halaman PDF 1046

```text
fewer assumptions than the CAPM and hence is more general. Finally, the APT does not
assume that all investors hold the market portfolio, a CAPM requirement that is clearly
not met in practice.
However, the APT faces several major hurdles in implementation, the most severe of
which is that the theory does not actually identify the relevant factors. The APT does not tell
us what factors influence returns, nor does it indicate how many factors should appear in
the model. There is some empirical evidence that only three or four factors are relevant—
perhaps inflation, industrial production, the spread between low- and high-grade bonds,
and the term structure of interest rates—but no one knows for sure.
The APT’s proponents argue that it is not necessary to identify the relevant factors.
Researchers use a statistical procedure called factor analysis to develop the APT para￾meters. Basically, they start with hundreds, or even thousands, of stocks and then create
several different portfolios, where the returns on each portfolio are not highly correlated
with returns on the other portfolios. Thus, each portfolio is apparently more heavily
influenced by one of the unknown factors than are the other portfolios. Then, the required
rate of return on each portfolio becomes the estimate for that unknown economic factor,
shown as rj in Equation 25-19. The sensitivities of each individual stock’s returns to the
returns on that portfolio are the factor sensitivities (betas). Unfortunately, the results of
factor analysis are not easily interpreted; hence, it does not provide significant insights
into the underlying economic determinants of risk.17
SELF-TEST
What is the primary difference between the APT and the CAPM?
What are some disadvantages of the APT?
An analyst has modeled the stock of Brown Kitchen Supplies using a two-factor APT model. The risk￾free rate is 5%, the required return on the first factor r1 is 10%, and the required return on the
second factor r2 is 15%. If bi1 0 5 and bi2 1 3, what is Brown’s required return? (20.5%)
SUMMARY
The primary goal of this chapter was to extend your knowledge of risk and return concepts.
The key concepts covered are listed here.
• The feasible set of portfolios represents all portfolios that can be constructed from a
given set of assets.
• An efficient portfolio is one that offers the most return for a given amount of risk or
the least risk for a given amount of return.
• The optimal portfolio for an investor is defined by the investor’s highest possible
indifference curve that is tangent to the efficient set of portfolios.
• The Capital Asset Pricing Model (CAPM) describes the relationship between market
risk and required rates of return.
17For additional discussion of the APT, see Edward L. Bubnys, “Simulating and Forecasting Utility Stock Returns:
Arbitrage Pricing Theory vs. Capital Asset Pricing Model,” The Financial Review, February 1990, pp. 1–23; David
H. Goldenberg and Ashok J. Robin, “The Arbitrage Pricing Theory and Cost-of-Capital Estimation: The Case of
Electric Utilities,” Journal of Financial Research, Fall 1991, pp. 181–196; and Ashok Robin and Ravi Shukla, “The
Magnitude of Pricing Errors in the Arbitrage Pricing Theory,” Journal of Financial Research, Spring 1991, pp. 65–82.
Chapter 25 Portfolio Theory and Asset Pricing Models 1009
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

## Halaman PDF 1047

```text
• The Capital Market Line (CML) describes the risk–return relationship for efficient
portfolios—that is, for portfolios consisting of a mix of the market portfolio and a
riskless asset.
• The Security Market Line (SML) is an integral part of the CAPM, and it describes the
risk–return relationship for individual assets. The required rate of return for any Stock i
is equal to the risk-free rate plus the market risk premium multiplied by the stock’s
beta coefficient: ri rRF rM rRF bi.
• Stock i’s beta coefficient, bi, is a measure of the stock’s market risk. Beta measures the
variability of a security’s returns relative to the stock market.
• The beta coefficient is measured by the slope of the stock’s characteristic line, which is
found by regressing past stock returns versus past market returns.
• In contrast to the CAPM, the Arbitrage Pricing Theory (APT) hypothesizes that
expected stock returns are due to more than one factor.
QUESTIONS
(25-1) Define the following terms, using graphs or equations to illustrate your answers wherever
feasible:
a. Portfolio; feasible set; efficient portfolio; efficient frontier
b. Indifference curve; optimal portfolio
c. Capital Asset Pricing Model (CAPM); Capital Market Line (CML)
d. Characteristic line; beta coefficient, b
e. Arbitrage Pricing Theory (APT)
(25-2) Security A has an expected rate of return of 6%, a standard deviation of returns of 30%,
a correlation coefficient with the market of 0.25, and a beta coefficient of 0.5. Security B
has an expected return of 11%, a standard deviation of returns of 10%, a correlation with the
market of 0.75, and a beta coefficient of 0.5. Which security is more risky? Why?
SELF-TEST PROBLEM Solution Shown in Appendix A
(ST-1) You are planning to invest $200,000. Two securities are available, A and B, and you can
invest in either of them or in a portfolio with some of each. You estimate that the
following probability distributions of returns are applicable for A and B:
Security A Security B
PA rA PB rB
0.1 10.0% 0.1 30.0%
0.2 5.0 0.2 0.0
0.4 15.0 0.4 20.0
0.2 25.0 0.2 40.0
0.1 40.0 0.1 70.0
r
^
A r
^
B 20 0%
σA σB 25 7%
Risk and Return
1010 Part 10 Special Topics
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

## Halaman PDF 1048

```text
a. The expected return for Security B is r^
B 20%, and σB 25 7%. Find r^
Aand σA.
b. Use Equation 25-3 to find the value of wA that produces the minimum risk portfolio.
Assume ρAB 0 5 for parts b and c.
c. Construct a table giving r^
p and σp for portfolios with wA 1 00, 0.75, 0.50, 0.25, 0.0,
and the minimum risk value of wA. (Hint: For wA 0 75, r^
p 16 25% and
σp 8 5%; for wA 0 5, r^
p 17 5% and σp 11 1%; for wA 0 25, r^
p 18 75%
and σp 17 9%.)
d. Graph the feasible set of portfolios and identify the efficient frontier of the
feasible set.
e. Suppose your risk–return trade-off function, or indifference curve, is tangent to the
efficient set at the point where r^
p 18%. Use this information, together with the
graph constructed in part d, to locate (approximately) your optimal portfolio. Draw
in a reasonable indifference curve, indicate the percentage of your funds invested in
each security, and determine the optimal portfolio’s σp and r^
p. (Hint: Estimate σp and
r
^
p graphically; then use the equation for r^
p to determine wA.)
f. Now suppose a riskless asset with a return rRF 10% becomes available. How would
this change the investment opportunity set? Explain why the efficient frontier
becomes linear.
g. Given the indifference curve in part e, would you change your portfolio? If so, how?
(Hint: Assume that the indifference curves are parallel.)
h. What are the beta coefficients of Stocks A and B? (Hint: Recognize that ri rRF
bi rM rRF and then solve for bi; assume that your preferences match those of most
other investors.)
PROBLEMS Answers Are in Appendix B
EASY PROBLEMS 1–2
The standard deviation of stock returns for Stock A is 40%. The standard deviation of the
market return is 20%. If the correlation between Stock A and the market is 0.70, then what
is Stock A’s beta?
An analyst has modeled the stock of Crisp Trucking using a two-factor APT model. The risk￾free rate is 6%, the expected return on the first factor r1 is 12%, and the expected return on
the second factor r2 is 8%. If bi1 0 7 and bi2 0 9, what is Crisp’s required return?
INTERMEDIATE PROBLEMS 3–4
Stock A has an expected return of 12% and a standard deviation of 40%. Stock B has an
expected return of 18% and a standard deviation of 60%. The correlation coefficient
between Stocks A and B is 0.2. What are the expected return and standard deviation of a
portfolio invested 30% in Stock A and 70% in Stock B?
The beta coefficient of an asset can be expressed as a function of the asset’s correlation
with the market as follows:
bi
ρiMσi
σM
a. Substitute this expression for beta into the Security Market Line (SML), Equation 25-9.
This results in an alternative form of the SML.
b. Compare your answer to part a with the Capital Market Line (CML), Equation 25-6.
What similarities do you observe? What conclusions can you draw?
(25-1)
Beta
(25-2)
APT
(25-3)
Two-Asset Portfolio
(25-4)
SML and CML
Comparison
Chapter 25 Portfolio Theory and Asset Pricing Models 1011
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

## Halaman PDF 1049

```text
CHALLENGING PROBLEMS 5–6
You are given the following set of data:
Historical Rates of Return
Year NYSE Stock X
1 26.5% 14.0%
2 37.2 23.0
3 23.8 17.5
4 7.2 2.0
5 6.6 8.1
6 20.5 19.4
7 30.6 18.2
a. Use a spreadsheet (or a calculator with a linear regression function) to determine
Stock X’s beta coefficient.
b. Determine the arithmetic average rates of return for Stock X and the NYSE over the
period given. Calculate the standard deviations of returns for both Stock X and the
NYSE.
c. Assume that the situation during Years 1 to 7 is expected to prevail in the future
(i.e., r^
X rX,Average, r^
M rM,Average, and both σX and bX in the future will equal their
past values). Also assume that Stock X is in equilibrium—that is, it plots on the
Security Market Line. What is the risk-free rate?
d. Plot the Security Market Line.
e. Suppose you hold a large, well-diversified portfolio and are considering adding to
that portfolio either Stock X or another stock, Stock Y, which has the same beta as
Stock X but a higher standard deviation of returns. Stocks X and Y have the same
expected returns: r^
X r
^
Y 10 6%. Which stock should you choose?
You are given the following set of data:
Historical Rates of Return
Year NYSE Stock Y
1 4.0% 3.0%
2 14.3 18.2
3 19.0 9.1
4 14.7 6.0
5 26.5 15.3
6 37.2 33.1
7 23.8 6.1
8 7.2 3.2
9 6.6 14.8
10 20.5 24.1
11 30.6 18.0
Mean 9 8% 9.8%
σ 19 6% 13.8%
(25-5)
Characteristic Line
and Security
Market Line
(25-6)
Characteristic Line
1012 Part 10 Special Topics
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

## Halaman PDF 1050

```text
a. Construct a scatter diagram showing the relationship between returns on Stock Y and
the market. Use a spreadsheet or a calculator with a linear regression function to
estimate beta.
b. Give a verbal interpretation of what the regression line and the beta coefficient show
about Stock Y’s volatility and relative risk as compared with those of other stocks.
c. Suppose the regression line were exactly as shown by your graph from part b but the
scatter plot of points was more spread out. How would this affect: (1) the firm’s risk if
the stock is held in a one-asset portfolio, and (2) the actual risk premium on the stock
if the CAPM holds exactly?
d. Suppose the regression line were downward sloping and the beta coefficient were
negative. What would this imply about: (1) Stock Y’s relative risk, (2) its correlation
with the market, and (3) its probable risk premium?
SPREADSHEET PROBLEM
(25-7) Start with the partial model in the file Ch25 P07 Build a Model.xlsx from the textbook’s
Web site. Following is information for the required returns and standard deviations of
returns for A, B, and C:
Stock ri σi
A 7.0% 33.11%
B 10.0 53.85
C 20.0 89.44
The correlation coefficients for each pair are shown below in a matrix, with each cell in
the matrix giving the correlation between the stock in that row and column. For example,
ρAB 0 1571 is in the row for A and the column for B. Notice that the diagonal values are
equal to 1 because a variable is always perfectly correlated with itself.
AB C
A 1.0000 0.1571 0.1891
B 0.1571 1.0000 0.1661
C 0.1891 0.1661 1.0000
a. Suppose a portfolio has 30% invested in A, 50% in B, and 20% in C. What are the
expected return and standard deviation of the portfolio?
b. The partial model lists six different combinations of portfolio weights. For each
combination of weights, find the required return and standard deviation.
c. The partial model provides a scatter diagram showing the required returns and
standard deviations already calculated. This provides a visual indicator of the feasible
set. If you seek a return of 10.5%, then what is the smallest standard deviation that
you must accept?
Feasible Portfolios
Chapter 25 Portfolio Theory and Asset Pricing Models 1013
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

## Halaman PDF 1051

```text
MINI CASE
You have been hired at the investment firm of Bowers & Noon. One of its clients doesn’t
understand the value of diversification or why stocks with the biggest standard deviations
don’t always have the highest expected returns. Your assignment is to address the client’s
concerns by showing the client how to answer the following questions.
a. Suppose Asset A has an expected return of 10% and a standard deviation of 20%.
Asset B has an expected return of 16% and a standard deviation of 40%. If the
correlation between A and B is 0.35, what are the expected return and standard
deviation for a portfolio consisting of 30% Asset A and 70% Asset B?
b. Plot the attainable portfolios for a correlation of 0.35. Now plot the attainable
portfolios for correlations of 1.0 and 1.0.
c. Suppose a risk-free asset has an expected return of 5%. By definition, its standard
deviation is zero, and its correlation with any other asset is also zero. Using only
Asset A and the risk-free asset, plot the attainable portfolios.
d. Construct a plausible graph that shows risk (as measured by portfolio standard
deviation) on the x-axis and expected rate of return on the y-axis. Now add an
illustrative feasible (or attainable) set of portfolios and show what portion of the
feasible set is efficient. What makes a particular portfolio efficient? Don’t worry about
specific values when constructing the graph—merely illustrate how things look with
“reasonable” data.
e. Add a set of indifference curves to the graph created for part b. What do these curves
represent? What is the optimal portfolio for this investor? Add a second set of
indifference curves that leads to the selection of a different optimal portfolio. Why do
the two investors choose different portfolios?
f. Now add the risk-free asset. What impact does this have on the efficient frontier?
g. Write out the equation for the Capital Market Line (CML), and draw it on the graph.
Interpret the plotted CML. Now add a set of indifference curves and illustrate how an
investor’s optimal portfolio is some combination of the risky portfolio and the risk￾free asset. What is the composition of the risky portfolio?
h. What is the Capital Asset Pricing Model (CAPM)? What are the assumptions that
underlie the model? What is the Security Market Line (SML)?
i. What is a characteristic line? How is this line used to estimate a stock’s beta
coefficient? Write out and explain the formula that relates total risk, market risk,
and diversifiable risk.
j. What are two potential tests that can be conducted to verify the CAPM? What are the
results of such tests? What is Roll’s critique of CAPM tests?
k. Briefly explain the difference between the CAPM and the Arbitrage Pricing Theory
(APT).
SELECTED ADDITIONAL CASE
The following case from CengageCompose covers many of the concepts discussed in this
chapter and is available at http://compose.cengage.com.
Klein-Brigham Series:
Case 2, “Peachtree Securities, Inc. (A).”
1014 Part 10 Special Topics
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

