# Chapter 8: Financial Options and Applications in Corporate Finance

[Daftar isi](SUMMARY.md) · [Panduan belajar](KAJIAN.md)

Sumber: PDF halaman 380–411. Teks ekstraksi; simbol, tabel, dan rumus belum seluruhnya diverifikasi secara visual.

## Halaman PDF 380

```text
CHAPTER 8
Financial Options and
Applications in Corporate
Finance
In 2015, Cisco had about 180 million outstanding employee stock options and about
5.1 billion outstanding shares of stock. If all these options are exercised, then the
option holders will own about 3.4% of Cisco’s stock: 0 180 5 1 0 180 0 034.
Many of these options may never be exercised, but any way you look at it, 180 million
is a lot of options.
In a typical grant, you receive options allowing you to purchase shares of stock at
a fixed price, called the strike price or exercise price, on or before a stated expiration
date. Most plans have a vesting period, during which you can’t exercise the options.
For example, suppose you are granted 1,000 options with a strike price of $50, an
expiration date 10 years from now, and a vesting period of 3 years. Even if the stock
price rises above $50 during the first 3 years, you can’t exercise the options because
of the vesting requirement. After 3 years, if you are still with the company, you have
the right to exercise the options. For example, if the stock goes up to $110, you could
pay the company $50 1,000 $50,000 and receive 1,000 shares of stock worth
$110,000. However, if you don’t exercise the options within 10 years, they will expire
and thus be worthless.
Even though the vesting requirement prevents you from exercising the options the
moment they are granted to you, the options clearly have some immediate value.
Therefore, if you are choosing between different job offers where options are
involved, you will need a way to determine the value of the alternative options. This
chapter explains how to value options, so read on.
343
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

## Halaman PDF 381

```text
There are two fundamental approaches to valuing assets. The first is the discounted cash
flow (DCF) approach, which we covered in previous chapters: An asset’s value is the
present value of its cash flows. The second is the option pricing approach. It is important
that every manager understands the basic principles of option pricing for the following
reasons. First, many projects allow managers to make strategic or tactical changes in plans
as market conditions change. The existence of these “embedded options” often means the
difference between a successful project and a failure. Understanding basic financial
options can help you manage the value inherent in these real options. Second, many
companies use derivatives to manage risk; many derivatives are types of financial options,
so an understanding of basic financial options is necessary before tackling derivatives.
Third, option pricing theory provides insights into the optimal debt/equity choice,
especially when convertible securities are involved. And fourth, knowing about financial
options will help you understand any employee stock options that you receive.
8-1 Overview of Financial Options
In general, an option is a contract that gives its owner the right to buy (or sell) an asset at
some predetermined price within a specified period of time. However, there are many
types of options and option markets.1 Consider the options reported in Table 8-1, which
is an extract from a Listed Options Quotations table as it might appear on a Web site or in
a daily newspaper. The first column reports the closing stock price. For example, the table
shows that General Computer Corporation’s (GCC) stock price closed at $53.50 on
January 7, 2016.
The Intrinsic Value of Stock Options
In previous chapters we showed that the intrinsic value of
an asset is the present value of its cash flows. This time
value of money approach works well for stocks and bonds,
but we must use another approach for options and
derivatives. If we can find a portfolio of stocks and risk-free
bonds that replicates an option’s cash flows, then the
intrinsic value of the option must be identical to the value
of the replicating portfolio.
Risk-free bond
Stock price = + … ++ D1
(1 + rs)1
D2
(1 + rs)2
D∞
(1 + rs)
∞
Portfolio of stocks and
risk-free bonds that
replicates cash flows
of the option
Value of option must
be the same as the
replicating portfolio
Cost of
equity (rs) Dividends (Dt)
1
For an in-depth treatment of options, see Don M. Chance and Robert Brooks, An Introduction to Derivatives
and Risk Management, 8th ed. (Mason, OH: South-Western, Cengage Learning, 2010), or John C. Hull, Options,
Futures, and Other Derivatives, 8th ed. (Upper Saddle River, NJ: Prentice-Hall, 2012).
resource
The textbook’s Web site
contains an Excel file
that will guide you
through the chapter’s
calculations. The file for
this chapter is Ch08 Tool
Kit.xlsx, and we
encourage you to open
the file and follow along
as you read the chapter.
344 Part 3 Stocks and Options
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

## Halaman PDF 382

```text
A call option gives its owner the right to buy a share of stock at a fixed price, which is
called the strike price (sometimes called the exercise price because it is the price at which
you exercise the option). A put option gives its owner the right to sell a share of stock at a
fixed strike price. For example, the first row in Table 8-1 is for GCC’s options that have a
$50 strike price. Observe that the table has columns for call options and for put options
with this strike price.
Each option has an expiration date, after which the option may not be exercised.
Table 8-1 reports data for options that expire in February, March, and May.2 If the option
can be exercised any time before the expiration, it is called an American option; if it can
be exercised only on its expiration date, it is a European option. All of GCC’s options are
American options. The first row shows that GCC has a call option with a strike price of
$50 that expires on May 21 (the third Friday in May 2016 is the 20th). The quoted price
for this option is $5.50.3
When the current stock price is greater than the strike price, the option is in-the￾money. For example, GCC’s $50 (strike) May call option is in-the-money by
$53 50 $50 $3 50. Thus, if the option were immediately exercised, it would have a
payoff of $3.50. On the other hand, GCC’s $55 (strike) May call is out-of-the-money
because the current $53.50 stock price is below the $55 strike price. Obviously, you
currently would not want to exercise this option by paying the $55 strike price for a
share of stock selling for $53.50. Therefore, the exercise value, which is the payoff from
immediately exercising an option, is:4
Exercise value MAX Current price of the stock Strike price, 0 (8-1)
An American option’s price always will be greater than (or equal to) its exercise value.
If the option’s price were less, you could buy the option and immediately exercise it,
TABLE 8-1
Listed Options Quotations for January 7, 2016
CALLS—LAST QUOTE PUTS—LAST QUOTE
Closing Price Strike Price February March May February March May
General Computer Corporation (GCC)
53.50 50 4.25 4.75 5.50 0.65 1.40 2.20
53.50 55 1.30 2.05 3.15 2.65 r 4.50
53.50 60 0.30 0.70 1.50 6.65 r 8.00
Note: r means not traded on January 7.
2
At its Web site, www.cboe.com/learncenter/glossary.aspx, the CBOE defines the expiration date as follows:
“The day on which an option contract becomes void. The expiration date for listed stock options is the Saturday
after the third Friday of the expiration month. Holders of options should indicate their desire to exercise, if they
wish to do so, by this date.” The CBOE also defines the expiration time as: “The time of day by which all exercise
notices must be received on the expiration date. Technically, the expiration time is currently 5:00PM on the
expiration date, but public holders of option contracts must indicate their desire to exercise no later than 5:30PM
on the business day preceding the expiration date. The times are Eastern Time.”
3
Option contracts are generally written in 100-share multiples, but to reduce confusion we focus on the cost and
payoffs of a single option.
4
MAX means choose the maximum. For example, MAX 15, 0 15 and MAX −10, 0 0.
Chapter 8 Financial Options and Applications in Corporate Finance 345
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

## Halaman PDF 383

```text
reaping a sure gain. For example, GCC’s May call with a $50 strike price sells for $5.50,
which is greater than its exercise value of $3.50. Also, GCC’s out-of-the-money May call
with a strike price of $55 sells for $3.15 even though it would be worthless if it had to be
exercised immediately. An option always will be worth more than zero as long as there is
still any chance it will end up in-the-money: Where there is life, there is hope! The
difference between the option’s price and its exercise value is called the time value because
it represents the extra amount over the option’s immediate exercise value that a purchaser
will pay for the chance the stock price will appreciate over time.5 For example, GCC’s May
call with a $50 strike price sells for $5.50 and has an exercise value of $3.50, so its time
value is $5 50 $3 50 $2 00.
Suppose you bought GCC’s $50 (strike) May call option for $5.50 and then the
stock price increased to $60. If you exercised the option by purchasing the stock for
the $50 strike price, you could immediately sell the share of stock at its market price
of $60, resulting in a payoff of $60 $50 $10. Notice that the stock itself had a return of
12 1% $60 $53 50 $53 50, but the option’s return was 81 8% $10 $5 50 $5 50.
Thus, the option offers the possibility of a higher return.
However, if the stock price fell to $50 and stayed there until the option expired, the
stock would have a return of 6 5% $50 00 $53 50 $53 50, but the option would
have a 100% loss (it would expire worthless). As this example shows, call options are a lot
riskier than stocks. This works to your advantage if the stock price goes up but to your
disadvantage if the stock price falls.
Suppose you bought GCC’s May put option (with a strike price of $50) for $2.20 and
then the stock price fell to $45. You could buy a share of stock for $45 and exercise the put
option, which would allow you to sell the share of stock at its strike price of $50. Your
payoff from exercising the put would be $5 $50 $45. Stockholders would lose money
because the stock price fell, but a put holder would make money. In this example, your
rate of return would be 127 3% $5 $2 20 $2 20. So if you think a stock price is
going to fall, you can make money by purchasing a put option. On the other hand, if the
stock price doesn’t fall below the strike price of $50 before the put expires, you would lose
100% of your investment in the put option.6
Options are traded on a number of exchanges, with the Chicago Board Options
Exchange (CBOE) being the oldest and the largest. Existing options can be traded in
the secondary market in much the same way that existing shares of stock are traded in
secondary markets. But unlike new shares of stock that are issued by corporations, new
options can be “issued” by investors. This is called writing an option.
For example, you could write a call option and sell it to some other investor. You
would receive cash from the option buyer at the time you wrote the option, but you would
be obligated to sell a share of stock at the strike price if the option buyer later decided to
exercise the option.7 Thus, each option has two parties, the writer and the buyer, with the
CBOE (or some other exchange) acting as an intermediary. Other than commissions, the
writer’s profits are exactly opposite those of the buyer. An investor who writes call options
against stock held in his or her portfolio is said to be selling covered options. Options
sold without the stock to back them up are called naked options.
5
Among traders, an option’s market price is also called its “premium.” This is particularly confusing because for
all other securities the word premium means the excess of the market price over some base price. To avoid
confusion, we will not use the word premium to refer to the option price.
6
Most investors don’t actually exercise an option prior to expiration. If they want to cash in the option’s profit or cut
its losses, they sell the option to some other investor. As you will see later in the chapter, the cash flow from selling an
American option before its expiration is always greater than (or equal to) the profit from exercising the option.
7
Your broker would require collateral to ensure that you kept this obligation.
346 Part 3 Stocks and Options
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

## Halaman PDF 384

```text
In addition to options on individual stocks, options are also available on several stock
indexes such as the NYSE Index and the S&P 100 Index. Index options permit one to
hedge (or bet) on a rise or fall in the general market as well as on individual stocks.
The leverage involved in option trading makes it possible for speculators with just a
few dollars to make a fortune almost overnight. Also, investors with sizable portfolios can
sell options against their stocks and earn the value of the option (less brokerage commis￾sions) even if the stock’s price remains constant. Most important, though, options can be
used to create hedges that protect the value of an individual stock or portfolio.8
Conventional options are generally written for 6 months or less, but a type of option
called a Long-Term Equity AnticiPation Security (LEAPS) is different. Like conventional
options, LEAPS are listed on exchanges and are available on both individual stocks and
stock indexes. The major difference is that LEAPS are long-term options, having maturities
of up to almost 3 years. One-year LEAPS cost about twice as much as the matching
3-month option, but because of their much longer time to expiration, LEAPS provide
buyers with more potential for gains and offer better long-term protection for a portfolio.
Corporations on whose stocks the options are written have nothing to do with the
option market. Corporations do not raise money in the option market, nor do they have
any direct transactions in it. Moreover, option holders do not vote for corporate directors
or receive dividends. There have been studies by the SEC and others as to whether option
trading stabilizes or destabilizes the stock market and whether this activity helps or
hinders corporations seeking to raise new capital. The studies have not been conclusive,
but research on the impact of option trading is ongoing.
SELF-TEST
What is an option? A call option? A put option?
Define a call option’s exercise value. Why is the market price of a call option always above its
exercise value?
Brighton Memory’s stock is currently trading at $50 a share. A call option on the stock with
a $35 strike price currently sells for $21. What is the exercise value of the call option? ($15.00)
What is the time value? ($6.00)
8-2 The Single-Period Binomial Option
Pricing Approach
We can use a model like the Capital Asset Pricing Model (CAPM) to calculate the
required return on a stock and then use that required return to discount its expected
future cash flows to find its value. No such model exists for the required return on
options, so we must use a different approach to find an option’s value. In Section 8-5 we
describe the Black-Scholes option pricing model, but in this section we explain the
binomial option pricing model. The idea behind this model is different from that of the
DCF model used for stock valuation. Instead of discounting cash flows at a required
return to obtain a price, as we did with the stock valuation model, we will use the option,
8
Insiders who trade illegally generally buy options rather than stock because the leverage inherent in options
increases the profit potential. However, it is illegal to use insider information for personal gain, and an insider
using such information would be taking advantage of the option seller. Insider trading, in addition to being
unfair and essentially equivalent to stealing, hurts the economy: Investors lose confidence in the capital markets
and raise their required returns because of an increased element of risk, and this raises the cost of capital and
thus reduces the level of real investment.
www
The Chicago Board
Options Exchange
provides 20-minute
delayed quotes for
equity, index, and LEAPS
options at www.cboe
.com.
Chapter 8 Financial Options and Applications in Corporate Finance 347
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

## Halaman PDF 385

```text
shares of stock, and the risk-free rate to construct a portfolio whose value we already
know and then deduce the option’s price from this portfolio’s value.
The following sections describe and apply the binomial option pricing model to
Western Cellular, a manufacturer of cell phones. Call options exist that permit the holder
to buy 1 share of Western at a strike price, X, of $35. Western’s options will expire at the
end of 6 months (t is the number of years until expiration, so t 0.5 for Western’s
options). Western’s stock price, P, is currently $40 per share. Given this background
information, we will use the binomial model to determine the call option’s value. The first
step is to determine the option’s possible payoffs, as described in the next section.
8-2a Payoffs in a Single-Period Binomial Model
In general, the time until expiration can be divided into many periods, with n denoting the
number of periods. But in a single-period model, which we describe in this section, there is
only one period. We assume that, at the end of the period, the stock’s price can take on only
one of two possible values, so this is called the binomial approach. For this example,
Western’s stock will either go up (u) by a factor of 1.25 or go down (d) by a factor of
0.80. If we were considering a riskier stock, then we would have assumed a wider range of
ending prices; we will show how to estimate this range later in the chapter. If we let u 1.25
and d 0.80, then the ending stock price will be either P u $40 1 25 $50 or
P d $40 0 80 $32. Figure 8-1 illustrates the stock’s possible price paths and contains
additional information about the call option that is explained in the text that follows.
When the option expires at the end of the period, Western’s stock will sell for either $50 or
$32. As shown in Figure 8-1, if the stock goes up to $50 then the option will have a payoff, Cu, of
$15 at expiration because the option is in-the-money: $50 $35 $15. If the stock price goes
down to $32, then the option’s payoff, Cd, will be zero because the option is out-of-the-money.
Financial Reporting for Employee Stock Options
When granted to executives and other employees, options
are a “hybrid” form of compensation. At some companies,
especially small ones, option grants may be a substitute for
cash wages: Employees are willing to take lower cash
salaries if they have options. Options also provide an
incentive for employees to work harder. Whether issued
to motivate employees or to conserve cash, options clearly
have value at the time they are granted, and they transfer
wealth from existing shareholders to employees to the
extent that they do not reduce cash expenditures or
increase employee productivity enough to offset their
value at the time of issue.
Companies like the fact that an option grant requires
no immediate cash expenditure, although it might dilute
shareholder wealth if it is exercised later. Employees, and
especially CEOs, like the potential wealth they receive
when they are granted options. When option grants were
relatively small, they didn’t show up on investors’ radar
screens. However, as the high-tech sector began making
mega-grants in the 1990s, and as other industries followed
suit, stockholders began to realize that large grants were
making some CEOs filthy rich at the stockholders’ expense.
Before 2005, option grants were barely visible in com￾panies’ financial reports. Even though such grants are
clearly a wealth transfer to employees, companies were
required only to footnote the grants and could ignore them
when reporting their income statements and balance
sheets. The Financial Accounting Standards Board now
requires companies to show option grants as an expense
on the income statement. To do this, the value of the
options is estimated at the time of the grant and then
expensed during the vesting period, which is the amount of
time the employee must wait before being allowed to exercise
the options. For example, if the initial value is $100 million and
the vesting period is 2 years, the company would report a
$50 million expense for each of the next 2 years. This approach
isn’t perfect, because the grant is not a cash expense; nor does
the approach take into account changes in the option’s value
after the initial grant. However, it does make the option grant
more visible to investors, which is a good thing.
resource
See Ch08 Tool Kit.xlsx
on the textbook’s Web
site.
348 Part 3 Stocks and Options
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

## Halaman PDF 386

```text
8-2b The Hedge Portfolio Approach
Suppose we created a portfolio by writing 1 call option and purchasing 1 share of stock.
As Figure 8-1 shows, if the stock price goes up then our portfolio’s stock will be worth
$50 but we will owe $15 on the option, so our portfolio’s net payoff is $35 $50 $15.
If the stock price goes down then our portfolio’s stock will be worth only $32, but the
amount we owe on the written option also will fall to zero, leaving the portfolio’s net
payoff at $32. The portfolio’s end-of-period price range is smaller than if we had just
owned the stock, so writing the call option reduces the portfolio’s price risk. Taking this
further: Is it possible for us to choose the number of shares held by our portfolio so that
it will have the same net payoff whether the stock goes up or down? If so, then our
portfolio is hedged and will have a riskless payoff when the option expires. Therefore, it
is called a hedge portfolio.
We are not really interested in investing in the hedge portfolio, but we want to use it
to help us determine the value of the option. The important point to recognize is that if
the hedge portfolio has a riskless net payoff when the option expires, then we can find the
present value of this payoff by discounting it at the risk-free rate. Our hedge portfolio’s
current value must equal this present value, which allows us to determine the option’s
value. The following example illustrates the steps in this approach.
1. FIND NS, THE NUMBER OF SHARES OF STOCK IN THE HEDGE PORTFOLIO
We want the portfolio’s payoff to be the same whether the stock goes up or down. If
we write 1 call option and buy Ns shares of stock, then the portfolio’s stock will be
worth Ns(P)(u) should the stock price go up, so its net payoff will be Ns(P)(u) − Cu.
FIGURE 8-1
Binomial Payoffs from Holding Western Cellular’s Stock or Call Option
Source: See the file Ch08 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Chapter 8 Financial Options and Applications in Corporate Finance 349
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

## Halaman PDF 387

```text
The portfolio’s stock will be worth Ns(P)(d) if the stock price goes down, so its net payoff
will be Ns(P)(d) − Cd. Setting these portfolio payoffs equal to one another (because we
want the portfolio to have the same ending value whether the stock goes up or down) and
then solving for Ns yields the number of shares of stock to buy for each call option in
order to create the hedge portfolio:
Ns
Cu Cd
P u P d
Cu Cd
P u d (8-2)
For Western, the hedge portfolio has 0.83333 share of stock:9
Ns
Cu Cd
P u P d
$15 $0
$50 $32 0 83333
2. FIND THE HEDGE PORTFOLIO’S PAYOFF
Our next step is to find the hedge portfolio’s payoff when the stock price goes up (you will
get the same result if instead you find the portfolio’s payoff when the stock goes down).
Recall that the hedge portfolio has Ns shares of stock and that we have written one call
option, so the call option’s payoff must be subtracted:
Hedge portfolio’s payoff if stock is up NsP u Cu
0 83333 $50 $15
$26 6665
Hedge portfolio’s payoff if stock is down NsP d Cd
0 83333 $32 $0
$26 6665
Figure 8-2 illustrates the payoffs of the hedge portfolio.
3. FIND THE PRESENT VALUE OF THE HEDGE PORTFOLIO’S PAYOFF
Because the hedge portfolio’s payoff is riskless, the current value of the hedge portfolio
must be equal to the present value of its riskless payoff. Suppose the nominal annual risk￾free rate, rRF, is 8%. What is the present value of the hedge portfolio’s riskless payoff of
$26.6665 in 6 months? Recall from Chapter 4 that the present value depends on how
frequently interest is compounded. Let’s assume that interest is compounded daily.10 We
can use a financial calculator to find the present value of the hedge portfolio’s payoff by
entering N 0 5 365 , because there are 365 days in a year and the contract expires in
half a year; I YR 8 365, because we want a daily interest rate; PMT 0; and
FV $26 6665, because we want to know the amount we would take today in exchange
for giving up the payoff when the option expires. Using these inputs, we solve for
PV $25.6210, which is the present value of the hedge portfolio’s payoff and which must
also be the current value of the components of the hedge portfolio.11
9
An easy way to remember this formula is to notice that Ns is equal to the range in possible option payoffs
divided by the range in possible stock prices.
10Option pricing models usually assume continuous compounding, which we discuss in Web Extension 4C
on the textbook’s Web site, but daily compounding works well. We will apply continuous compounding in
Sections 8-3 and 8-4.
11We could also solve for the present value using the present value equation with the daily periodic interest rate
and the number of daily periods: PV $26 6665 1 0 08 365 0 5 365 $25 6210.
resource
See Ch08 Tool Kit.xlsx
on the textbook’s Web
site.
350 Part 3 Stocks and Options
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

## Halaman PDF 388

```text
4. FIND THE OPTION’S VALUE
The current value of the hedge portfolio is the value of the stock, Ns(P), less the value of
the call option we wrote:
Current value of hedge portfolio Ns P VC
Because the payoff is riskless, the current value of the hedge portfolio must also equal the
present value of the riskless payoff:
Current value of hedge portfolio Present value of riskless payoff
Substituting for the current value of the hedge portfolio, we get:
Ns P VC Present value of riskless payoff
Solving for the call option’s value, we get:
VC Ns P Present value of riskless payoff
For Western’s option, this is:
VC 0 83333 $40 $25 621
$7 71
8-2c Hedge Portfolios and Replicating Portfolios
In our previous derivation of the call option’s value, we combined an investment in the stock
with writing a call option to create a risk-free investment. We can modify this approach and
create a portfolio that replicates the call option’s payoffs. For example, suppose we formed
FIGURE 8-2
Hedge Portfolio with Riskless Payoffs
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
193
194
195
196
197
198
A B CD E F
Strike price: X = $35.00
Current stock price: P = $40.00
Up factor for stock price: u = 1.25
Down factor for stock price: d = 0.80
Up option payoff: Cu = MAX[0,P(u)‐X] = $15.00
Down option payoff: Cd =MAX[0,P(d)‐
‐ ‐
X] = $0.00
Number of shares of stock in portfolio: Ns = (Cu Cd) / P(u d) = 0.83333
Stock price = P (u) = $50.00
P, Portfolio's stock payoff: = P(u)(Ns) = $41.67
current Subtract option's payoff: Cu = $15.00
stock price Portfolio's net payoff = P(u)Ns ‐ Cu = $26.67
$40
Stock price = P (d) = $32.00
Portfolio's stock payoff: = P(d)(Ns) = $26.67
Subtract option's payoff: Cd = $0.00
Portfolio's net payoff = P(d)Ns 199 ‐ Cd = $26.67
200
Source: See the file Ch08 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure's rounded values will be inexact.
Chapter 8 Financial Options and Applications in Corporate Finance 351
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

## Halaman PDF 389

```text
a portfolio by purchasing 0.83333 shares of Western’s stock and borrowing $25.621 at the
risk-free rate (this is equivalent to selling a T-bill short). In 6 months, we would repay the
future value of a $25.621, compounded daily at the risk-free rate. Using a financial calculator,
input N 0 5 365 , I YR 8 365, PV $25 621, and solve for FV $26 6665.12 If the
stock goes up, our net payoff would be 0 83333 $50 $26 6665 $15 00. If the stock goes
down, our net payoff would be 0 83333 $32 $26 6665 $0. The portfolio’s payoffs are
exactly equal to the option’s payoffs as shown in Figure 8-1, so our portfolio of 0.83333 shares
of stock and the $25.621 that we borrowed would exactly replicate the option’s payoffs.
Therefore, this is called a replicating portfolio. Our cost to create this portfolio is the cost of
the stock less the amount we borrowed:
Cost of replicating portfolio 0 83333 $40 $25 621 $7 71
If the call option did not sell for exactly $7.71, then a clever investor could make a sure
profit. For example, suppose the option sold for $8. The investor would write an option,
which would provide $8 of cash now but would obligate the investor to pay either $15 or
$0 in 6 months when the option expires. However, the investor could use the $8 to create
the replicating portfolio, leaving the investor with $8 $7 71 $0 29. In 6 months, the
replicating portfolio will pay either $15 or $0. Thus, the investor isn’t exposed to any risk—
the payoffs received from the replicating portfolio exactly offset the payoffs owed on the
option. The investor uses none of his own money, has no risk, has no net future obligations,
but has $0.29 in cash. This is arbitrage, and if such an arbitrage opportunity existed then
the investor would scale it up by writing thousands of options.13
Such arbitrage opportunities don’t persist for long in a reasonably efficient economy
because other investors will also see the opportunity and will try to do the same thing. With
so many investors trying to write (i.e., sell) the option, its price will fall; with so many
investors trying to purchase the stock, its price will increase. This will continue until the
option and replicating portfolio have identical prices. And because our financial markets are
really quite efficient, you would never observe the derivative security and the replicating
portfolio trading for different prices—they would always have the same price and there would
be no arbitrage opportunities. What this means is that, by finding the price of a portfolio that
replicates a derivative security, we have also found the price of the derivative security itself!
SELF-TEST
Describe how a risk-free hedge portfolio can be created using stocks and options.
How can such a portfolio be used to help estimate a call option’s value?
What is a replicating portfolio, and how is it used to find the value of a derivative security?
What is arbitrage?
Lett Incorporated’s stock price is now $50, but it is expected either to rise by a factor of 1.5 or
fall by a factor of 0.7 by the end of the year. There is a call option on Lett’s stock with a strike
price of $55 and an expiration date 1 year from now. What are the stock’s possible prices at the
end of the year? ($75 or $35) What is the call option’s payoff if the stock price goes up? ($20)
If the stock price goes down? ($0) If we sell 1 call option, how many shares of Lett’s stock must
we buy to create a riskless hedged portfolio consisting of the option position and the stock?
(0.5) What is the payoff of this portfolio? ($17.50) If the annual risk-free rate is 6%, then how
much is the riskless portfolio worth today (assuming daily compounding)? ($16.48) What is the
current value of the call option? ($8.52)
12Alternatively, use the present value equation with daily compounding: $25 621 1 0 08 365 365 0 5 1 $26 6665.
13If the option sold for less than the replicating portfolio, the investor would raise cash by shorting the portfolio
and use the cash to purchase the option, again resulting in arbitrage profits.
352 Part 3 Stocks and Options
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

## Halaman PDF 390

```text
8-3 The Single-Period Binomial Option
Pricing Formula14
The hedge portfolio approach works well if you only want to find the value of one type of
option with one period until expiration. But in all other situations, the step-by-step
approach becomes tedious very quickly. The following sections describe a formula that
replaces the step-by-step approach.
8-3a The Binomial Option Pricing Formula
With a little (or a lot!) of algebra, we can derive a single formula for a call option. Instead
of using daily compounding, we use continuous compounding to make the binomial
formula consistent with the Black-Scholes formula in Section 8-5.15 We also add a new
variable, n, which is the number of periods until expiration at time t. We only consider
1 period (i.e., n 1) in this example, but we consider multiple periods in Section 8-4.
Here is the resulting binomial option pricing formula:
VC
Cu
erRF t n d
u d Cd
u erRF t n
u d
erRF t n
(8-3)
After programming it into Excel, which we did for this chapter’s Tool Kit, it is easy to
change inputs and determine the new value of a call option.
We can apply this formula to Western’s call option:
VC
$15 e0 08 0 5 1 0 80
1 25 0 80 $0 1 25 e0 08 0 5 1
1 25 0 80
e0 08 0 5 1
$15 0 5351 $0 0 4649
1 04081 $7 71
Notice that this is the same value that resulted from the step-by-step process shown earlier.
The binomial option pricing formula in Equation 8-3 does not include the actual
probabilities that the stock will go up or down, nor does it include the expected stock
return, which is not what one might expect. After all, the higher the stock’s expected return,
the greater the chance that the call will be in-the-money at expiration. Note, however, that
the stock’s expected return is already indirectly incorporated into the stock price.
8-3b Primitive Securities and the Binomial Option
Pricing Formula
If we want to value other Western call options or puts that expire in 6 months, then we
can use Equation 8-3, but there is a time-saving approach. Notice that for options with the
same time left until expiration, Cu and Cd are the only variables that depend on the option
itself. The other variables depend only on the stock process (u and d), the risk-free rate,
14The material in this section is relatively technical, and some instructors may choose to skip it with no loss in
continuity.
15With daily compounding, the present value is equal to the future value divided by (1 + rRF/365)365(0.5/1). With
continuous compounding, the present value is e−rRF(t/n). See Web Extension 4C on the textbook’s Web site for more
discussion of continuous compounding.
Chapter 8 Financial Options and Applications in Corporate Finance 353
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

## Halaman PDF 391

```text
the time until expiration, and the number of periods until expiration. If we group these
variables together, we can then define πu and πd as:
πu
erRF t n d
u d
erRF t n
(8-4)
and
πd
u erRF t n
u d
erRF t n
(8-5)
By substituting these values into Equation 8-3, we obtain an option pricing model that
can be applied to all of Western’s 6-month options:
VC Cuπu Cdπd (8-6)
In this example, πu and πd are:
πu
e0 08 0 5 1 0 80
1 25 0 80
e0 08 0 5 1 0 5142
and
πd
1 25 e0 08 0 5 1
1 25 0 80
e0 08 0 5 1 0 4466
Using Equation 8-6, the value of Western’s 6-month call option with a strike price of
$35 is:
VC Cuπu Cdπd
$15 0 5142 $0 0 4466
$7 71
Sometimes πu and πd are called primitive securities because πu is the price of a simple
security that pays $1 if the stock goes up and nothing if it goes down; πd is the opposite.
This means that we can use πu and πd to find the price of any 6-month option on
Western. For example, suppose we want to find the value of a 6-month call option on
Western but with a strike price of $30. Rather than reinvent the wheel, all we have to do is
find the payoffs of this option and use the same values of πu and πd in Equation 8-6. If the
stock goes up to $50, the option will pay $50 − $30 $20; if the stock falls to $32, the
option will pay $32 − $30 $2. The value of the call option is:
Value of 6-month call with $30 strike price Cuπu Cdπd
$20 0 5141 $2 0 4466
$11 18
354 Part 3 Stocks and Options
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

## Halaman PDF 392

```text
It is a bit tedious initially to calculate πu and πd, but once you save them, it is easy to
find the value of any 6-month call or put option on the stock. In fact, you can use these π’s
to find the value of any security with payoffs that depend on Western’s 6-month stock
prices, which makes them a very powerful tool.
SELF-TEST
Yegi’s Fine Phones has a current stock price of $30. You need to find the value of a call option
with a strike price of $32 that expires in 3 months. Use the binomial model with one period until
expiration (i.e., n 1). The factor for an increase in stock price is u = 1.15; the factor for a
downward movement is d = 0.85. What are the possible stock prices at expiration? ($34.50 or
$25.50) What are the option’s possible payoffs at expiration? ($2.50 or $0) What are πu and
πd? (0.5422 and 0.4429) What is the current value of the option (assume each month is 1/12 of
a year)? ($1.36)
8-4 The Multi-Period Binomial Option
Pricing Model16
Clearly, the one-period example is simplified. Although you could duplicate buying 0.8333
share and writing one option by buying 8,333 shares and writing 10,000 options, the stock
price assumptions are unrealistic—Western’s stock price could be almost anything after
6 months, not just $50 or $32. However, if we allowed the stock to move up or down more
often, then a more realistic range of ending prices would result. In other words, dividing
the time until expiration into more periods would improve the realism of the resulting
prices at expiration. The key to implementing a multi-period binomial model is to keep
the stock return’s annual standard deviation the same no matter how many periods you
have during a year. In fact, analysts typically begin with an estimate of the annual
standard deviation and use it to determine u and d. The derivation is beyond the scope
of a financial management textbook, but the appropriate equations are:
u eσ t n (8-7)
d 1
u
(8-8)
where σ is the annualized standard deviation of the stock’s return, t is the time in years
until expiration, and n is the number of periods until expiration.
The standard deviation of Western’s stock returns is 0.315573, and application of
Equations 8-7 and 8-8 confirms the values of u and d that we used previously:
u e0 315573 0 5 1 1 25 and d 1
1 25
0 80
Now suppose we allow stock prices to change every 3 months (which is 0.25 years).
Using Equation 8-7 and 8-8, we estimate u and d to be:
u e0 31573 0 5 2 1 1709 and d 1
1 1709
0 8540
16The material in this section is relatively technical, and some instructors may choose to skip it with no loss in
continuity.
Chapter 8 Financial Options and Applications in Corporate Finance 355
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

## Halaman PDF 393

```text
At the end of the first 3 months, Western’s price would either rise to $40 1 1709 $46 84
or fall to $40 0 8540 $34 16. If the price rises in the first 3 months to $46.84, then it
would either go up to $46 84 1 1709 $54 84 or go down to $46 84 0 8540 $40 at
expiration. If instead the price initially falls to $40 0 8540 $34 16 during the first 3 months,
then it would either go up to $34 16 1 1709 $40 or go down to $34 16 0 8540 $29 17
by expiration. This pattern of stock price movements is called a binomial lattice and is shown in
Figure 8-3.
Because the interest rate and the volatility (as defined by u and d) are constant for
each period, we can calculate πu and πd for any period and apply these same values for
each period:17
πu
e0 08 0 5 2 0 80
1 25 0 80
e0 08 0 5 2 0 51400
πd
1 25 e0 08 0 5 2
1 25 0 80
e0 08 0 5 2 0 46620
These values are shown in Figure 8-3.
The lattice shows the possible stock prices at the option’s expiration and we know the
strike price, so we can calculate the option payoffs at expiration. Figure 8-3 also shows the
option payoffs at expiration. If we focus only on the upper right portion of the lattice
shown inside the dotted lines, then it is similar to the single-period problem we solved in
Section 8-3. In fact, we can use the binomial option pricing model from Equation 8-6 to
determine the value of the option in 3 months given that the stock price increased to
$46.84. As shown in Figure 8-3, the option will be worth $12.53 in 3 months if the
stock price goes up to $46.84. We can repeat this procedure on the lower right portion of
Figure 8-3 to determine the call option’s value in 3 months if the stock price falls to
$34.16; in this case, the call’s value would be $2.57. Finally, we can use Equation 8-6 and
the 3-month option values just calculated to determine the current price of the option,
which is $7.64. Thus, we are able to find the current option price by solving three simple
binomial problems.
If we broke the year into smaller periods and allowed the stock price to move up or
down more often, then the lattice would have an even more realistic range of possible
ending stock prices. Of course, estimating the current option price would require solving
lots of binomial problems within the lattice, but each problem is simple and computers
can solve them rapidly. With more outcomes, the resulting estimated option price is more
accurate. For example, if we divide the year into 15 periods then the estimated price is
$7.42. With 50 periods, the price is $7.39. With 100 periods it is still $7.39, which shows
that the solution converges to its final value within a relatively small number of steps. In
fact, as we break the time to expiration into smaller and smaller periods, the solution for
the binomial approach converges to the Black-Scholes solution, which is described in the
next section.
The binomial approach is widely used to value options with more complicated payoffs
than the call option in our example, such as employee stock options. This is beyond the
scope of a financial management textbook, but if you are interested in learning more
about the binomial approach, you should take a look at the textbooks by Don Chance and
John Hull cited in footnote 1.
17These values were calculated in Excel, so there may be small differences due to rounding in intermediate steps.
resource
See Ch08 Tool Kit.xlsx
on the textbook’s Web
site.
356 Part 3 Stocks and Options
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

## Halaman PDF 394

```text
SELF-TEST
Ringling Cycle’s stock price is now $20. You need to find the value of a call option with a strike
price of $22 that expires in 2 months. You want to use the binomial model with 2 periods (each
period is a month). Your assistant has calculated that u 1.1553, d 0.8656, πu 0.4838, and
πd 0.5095. Draw the binomial lattice for stock prices. What are the possible prices after
1 month? ($23.11 or $17.31) After 2 months? ($26.69, $20, or $14.99) What are the option’s
possible payoffs at expiration? ($4.69, $0, or $0) What will the option’s value be in 1 month if the
stock goes up? ($2.27) What will the option’s value be in 1 month if the stock price goes down?
($0) What is the current value of the option (assume each month is 1/12 of a year)? ($1.10)
8-5 The Black-Scholes Option Pricing Model (OPM)
The Black-Scholes option pricing model (OPM), developed in 1973, helped give rise to
the rapid growth in options trading. This model has been programmed into many
handheld and Web-based calculators, and it is widely used by option traders.
FIGURE 8-3
Two-Period Binomial Lattice and Option Valuation
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
A B CD E F G H I
Standard deviation of stock return: = 31.5573%
Current stock price: P = $40.00
Up factor for stock price: u = 1.1709
Down factor for stock price: d = 0.8540
Strike price: X = $35.00
Risk‐free rate: r RF = 8.00%
Years to expiration: t = 0.50
Number of periods until expiration: n = 2
Price of $1 payoff if stock goes up: u = 0.51400
Price of $1 payoff if stock goes down: d = 0.46620
Stock = P (u) (u) = $54.84
Cuu = Max[P(u)(u) X, 0]
Cuu = $19.84
Stock = P (u) = $46.84
Cu = Cuu u + Cud d
Cu = $12.53 Stock = P (u) (d) = P (d) (u)
P 00.04$= kcotS = $40.00
VC=Cu u+Cd d Cud = Cdu = Max[P(u)(d) X, 0]
VC = $7.64 Cud = $5.00
Stock = P (d) = $34.16
Cd = Cdu u + Cdd d
Cd = $2.57
Stock = P (d) (d) = $29.17
Cdd = Max[P(d)(d) X, 0]
Cdd = $0.00
N wo 3 m m shtno 6 onths
477
478
Source: See the file Ch08 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure's rounded values will be inexact.
Chapter 8 Financial Options and Applications in Corporate Finance 357
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

## Halaman PDF 395

```text
8-5a OPM Assumptions and Results
In deriving their model to value call options, Fischer Black and Myron Scholes made the
following assumptions.
1. The stock underlying the call option provides no dividends or other distributions
during the life of the option.
2. There are no transaction costs for buying or selling either the stock or the option.
3. The short-term, risk-free interest rate is known and is constant during the life of the option.
4. Any purchaser of a security may borrow any fraction of the purchase price at the
short-term, risk-free interest rate.
5. Short selling is permitted, and the short seller will receive immediately the full cash
proceeds of today’s price for a security sold short.
6. The call option can be exercised only on its expiration date.
7. Trading in all securities takes place continuously, and the stock price moves randomly.
The derivation of the Black-Scholes model rests on the same concepts as the binomial
model, except time is divided into such small increments that stock prices change continu￾ously. The Black-Scholes model for call options consists of the following three equations:
VC P N d1 −Xe−rRFt N d2 (8-9)
d1
ln P X rRF σ2 2 t
σ t
(8-10)
d2 d1 σ t (8-11)
The variables used in the Black-Scholes model are explained next.
VC Current value of the call option.
P Current price of the underlying stock.
N(di) Probability that a deviation less than di will occur in a standard
normal distribution. Thus, N(d1) and N(d2) represent areas under
a standard normal distribution function.
X Strike price of the option.
e ≈ 2.7183.
rRF Risk-free interest rate.18
t Time until the option expires (the option period).
In(P/X) Natural logarithm of P/X.
σ Standard deviation of the rate of return on the stock.
18The correct process to estimate the risk-free rate for use in the Black-Scholes model for an option with 6 months to
expiration is to find the annual nominal rate (compounded continuously) that has the same effective annual rate as a
6-month T-bill. For example, suppose a 6-month T-bill is yielding a 6-month periodic rate of 4.081%. The risk-free
rate to use in the Black-Scholes model is rRF 1n 1 0 0408 0 5 8%. Under continuous compounding, a
nominal rate of 8% produces an effective rate of yields e0 08 1 8 33%. This is the same effective rate yielded by
the T-bill: 1 0 0408 2 1 8 33%. The same approach can be applied for options with different expiration
periods. We will provide the appropriate risk-free rate for all problems and examples.
www
For a Web-based option
calculator, see
www.cboe.com/
LearnCenter/Option
Calculator.aspx.
www
Robert’s Online Option
Pricer can be accessed
at www.intrepid.com/
robertl/index.html. The
site provides a financial
service over the Internet
to small investors for
option pricing, giving
anyone a means to price
option trades without
having to buy expensive
software and hardware.
358 Part 3 Stocks and Options
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

## Halaman PDF 396

```text
The value of the option is a function of five variables: (1) P, the stock’s price; (2) t,
the option’s time to expiration; (3) X, the strike price; (4) σ, the standard deviation of
the underlying stock; and (5) rRF, the risk-free rate. We do not derive the Black-Scholes
model—the derivation involves some extremely complicated mathematics that go far
beyond the scope of this text. However, it is not difficult to use the model. Under the
assumptions set forth previously, if the option price is different from the one found by
Equation 8-9, then this would provide the opportunity for arbitrage profits, which
would force the option price back to the value indicated by the model. As we noted
earlier, the Black-Scholes model is widely used by traders because actual option prices
conform reasonably well to values derived from the model.
8-5b Application of the Black-Scholes Option
Pricing Model to a Call Option
The current stock price (P), the exercise price (X), and the time to maturity (t) can all be
obtained from a newspaper, such as The Wall Street Journal, or from the Internet, such as
the CBOE’s Web site. The risk-free rate (rRF) is the yield on a Treasury bill with a
maturity equal to the option expiration date. The annualized standard deviation of stock
returns (σ) can be estimated from daily stock prices. First, find the stock return for each
trading day for a sample period, such as each trading day of the past year. Second,
estimate the variance of the daily stock returns. Third, multiply this estimated daily
variance by the number of trading days in a year, which is approximately 250.19 Take
the square root of the annualized variance, and the result is an estimate of the annualized
standard deviation.
We will use the Black-Scholes model to estimate Western’s call option that we
discussed previously. Here are the inputs:
P $40
X $35
t 6 months 0 5 years
rRF 8 0% 0 080
σ 31 557% 0 31557
Given this information, we first estimate d1 and d2 from Equation 8-10 and 8-11:
d1
1n $40 $35 0 08 0 315572 2 0 5
0 31557 0 5
0 13353 0 064896
0 22314
0 8892
d2 d1 0 31557 0 5 0 6661
19If stocks traded every day of the year, then each return covers a 24-hour period; you would simply estimate the
variance of the 1-day returns with your sample of daily returns and then multiply this estimate by 365 for an estimate
of the annual variance. However, stocks don’t trade every day because of weekends and holidays. If you measure
returns from the close of one trading day until the close of the next trading day (called “trading-day returns”), then
some returns are for 1 day (such as Thursday close to Friday close) and some are for longer periods, like the 3-day
return from Friday close to Monday close. It might seem reasonable that the 3-day returns have 3 times the variance
of a 1-day return and should be treated differently when estimating the daily return variance, but that is not the case.
It turns out that the 3-day return over a weekend has only slightly higher variance than a 1-day return (perhaps
because of less new information on non-weekdays), and so it is reasonable to treat all of the trading-day returns the
same. With roughly 250 trading days in a year, most analysts take the estimate of the variance of daily returns and
multiply by 250 (or 252, depending on the year, to be more precise) to obtain an estimate of the annual variance.
resource
See Ch08 Tool Kit.xlsx
on the textbook’s Web
site for all calculations.
Chapter 8 Financial Options and Applications in Corporate Finance 359
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

## Halaman PDF 397

```text
Note that N(d1) and N(d2) represent areas under a standard normal distribution function.
The easiest way to calculate this value is with Excel. For example, we can use the function
NORMSDIST(0.8892), which returns a value of N(d1) N(0.8892) 0.8131. Simi￾larly, the NORMSDIST function returns a value of N d2 0 7473.20 We can use those
values to solve Equation 8-9:
VC $40 N 0 8892 $35e 0 08 0 5 N 0 6661
$7 39
Thus, the value of the option is $7.39. This is the same value we found using the binomial
approach with 100 periods in the year.
8-5c The Five Factors That Affect Call Option Prices
The Black-Scholes model has five inputs, so there are five factors that affect call option
prices. As we will see in the next section, these five inputs also affect put option prices.
Figure 8-4 shows how three of Western Cellular’s call options are affected by Western’s
stock price (all three options have a strike price of $35). The three options expire in 1 year,
in 6 months (0.5 years, like the option in our example), and in 3 months (or 0.25 years),
respectively.
Figure 8-4 offers several insights regarding option valuation. Notice that for all stock
prices in the Figure, the call option prices are always above the exercise value. If this were not
true, then an investor could purchase the call and immediately exercise it for a quick profit.21
Also, when the stock price falls far below the strike price, call option prices fall toward
zero. In other words, calls lose value as they become more and more out-of-the-money.
When the stock price greatly exceeds the strike price, call option prices fall toward the
exercise value. Thus, for very high stock prices, call options tend to move up and down by
about the same amount as does the stock price.
Call option prices increase if the stock price increases. This is because the strike price
is fixed, so an increase in stock price increases the chance that the option will be in-the￾money at expiration. Although we don’t show it in the figure, an increase in the strike
price would obviously cause a decrease in the call option’s value because higher strike
prices mean a lower chance of being in-the-money at expiration.
The 1-year call option always has a greater value than the 6-month call option, which
always has a greater value than the 3-month call option; thus, the longer a call option has
until expiration, the greater its value. Here is the intuition for that result. With a long time
until expiration, the stock price has a chance to increase well above the strike price by the
expiration date. Of course, with a long time until expiration, there is also a chance that the
stock price will fall far below the strike price by expiration. But there is a big difference in
payoffs for being well in-the-money versus far out-of-the-money. Every dollar that the
stock price is above the strike price means an extra dollar of payoff, but no matter how far
the stock price is below the strike price, the payoff is zero. When it comes to a call option,
the gain in value due to the chance of finishing well in-the-money with a big payoff more
than compensates for the loss in value due to the chance of being far out-of-the money.
20If you do not have access to Excel, then you can use the table in Appendix D. For example, the table shows that the
value for d1 0.88 is 0.5000 + 0.3106 0.8106 and that the value for d1 0.89 is 0.5000 + 0.3133 0.8133, so
N(0.8892) lies between 0.8106 and 0.8133. You could interpolate tofind a closer value, but we suggest using Excel instead.
21More precisely, this statement is true for all American call options (which can be exercised before expiration) and for
European call options written on stocks that pay no dividends. Although European options may not be exercised prior
to expiration, investors could earn a riskless profit if the call price were less than the exercise value by selling the stock
short, purchasing the call, and investing at the risk-free rate an amount equal to the present value of the strike price.
The vast majority of call options are American options, so the call price is almost always above the exercise value.
resource
See Ch08 Tool Kit.xlsx
on the textbook’s Web
site.
360 Part 3 Stocks and Options
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

## Halaman PDF 398

```text
How does volatility affect call options? Following are the Black-Scholes model prices
for Western’s call option with the original inputs except for different standard deviations.
The original standard deviation and option price are shown in bold:
Standard Deviation (σ) Call Option Price
0.00001 $ 6.37
0.10000 6.38
0.31557 7.39
0.40000 8.07
0.60000 9.87
0.90000 12.70
The first row shows the option price if there is very little stock volatility.22 Notice that
as volatility increases, so does the option price. Therefore, the riskier the underlying
FIGURE 8-4
Values of Western Cellular’s Call Options with a Strike Price of $35
0
0
5
5
10
10
15
15
20
20
25 30
25
30
$
35 40 45 50 55 60
Stock Price ($)
Exercise Value
VC if t = 1
VC if t = 0.5
VC if t = 0.25
22If a stock’s standard deviation is close to zero, then a stock is similar to a risk-free security and its price will
grow at the risk-free rate. Suppose the current price is P0 and it grows to a value of PT when it expires at time T.
If PT is greater than the exercise price, the payoff at time T will be PT – X. Because PT is almost risk-free (due to
the very low stock volatility) and X is known with certainty, the payoff should be discounted at the risk-free rate
to find the value of the call option. The stock price grew from P0 to PT at the risk-free rate, so the present value of
PT is P0. when discounted at the risk-free rate. Therefore, if stock volatility is very low and P0 is not too far below
the strike price, the value of the call option is approximately equal to the current stock price minus the present
value of the option. This means that the value of Western’s call option would be about $6.37 if the standard
deviation is very low (assuming daily compounding):
VC for σ 0 00001 ≈ $40 $35
1
0 08
365
365 0 5 $6 37
Observe that this is the same value given by the Black-Scholes model, even though we calculated it more directly.
This approach only works if the volatility is almost zero and the stock price is not too far below the strike price.
resource
See Ch08 Tool Kit.xlsx
for all calculations.
Chapter 8 Financial Options and Applications in Corporate Finance 361
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

## Halaman PDF 399

```text
security, the more valuable the option. To see why this makes sense, suppose you bought a
call option with a strike price equal to the current stock price. If the stock had no risk
(which means σ 0), then there would be a zero probability of the stock going up, hence
a zero probability of making money on the option. On the other hand, if you bought a call
option on a higher-volatility stock, there would be a higher probability that the stock
would increase well above the strike price by the expiration date. Of course, with higher
volatility there also would be a higher probability that the stock price would fall far below
the strike price. But as we previously explained, an increase in the price of the stock helps
call option holders more than a decrease hurts them: The greater the stock’s volatility, the
greater the value of the option. This makes options on risky stocks more valuable than
those on safer, low-risk stocks. For example, an option on Cisco should have a greater
value than an otherwise identical option on Kroger, the grocery store chain.
The risk-free rate also has a relatively small impact on option prices. Shown here are
the prices for Western’s call option with the original inputs except for the risk-free rate,
which is allowed to vary.
Risk-free rate (rRF) Call option price
0% $6.41
4 6.89
8 7.39
12 7.90
20 8.93
Taxes and Stock Options
If an employee stock option grant meets certain conditions, it is
called a “tax-qualifying grant” or sometimes an “Incentive Stock
Option”; otherwise, it is a “nonqualifying grant.” For example,
suppose you receive a grant of 1,000 options with an exercise
price of $50. If the stock price goes to $110 and you exercise the
options, you must pay $50(1,000) $50,000 for stock that is
worth $110,000, which is a sweet deal. But what is your tax
liability? If you receive a nonqualifying grant, then you are liable
for ordinary income taxes on 1,000($110 − $50) $60,000 when
you exercise the option. But if it is a tax-qualified grant, you
owe no regular taxes when exercised. By waiting at least a year
and then selling the stock for, say, $150, you would have a
long-term capital gain of 1,000($150 − $50) $100,000, which
would be taxed at the lower capital gains rate.
Before you gloat over your newfound wealth, you had better
consult your accountant. Your “profit” when you exercise the tax￾qualified options isn’t taxable under the regular tax code, but it is
under the Alternative Minimum Tax (AMT) code. With an AMT tax
rate of up to 28%, you might owe as much as 0.28($110 − $50)
(1,000) $16,800. Here’s where people get into trouble. The AMT
tax isn’t due until the following April, so you might think about
waiting until then to sell some stock to pay your AMT tax (so that
the sale will qualify as a long-term capital gain).
But what happens if the stock price falls to $5 by next
April? You can sell your stock, which raises only $5(1,000)
$5,000 in cash. Without going into the details, you will have
a long-term capital loss of 1,000($50 − $5) $45,000 but
IRS regulations limit your net capital loss in a single year to
$3,000. In other words, the cash from the sale and the tax
benefit from the capital loss aren’t nearly enough to cover
the AMT tax. You may be able to reduce your taxes in future
years because of the AMT tax you pay this year and the carry￾forward of the remaining long-term capital loss, but that
doesn’t help right now. You lost $45,000 of your original
$50,000 investment, you now have very little cash, and—adding
insult to injury—the IRS will insist that you also pay the $16,800
AMT tax.
This is exactly what happened to many people who
made paper fortunes in the dot-com boom only to see them
evaporate in the ensuing bust. They were left with worthless
stock but multimillion-dollar AMT tax obligations. In fact,
many still have IRS liens garnishing their wages until they
eventually pay their AMT tax. So if you receive stock options,
we congratulate you. But unless you want to be the next
poster child for poor financial planning, we advise you to
settle your AMT tax when you incur it.
resource
See Ch08 Tool Kit.xlsx
for all calculations.
362 Part 3 Stocks and Options
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

## Halaman PDF 400

```text
As the risk-free rate increases, the value of the option increases. The principal effect of an
increase in rRF is to reduce the present value of the exercise price, which increases the
current value of the option. Option prices in general are not very sensitive to interest rate
changes, at least not to changes within the ranges normally encountered.
Myron Scholes and Robert Merton (who also was a pioneer in the field of options)
were awarded the 1997 Nobel Prize in Economics, and Fischer Black would have been a
co-recipient had he still been living. Their work provided analytical tools and methodol￾ogies that are widely used to solve many types of financial problems, not just option
pricing. Indeed, the entire field of modern risk management is based primarily on their
contributions. Although the Black-Scholes model was derived for a European option that
can be exercised only on its maturity date, it also applies to American options that don’t
pay any dividends prior to expiration. The textbooks by Don Chance and John Hull (cited
in footnote 1) show adjusted models for dividend-paying stocks.
SELF-TEST
What is the purpose of the Black-Scholes option pricing model?
Explain what a “riskless hedge” is and how the riskless hedge concept is used in the Black￾Scholes OPM.
Describe the effect of a change in each of the following factors on the value of a call option:
(1) stock price, (2) exercise price, (3) option life, (4) risk-free rate, and (5) stock return standard
deviation (i.e., risk of stock).
Using an Excel worksheet, what is the value of a call option with these data: P $35,
X $25, rRF 6%, t 0 5 6 months , and 0 6? ($12.05)
8-6 The Valuation of Put Options
A put option gives its owner the right to sell a share of stock. Suppose a stock pays no
dividends and a put option written on the stock can be exercised only upon its expiration
date. What is the put’s value? Rather than reinventing the wheel, we can establish the
price of a put relative to the price of a call.
8-6a Put-Call Parity
Consider the payoffs for two portfolios at expiration date T, as shown in Table 8-2. The
first portfolio consists of a put option and a share of stock; the second has a call option
(with the same strike price and expiration date as the put option) and some cash. The
amount of cash is equal to the present value of the strike price discounted at the
continuously compounded risk-free rate, which is Xe−r
RFt
. At expiration, the value of this
cash will equal the strike price, X.
If PT, the stock price at expiration date T, is less than X, the strike price, when the
option expires, then the payoff of the put option at expiration is X − PT. Therefore, the
payoff of Portfolio 1, which contains the put and the stock, is equal to X minus PT plus PT,
or just X. For Portfolio 2, the payoff of the call is zero at expiration (because the call
option is out-of-the-money), and the value of the cash is X, for a total payoff of X. Notice
that both portfolios have the same payoffs if the stock price is less than the strike price.
What if the stock price is greater than the strike price at expiration? In this case, the
put is worth nothing, so the payoff of Portfolio 1 is equal to PT, the stock price at
expiration. The call option is worth PT − X, and the cash is worth X, so the payoff of
Portfolio 2 is PT. Hence the payoffs of the two portfolios are equal at expiration regardless
of whether the stock price is below or above the strike price.
Chapter 8 Financial Options and Applications in Corporate Finance 363
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

## Halaman PDF 401

```text
If the two portfolios have identical payoffs, then they must have identical values. This
is known as the put–call parity relationship:
Put option Stock Call option PV of exercise price
If VC is the Black-Scholes value of the call option, then the value of a put is: 23
Put option VC P Xe rRFt (8-12)
For example, consider a put option written on the stock discussed in the previous section.
If the put option has the same exercise price and expiration date as the call, then its price is:
Put option $7 39 $40 $35 e 0 08 0 5
$7 39 $40 $33 63 $1 02
It is also possible to modify the Black-Scholes call option formula to obtain a put
option formula:
Put option P N d1 1 Xe rRFt N d2 1 (8-13)
The only difference between this formula for puts and the formula for calls is the
subtraction of 1 from N(d1) and N(d2) in the call option formula.
8-6b The Five Factors That Affect Put Option Prices
Just like with call options, the exercise price, the underlying stock price, the time to
expiration, the stock’s standard deviation, and the risk-free rate affect the price of a put
option. Because a put pays off when the stock price declines below the exercise price, the
impact of the underlying stock price and exercise price and risk-free rate on the put are
opposite that of the call option. That is, put prices are higher when the stock price is lower
and when the exercise price is higher. Put prices are also lower when the risk-free rate is
higher, mostly because a higher risk-free rate reduces the present value of the exercise
price, which for a put is a payout to the option holder when the option is exercised.
TABLE 8-2
Portfolio Payoffs
Payoff at Expiration If:
PT < X PT ≥ X
Put X − PT 0
Stock PT PT
Portfolio 1: X PT
Call 0 PT − X
Cash X X
Portfolio 2: X PT
23This model cannot be applied to an American put option or to a European option on a stock that pays a
dividend prior to expiration. For an explanation of valuation approaches in these situations, see the books by
Chance and Hull cited in footnote 1.
364 Part 3 Stocks and Options
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

## Halaman PDF 402

```text
On the other hand, put options are affected by the stock’s standard deviation just like
call options. Both put and call option prices are higher when the stock’s standard
deviation is higher. This is true for put options because the higher the standard deviation,
the bigger the chance of a large stock price decline and a large put payoff. The effect of the
time to maturity on the put option price is indeterminate. A call option is more valuable
the longer the maturity, but some puts are more valuable the longer to maturity, and some
are less valuable. For example, consider an in-the-money put option (the stock price is
below the exercise price) on a stock with a low standard deviation. In this case a longer
maturity put option is less valuable than a shorter maturity put option because the longer
the time to maturity, the more likely the stock is to grow and erode the put’s payoff. But if
the stock’s standard deviation is high, then the longer maturity put option will be more
valuable because the likelihood of the stock declining even more and resulting in a high
payoff to the put is greater.
SELF-TEST
In words, what is put–call parity?
A put option written on the stock of Taylor Enterprises (TE) has an exercise price of $25
and 6 months remaining until expiration. The risk-free rate is 6%. A call option written on
TE has the same exercise price and expiration date as the put option. TE’s stock price is
$35. If the call option has a price of $12.05, then what is the price (i.e., value) of the put
option? ($1.31)
Explain why both put and call options are worth more if the stock return standard deviation is
higher, but put and call options are affected oppositely by the stock price.
8-7 Applications of Option Pricing in
Corporate Finance
Option pricing is used in four major areas of corporate finance: (1) real options analysis
for project evaluation and strategic decisions, (2) risk management, (3) capital structure
decisions, and (4) compensation plans.
8-7a Real Options
Suppose a company has a 1-year proprietary license to develop a software application
for use in a new generation of wireless cellular telephones. Hiring programmers and
marketing consultants to complete the project will cost $30 million. The good news is
that if consumers love the new cell phones, there will be a tremendous demand for the
software. The bad news is that if sales of the new cell phones are low, the software
project will be a disaster. Should the company spend the $30 million and develop the
software?
Because the company has a license, it has the option of waiting for a year, at which
time it might have a much better insight into market demand for the new cell phones. If
demand is high in a year, then the company can spend the $30 million and develop the
software. If demand is low, it can avoid losing the $30 million development cost by
simply letting the license expire. Notice that the license is analogous to a call option: It
gives the company the right to buy something (in this case, software for the new cell
phones) at a fixed price ($30 million) at any time during the next year. The license gives
the company a real option, because the underlying asset (the software) is a real asset
and not a financial asset.
Chapter 8 Financial Options and Applications in Corporate Finance 365
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

## Halaman PDF 403

```text
There are many other types of real options, including the option to increase capacity
at a plant, to expand into new geographical regions, to introduce new products, to switch
inputs (such as gas versus oil), to switch outputs (such as producing sedans versus SUVs),
and to abandon a project. Many companies now evaluate real options with techniques
that are similar to those described earlier in the chapter for pricing financial options.
8-7b Risk Management
Suppose a company plans to issue $400 million of bonds in 6 months to pay for a new
plant now under construction. The plant will be profitable if interest rates remain at
current levels, but if rates rise then it will be unprofitable. To hedge against rising rates,
the company could purchase a put option on Treasury bonds. If interest rates go up then
the company would “lose” because its bonds would carry a high interest rate, but it would
have an offsetting gain on its put options. Conversely, if rates fall then the company would
“win” when it issues its own low-rate bonds, but it would lose on the put options. By
purchasing puts, the company has hedged the risk due to possible interest rate changes
that it would otherwise face.
Another example of risk management is a firm that bids on a foreign contract. For
example, suppose a winning bid means that the firm will receive a payment of 12 million
euros in 9 months. At a current exchange rate of $1.57 per euro, the project would be
profitable. But if the exchange rate falls to $1.10 per euro, the project would be a loser.
To avoid exchange rate risk, the firm could take a short position in a forward contract that
allows it to convert 12 million euros into dollars at a fixed rate of $1.50 per euro in
9 months, which would still ensure a profitable project. This eliminates exchange rate risk
if the firm wins the contract, but what if the firm loses the contract? It would still be
obligated to sell 12 million euros at a price of $1.50 per euro, which could be a disaster.
For example, if the exchange rate rises to $1.75 per euro, then the firm would have to
spend $21 million to purchase 12 million euros at a price of $1.75/€ and then sell the
euros for $18 million ($1.50/€)(€12 million), a loss of $3 million.
To eliminate this risk, the firm could instead purchase a currency put option that
allows it to sell 12 million euros in 9 months at a fixed price of $1.50 per euro. If the
company wins the bid, it will exercise the put option and sell the 12 million euros for
$1.50 per euro if the exchange rate has declined. If the exchange rate hasn’t declined,
then it will sell the euros on the open market for more than $1.50 and let the option
expire. On the other hand, if the firm loses the bid, it has no reason to sell euros and
could let the option contract expire. Note, however, that even if the firm doesn’t win the
contract, it still is gambling on the exchange rate because it owns the put; if the price of
euros declines below $1.50, the firm will still make some money on the option. Thus, the
company can lock in the future exchange rate if it wins the bid and can avoid any net
payment at all if it loses the bid. The total cost in either scenario is equal to the initial
cost of the option. In other words, the cost of the option is like insurance that guarantees
the exchange rate if the company wins the bid and guarantees no net obligations if it
loses the bid.
Many other applications of risk management involve futures contracts and other
complex derivatives rather than calls and puts. However, the principles used in pricing
derivatives are similar to those used earlier in this chapter for pricing options. Thus,
financial options and their valuation techniques play key roles in risk management.
8-7c Capital Structure Decisions
Decisions regarding the mix of debt and equity used to finance operations are quite
important. One interesting aspect of the capital structure decision is based on option
366 Part 3 Stocks and Options
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

## Halaman PDF 404

```text
pricing. For example, consider a firm with debt requiring a final principal payment of
$60 million in 1 year. If the company’s value 1 year from now is $61 million, then it can
pay off the debt and have $1 million left for stockholders. If the firm’s value is less than
$60 million, then it may well file for bankruptcy and turn over its assets to creditors,
resulting in stockholders’ equity of zero. In other words, the value of the stockholders’
equity is analogous to a call option: The equity holders have the right to buy the assets for
$60 million (which is the face value of the debt) in 1 year (when the debt matures).
Suppose the firm’s owner-managers are considering two projects. One project has very
little risk, and it will result in an asset value of either $59 million or $61 million. The other
has high risk, and it will result in an asset value of either $20 million or $100 million.
Notice that the equity will be worth zero if the assets are worth less than $60 million, so
the stockholders will be no worse off if the assets end up at $20 million than if they end up
at $59 million. On the other hand, the stockholders would benefit much more if the
assets were worth $100 million rather than $61 million. Thus, the owner-managers have
an incentive to choose risky projects, which is consistent with an option’s value rising
with the risk of the underlying asset. Potential lenders recognize this situation, so they
build covenants into loan agreements that restrict managers from making excessively
risky investments.
Not only does option pricing theory help explain why managers might want to choose
risky projects (consider, for example, the cases of Enron, Lehman Brothers, and AIG) and
why debtholders might want restrictive covenants, but options also play a direct role in
capital structure choices. For example, a firm could choose to issue convertible debt,
which gives bondholders the option to convert their debt into stock if the value of the
company turns out to be higher than expected. In exchange for this option, bondholders
charge a lower interest rate than for nonconvertible debt. Because owner-managers must
share the wealth with convertible-bond holders, they have a smaller incentive to gamble
with high-risk projects.
8-7d Compensation Plans
Many companies use stock options as a part of their compensation plans. It is important
for boards of directors to understand the value of these options before they grant them to
employees. We discuss compensation issues associated with stock options in more detail
in Chapter 13.
SELF-TEST
Describe four ways that option pricing is used in corporate finance.
SUMMARY
In this chapter we discussed option pricing topics, which included the following:
• Financial options are instruments that (1) are created by exchanges rather than firms,
(2) are bought and sold primarily by investors, and (3) are of importance to both
investors and financial managers.
• The two primary types of financial options are (1) call options, which give the holder
the right to purchase a specified asset at a given price (the exercise, or strike, price) for
a given period of time, and (2) put options, which give the holder the right to sell an
asset at a given price for a given period of time.
Chapter 8 Financial Options and Applications in Corporate Finance 367
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

## Halaman PDF 405

```text
• A call option’s exercise value is defined as the maximum of zero or the current price of
the stock less the strike price.
• The Black-Scholes option pricing model (OPM) or the binomial model can be used to
estimate the value of a call option.
• The five inputs to the Black-Scholes model are (1) P, the current stock price; (2) X, the
strike price; (3) rRF, the risk-free interest rate; (4) t, the remaining time until expiration;
and (5) σ, the standard deviation of the stock’s rate of return.
• A call option’s value increases if P increases, X decreases, rRF increases, t increases, or σ
increases.
• The put–call parity relationship states that:
Put option Stock Call option PV of exercise price
QUESTIONS
(8-1) Define each of the following terms:
a. Option; call option; put option
b. Exercise value; strike price
c. Black-Scholes option pricing model
(8-2) Why do options sell at prices higher than their exercise values?
(8-3) Describe the effect on a call option’s price that results from an increase in each of the
following factors: (1) stock price, (2) strike price, (3) time to expiration, (4) risk-free rate,
and (5) standard deviation of stock return.
SELF-TEST PROBLEMS Solutions Shown in Appendix A
(ST-1) The current price of a stock is $40. In 1 year, the price will be either $60 or $30. The
annual risk-free rate is 5%. Find the price of a call option on the stock that has an exercise
price of $42 and that expires in 1 year. (Hint: Use daily compounding.)
(ST-2) Use the Black-Scholes Model to find the price for a call option with the following
inputs: (1) Current stock price is $22. (2) Strike price is $20. (3) Time to expiration
is 6 months. (4) Annualized risk-free rate is 5%. (5) Standard deviation of stock
return is 0.7.
PROBLEMS Answers Are in Appendix B
EASY PROBLEMS 1–2
A call option on the stock of Bedrock Boulders has a market price of $7. The stock sells for
$30 a share, and the option has a strike price of $25 a share. What is the exercise value of
the call option? What is the option’s time value?
The exercise price on one of Flanagan Company’s options is $15, its exercise value is
$22, and its time value is $5. What are the option’s market value and the price of the
stock?
Binomial Option
Pricing
Black-Scholes Model
(8-1)
Options
(8-2)
Options
368 Part 3 Stocks and Options
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

## Halaman PDF 406

```text
INTERMEDIATE PROBLEMS 3–4
Assume that you have been given the following information on Purcell Industries:
Current stock price $15 Strike price of option $15
Time to maturity of option 6 months Risk-free rate 6%
Variance of stock return 0.12
d1 0.24495 N(d1) 0.59675
d2 0.00000 N(d2) 0.50000
According to the Black-Scholes option pricing model, what is the option’s value?
The current price of a stock is $33, and the annual risk-free rate is 6%. A call option with a
strike price of $32 and with 1 year until expiration has a current value of $6.56. What is
the value of a put option written on the stock with the same exercise price and expiration
date as the call option?
CHALLENGING PROBLEMS 5–7
Use the Black-Scholes Model to find the price for a call option with the following
inputs: (1) Current stock price is $30. (2) Strike price is $35. (3) Time to expiration
is 4 months. (4) Annualized risk-free rate is 5%. (5) Variance of stock return
is 0.25.
The current price of a stock is $20. In 1 year, the price will be either $26 or $16. The
annual risk-free rate is 5%. Find the price of a call option on the stock that has a strike
price of $21 and that expires in 1 year. (Hint: Use daily compounding.)
The current price of a stock is $15. In 6 months, the price will be either $18 or $13.
The annual risk-free rate is 6%. Find the price of a call option on the stock that
has a strike price of $14 and that expires in 6 months. (Hint: Use daily
compounding.)
SPREADSHEET PROBLEM
(8-8) Start with the partial model in the file Ch08 P08 Build a Model.xls on the textbook’s
Web site. You have been given the following information for a call option on the
stock of Puckett Industries: P $65.00, X $70.00, t 0.50, rRF 5.00% and
σ 0.50.
a. Use the Black-Scholes option pricing model to determine the value of the call option.
b. Suppose there is a put option on Puckett’s stock with exactly the same inputs as the
call option. What is the value of the put?
MINI CASE
Assume that you have just been hired as a financial analyst by Triple Play, a mid-sized
California company that specializes in creating high-fashion clothing. Because no one at
Triple Play is familiar with the basics of financial options, you have been asked to
prepare a brief report that the firm’s executives can use to gain a cursory understanding
of the topic.
(8-3)
Black-Scholes Model
(8-4)
Put–Call Parity
(8-5)
Black-Scholes Model
(8-6)
Binomial Model
(8-7)
Binomial Model
Build a Model:
Black-Scholes Model
resource
Chapter 8 Financial Options and Applications in Corporate Finance 369
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

## Halaman PDF 407

```text
To begin, you gathered some outside materials on the subject and used these materials
to draft a list of pertinent questions that need to be answered. In fact, one possible
approach to the report is to use a question-and-answer format. Now that the questions
have been drafted, you have to develop the answers.
a. What is a financial option? What is the single most important characteristic of an
option?
b. Options have a unique set of terminology. Define the following terms:
(1) Call option
(2) Put option
(3) Strike price or exercise price
(4) Expiration date
(5) Exercise value
(6) Option price
(7) Time value
(8) Writing an option
(9) Covered option
(10) Naked option
(11) In-the-money call
(12) Out-of-the-money call
(13) LEAPS
c. Consider Triple Play’s call option with a $25 strike price. The following table contains
historical values for this option at different stock prices:
Stock Price Call Option Price
$25 $3.00
30 7.50
35 12.00
40 16.50
45 21.00
50 25.50
(1) Create a table that shows (a) stock price, (b) strike price, (c) exercise value, (d) option
price, and (e) the time value, which is the option’s price less its exercise value.
(2) What happens to the time value as the stock price rises? Why?
d. Consider a stock with a current price of P = $27. Suppose that over the next 6 months
the stock price will either go up by a factor of 1.41 or down by a factor of 0.71.
Consider a call option on the stock with a strike price of $25 that expires in 6 months.
The risk-free rate is 6%.
(1) Using the binomial model, what are the ending values of the stock price? What
are the payoffs of the call option?
(2) Suppose you write one call option and buy Ns shares of stock. How many shares
must you buy to create a portfolio with a riskless payoff (i.e., a hedge portfolio)?
What is the payoff of the portfolio?
(3) What is the present value of the hedge portfolio? What is the value of the call
option?
(4) What is a replicating portfolio? What is arbitrage?
370 Part 3 Stocks and Options
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

## Halaman PDF 408

```text
e. In 1973, Fischer Black and Myron Scholes developed the Black-Scholes option pricing
model (OPM).
(1) What assumptions underlie the OPM?
(2) Write out the three equations that constitute the model.
(3) According to the OPM, what is the value of a call option with the following
characteristics?
Stock price $27.00
Strike price $25.00
Time to expiration 6 month 0.5 years
Risk-free rate 6.0%
Stock return standard deviation 0.49
f. What impact does each of the following parameters have on the value of a call option?
(1) Current stock price
(2) Strike price
(3) Option’s term to maturity
(4) Risk-free rate
(5) Variability of the stock price
g. What is put–call parity?
Chapter 8 Financial Options and Applications in Corporate Finance 371
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

## Halaman PDF 409

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

## Halaman PDF 410

```text
PART 4
Projects and Their
Valuation
CHAPTER 9
The Cost of Capital 375
CHAPTER 10
The Basics of Capital Budgeting: Evaluating Cash Flows 413
CHAPTER 11
Cash Flow Estimation and Risk Analysis 453
© EpicStockMedia/Shutterstock.com
373
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

## Halaman PDF 411

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

