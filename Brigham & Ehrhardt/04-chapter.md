# Chapter 4: Time Value of Money

[Daftar isi](SUMMARY.md) · [Panduan belajar](KAJIAN.md)

Sumber: PDF halaman 176–229. Teks ekstraksi; simbol, tabel, dan rumus belum seluruhnya diverifikasi secara visual.

## Halaman PDF 176

```text
CHAPTER 4
Time Value of Money
When you graduate and go to work, your compensation package will almost certainly
include either a defined benefit (DB) or a defined contribution (DC) pension plan.
Under a DB plan, the company will put funds for you into its pension fund, which will
then invest in stocks, bonds, real estate, and so forth and then use those funds to
make the promised payments after you retire. Under a DC plan, the company will put
money into your 401(k) plan (which is essentially a mutual fund), you will decide what
type of assets to buy, and you will withdraw money after you retire. The analysis
required to set up a good retirement program is based on the subject of this chapter,
the time value of money (TVM).
How do you suppose a stock market crash like we had in 2008, with the average
stock down about 40%, will affect DB and DC retirement plans? If you have a 401(k)
plan that holds stocks, as most people do, TVM analysis would show clearly that you
will have to work longer than you expected, reduce your post-retirement standard of
living, or both.
With a DB plan, a stock market decline reduces the value of the investments set
aside for you by the company. If there is also a decline in interest rates, as there was
in 2008, TVM analysis shows that the amount of money the company should set aside
for you goes up. Thus, the company’s pension funding status, which is the difference
between the value of the pension plan’s investments and the amount the plan should
have on hand to cover the future obligations, becomes severely underfunded if the
market crashes and interest rates fall. This can even lead to bankruptcy, in which case
you might end up with retirement payments from the government instead of from the
company, with the government’s payments a lot lower than those promised by the
company’s plan. If you don’t believe us, ask someone who recently retired from a
bankrupt airline or auto company.
139
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

## Halaman PDF 177

```text
In Chapter 1, we saw that the primary objective of financial management is to maximize
the intrinsic value of a firm’s stock. We also saw that stock values depend on the timing of
the cash flows investors expect from an investment—a dollar expected sooner is worth
more than a dollar expected further in the future. Therefore, it is essential for financial
managers to understand the time value of money and its impact on stock prices. In this
chapter we will explain exactly how the timing of cash flows affects asset values and rates
of return.
The principles of time value analysis have many applications, including retirement
planning, loan payment schedules, and decisions to invest (or not) in new equipment. In
fact, of all the concepts used in finance, none is more important than the time value of
money (TVM), also called discounted cash flow (DCF) analysis. Time value concepts are
used throughout the remainder of the book, so it is vital that you understand the material
in this chapter and be able to work the chapter’s problems before you move on to
other topics.
4-1 Time Lines
The first step in a time value analysis is to set up a time line to help you visualize
what’s happening in the particular problem. To illustrate, consider the following
Corporate Valuation and the Time Value of Money
In Chapter 1 we explained: (1) that managers should
strive to make their firms more valuable, and (2) that
the value of a firm is determined by the size, timing,
and risk of its free cash flows (FCF). Recall from Chapter
2 that free cash flows are the cash flows available for
distribution to all of a firm’s investors (stockholders and
creditors). We explain how to calculate the weighted
average cost of capital (WACC) in Chapter 9, but it is
enough for now to think of the WACC as the average rate
of return required by all of the firm’s investors. The
intrinsic value of a company is given by the following
diagram. Note that central to this value is discounting
the free cash flows at the WACC in order to find the value
of the firm. This discounting is one aspect of the time
value of money. We discuss time value of money techni￾ques in this chapter.
Required investments in operating capital
Net operating profit aer taxes
–
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
140 Part 2 Fixed Income Securities
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

## Halaman PDF 178

```text
diagram, where PV represents $100 that is in a bank account today and FV is the
value that will be in the account at some future time (3 years from now in this
example):
Periods
Cash PV = $100 FV = ?
0 1 5% 2 3
The intervals from 0 to 1, 1 to 2, and 2 to 3 are time periods such as years or months.
Time 0 is today, and it is the beginning of Period 1; Time 1 is one period from today, and
it is both the end of Period 1 and the beginning of Period 2; and so on. In our example,
the periods are years, but they could also be quarters or months or even days. Note again
that each tick mark corresponds to both the end of one period and the beginning of the
next one. Thus, if the periods are years, the tick mark at Time 2 represents both the end of
Year 2 and the beginning of Year 3.
Cash flows are shown directly below the tick marks, and the relevant interest rate is
shown just above the time line. Unknown cash flows, which you are trying to find, are
indicated by question marks. Here the interest rate is 5%; a single cash outflow, $100, is
invested at Time 0; and the Time-3 value is unknown and must be found. In this
example, cash flows occur only at Times 0 and 3, with no flows at Times 1 or 2. We will,
of course, deal with situations where multiple cash flows occur. Note also that in our
example the interest rate is constant for all 3 years. The interest rate is generally held
constant, but if it varies, then in the diagram we show different rates for the different
periods.
Time lines are especially important when you are first learning time value
concepts, but even experts use them to analyze complex problems. Throughout the
book, our procedure is to set up a time line to show what’s happening, provide
an equation that must be solved to find the answer, and then explain how to solve
the equation with a regular calculator, a financial calculator, and a computer
spreadsheet.
SELF-TEST
Do time lines deal only with years, or could other periods be used?
Set up a time line to illustrate the following situation: You currently have $2,000 in a 3-year
certificate of deposit (CD) that pays a guaranteed 4% annually. You want to know the value of
the CD after 3 years.
4-2 Future Values
A dollar in hand today is worth more than a dollar to be received in the future—if
you had the dollar now, you could invest it, earn interest, and end up with more than
one dollar in the future. The process of going forward, from present values (PVs) to
future values (FVs), is called compounding. To illustrate, refer back to our 3-year
time line and assume that you have $100 in a bank account that pays a guaranteed
5% interest each year. How much would you have at the end of Year 3? We first
define some terms, and then we set up a time line and show how the future value is
calculated.
resource
The textbook’s Web site
contains an Excel file
that will guide you
through the chapter’s
calculations. The file for
this chapter is Ch04 Tool
Kit.xlsx, and we
encourage you to open
the file and follow along
as you read the chapter.
Chapter 4 Time Value of Money 141
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

## Halaman PDF 179

```text
PV Present value, or beginning amount. In our example, PV $100.
FVN Future value, or ending amount, in the account after N periods. Whereas
PV is the value now, or the present value, FVN is the value N periods into
the future, after interest earned has been added to the account.
CFt Cash flow. Cash flows can be positive or negative. For a borrower, the first
cash flow is positive and the subsequent cash flows are negative, and the reverse
holds for a lender. The cash flow for a particular period is often given a subscript,
CFt, where t is the period. Thus, CF0 PV the cash flow at Time 0,
whereas CF3 would be the cash flow at the end of Period 3. In this example the
cash flows occur at the ends of the periods, but in some problems they occur at
the beginning.
I Interest rate earned per year. (Sometimes a lowercase i is used.) Interest
earned is based on the balance at the beginning of each year, and we assume
that interest is paid at the end of the year. Here I 5% or, expressed as a
decimal, 0.05. Throughout this chapter, we designate the interest rate as I
(or I/YR, for interest rate per year) because that symbol is used on most
financial calculators. Note, though, that in later chapters we use the symbol
“r” to denote the rate because r (for rate of return) is used more often in the
finance literature. Also, in this chapter we generally assume that interest
payments are guaranteed by the U.S. government and hence are riskless (i.e.,
certain). In later chapters we will deal with risky investments, where the rate
actually earned might be different from its expected level.
INT Dollars of interest earned during the year (Beginning amount) × I. In
our example, INT $100 0 05 $5 for Year 1, but it rises in subsequent
years as the amount at the beginning of each year increases.
N Number of periods involved in the analysis. In our example, N 3.
Sometimes the number of periods is designated with a lowercase n, so both
N and n indicate number of periods.
We can use four different procedures to solve time value problems.1 These methods are
described next.
4-2a Step-by-Step Approach
The time line itself can be modified and used to find the FV of $100 compounded for
3 years at 5%, as shown below:
Time
Amount at beginning of period $100.00
0 1 2 5% 3
$105.00 $110.25 $115.76
1
A fifth procedure is called the tabular approach, which uses tables that provide “interest factors”; this procedure
was used before financial calculators and computers became available. Now, though, calculators and spreadsheets
such as Excel are programmed to calculate the specific factor needed for a given problem, which is then used to
find the FV. This is much more efficient than using the tables. Also, calculators and spreadsheets can handle
fractional periods and fractional interest rates. For these reasons, tables are not used in business today; hence we
do not discuss them in the text. However, because some professors cover the tables for pedagogical purposes, we
discuss them in Web Extension 4A, on the textbook’s Web site.
142 Part 2 Fixed Income Securities
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

## Halaman PDF 180

```text
We start with $100 in the account, which is shown at t 0. We then multiply the initial
amount, and each succeeding beginning-of-year amount, by 1 I 1 05 .
• You earn $100 0 05 $5 of interest during the first year, so the amount at the end of
Year 1 (or at t 1) is:
FV1 PV INT
PV PV I
PV 1 I
$100 1 0 05 $100 1 05 $105
• We begin the second year with $105, earn 0 05 $105 $5 25 on the now larger
beginning-of-period amount, and end the year with $110.25. Interest during Year 2 is
$5.25, and it is higher than the first year’s interest, $5, because we earned $5 0 05 $0 25
interest on the first year’s interest. This is called “compounding,” and interest earned on
interest is called “compound interest.”
• This process continues, and because the beginning balance is higher in each successive
year, the interest earned each year increases.
• The total interest earned, $15.76, is reflected in the final balance, $115.76.
The step-by-step approach is useful because it shows exactly what is happening.
However, this approach is time-consuming, especially if the number of years is large
and you are using a calculator rather than Excel, so streamlined procedures have been
developed.
4-2b Formula Approach
In the step-by-step approach, we multiplied the amount at the beginning of each period
by 1 I 1 05 . Notice that the value at the end of Year 2 is:
FV2 FV1 1 I
PV 1 I 1 I
PV 1 I 2
100 1 05 2 $110 25
If N 3, then we multiply PV by (1 + I) three different times, which is the same as
multiplying the beginning amount by 1 I 3
. This concept can be extended, and the
result is this key equation:
FVN PV 1 I N (4-1)
We can apply Equation 4-1 to find the FV in our example:
FV3 $100 1 05 3 $115 76
Equation 4-1 can be used with any calculator, even a nonfinancial calculator that has an
exponential function, making it easy to find FVs no matter how many years are
involved.
4-2c Financial Calculators
Financial calculators were designed specifically to solve time value problems. First, note
that financial calculators have five keys that correspond to the five variables in the basic
time value equations. Equation 4-1 has only four variables, but we will shortly deal with
Chapter 4 Time Value of Money 143
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

## Halaman PDF 181

```text
situations where a fifth variable (a set of periodic additional payments) is involved. We
show the inputs for our example above their keys in the following diagram, and the
output, which is the FV, below its key. Because there are no periodic payments in this
example, we enter 0 for PMT. We describe the keys in more detail below the diagram.
Inputs 3 5 –100 0
N I/YR PV PMT FV
Output 115.76
N Number of periods 3. Some calculators use n rather than N.
I YR Interest rate per period 5. Some calculators use i or I rather than
I/YR. Calculators are programmed to automatically convert the 5 to the
decimal 0.05 before doing the arithmetic.
PV Present value 100. In our example we begin by making a deposit, which
is an outflow of 100, so the PV is entered with a negative sign. On most
calculators you must enter the 100, then press the +/− key to switch from
+100 to −100. If you enter −100 directly, this will subtract 100 from the
last number in the calculator, which will give you an incorrect answer
unless the last number was zero.
PMT Payment. This key is used if we have a series of equal, or constant,
payments. Because there are no such payments in our current problem,
we enter PMT 0. We will use the PMT key later in this chapter.
FV Future value. In our example, the calculator automatically shows the FV as
a positive number because we entered the PV as a negative number. If we
had entered the 100 as a positive number, then the FV would have been
negative. Calculators automatically assume that either the PV or the FV
must be negative.
As noted in our example, you first enter the four known values (N, I/YR, PV, and PMT)
and then press the FV key to get the answer, FV 115 76.
4-2d Spreadsheets
Spreadsheets are ideally suited for solving many financial problems, including those
dealing with the time value of money.2 Spreadsheets are obviously useful for calculations,
but they can also be used like a word processor to create exhibits like our Figure 4-1,
which includes text, drawings, and calculations. We use this figure to show that four
methods can be used to find the FV of $100 after 3 years at an interest rate of 5%. The
time line on Rows 36 to 37 is useful for visualizing the problem, after which the
spreadsheet calculates the required answer. Note that the letters across the top designate
columns, the numbers down the left column designate rows, and the rows and columns
2
The file Ch04 Tool Kit.xlsx on the book’s Web site does the calculations in the chapter using Excel. We highly
recommend that you study the models in this Tool Kit. Doing so will give you practice with Excel, and that will
help you tremendously in later courses, in the job market, and in the workplace. Also, going through the models
will improve your understanding of financial concepts.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
144 Part 2 Fixed Income Securities
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

## Halaman PDF 182

```text
jointly designate cells. Thus, cell C32 shows the amount of the investment, $100, and it is
given a minus sign because it is an outflow.
It is useful to put all inputs in a section of the spreadsheet designated “INPUTS.” In Figure 4-1,
we put the inputs in the aqua-colored range of cells. Rather than enter fixed numbers into the
model’s formulas, we enter the cell references for the inputs. This makes it easy to modify the
problem by changing the inputs and then automatically use the new data in the calculations.
Time lines are important for solving finance problems because they help us visualize
what’s happening. When we work a problem by hand we usually draw a time line, and
when we work a problem with Excel, we set the model up as a time line. For example, in
Figure 4-1 Rows 36 to 37 are indeed a time line. It’s easy to construct time lines with Excel,
with each column designating a different period on the time line.
On Row 39, we use Excel to go through the step-by-step calculations, multiplying the
beginning-of-year values by (1 + I) to find the compounded value at the end of each
period. Cell G39 shows the final result of the step-by-step approach.
We illustrate the formula approach in Row 41, using Excel to solve Equation 4-1 to find
the FV. Cell G41 shows the formula result, $115.76. As it must, it equals the step-by-step result.
Rows 43 to 45 illustrate the financial calculator approach, which again produces the
same answer, $115.76.
Hints on Using Financial Calculators
When using a financial calculator, make sure it is set up as
indicated below. Refer to your calculator manual or to our
calculator tutorial on the textbook’s Web site for informa￾tion on setting up your calculator.
One payment per period. Many calculators “come out
of the box” assuming that 12 payments are made per
year; that is, they assume monthly payments. However,
in this book we generally deal with problems in which
only one payment is made each year. Therefore, you
should set your calculator at one payment per year
and leave it there. See our tutorial or your calculator
manual if you need assistance. We will show you how
to solve problems with more than 1 payment per year in
Section 4-15.
End mode. With most contracts, payments are made at
the end of each period. However, some contracts call for
payments at the beginning of each period. You can
switch between “End Mode” and “Begin Mode” depend￾ing on the problem you are solving. Because most of the
problems in this book call for end-of-period payments, you
should return your calculator to End Mode after you work
a problem in which payments are made at the beginning
of periods.
Negative sign for outflows. When first learning how to
use financial calculators, students often forget that one
cash flow must be negative. Mathematically, financial
calculators solve a version of this equation:
PV 1 I N FVN 0 (4-2)
Notice that for reasonable values of I, either PV or FVN must be
negative, and the other one must be positive to make the equation
equal 0. This is reasonable because, in all realistic situations, one
cash flow is an outflow (which should have a negative sign) and
one is an inflow (which should have a positive sign). For example, if
you make a deposit (which is an outflow, and hence should have a
negative sign), then you will expect to make a later withdrawal
(which is an inflow with a positive sign). The bottom line is that one
of your inputs for a cash flow must be negative and one must be
positive. This generally means typing the outflow as a positive
number and then pressing the +/− key to convert from + to − before
hitting the enter key.
Decimal places. When doing arithmetic, calculators
allow you to show from 0 to 11 decimal places on the
display. When working with dollars, we generally specify
two decimal places. When dealing with interest rates, we
generally specify two places if the rate is expressed as a
percentage, like 5.25%, but we specify four places if the
rate is expressed as a decimal, like 0.0525.
Interest rates. For arithmetic operations with a nonfinancial
calculator, the rate 5.25% must be stated as a decimal, .0525.
However, with a financial calculator you must enter 5.25, not
.0525, because financial calculators are programmed to
assume that rates are stated as percentages.
Chapter 4 Time Value of Money 145
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

## Halaman PDF 183

```text
The last section, in Rows 47 to 49, illustrates Excel’s future value (FV) function.
You can access the function wizard by clicking the f
x symbol in Excel’s formula bar.
Then select the category for Financial functions, and then the FV function, which
is =FV(I,N,0,PV), as shown in Cell E47.3 Cell E48 shows how the formula would
look with numbers as inputs; the actual function itself is entered in Cell G48, but it
shows up in the table as the answer, $115.76. If you access the model and put the
pointer on Cell G48, you will see the full formula. Finally, Cell E49 shows how the
formula would look with cell references rather than fixed values as inputs, with the
actual function again in Cell G49. We generally use cell references as function inputs
because this makes it easy to change inputs and see how those changes affect the
output. This is called “sensitivity analysis.” Many real-world financial applications use
sensitivity analysis, so it is useful to form the habit of setting up an input data section
and then using cell references rather than fixed numbers in the functions.
When entering interest rates in Excel, you can use either actual numbers or percen￾tages, depending on how the cell is formatted. For example, we first formatted Cell C33 to
FIGURE 4-1
Alternative Procedures for Calculating Future Values
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
3
All functions begin with an equal sign. The third entry is zero in this example, which indicates that there are no
periodic payments. Later in this chapter we will use the FV function in situations where we have nonzero periodic
payments. Also, for inputs we use our own notation, which is similar but not identical to Excel’s notation.
146 Part 2 Fixed Income Securities
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

## Halaman PDF 184

```text
Percentage, and then typed in 5, which showed up as 5%. However, Excel uses 0.05 for the
arithmetic. Alternatively, we could have formatted C33 as a Number, in which case we
would have typed “0.05.” If a cell is formatted to Number and you enter 5, then Excel
would think you meant 500%. Thus, Excel’s procedure is different from the convention
used in financial calculators.
Sometimes students are confused about the sign of the initial $100. We used +$100 in
Rows 39 and 41 as the initial investment when calculating the future value using the step￾by-step method and the future value formula, but we used −$100 with a financial
calculator and the spreadsheet function in Rows 43 and 48. When must you use a positive
value and when must you use a negative value? The answer is that whenever you set up a
time line and use either a financial calculator’s time value functions or Excel’s time value
functions, you must enter the signs that correspond to the “direction” of the cash flows.
Cash flows that go out of your pocket (outflows) are negative, but cash flows that come
into your pocket (inflows) are positive. In the case of the FV function in our example, if
you invest $100 (an outflow, and therefore negative) at Time 0, then the bank will make
available to you $115.76 (an inflow, and therefore positive) at Time 3. In essence, the FV
function on a financial calculator or Excel answers the question “If I invest this much now,
how much will be available to me at a time in the future?” The investment is an outflow
and negative, and the amount available to you is an inflow and positive. If you use
algebraic formulas, then you must keep track of whether the value is an outflow or an
inflow yourself. When in doubt, refer back to a correctly constructed time line.
4-2e Comparing the Procedures
The first step in solving any time value problem is to understand what is happening and
then to diagram it on a time line. Woody Allen said that 90% of success is just showing
up. With time value problems, 90% of success is correctly setting up the time line.
After you diagram the problem on a time line, your next step is to pick one of the four
approaches shown in Figure 4-1 to solve the problem. Any one approach may be used, but
your choice will depend on the particular situation.
All business students should know Equation 4-1 by heart and should also know how
to use a financial calculator. So, for simple problems such as finding the future value of a
single payment, it is generally easiest and quickest to use either the formula approach or a
financial calculator. However, for problems that involve several cash flows, the formula
approach usually is time-consuming, so either the calculator or spreadsheet approach
would generally be used. Calculators are portable and quick to set up, but if many
calculations of the same type must be done, or if you want to see how changes in an
input such as the interest rate affect the future value, then the spreadsheet approach is
generally more efficient. If the problem has many irregular cash flows, or if you want to
analyze alternative scenarios using different cash flows or interest rates, then the spread￾sheet approach definitely is the most efficient procedure.
Spreadsheets have two additional advantages over calculators. First, it is easier to
check the inputs with a spreadsheet because they are visible; with a calculator the inputs
are buried somewhere in the machine. Thus, you are less likely to make a mistake in a
complex problem when you use the spreadsheet approach. Second, with a spreadsheet,
you can make your analysis much more transparent than you can when using a calculator.
This is not necessarily important when all you want is the answer, but if you need to
present your calculations to others, like your boss, it helps to be able to show intermediate
steps, which enables someone to go through your exhibit and see exactly what you did.
Transparency is also important when you must go back, sometime later, and reconstruct
what you did.
Chapter 4 Time Value of Money 147
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

## Halaman PDF 185

```text
You should understand the various approaches well enough to make a rational
choice, given the nature of the problem and the equipment you have available. In any
event, you must understand the concepts behind the calculations, and you also must
know how to set up time lines in order to work complex problems. This is true for stock
and bond valuation, capital budgeting, lease analysis, and many other types of financial
problems.
4-2f Graphic View of the Compounding Process
Figure 4-2 shows how a $100 investment grows (or declines) over time at different interest
rates. Interest rates are normally positive, but the “growth” concept is broad enough to
include negative rates. We developed the curves by solving Equation 4-1 with different
values for N and I. The interest rate is a growth rate: If money is deposited and earns 5%
per year, then your funds will grow by 5% per year. Note also that time value concepts can
be applied to anything that grows—sales, population, earnings per share, or your future
salary. Also, as noted before, the “growth rate” can be negative, as was sales growth for a
number of auto companies in recent years.
4-2g Simple Interest versus Compound Interest
As explained earlier, when interest is earned on the interest earned in prior periods, we
call it compound interest. If interest is earned only on the principal, we call it simple
interest. The total interest earned with simple interest is equal to the principal multi￾plied by the interest rate times the number of periods: PV(I)(N). The future value is
equal to the principal plus the interest: FV PV PV I N . For example, suppose you
FIGURE 4-2
Growth of $100 at Various Interest Rates and Time Periods
$0
$100
$200
$300
$400
$500
$600
1 2 3 4 5 6 7 8 9 10
Years
I = 20%
I = 0%
I = –20%
I = 5%
I = 10%
FV of $100
Aer N Years
resource
See Ch04 Tool Kit.xlsx
for all calculations.
148 Part 2 Fixed Income Securities
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

## Halaman PDF 186

```text
deposit $100 for 3 years and earn simple interest at an annual rate of 5%. Your balance
at the end of 3 years would be:
FV PV PV I N
$100 $100 5% 3
$100 $15 $115
Notice that this is less than the $115.76 we calculated earlier using compound interest.
Most applications in finance are based on compound interest, but you should be aware
that simple interest is still specified in some legal documents.
SELF-TEST
Explain why this statement is true: “A dollar in hand today is worth more than a dollar to be
received next year, assuming interest rates are positive.”
What is compounding? What would the future value of $100 be after 5 years at 10% compound
interest? ($161.05)
Suppose you currently have $2,000 and plan to purchase a 3-year certificate of deposit (CD)
that pays 4% interest, compounded annually. How much will you have when the CD matures?
($2,249.73) How would your answer change if the interest rate were 5%, or 6%, or 20%? (Hint:
With a calculator, enter N 3, I YR 4, PV 2000, and PMT 0; then press FV to get
2,249.73. Then, enter I YR 5 to override the 4% and press FV again to get the second answer.
In general, you can change one input at a time to see how the output changes.) ($2,315.25;
$2,382.03; $3,456.00)
A company’s sales in 2012 were $100 million. If sales grow by 8% annually, what will they be 10
years later? ($215.89 million) What would they be if they decline by 8% per year for 10 years?
($43.44 million)
How much would $1, growing at 5% per year, be worth after 100 years? ($131.50) What would
FV be if the growth rate were 10%? ($13,780.61)
4-3 Present Values
Suppose you have some extra money and want to make an investment. A broker offers to
sell you a bond that will pay a guaranteed $115.76 in 3 years. Banks are currently offering
a guaranteed 5% interest on 3-year certificates of deposit (CDs), and if you don’t buy the
bond you will buy a CD. The 5% rate paid on the CD is defined as your opportunity cost,
or the rate of return you would earn on an alternative investment of similar risk if you
don’t invest in the security under consideration. Given these conditions, what’s the most
you should pay for the bond?
4-3a Discounting a Future Value to Find the
Present Value
First, recall from the future value example in the last section that if you invested $100
at 5% in a CD, it would grow to $115.76 in 3 years. You would also have $115.76
after 3 years if you bought the bond. Therefore, the most you should pay for the bond
is $100—this is its “fair price,” which is also its intrinsic, or fundamental, value. If
you could buy the bond for less than $100, then you should buy it rather than invest
in the CD. Conversely, if its price were more than $100, you should buy the CD. If
the bond’s price were exactly $100, you should be indifferent between the bond and
the CD.
Chapter 4 Time Value of Money 149
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

## Halaman PDF 187

```text
The $100 is defined as the present value, or PV, of $115.76 due in 3 years when the
appropriate interest rate is 5%. In general, the present value of a cash flow due N years in
the future is the amount that, if it were on hand today, would grow to equal the given
future amount. Because $100 would grow to $115.76 in 3 years at a 5% interest rate, $100
is the present value of $115.76 due in 3 years at a 5% rate.
Finding present values is called discounting, and as previously noted, it is the reverse of
compounding: If you know the PV, you can compound it to find the FV; or if you know the FV,
you can discount it to find the PV. Indeed, we simply solve Equation 4-1, the formula for the
future value, for the PV to produce the present value equation as follows:
Compounding to find future values : Future value FVN PV 1 I N (4-1)
Discounting to find present values : Present value PV
FVN
1 I N (4-3)
The top section of Figure 4-3 shows inputs and a time line for finding the present
value of $115.76 discounted back for 3 years. We first calculate the PV using the step-by￾step approach. When we found the FV in the previous section, we worked from left to
right, multiplying the initial amount and each subsequent amount by (1 + I). To find
present values, we work backwards, or from right to left, dividing the future value and
each subsequent amount by (1 + I), with the present value of $100 shown in Cell D105.
The step-by-step procedure shows exactly what’s happening, and that can be quite useful
It’s a Matter of Trust
One of our Founding Fathers, Benjamin Franklin, wanted to
make a donation to the cities of Boston and Philadelphia,
but he didn’t want the cities to squander the money before
it had grown enough to make a big impact. His solution was
the “Methuselah Trust.” When Franklin died in 1790, his will
left £1,000, at that time about $4,550, to Philadelphia and to
Boston, but on the condition that it would be invested for
100 years, after which some of the proceeds were to be used
for the public projects (primarily trade schools and water
works) and the rest invested for another 100 years. Depending
on interest rates, this strategy could generate quite a bit of
money! For example, if half of his bequest, $2,275, remained
invested at 5% compound interest for the entire 200 years, the
value in 1990 would be $39.3 million! The ultimate payout,
however, was only about $7 million, because substantial
amounts were eaten up by trustee fees, taxes, and legal
battles. Franklin certainly would have been disappointed!
In 1936 an eccentric investor and New York lawyer,
Jonathan Holden, decided to expand on Franklin’s idea by
donating a series of 500-year and 1,000-year trusts to Hartwick
College and several other recipients. By 2008 Hartwick College’s
trust had grown in value to about $9 million; if invested at 5% for
the remaining 928 years of its planned life, its value would grow
to $9 million 1 05 928 $4 15 1026. That is a lot of dollars
by any measure! For example, that amount in million-dollar bills
(if they existed by then) would paper the earth 10,000 times over,
or laid end to end would reach the nearest star, Alpha Centauri,
more than 1,000 times. In a move that surely would have dis￾appointed Holden, Hartwick College was able to convert the
trust into annual cash flows of about $450,000 a year.
The trusts of Franklin and Holden didn’t turn out exactly
as they had planned—Franklin’s trust didn’t grow adequately,
and Holden’s trust was converted into annual cash flows. This
goes to show that you can’t always trust a trust!
Sources: Jake Palmateer, “On the Bright Side: Hartwick College Receives $9 million
Trust,” The Daily Star, Oneonta, NY, January 22, 2008, http://thedailystar.com/
local/x112892349/On-The-Bright-Side-Hartwick-College-receives-9M-trust/
print; Lewis H. Lapham, “Trust Issues,” Lapham’s Quarterly, Friday, December 2,
2011, www.laphamsquarterly.org/essays/trust-issues.php?page=1.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
150 Part 2 Fixed Income Securities
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

## Halaman PDF 188

```text
when you are working complex problems or trying to explain a model to others. However,
it’s inefficient, especially if you are dealing with more than a year or two.
A more efficient procedure is to use the formula approach in Equation 4-3, simply dividing
the future value by 1 I N. This gives the same result, as we see in Figure 4-3, Cell G107.
Equation 4-2 is actually programmed into financial calculators. As shown in Figure 4-3,
Rows 109 to 111, we can find the PV by entering values for N 3, I YR 5, PMT 0,
and FV 115 76, and then pressing the PV key to get −100.
Excel also has a function that solves Equation 4-3—this is the PV function, and it is
written as =PV(I,N,0,FV).
4 Cell E126 shows the inputs to this function. Next, Cell E114
shows the Excel function with fixed numbers as inputs, with the actual function and the
resulting −$100 in Cell G114. Cell E115 shows the Excel function using cell references,
with the actual function and the resulting −$100 in Cell G115.
As with the future value calculation, students often wonder why the result of the present
value calculation is sometimes positive and sometimes negative. In the algebraic calculations in
Rows 105 and 107 the result is +$100, while the result of the calculation using a financial
calculator or Excel’s function in Rows 111 and 114 is –$100. Again, the answer is in the signs of a
correctly constructed time line. Outflows are negative and inflows are positive. The PV function
for Excel and a financial calculator answer the question “How much must I invest today in order
FIGURE 4-3
Alternative Procedures for Calculating Present Values
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
A B C D E FG
INPUT S:
Future payment = CFN = FV = $115.76
Interest rate = I = 5.00%
No. of periods = N = 3
T ime eniL sdoireP : 0 1 23
Cash PV = ? 0 0 $115.76
1. Step‐by‐S :pet 00.001$ $105.00 $110.25 $115.76
2. Formula: PV = FVN/(1+I)N PV = $115.76/(1.05) 3 = $100.00
3:stupnI 5 0 115.76
3. Financial Calculator: N I/YR PV PMT FV
Output: $100.00
4. Spreadsheet: PV function: PV = =PV(I,N,0,FV)
Fixed inputs: PV = =PV(0.05,3,0,115.76) = $100.00
Cell references: PV = =PV(C99,C100,0,C98) = $100.00
In the formula, the terms are entered in this sequence: interest, periods, 0 to indicate no periodic
cash and then the FV. T he data can be entered as numbers or, better yet, as cell references.
116
117
flow:
flows, fixed
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
4
The third entry in the PV function is zero to indicate that there are no intermediate payments in this example.
Chapter 4 Time Value of Money 151
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

## Halaman PDF 189

```text
to have available to me a certain amount of money in the future?” If you want to have $115.76
available in 3 years (an inflow to you, and therefore positive), then you must invest $100 today
(an outflow, and therefore negative). If you use the algebraic functions as in Rows 105 and 107,
you must keep track of whether the results of your calculations are inflows or outflows.
The fundamental goal of financial management is to maximize the firm’s intrinsic
value, and the intrinsic value of a business (or any asset, including stocks and bonds) is
the present value of its expected future cash flows. Because present value lies at the heart
of the valuation process, we will have much more to say about it in the remainder of this
chapter and throughout the book.
4-3b Graphic View of the Discounting Process
Figure 4-4 shows that the present value of a sum to be received in the future decreases and
approaches zero as the payment date is extended further and further into the future; it
also shows that, the higher the interest rate, the faster the present value falls. At relatively
high rates, funds due in the future are worth very little today, and even at relatively low
rates present values of sums due in the very distant future are quite small. For example, at
a 20% discount rate, $100 due in 40 years would be worth less than 7 cents today.
(However, 1 cent would grow to almost $1 million in 100 years at 20%.)
SELF-TEST
What is “discounting,” and how is it related to compounding? How is the future value equation
(4-1) related to the present value equation (4-3)?
How does the present value of a future payment change as the time to receipt is lengthened?
As the interest rate increases?
Suppose a risk-free bond promises to pay $2,249.73 in 3 years. If the going risk-free interest
rate is 4%, how much is the bond worth today? ($2,000) How much is the bond worth if it
matures in 5 rather than 3 years? ($1,849.11) If the risk-free interest rate is 6% rather than 4%,
how much is the 5-year bond worth today? ($1,681.13)
How much would $1 million due in 100 years be worth today if the discount rate were 5%?
($7,604.49) What if the discount rate were 20%? ($0.0121)
FIGURE 4-4
Present Value of $100 at Various Interest Rates and Time Periods
$0
$20
$40
$60
$80
$100
0 10 20 30 40
Years
Present Value
of $100
I = 0%
I = 20%
I = 10%
I = 5%
resource
See Ch04 Tool Kit.xlsx
for all calculations.
152 Part 2 Fixed Income Securities
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

## Halaman PDF 190

```text
4-4 Finding the Interest Rate, I
We have used Equations 4-1, 4-2, and 4-3 to find future and present values. Those
equations have four variables, and if we know three of them, then we (or our calculator
or Excel) can solve for the fourth. Thus, if we know PV, I, and N, we can solve Equation 4-1
for FV, or if we know FV, I, and N, we can solve Equation 4-3 to find PV. That’s what we
did in the preceding two sections.
Now suppose we know PV, FV, and N, and we want to find I. For example, suppose we
know that a given security has a cost of $100 and that it will return $150 after 10 years. Thus,
we know PV, FV, and N, and we want to find the rate of return we will earn if we buy the
security. Here’s the solution using Equation 4-1 (with FV on the right side of the formula):
PV 1 I N FV
$100 1 I 10 $150
1 I 10 $150 $100
1 I 10 1 5
1 I 1 5 1 10
1 I 1 0414
I 0 0414 4 14%
Finding the interest rate by solving the formula takes a little time and thought, but
financial calculators and spreadsheets find the answer almost instantly. Here’s the calcu￾lator setup:
Inputs 10
4.14
–100 0 150
N I/YR PV PMT FV
Output
Enter N 10, PV 100, PMT 0 (because there are no payments until the security
matures), and FV 150. Then, when you press the I/YR key, the calculator gives the
answer, 4.14%. Notice that the PV is a negative value because it is a cash outflow (an
investment) and the FV is positive because it is a cash inflow (a return of the investment).
If you enter both PV and FV as positive numbers (or both as negative numbers), you will
get an error message rather than the answer.
In Excel, the RATE function can be used to find the interest rate: =RATE(N,PMT,PV,FV).
For this example, the interest rate is found as =RATE(10,0,−100,150) = 0.0414 = 4.14%. See
the file Ch04 Tool Kit.xlsx on the textbook’s Web site for an example.
SELF-TEST
Suppose you can buy a U.S. Treasury bond that makes no payments until the bond matures
10 years from now, at which time it will pay you $1,000.5 What interest rate would you earn if
you bought this bond for $585.43? (5.5%) What rate would you earn if you could buy the bond
for $550? (6.16%) For $600? (5.24%)
Microsoft earned $0.33 per share in 1997. Fourteen years later, in 2011, it earned $2.75. What
was the growth rate in Microsoft’s earnings per share (EPS) over the 14-year period? (16.35%)
If EPS in 2011 had been $2.00 rather than $2.75, what would the growth rate have been?
(13.73%)
5
This is a STRIP bond, which we explain in Chapter 5.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
Chapter 4 Time Value of Money 153
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

## Halaman PDF 191

```text
4-5 Finding the Number of Years, N
We sometimes need to know how long it will take to accumulate a specific sum of money,
given our beginning funds and the rate we will earn. For example, suppose we now have
$500,000 and the interest rate is 4.5%. How long will it be before we have $1 million?
Here’s Equation 4-1, showing all the known variables:
$1,000,000 $500,000 1 0 045 N (4-1)
We need to solve for N, and we can use three procedures: a financial calculator, Excel (or
some other spreadsheet), or by working with natural logs. As you might expect, the
calculator and spreadsheet approaches are easier.6 Here’s the calculator setup:
Inputs 4.5
15.7473
–500000 0 1000000
N I/YR PV PMT FV
Output
Enter I YR 4 5, PV 500000, PMT 0, and FV = 1000000. We press the N key to get
the answer, 15.7473 years. In Excel, we would use the NPER function: =NPER(I,PMT,PV,
FV). Inserting data, we have =NPER(0.045,0,−500000,1000000) = 15.7473. The chapter’s
tool kit, Ch04 Tool Kit.xlsx, shows this example.
SELF-TEST
How long would it take $1,000 to double if it were invested in a bank that pays 6% per year?
(11.9 years) How long would it take if the rate were 10%? (7.27 years)
A company’s 2013 earnings per share were $2.75, and its growth rate during the prior 14 years
was 16.35% per year. If that growth rate were maintained, how long would it take for EPS to
double? (4.58 years)
4-6 Perpetuities
The previous sections examined the relationship between the present value and future
value of a single payment at a fixed point in time. However, some securities promise to
make payments forever. For example, preferred stock, which we discuss in Chapter 7,
promises to pay a dividend forever. Another “forever” security originated in the mid-1700s
when the British government issued some bonds that never matured and whose proceeds were
used to pay off other British bonds. Because this action consolidated the government’s debt, the
new bonds were called “consols.” The term stuck, and now any bond that promises to pay
interest perpetually is called a consol, or a perpetuity. The interest rate on the consols was 2.5%,
so a consol with a face value of ₤1,000 would pay ₤25 per year in perpetuity (₤ is the currency
symbol for a British pound).
6
Here’s the setup for the log solution. First, transform Equation 4-1 as indicated, then find the natural logs using
a financial calculator, and then solve for N:
$1,000,000 $500,000 1 0 045 N
2 1 0 045 N
ln 2 N ln 1 045
N 0 6931 0 0440 15 7473 years
resource
See Ch04 Tool Kit.xlsx
for all calculations.
154 Part 2 Fixed Income Securities
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

## Halaman PDF 192

```text
A consol, or perpetuity, is simply an annuity whose promised payments extend out
forever. Since the payments go on forever, you can’t apply the step-by-step approach.
However, it’s easy to find the PV of a perpetuity with the following formula:7
PV of a perpetuity PMT
I (4-4)
We can use Equation 4-4 to find the value of a British consol with a face value of
₤1,000 that pays ₤25 per year in perpetuity. The answer depends on the interest rate being
earned on investments of comparable risk at the time the consol is being valued.
Originally, the “going rate” as established in the financial marketplace was 2.5%, so
originally the consol’s value was ₤1,000:
Consol’s valueOriginally ₤25 0 025 ₤1,000
The annual payment is still ₤25 today, but the going interest rate has risen to about 5.2%,
causing the consol’s value to fall to ₤480.77:
Consol’s valueToday ₤25 0 052 ₤480 77
Note, though, that if interest rates decline in the future, say to 2%, then the value of the
consol will rise to ₤1,250.00:
Consol’s value if rates decline to 2% ₤25 0 02 ₤1,250 00
These examples demonstrate an important point: When interest rates change, the prices of
outstanding bonds also change, but inversely to the change in rates. Thus, bond prices
decline if rates rise, and prices increase if rates fall. This holds for all bonds, both consols
and those with finite maturities. We discuss this point in more detail in Chapter 5, where
we cover bonds in depth.
SELF-TEST
What is the present value of a perpetuity that pays ₤1,000 per year, beginning 1 year from now,
if the appropriate interest rate is 5%? ( 20,000) What would the value be if the perpetuity
began its payments immediately? ( 21,000) (Hint: Just add the ₤1,000 to be received
immediately to the formula value of the annuity.)
Do bond prices move directly or inversely with interest rates—that is, what happens to the
value of a bond if interest rates increase or decrease?
4-7 Annuities
Thus far, we have dealt with single payments, or “lump sums.” However, assets such as
bonds provide a series of cash inflows over time, and obligations such as auto loans,
student loans, and mortgages call for a series of payments. If the payments are equal and
are made at fixed intervals, then we have an annuity. For example, $100 paid at the end of
each of the next 3 years is a 3-year annuity.
7
Here is an intuitive explanation for Equation 4-4. Suppose you deposit an amount equal to PV in a bank that pays an
interest rate of I. Each year you would be able to withdraw an amount equal to I × PV. If you left your deposit in
forever, you could withdraw a payment of I × PV forever: PMT I PV. Rearranging, we get Equation 4-4. This is
only an intuitive explanation, so see Web Extension 4B on the textbook’s Web site for a mathematical derivation of
the perpetuity formula.
Chapter 4 Time Value of Money 155
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

## Halaman PDF 193

```text
If payments occur at the end of each period, then we have an ordinary annuity, which
is also called a deferred annuity. Payments on mortgages, car loans, and student loans are
generally made at the ends of the periods and thus are ordinary annuities. If the payments
are made at the beginning of each period, then we have an annuity due. Rental lease
payments, life insurance premiums, and lottery payoffs (if you are lucky enough to win
one!) are examples of annuities due. Ordinary annuities are more common in finance, so
when we use the term “annuity” in this book, you may assume that the payments occur at
the ends of the periods unless we state otherwise.
Next we show the time lines for a $100, 3-year, 5%, ordinary annuity and for the same
annuity on an annuity due basis. With the annuity due, each payment is shifted back (to
the left) by 1 year. In our example, we assume that a $100 payment will be made each
year, so we show the payments with minus signs.
Periods
Payments –$100 –$100 –$100
0 1 5% 2 3
Ordinary Annuity:
Periods
Payments –$100 –$100 –$100
0 1 5% 2 3
Annuity Due:
As we demonstrate in the following sections, we can find an annuity’s future
value, present value, the interest rate built into the contracts, how long it takes to
reach a financial goal using the annuity, and, if we know all of those values, the size
of the annuity payment. Keep in mind that annuities must have constant payments
and a fixed number of periods. If these conditions don’t hold, then the series is not an
annuity.
SELF-TEST
What’s the difference between an ordinary annuity and an annuity due?
Why should you prefer to receive an annuity due with payments of $10,000 per year for 10 years
than an otherwise similar ordinary annuity?
4-8 Future Value of an Ordinary Annuity
Consider the ordinary annuity whose time line was shown previously, where you deposit
$100 at the end of each year for 3 years and earn 5% per year. Figure 4-5 shows how to
calculate the future value of the annuity (FVAN), using the same approaches we used for
single cash flows.
As shown in the step-by-step section of Figure 4-5, we compound each payment out
to Time 3, and then sum those compounded values in Cell F254 to find the annuity’s FV,
FVA3 $315 25 (we ignore the negative signs in the time line to be consistent with the
results from the other methods). The first payment earns interest for two periods,
the second for one period, and the third earns no interest because it is made at the end
of the annuity’s life. This approach is straightforward, but if the annuity extends out for
many years, it is cumbersome and time-consuming.
156 Part 2 Fixed Income Securities
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

## Halaman PDF 194

```text
As you can see from the time line diagram, with the step-by-step approach we apply
the following equation with N 3 and I 5%:
FVAN PMT 1 I N−1 PMT 1 I N−2 PMT 1 I N−3
$100 1 05 2 $100 1 05 1 $100 1 05 0
$315 25
For the general case, the future value of an annuity is:
FVAN PMT 1 I N−1 PMT 1 I N−2 PMT 1 I N−3 PMT 1 I 0
As shown in Web Extension 4B on the textbook’s Web site, the future value of an
annuity can be written as follows:8
FIGURE 4-5
Summary: Future Value of an Ordinary Annuity
– –
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus, intermediate
calculations using the figure’s rounded values will be inexact.
8
Section 4-4 shows that the present value of an infinitely long annuity, called a perpetuity, is equal to PMT/I. The
cash flows of an ordinary annuity of N periods are equal to the cash flows of a perpetuity minus the cash flows of
a perpetuity that begins at year N + 1. Therefore, the future value of an N-period annuity is equal to the future
value (as of year N) of a perpetuity minus the value (as of year N) of a perpetuity that begins at year N + 1. See
Web Extension 4B on the textbook’s Web site for details regarding derivations of Equation 4-5.
Chapter 4 Time Value of Money 157
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

## Halaman PDF 195

```text
FVAN PMT
1 I N
I − 1
I
PMT
1 I N−1
I (4-5)
Using Equation 4-5, the future value of the annuity is found to be $315.25:
FVA3 $100 1 0 05 3
−1
0 05 $315 25
As you might expect, annuity problems can be solved easily using a financial calcu￾lator or a spreadsheet, most of which have the following formula built into them:
PV 1 I N PMT
1 I N−1
I
FV 0 (4-6)
The procedure when dealing with annuities is similar to what we have done thus far for
single payments, but the presence of recurring payments means that we must use the
PMT key. Here’s the calculator setup for our illustrative annuity:
Inputs 3 5
315.25
0 –100
N I/YR PV PMT FV
Output
End Mode
We enter PV 0 because we start off with nothing, and we enter PMT 100 because
we will deposit this amount in the account at the end of each of the 3 years. The interest
rate is 5%, and when we press the FV key we get the answer, FVA3 315 25.
Because this is an ordinary annuity, with payments coming at the end of each year, we
must set the calculator appropriately. As noted earlier, most calculators “come out of the
box” set to assume that payments occur at the end of each period—that is, to deal with
ordinary annuities. However, there is a key that enables us to switch between ordinary
annuities and annuities due. For ordinary annuities, the designation “End Mode” or some￾thing similar is used, while for annuities due the designator is “Begin,” “Begin Mode,”
“Due,” or something similar. If you make a mistake and set your calculator on Begin Mode
when working with an ordinary annuity, then each payment will earn interest for 1 extra
year, which will cause the compounded amounts, and thus the FVA, to be too large.
The spreadsheet approach uses Excel’s FV function, =FV(I,N,PMT,PV). In our
example, we have =FV(0.05,3,−100,0), and the result is again $315.25.
SELF-TEST
For an ordinary annuity with 5 annual payments of $100 and a 10% interest rate, for how many
years will the first payment earn interest, and what is the compounded value of this payment
at the end? (4 years, $146.41) Answer these questions for the fifth payment. (0 years, $100)
Assume that you plan to buy a condo 5 years from now, and you estimate that you can save
$2,500 per year toward a down payment. You plan to deposit the money in a bank that pays
4% interest, and you will make the first deposit at the end of this year. How much will you have
after 5 years? ($13,540.81) How would your answer change if the bank’s interest rate were
increased to 6%, or decreased to 3%? ($14,092.73; $13,272.84)
resource
See Ch04 Tool Kit.xlsx
for all calculations.
158 Part 2 Fixed Income Securities
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

## Halaman PDF 196

```text
4-9 Future Value of an Annuity Due
Because each payment occurs one period earlier with an annuity due, the payments will all
earn interest for one additional period. Therefore, the FV of an annuity due will be greater
than that of a similar ordinary annuity.
If you followed the step-by-step procedure, you would see that our illustrative
annuity due has a FV of $331.01 versus $315.25 for the ordinary annuity. See
Ch04 Tool Kit.xlsx on the textbook’s Web site for a summary of future value
calculations.
With the formula approach, we first use Equation 4-5, but because each payment
occurs one period earlier, we multiply the Equation 4-5 result by (1 + I):
FVAdue FVAordinary 1 I (4-7)
Thus, for the annuity due, FVAdue $315 25 1 05 $331 01, which is the same result
as found with the step-by-step approach.
With a calculator, we input the variables just as we did with the ordinary annuity, but
we now set the calculator to Begin Mode to get the answer, $331.01:
Inputs 3 5
331.01
0 –100
N I/YR PV PMT FV
Output
Begin Mode
In Excel, we still use the FV function, but we must indicate that we have an annuity
due. The function is =FV(I,N,PMT,PV,Type), where “Type” indicates the type of
annuity. If Type is omitted, then Excel assumes that it is 0, which indicates an ordinary
annuity. For an annuity due, Type 1. As shown in Ch04 Tool Kit.xlsx, the function is
=FV(0.05,3,−100,0,1) = $331.01.
The Power of Compound Interest
Assume that you are 26 and just received your MBA. After
reading the introduction to this chapter, you decide to start
investing in the stock market for your retirement. Your goal is to
have $1 million when you retire at age 65. Assuming you earn
10% annually on your stock investments, how much must you
invest at the end of each year in order to reach your goal?
The answer is $2,491, but this amount depends criti￾cally on the return your investments earn. If your return
drops to 8%, the required annual contribution would rise
to $4,185. On the other hand, if the return rises to 12%, you
would need to put away only $1,462 per year.
What if you are like most 26-year-olds and wait until
later to worry about retirement? If you wait until age 40,
you will need to save $10,168 per year to reach your
$1 million goal, assuming you can earn 10%, but $13,679
per year if you earn only 8%. If you wait until age 50
and then earn 8%, the required amount will be $36,830
per year!
Although $1 million may seem like a lot of money, it
won’t be when you get ready to retire. If inflation averages
5% a year over the next 39 years, then your $1 million nest
egg would be worth only $149,148 in today’s dollars. If you
live for 20 years after retirement and earn a real 3% rate of
return, your annual retirement income in today’s dollars
would be only $9,733 before taxes. So, after celebrating
your graduation and new job, start saving!
resource
See Ch04 Tool Kit.xlsx
for all calculations.
Chapter 4 Time Value of Money 159
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

## Halaman PDF 197

```text
SELF-TEST
Why does an annuity due always have a higher future value than an ordinary annuity?
If you know the value of an ordinary annuity, explain why you could find the value of the
corresponding annuity due by multiplying by (1+I).
Assume that you plan to buy a condo 5 years from now and that you need to save for a down
payment. You plan to save $2,500 per year, with the first payment being made immediately
and deposited in a bank that pays 4%. How much will you have after 5 years? ($14,082.44)
How much would you have if you made the deposits at the end of each year? ($13,540.81)
4-10 Present Value of Ordinary Annuities and
Annuities Due
The present value of any annuity (PVAN) can be found using the step-by-step, formula,
calculator, or spreadsheet methods. We begin with ordinary annuities.
4-10a Present Value of an Ordinary Annuity
See Figure 4-6 for a summary of the different approaches for calculating the present value
of an ordinary annuity.
As shown in the step-by-step section of Figure 4-6, we discount each payment back to
Time 0, and then sum those discounted values to find the annuity’s PV, PVA3 $272 32
(we ignore the negative signs in the time line to be consistent with the results from the
other methods). This approach is straightforward, but if the annuity extends out for many
years, it is cumbersome and time-consuming.
The time line diagram shows that with the step-by-step approach we apply the
following equation with N 3 and I 5%:
PVAN PMT 1 I 1 PMT 1 I 2 PMT 1 I N
The present value of an annuity can be written as:9
PVAN PMT
1
I − 1
I 1 I N (4-8)
For our example annuity, the present value is:
PVA3 $100 1
0 05 − 1
0 05 1 0 05 3 $272 32
Financial calculators are programmed to solve Equation 4-6, so we input the variables
and press the PV key, first making sure the calculator is set to End Mode. The calculator
setup is shown below:
Inputs 3 5
272.32
–100 0
N I/YR PV PMT FV
Output
End Mode
(Ordinary
Annuity)
9
See Web Extension 4B on the textbook’s Web site for details of this derivation.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
160 Part 2 Fixed Income Securities
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

## Halaman PDF 198

```text
The last section of Figure 4-6 shows the spreadsheet solution using Excel’s built-in PV
function: =PV(I,N,PMT,FV). In our example, we have =PV(0.05,3,−100,0) with a resulting
value of $272.32.
4-10b Present Value of Annuities Due
Because each payment for an annuity due occurs one period earlier, the payments will all
be discounted for one less period. Therefore, the PV of an annuity due must be greater
than that of a similar ordinary annuity.
If you went through the step-by-step procedure, you would see that our example
annuity due has a PV of $285.94 versus $272.32 for the ordinary annuity. See Ch04 Tool
Kit.xlsx for this and the other calculations.
With the formula approach, we first use Equation 4-8 to find the value of the ordinary
annuity and then, because each payment now occurs one period earlier, we multiply the
Equation 4-8 result by (1 + I):
FIGURE 4-6
Summary: Present Value of an Ordinary Annuity
–
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
Chapter 4 Time Value of Money 161
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

## Halaman PDF 199

```text
PVAdue PVAordinary 1 I (4-9)
PVAdue $272 32 1 05 $285 94
With a financial calculator, the inputs are the same as for an ordinary annuity, except
you must set the calculator to Begin Mode:
Inputs 3 5
285.94
–100 0
N I/YR PV PMT FV
Output
Begin Mode
(Annuity
Due)
In Excel, we again use the PV function, but now we must indicate that we have an
annuity due. The function is now =PV(I,N,PMT,FV,Type), where “Type” is the type of
annuity. If Type is omitted then Excel assumes that it is 0, which indicates an ordinary
annuity; for an annuity due, Type 1. As shown in Ch04 Tool Kit.xlsx, the function for
this example is =PV(0.05,3,−100,0,1) = $285.94.
SELF-TEST
Why does an annuity due have a higher present value than an ordinary annuity?
If you know the present value of an ordinary annuity, what’s an easy way to find the PV of the
corresponding annuity due?
What is the PVA of an ordinary annuity with 10 payments of $100 if the appropriate interest
rate is 10%? ($614.46) What would the PVA be if the interest rate were 4%? ($811.09) What
if the interest rate were 0%? ($1,000.00) What would the PVAs be if we were dealing with
annuities due? ($675.90, $843.53, and $1,000.00)
Assume that you are offered an annuity that pays $100 at the end of each year for 10 years.
You could earn 8% on your money in other equally risky investments. What is the most you
should pay for the annuity? ($671.01) If the payments began immediately, then how much
would the annuity be worth? ($724.69)
4-11 Finding Annuity Payments, Periods,
and Interest Rates
In the three preceding sections we discussed how to find the FV and PV of ordinary
annuities and annuities due, using these four methods: step-by-step, formula, financial
calculator, and Excel. Five variables are involved—N, I, PMT, FV, and PV—and if
you know any four, you can find the fifth by solving Equation 4-6 for ordinary annuities
(for annuities due, substitute PMT(1+I) for PMT in Equation 4-6 and solve for the
unknown variable). However, a trial-and-error procedure is generally required to find
N or I, and that can be quite tedious if performed manually. Therefore, we discuss only
the financial calculator and spreadsheet approaches for finding N and I.
4-11a Finding Annuity Payments, PMT
We need to accumulate $10,000 and have it available 5 years from now. We can earn 6%
on our money. Thus, we know that FV 10,000, PV 0, N 5, and I YR 6. We
can enter these values in a financial calculator and then press the PMT key to find our
required deposits. However, the answer depends on whether we make deposits at the end
resource
See Ch04 Tool Kit.xlsx
for all calculations.
162 Part 2 Fixed Income Securities
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

## Halaman PDF 200

```text
of each year (ordinary annuity) or at the beginning (annuity due), so the mode must be
set properly. Here are the results for each type of annuity:
Inputs 5 6 0 10000
–1,773.96
N I/YR PV PMT FV
Output
End Mode
(Ordinary
Annuity)
Inputs 5 6 0 10000
–1,673.55
N I/YR PV PMT FV
Output
Begin Mode
(Annuity
Due)
Thus, you must put away $1,773.96 per year if you make payments at the end of each year,
but only $1,673.55 if the payments begin immediately. Finally, note that the required
payment for the annuity due is the ordinary annuity payment divided by (1 + I):
$1,773 96 1 06 $1,673 55.
Excel can also be used to find annuity payments, as shown below for the two types of
annuities. For end-of-year (ordinary) annuities, “Type” can be left blank or a 0 can be
inserted. For beginning-of-year annuities (annuities due), the same function is used but
now Type is designated as 1. Here is the setup for the two types of annuities.
Function : PMT I,N,PV,FV,Type
Ordinary annuity : PMT 0 06,5,0,10000 −$1,773 96
Annuity due : PMT 0 06,5,0,10000,1 −$1,673 55
Variable Annuities: Good or Bad?
Retirees appreciate stable, predictable income, so they often buy
annuities. Insurance companies have been the traditional sup￾pliers, using the payments they receive to buy high-grade bonds,
whose interest is then used to make the promised payments.
Such annuities were quite safe and stable and provided returns
of around 7.5%. However, returns on stocks (dividends plus
capital gains) have historically exceeded bonds’ returns (inter￾est). Therefore, some insurance companies in the 1990s began to
offer variable annuities, which were backed by stocks instead of
bonds. If stocks earned in the future as much as they had in the
past, then variable annuities could offer returns of about 9%; this
is better than the return on fixed-rate annuities. If stock returns
turned out to be lower in the future than they had been in the
past (or even had negative returns), then the variable annuities
promised a guaranteed minimum payment of about 6.5%. Vari￾able annuities appealed to many retirees, so companies that
offered them had a significant competitive advantage.
The insurance company that pioneered variable annu￾ities, The Hartford Financial Services Group, tried to hedge
its position with derivatives that paid off if stocks went
down. But like so many other derivatives-based risk man￾agement programs, this one went awry in 2008 because
stock losses exceeded the assumed worst-case scenario.
The Hartford, which was founded in 1810 and was one of
the oldest and largest U.S. insurance companies at the
beginning of 2008, saw its stock price fall from $85.54 per
share to $4.16. Because of the general stock market crash,
investors feared that The Hartford would be unable to make
good on its variable annuity promises, and this would lead
to bankruptcy. The company was bailed out by the eco￾nomic stimulus package, but this venerable old firm will
never be the same again.
Source: Leslie Scism and Liam Pleven, “Hartford Aims to Take Risk Out of
Annuities,” Online Wall Street Journal, January 13, 2009.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
Chapter 4 Time Value of Money 163
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

## Halaman PDF 201

```text
4-11b Finding the Number of Periods, N
Suppose you decide to make end-of-year deposits, but you can save only $1,200 per year.
Again assuming that you would earn 6%, how long would it take you to reach your
$10,000 goal? Here is the calculator setup:
Inputs 6 0 –1200 10000
6.96
N I/YR PV PMT FV
Output
End Mode
With these smaller deposits, it would take 6.96 years, not 5 years, to reach the $10,000
target. If you began the deposits immediately, then you would have an annuity due and N
would be slightly less, 6.63 years.
With Excel, you can use the NPER function: =NPER(I,PMT,PV,FV, Type). For our
ordinary annuity example, Type is left blank (or 0 is inserted) and the function is =NPER
(0.06,−1200,0,10000) = 6.96. If we put in 1 for Type, we would find N 6 63.
4-11c Finding the Interest Rate, I
Now suppose you can save only $1,200 annually, but you still need to have the $10,000 in
5 years. What rate of return would you have to earn to reach your goal? Here is the
calculator setup:
Inputs 5 0 –1200 10000
25.78
N I/YR PV PMT FV
Output
End Mode
Thus, you would need to earn a whopping 25.78%! About the only way to earn such a
high return would be either to invest in speculative stocks or head to a Las Vegas casino.
Of course, speculative stocks and gambling aren’t like making deposits in a bank with a
guaranteed rate of return, so there would be a high probability that you’d end up with
nothing. So, you should probably save more, lower your $10,000 target, or extend your
Using the Internet for Personal Financial Planning
How good are your financial planning skills? For example,
should you buy or lease a car? How much and how soon
should you begin to save for your children’s education?
How expensive a house can you afford? Should you refi￾nance our home mortgage? How much must you save each
year if you are to retire comfortably? The answers to these
questions are often complicated and depend on a number
of factors, such as projected housing and education costs,
interest rates, inflation, expected family income, and stock
market returns.
Fortunately, you should be able to use time value of money
concepts and online resources to begin developing you finan￾cial plan. In addition to the online data sources described in
Chapter 2, an excellent source of information is available at
www.smartmoney.com. Smartmoney is a personal finance
magazine produced by the publishers of The Wall Street Jour￾nal. If you go to Smartmoney’s Web site, you will find a section
entitled “Tools.” This section has a number of financial calcu￾lators, spreadsheets, and descriptive materials that cover a
wide range of personal finance issues.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
164 Part 2 Fixed Income Securities
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

## Halaman PDF 202

```text
time horizon. It might be appropriate to seek a somewhat higher return, but trying to earn
25.78% in a 6% market would involve speculation, not investing.
In Excel, you can use the RATE function: =RATE(N,PMT,PV,FV,Type). For our
example, the function is =RATE(5,−1200,0,10000) = 0.2578 = 25.78%. If you decide to
make the payments beginning immediately, then the required rate of return would decline
sharply, to 17.54%.
SELF-TEST
You just inherited $100,000 and invested it at 7% per year. How large a withdrawal could you make
at the end of each of the next 10 years and end up with zero? ($14,237.75) How would your
answer change if you made withdrawals at the beginning of each year? ($13,306.31)
If you have $100,000 that is invested at 7% and you wanted to withdraw $10,000 at the end of each
year, how long will your funds last? (17.8 years) How long would they last if you earned 0%?
(10 years) How long would they last if you earned the 7% but limited your withdrawals to $7,000
per year? (forever)
Your uncle named you as the beneficiary of his life insurance policy. The insurance company
gives you a choice of $100,000 today or a 12-year annuity of $12,000 at the end of each year.
What rate of return is the insurance company offering? (6.11%)
You just inherited an annuity that will pay you $10,000 per year for 10 years, and you receive
the first payment today. A professional investor offers to give you $60,000 for the annuity. If you
sell it to him, what rate of return will he earn on the investment? (13.70%) If you think a “fair”
rate of return would be 6%, how much should you ask for the annuity? ($78,016.92)
4-12 Uneven, or Irregular, Cash Flows
The definition of an annuity includes the term constant payment, which suggests that
annuities involve a set of identical payments over a given number of periods. Although many
financial decisions do involve constant payments, many others involve cash flows that are
uneven or irregular. For example, the dividends on common stocks are typically expected to
increase over time, and the investments that companies make in new products, expanded
production capacity, and replacement machinery almost always generate cash flows that vary
from year to year. Throughout the book, we use the term payment (PMT) in situations where
the cash flows are constant and thus an annuity is involved; if different cash flows occur in
different time periods, t, then we use the term CFt to designate the cash flow in period t.
There are two important classes of uneven cash flows: (1) those in which the cash flow
stream consists of a series of annuity payments plus an additional final lump sum in
Year N, and (2) all other uneven streams. Bonds are an instance of the first type, while
stocks and capital investments illustrate the second type. Here’s an example of each type.
0 1 2 4 Periods I = 12%
Cash ows
3 5
$0 $100 $100 $100 $100 $ 100
$1,000
$1,100
Stream 1. Annuity plus an additional final payment:
0 1 2 4 Periods I = 12%
Cash ows
3 5
$0 $100 $300 $300 $300 $500
Stream 2. Irregular cash flow stream:
Chapter 4 Time Value of Money 165
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

## Halaman PDF 203

```text
Equation 4-10 can be used, following the step-by-step procedure, to find the PV of either
stream. However, as we shall see, the solution process differs significantly for the two
types.
PV
CF1
1 I 1
CF2
1 I 2
CFN
1 I N
N
t 1
CFt
1 I t (4-10)
4-12a Annuity Plus Additional Final Payment
First, consider Stream 1 and notice that it is a 5-year, 12%, ordinary annuity plus a final
payment of $1,000. We can find the PV of the annuity, find the PV of the final payment,
and then sum them to get the PV of the stream. Financial calculators are programmed to
do this for us—we use all five time value of money (TVM) keys, entering the data for the
four known values as shown below, and then pressing the PV key to get the answer:
Inputs 5 12 100 1000
–927.90
N I/YR PV PMT FV
Output
Similarly, we could use Excel’s PV function: =PV(I,N,PMT,FV) = PV(0.12,5,100,1000) =
−$927.90. Note that the process is similar to that for annuities, except we now have a
nonzero value for FV.
4-12b Irregular Cash Flow Stream
Now consider the irregular stream, which is analyzed in Figure 4-7. The top section shows
the basic time line, which contains the inputs, and we first use the step-by-step approach
to find PV $1 016 35. Note that we show the PV of each cash flow directly below the
cash flow, and then we sum these PVs to find the PV of the stream. This setup saves space
as compared with showing the individual PVs in a column, and it is also transparent and
thus easy to understand.
Now consider the financial calculator approach. The cash flows don’t form an annuity,
so you can’t use the annuity feature on the calculator. You could, of course, use the
calculator in the step-by-step procedure, but financial calculators have a feature—the cash
flow register—that allows you to find the present value more efficiently. First, you input
the individual cash flows, in chronological order, into the cash flow register.10 Cash flows
are designated CF0, CF1, CF2, CF3, and so on, up to the last cash flow, CFN. Next, you
enter the interest rate, I/YR. At this point, you have substituted in all the known values of
Equation 4-10, so when you press the NPV key you get the PV of the stream. The
calculator finds the PV of each cash flow and sums them to find the PV of the entire
stream. To input the cash flows for this problem, enter 0 (because CF0 0), 100, 300, 300,
300, and 500 in that order into the cash flow register, enter I YR 12, and then press
NPV to obtain the answer, $1,016.35.
10These instructions are for the HP 10bII+, but most other financial calculators work in a similar manner.
166 Part 2 Fixed Income Securities
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

## Halaman PDF 204

```text
Two points should be noted. First, when dealing with the cash flow register, the
calculator uses the term “NPV” rather than “PV.” The N stands for “net,” so NPV is the
abbreviation for “net present value,” which is simply the net present value of a series of
positive and negative cash flows, including any cash flow at time zero. The NPV function
will be used extensively when we get to capital budgeting, where CF0 is generally the cost
of the project.
The second point to note is that repeated cash flows with identical values can be
entered into the cash flow register more efficiently on some calculators by using the
Nj key. In this illustration, you would enter CF0 0, CF1 100, CF2 300, Nj 3
(which tells the calculator that the 300 occurs 3 times), and CF5 500.11 Then enter
I 12, press the NPV key, and 1,016.35 will appear in the display. Also, note that
numbers entered into the cash flow register remain in the register until they are
cleared. Thus, if you previously worked a problem with eight cash flows, and then
moved to one with only four cash flows, the calculator would simply add the cash
flows from the second problem to those of the first problem, and you would get an
incorrect answer. Therefore, you must be sure to clear the cash flow register before
starting a new problem.
Spreadsheets are especially useful for solving problems with uneven cash flows.
You enter the cash flows in the spreadsheet as shown in Figure 4-7 on Row 471. To
FIGURE 4-7
Present Value of an Irregular Cash Flow Stream
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
11On some calculators, instead of entering CF5 500, you enter CF3 500, because this is the next cash flow
different from 300.
resource
See Ch04 Tool Kit.xlsx
for all calculations.
Chapter 4 Time Value of Money 167
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

## Halaman PDF 205

```text
find the PV of these cash flows without going through the step-by-step process, you
would use the NPV function. First put the cursor on the cell where you want the
answer to appear, Cell G481, click the function wizard, choose Financial, scroll down
to NPV, and click OK to get the dialog box. Then enter C467 (or 0.12) for Rate and
enter either the individual cash flows or the range of cells containing the cash flows,
C471:G471, for Value 1. Be very careful when entering the range of cash flows. With
a financial calculator, you begin by entering the Time-0 cash flow. With Excel, you do
not include the Time-0 cash flow; instead, you begin with the Time-1 cash flow. Now,
when you click OK, you get the PV of the stream, $1,016.35. Note that you can use
the PV function if the payments are constant, but you must use the NPV function if
the cash flows are not constant. Finally, note that Excel has a major advantage over
financial calculators in that you can see the cash flows, which makes it easy to spot
data-entry errors. With a calculator, the numbers are buried in the machine, making
it harder to check your work.
SELF-TEST
Could you use Equation 4-3, once for each cash flow, to find the PV of an uneven stream of cash
flows?
What is the present value of a 5-year ordinary annuity of $100 plus an additional $500 at
the end of Year 5 if the interest rate is 6%? ($794.87) What would the PV be if the $100
payments occurred in Years 1 through 10 and the $500 came at the end of Year 10?
($1,015.21)
What is the present value of the following uneven cash flow stream: $0 at Time 0, $100 at the
end of Year 1 (or at Time 1), $200 at the end of Year 2, $0 at the end of Year 3, and $400 at the
end of Year 4—assuming the interest rate is 8%? ($558.07)
Would a “typical” common stock provide cash flows more like an annuity or more like an
uneven cash flow stream?
4-13 Future Value of an Uneven Cash Flow Stream
The future value of an uneven cash flow stream is found by compounding each payment
to the end of the stream and then summing the future values:
FV CF0 1 I N CF1 1 I N 1 CF2 1 I N 2 CFN−1 1 I CFN
N
t 0
CFt 1 I N−t (4-11)
The future value of our illustrative uneven cash flow stream is $1,791.15, as shown in
Figure 4-8.
Most financial calculators have a net future value (NFV) key, which, after the cash flows
and interest rate have been entered, can be used to obtain the future value of an uneven cash
flow stream. If your calculator doesn’t have the NFV feature, you can first find the net present
value of the stream, and then find its net future value as NFV NPV 1 I N. In the
illustrative problem, we find PV 1 016 35 using the cash flow register and I 12. Then
we use the TVM register, entering N 5, I 12, PV 1016 35, and PMT 0. When we
press FV, we find FV 1 791 15, which is the same as the value shown on the time line in
Figure 4-8. As Figure 4-8 also shows, the same procedure can be used with Excel.
168 Part 2 Fixed Income Securities
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

## Halaman PDF 206

```text
SELF-TEST
What is the future value of this cash flow stream: $100 at the end of 1 year, $150 after 2 years,
and $300 after 3 years, assuming the appropriate interest rate is 15%? ($604.75)
4-14 Solving for I with Irregular Cash Flows
Before financial calculators and spreadsheets existed, it was extremely difficult to find I if
the cash flows were uneven. However, with spreadsheets and financial calculators it’s easy
to find I. If you have an annuity plus a final lump sum, you can input values for N, PV,
PMT, and FV into the calculator’s TVM registers and then press the I/YR key. Here’s the
setup for Stream 1 from Section 4-12, assuming we must pay $927.90 to buy the asset:
Inputs 5 –927.90 100 1000
12.00
N I/YR PV PMT FV
Output
The rate of return on the $927.90 investment is 12%.
Finding the interest rate for an irregular cash flow stream with a calculator is a bit
more complicated. Figure 4-9 shows Stream 2 from Section 4-12, assuming a required
investment of CF0 −$1,000. First, note that there is no simple step-by-step method for
finding the rate of return—finding the rate for this investment requires a trial-and-error
process, which is terribly time-consuming. Therefore, we really need a financial calculator
or a spreadsheet. With a calculator, we would enter the CFs into the cash flow register and
then press the IRR key to get the answer. IRR stands for “internal rate of return,” and it is
FIGURE 4-8
Future Value of an Irregular Cash Flow Stream
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Chapter 4 Time Value of Money 169
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

## Halaman PDF 207

```text
the rate of return the investment provides. The investment is the cash flow at Time 0, and it
must be entered as a negative number. When we enter those cash flows in the calculator’s
cash flow register and press the IRR key, we get the rate of return on the $1,000
investment, 12.55%. Finally, note that once you have entered the cash flows in the
calculator’s register, you can find both the investment’s net present value (NPV) and its
internal rate of return. For investment decisions, we typically want both of these numbers.
Therefore, we generally enter the data once and then find both the NPV and the IRR.
You would get the same answer using Excel’s IRR function, as shown in Figure 4-9.
Notice that when using the IRR—unlike using the NPV function—you must include all
cash flows, including the Time-0 cash flow.
SELF-TEST
An investment costs $465 now and is expected to produce cash flows of $100 at the end of each
of the next 4 years, plus an extra lump-sum payment of $200 at the end of the fourth year.
What is the expected rate of return on this investment? (9.05%)
An investment costs $465 and is expected to produce cash flows of $100 at the end of Year 1,
$200 at the end of Year 2, and $300 at the end of Year 3. What is the expected rate of return on
this investment? (11.71%)
4-15 Semiannual and Other Compounding Periods
In most of our examples thus far, we assumed that interest is compounded once a year, or
annually. This is annual compounding. Suppose, however, that you put $1,000 into a
bank that pays a 6% annual interest rate but credits interest every 6 months. This is
semiannual compounding. If you leave your funds in the account, how much would you
have at the end of 1 year under semiannual compounding? Note that you will receive $60
of interest for the year with annual compounding. With seminannual compounding, you
will receive $30 of it after only 6 months and you will earn interest on the first $30 during
the second 6 months, so you will end the year with more than the $60 you would have had
under annual compounding. You would be even better off under quarterly, monthly,
weekly, or daily compounding. Note also that virtually all bonds pay interest semiannu￾ally; most stocks pay dividends quarterly; most mortgages, student loans, and auto loans
involve monthly payments; and most money fund accounts pay interest daily. Therefore,
it is essential that you understand how to deal with nonannual compounding.
FIGURE 4-9
IRR of an Uneven Cash Flow Stream
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
170 Part 2 Fixed Income Securities
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

## Halaman PDF 208

```text
4-15a Types of Interest Rates
When we move beyond annual compounding, we must deal with the following four types
of interest rates:
• Nominal annual rates, given the symbol INOM
• Annual percentage rates, termed APR rates
• Periodic rates, denoted as IPER
• Effective annual rates, given the symbol EAR or EFF%
NOMINAL (OR QUOTED) RATE, INOM
12
This is the rate quoted by banks, brokers, and other financial institutions. So, if you talk
with a banker, broker, mortgage lender, auto finance company, or student loan officer
about rates, the nominal rate is the one he or she will normally quote you. However, to be
meaningful, the quoted nominal rate must also include the number of compounding
periods per year. For example, a bank might offer you a CD at 6% compounded daily,
while a credit union might offer 6.1% compounded monthly.
Note that the nominal rate is never shown on a time line, and it is never used as an
input in a financial calculator (except when compounding occurs only once a year). If more
frequent compounding occurs, you must use periodic rates.
PERIODIC RATE, IPER
This is the rate charged by a lender or paid by a borrower each period. It can be a rate per
year, per 6 months (semiannually), per quarter, per month, per day, or per any other time
interval. For example, a bank might charge 1.5% per month on its credit card loans, or a
finance company might charge 3% per quarter on installment loans.
We find the periodic rate as follows:
Periodic rate IPER INOM M (4-12)
where INOM is the nominal annual rate and M is the number of compounding periods per
year. Thus, a 6% nominal rate with semiannual payments results in a periodic rate of
Periodic rate IPER 6% 2 3 00%
If only one payment is made per year then M 1, in which case the periodic rate would
equal the nominal rate: 6% 1 6%.
The periodic rate is the rate shown on time lines and used in calculations.13 To
illustrate, suppose you invest $100 in an account that pays a nominal rate of 12%,
12The term nominal rate as used here does not have the same meaning as it did in Chapter 1. There, nominal
interest rates referred to stated market rates as opposed to real (zero-inflation) rates. In this chapter, the term
nominal rate means the stated, or quoted, annual rate as opposed to the effective annual rate, which we explain
later. In both cases, though, nominal means stated, or quoted, as opposed to some sort of adjusted rate.
13The only exception is in cases where: (1) annuities are involved and (2) the payment periods do not correspond
to the compounding periods. In such cases—for example, if you are making quarterly payments into a bank
account to build up a specified future sum but the bank pays interest on a daily basis—then the calculations are
more complicated. For such problems, the simplest procedure is to determine the periodic (daily) interest rate by
dividing the nominal rate by 365 (or by 360 if the bank uses a 360-day year), then compound each payment over
the exact number of days from the payment date to the terminal point, and then sum the compounded payments
to find the future value of the annuity. This is a simple process with a computer.
Chapter 4 Time Value of Money 171
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

## Halaman PDF 209

```text
compounded quarterly, or 3% per period. How much would you have after 2 years if you
leave the funds on deposit? First, here is the time line for the problem:
−$100 FV=?
Quarters 0 1 2 3 4 5 6 7 8 3%
To find the FV, we would use this modified version of Equation 4-1:
FVN PV 1 IPER
Number of periods PV 1
INOM
M
MN
(4-13)
$100 1 0 12
4
4 2
$100 1 0 03 8 $126 68
With a financial calculator, we find the FV using these inputs: N 4 2 8,
I 12 4 3, PV 100, and PMT 0. The result is again FV $126 68:14
Inputs 8 3 –100 0
126.68
N I/YR PV PMT FV
Output
EFFECTIVE (OR EQUIVALENT) ANNUAL RATE (EAR OR EFF%)
This is the annual (interest once a year) rate that produces the same final result as
compounding at the periodic rate for M times per year. The EAR, also called EFF% (for
effective percentage rate), is found as follows:15
EAR EFF% 1 IPER
M−1 0
1
INOM
M
M
−1 0
(4-14)
Here INOM M is the periodic rate, and M is the number of periods per year. If a bank
would lend you money at a nominal rate of 12%, compounded quarterly, then the EFF%
rate would be 12.5509%:
14Most financial calculators have a feature that allows you to set the number of payments per year and then use
the nominal annual interest rate. However, students tend to make fewer errors when using the periodic rate with
their calculators set for one payment per year (i.e., per period), so this is what we recommend. Note also that you
cannot use a normal time unless you use the periodic rate.
15You could also use the “interest conversion feature” of a financial calculator. Most financial calculators are
programmed to find the EFF% or, given the EFF%, to find the nominal rate; this is called “interest rate
conversion.” You enter the nominal rate and the number of compounding periods per year, and then press the
EFF% key to find the effective annual rate. However, we generally use Equation 4-14 because it’s easy and because
using the equation reminds us of what we are really doing. If you do use the interest rate conversion feature on your
calculator, don’t forget to reset your settings afterward. Interest conversion is discussed in our calculator tutorials.
172 Part 2 Fixed Income Securities
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

## Halaman PDF 210

```text
Rate on bank loan: EFF% 1 0 03 4
− 1 0 1 03 4 − 1 0
1 125509 − 1 0 0 125509 12 5509%
To see the importance of the EFF%, suppose that—as an alternative to the bank loan—you
could borrow on a credit card that charges 1% per month. Would you be better off using
the bank loan or credit card loan? To answer this question, the cost of each alternative
must be expressed as an EFF%. We just saw that the bank loan’s effective cost is 12.5509%.
The cost of the credit card loan, with monthly payments, is slightly higher, 12.6825%:
Credit card loan: EFF% 1 0 01 12 − 1 0 1 01 12 − 1 0
1 126825 − 1 0 0 126825 12 6825%
This result is logical: Both loans have the same 12% nominal rate, yet you would have to make
the first payment after only 1 month on the credit card versus 3 months under the bank loan.
The EFF% rate is rarely used in calculations. However, it must be used to compare the
effective costs of different loans or rates of return on different investments when payment
periods differ, as in our example of the credit card versus a bank loan.
4-15b The Result of Frequent Compounding
What would happen to the future value of an investment if interest were compounded
annually, semiannually, quarterly, or some other less-than-annual period? Because interest
will be earned on interest more often, you should expect higher future values the more
frequently compounding occurs. Similarly, you should expect the effective annual rate to
increase with more frequent compounding. As Figure 4-10 shows, these results do occur—
the future value and the EFF% do increase as the frequency of compounding increases.
Notice that the biggest increase in FV (and in EFF%) occurs when compounding goes from
annual to semiannual, and notice also that moving from monthly to daily compounding has
a relatively small impact. Although Figure 4-10 shows daily compounding as the smallest
interval, it is possible to compound even more frequently. At the limit, compounding can
occur continuously. This is explained in Web Extension 4C on the textbook’s Web site.
Truth in Lending: What Loans Really Cost
Congress passed the Consumer Credit Protection Act in
1968. The Truth in Lending provisions in the Act require
banks and other lenders to disclose the annual percen￾tage rate (APR) they are charging. For example, suppose
you plan to buy a fancy TV set that costs $3,000, and the
store offers you credit for 1 year at an “add-on” quoted
rate of 8%. Here we first find the total dollars of interest
by multiplying the $3,000 you are borrowing times 8%,
resulting in $240. Add the interest to the $3,000 cost of
the TV, for a total loan of $3,240. Then divide the total
loan by 12 to get the monthly payments: $3 240 12 $270
per month, with the first payment made at the time of
purchase. Therefore, we have a 12-month annuity due with
payments of $270. Is your cost really the 8% that you were
quoted?
To find the APR, set your calculator to Begin Mode,
then enter N 12, PV 3000, PMT 270, and FV 0.
Then, when you press the I/YR key, you get the periodic rate,
1.4313%. You then multiply by 12 to get the APR, 17.1758%. You
could also find the EFF%, which is 18.5945%. We show these
calculations using both the calculator and Excel, along with a
time line that helps us visualize what’s happening, in the chap￾ter’s Excel Tool Kit.
The 17.1758% APR that the dealer is required to report
is a much better indicator of the loan’s cost than the 8%
nominal rate, but it still does not reflect the true cost,
which is the 18.5945% effective annual rate. Thus, buying
the TV on time would really cost you 18.5945%. If you don’t
know what’s happening when you buy on time or borrow,
you may pay a lot more than you think!
Chapter 4 Time Value of Money 173
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

## Halaman PDF 211

```text
SELF-TEST
Would you rather invest in an account that pays a 7% nominal rate with annual compounding
or with monthly compounding? If you borrowed at a nominal rate of 7%, would you rather
make annual or monthly payments? Why?
What is the future value of $100 after 3 years if the appropriate interest rate is 8%, compounded
annually? ($125.97) Compounded monthly? ($127.02)
What is the present value of $100 due in 3 years if the appropriate interest rate is 8%, compounded
annually? ($79.38) Compounded monthly? ($78.73)
Define the following terms: annual percentage rate (APR), effective annual rate (EFF%), and
nominal interest rate INOM .
A bank pays 5% with daily compounding on its savings accounts. Should it advertise the nominal
or effective rate if it is seeking to attract new deposits?
Credit card issuers must by law print their annual percentage rate on their monthly
statements. A common APR is 18%, with interest paid monthly. What is the EFF% on such a
loan? (19.56%)
Some years ago banks weren’t required to reveal the rate they charged on credit cards. Then
Congress passed a “truth in lending” law that required them to publish their APR rate. Is the
APR rate really the most truthful rate, or would the EFF% be even more truthful?
4-16 Fractional Time Periods16
So far we have assumed that payments occur at either the beginning or the end of periods,
but not within periods. However, we occasionally encounter situations that require
compounding or discounting over fractional periods. For example, suppose you deposited
FIGURE 4-10
Effect on $100 of Compounding More Frequently than Once a Year
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a We used 365 days per year in the calculations.
b
The EFF% is calculated as 1 IPER M − 1. c
The future value is calculated as $100(1 + EFF%).
16This section is interesting and useful but relatively technical. It can be omitted, at the option of the instructor,
without loss of continuity.
174 Part 2 Fixed Income Securities
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

## Halaman PDF 212

```text
$100 in a bank that pays a nominal rate of 10%, compounded daily, based on a 365-day year.
How much would you have after 9 months? The answer of $107.79 is found as follows:17
Periodic rate IPER 0 10 365 0 000273973 per day
Number of days 9 12 365 0 75 365
273 75 days, rounded to 274
Ending amount $100 1 000273973 274 $107 79
Now suppose that instead you borrow $100 at a nominal rate of 10% per year and are
charged simple interest, which means that interest is not charged on interest. If the loan is
outstanding for 274 days (or 9 months), how much interest would you have to pay? The
interest owed is equal to the principal multiplied by the interest rate times the number
of periods. In this case, the number of periods is equal to a fraction of a year:
N 274 365 0 7506849:
Interest owed $100 10% 0 7506849 $7 51
Another approach would be to use the daily rate rather than the annual rate and thus
to use the exact number of days rather than the fraction of the year:
Interest owed $100 0 000273973 274 $7 51
You would owe the bank a total of $107.51 after 274 days. This is the procedure most
banks use to calculate interest on loans, except that they generally require borrowers to
pay the interest on a monthly basis rather than after 274 days; this more frequent
compounding raises the EFF% and thus the total amount of interest paid.
SELF-TEST
Suppose a company borrowed $1 million at a rate of 9%, using simple interest, with interest
paid at the end of each month. The bank uses a 360-day year. How much interest would the
firm have to pay in a 30-day month? ($7,500.00) What would the interest be if the bank used a
365-day year? ($7,397.26)
Suppose you deposited $1,000 in a credit union that pays 7% with daily compounding and a
365-day year. What is the EFF%? (7.250098%) How much could you withdraw after 7 months,
assuming this is 7/12 of a year? ($1,041.67)
4-17 Amortized Loans
An extremely important application of compound interest involves loans that are paid off
in installments over time. Included are automobile loans, home mortgage loans, student
loans, and many business loans. A loan that is to be repaid in equal amounts on a
monthly, quarterly, or annual basis is called an amortized loan.
18
17We assume that these 9 months constitute 9/12 of a year. Also, bank deposit and loan contracts specifically
state whether they are based on a 360-day or a 365-day year. If a 360-day year is used, then the daily rate is
higher, so the effective rate is also higher. Here we assumed a 365-day year. Finally, note that banks use software
with built-in calendars, so they calculate the exact number of days.
Note also that banks often treat such loans as follows: (1) They require monthly payments, and they
calculate the interest for the month by multiplying the periodic rate by the beginning-of-month balance times the
number of days in the month. This is called “simple interest.” (2) The interest for the month is either added to the
next beginning of month balance, or the borrower must actually pay the earned interest. In this case, the EFF% is
based on 12 compounding periods, not 365 as is assumed in our example.
18The word amortized comes from the Latin mors, meaning “death,” so an amortized loan is one that is “killed
off” over time.
Chapter 4 Time Value of Money 175
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

## Halaman PDF 213

```text
4-17a Payments
Suppose a company borrows $100,000, with the loan to be repaid in 5 equal payments at the end
of each of the next 5 years. The lender charges 6% on the balance at the beginning of each year.
Here’s a picture of the situation:
0 I = 6% 3 4
$100,000 PMT PMT PMT PMT PMT
1 2 5
Our task is to find the amount of the payment, PMT, such that the sum of their PVs
equals the amount of the loan, $100,000:
$100,000 PMT
1 06 1
PMT
1 06 2
PMT
1 06 3
PMT
1 06 4
PMT
1 06 5
5
t 1
PMT
1 06 t
It is possible to solve the annuity formula, Equation 4-8, for PMT, but it is much easier to
use a financial calculator or spreadsheet. With a financial calculator, we insert values as
shown below to get the required payments, $23,739.64:
Inputs 5 6 100000 0
–23,739.64
N I/YR PV PMT FV
Output
What You Know Is What You Get: Not in Payday Lending
When money runs low toward the end of a month, many
individuals turn to payday lenders. If a borrower’s applica￾tion is approved, the payday lender makes a short-term
loan, which will be repaid with the next paycheck. In fact,
on the next payday the lender actually transfers the repay￾ment from the borrower’s bank account. This repayment
consists of the amount borrowed plus a fee.
How costly are payday loans? The lender charges a fee of
about $15 to $17 per $100 borrowed. A typical loan is for about
$350, so the typical fee is about $56. A typical borrower gets
paid about every 2 weeks, so the loan is for a very short amount
of time. With a big fee and a short time until repayment, the
typical payday loan has an APR of over 400%.
How informed are borrowers? Two professors at the
University of Chicago set out to answer this question. When
loans are approved, borrowers receive a form to sign that
shows the APR. However, subsequent telephone surveys of
borrowers show that over 40% of borrowers thought their
APR was around 15%; perhaps not coincidentally, these are
similar numerals to the fee schedules that are posted
prominently in the lender’s office.
The professors then did an experiment (with the agree￾ment of 77 payday loan stores) in which they provided more
information than just the APR. One group of borrowers received
information about the APR of the payday loan as compared to
the APRs of other loans, such as car loans. A second group
received information about the dollar cost of the payday loan
as compared to the dollar cost of other loans, such as car loans.
A third group received information about how long it takes
most payday borrowers to repay their loans (which is longer
than the next payday; borrowers tend to extend the loan for
additional pay periods, accruing additional fees).
Compared to a control group with no additional infor￾mation, the results show that some borrowers with addi￾tional information decided not to take the loan; other
borrowers reduced the amount that they borrow. These
findings suggest that better information helps borrowers
make less costly decisions. The more you know, the less
you get, at least when it comes to costly payday loans.
Source: Marianne Bertrand and Adair Morse, “Information Disclosure, Cognitive
Biases, and Payday Borrowing,” Journal of Finance, Vol. 66, No. 6, December
2011, pp. 1865–1893.
176 Part 2 Fixed Income Securities
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

## Halaman PDF 214

```text
With Excel, you would use the PMT function: =PMT(I,N,PV,FV) = PMT(0.06,5,100000,0) =
−$23,739.64. Thus, we see that the borrower must pay the lender $23,739.64 per year for the
next 5 years.
4-17b Amortization Schedules
Each payment will consist of two parts—part interest and part repayment of principal.
This breakdown is shown in the amortization schedule given in Figure 4-11. The interest
component is relatively high in the first year, but it declines as the loan balance decreases.
For tax purposes, the borrower would deduct the interest component while the lender
would report the same amount as taxable income. Over the 5 years, the lender will earn
6% on its investment and also recover the amount of its investment.
4-17c Mortgage Interest Payments
Now consider a 30-year home mortgage of $250,000 at an annual rate of 6%. How much
interest will the borrower pay over the life of the loan? How much in the first year?
Begin by finding the monthly payment. The financial calculator inputs are shown
below (notice that N and I/YR are adjusted to reflect monthly payments):
Inputs 360 0.5% 250000 0
–1,498.8763
N I/YR PV PMT FV
Output
FIGURE 4-11
Loan Amortization Schedule, $100,000 at 6% for 5 Years
Source: See the file Ch04 Tool Kit.xlsx. Numbers are reported as rounded values for clarity, but are calculated using Excel’s full precision. Thus,
intermediate calculations using the figure’s rounded values will be inexact.
Notes:
a Interest in each period is calculated by multiplying the loan balance at the beginning of the year by the interest rate. Therefore, interest in Year 1 is
$100,000 0 06 $6,000; in Year 2 it is $82,260 36 0 06 $4,935 62; and so on. b Repayment of principal is the $23,739.64 annual payment minus the interest charge for the year, $17,739.64 for Year 1.
Chapter 4 Time Value of Money 177
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

## Halaman PDF 215

```text
The total amount of payments is 360($1,498.8763) ≈ $539,595. The borrower pays back
the borrowed $250,000 over the life of the loan, so the total interest paid is
$539,595 − $250,000 $289,595.
To find the amount of interest paid in the first year, we could construct a monthly
amortization schedule as in Figure 4-11 and add up the monthly interest payments for the
first year. There is an easier way, though. Begin by finding the amount the borrower owes at
the end of the first year. We know the number of remaining payments 360 − 12 348
and the amount of each payment ($1,498.88), so we can solve for the PV:
Inputs 348 0.5% –1498.88 0
246,930.58
N I/YR PV PMT FV
Output
The amount of principal repaid in the first year is the difference between the starting
value and the value at the end of the year: $250,000 − $246,930 58 $3,069 42. The total
payments during the year are 12 $1,498 88 $17,986 56. So the total interest paid in the
year is $17,986 56 − $3,069 42 $14,917 14. Almost 83% of the payments in the first
year go to interest!
Now consider a 15-year mortgage. To compare apples to apples, assume the interest
rate stays at 6%, although it probably would be a bit lower. Changing N to 180, the new
payment is $2,109.6421. The total amount of payments is 180 $2,109 6421 ≈ $379,736
and the total interest paid is $379,736 $250,000 $129,736, a big decrease from the
$289,595 paid on the 30-year mortgage. As this example shows, increasing the monthly
payment can dramatically reduce the total interest paid and the time required to pay off
the mortgage.
SELF-TEST
Consider again the example in Figure 4-11. If the loan were amortized over 5 years with
60 equal monthly payments, how much would each payment be, and how would the
first payment be divided between interest and principal? (Each payment would be
$1,933.28; the first payment would have $500 of interest and $1,433.28 of principal
repayment.)
Suppose you borrowed $30,000 on a student loan at a rate of 8% and now must repay it
in three equal installments at the end of each of the next 3 years. How large would your
payments be, how much of the first payment would represent interest and how much
would be principal, and what would your ending balance be after the first year?
(PMT $11,641.01; interest $2,400; principal $9,241.01; balance at end of Year
1 $20,758.99)
4-18 Growing Annuities19
Normally, an annuity is defined as a series of constant payments to be received over a
specified number of periods. However, the term growing annuity is used to describe a
series of payments that grow at a constant rate.
19This section is interesting and useful but relatively technical. It can be omitted, at the option of the instructor,
without loss of continuity. Also, although an annuity is constant, the expression “growing annuity” is widely
used. Therefore, we will use it, too, even though it is a contradiction in terms.
178 Part 2 Fixed Income Securities
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

## Halaman PDF 216

```text
4-18a Example 1: Finding a Constant Real Income
Growing annuities are often used in the area of financial planning, where a prospective retiree
wants to determine the maximum constant real, or inflation-adjusted, withdrawals that he or
she can make over a specified number of years. For example, suppose a 65-year-old is
contemplating retirement. The individual expects to live for another 20 years, has a $1
million nest egg, expects the investments to earn a nominal annual rate of 6%, expects
inflation to average 3% per year, and wants to withdraw a constant real amount annually over
the next 20 years so as to maintain a constant standard of living. If the first withdrawal is to be
made today, what is the amount of that initial withdrawal?
This problem can be solved in three ways: (1) Set up a spreadsheet model that is
similar to an amortization table, where the account earns 6% per year, withdrawals rise at
the 3% inflation rate, and Excel’s Goal Seek feature is used to find the initial inflation￾adjusted withdrawal. A zero balance will be shown at the end of the 20th year. (2) Use a
The Great Recession of 2007
An Accident Waiting to Happen: Option Reset
Adjustable Rate Mortgages
Option reset adjustable rate mortgages (ARMs) give the bor￾rower some choices regarding the initial monthly payment. One
popular option ARM allowed borrowers to make a monthly
payment equal to only half of the interest due in the first
month. Because the monthly payment was less than the inter￾est charge, the loan balance grew each month. When the loan
balance exceeded 110% of the original principal, the monthly
payment was reset to fully amortize the now-larger loan at the
prevailing market interest rates.
Here’s an example. Someone borrows $325,000 for 30
years at an initial rate of 7%. The interest accruing in the
first month is 7% 12 $325,000 $1,895 83. Therefore,
the initial monthly payment is 50% $1,895 83 $947 92.
Another $947.92 of deferred interest is added to the loan
balance, taking it up to $325,000 $947 92 $325,947 82.
Because the loan is now larger, interest in the second
month is higher, and both interest and the loan balance
will continue to rise each month. The first month after the
loan balance exceeds 110% $325,000 $357,500, the con￾tract calls for the payment to be reset so as to fully amor￾tize the loan at the then-prevailing interest rate.
First, how long would it take for the balance to exceed
$357,500? Consider this from the lender’s perspective: The
lender initially pays out $325,000, receives $947.92 each
month, and then would receive a payment of $357,500 if
the loan were payable when the balance hit that amount,
with interest accruing at a 7% annual rate and with monthly
compounding. We enter these values into a financial calculator:
I 7% 12, PV 325000, PMT 947 92, and FV 357500.
We solve for N 31 3 months, rounded up to 32 months. Thus,
the borrower will make 32 payments of $947.92 before the ARM
resets.
The payment after the reset depends upon the terms of the
original loan and the market interest rate at the time of the
reset. For many borrowers, the initial rate was a lower-than￾market “teaser” rate, so a higher-than-market rate would be
applied to the remaining balance. For this example, we will
assume that the original rate wasn’t a teaser and that the rate
remains at 7%. Keep in mind, though, that for many borrowers
the reset rate was higher than the initial rate. The balance
after the 32nd payment can be found as the future value of
the original loan and the 32 monthly payments, so we enter
these values in the financial calculator: N 32, I 7% 12,
PMT 947 92, PV 325000, and then solve for
FV $358,242 84. The number of remaining payments to
amortize the $358,424.84 loan balance is 360 32 328, so
the amount of each payment is found by setting up the calcu￾lator as N 328, I 7% 12, PV 358242 84, and FV 0. Sol￾ving, we find that PMT $2,453 94.
Even if interest rates don’t change, the monthly pay￾ment jumps from $947.92 to $2,453.94 and would increase
even more if interest rates were higher at the reset. This is
exactly what happened to millions of American home￾owners who took out option reset ARMS in the early
2000s. When large numbers of resets began in 2007,
defaults ballooned. The accident caused by option reset
ARMs didn’t wait very long to happen!
resource
See Ch04 Tool Kit.xlsx
for all calculations.
© Mihai Simonia
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

## Halaman PDF 217

```text
financial calculator, where we first calculate the real rate of return, adjusted for inflation,
and use it for I/YR when finding the payment for an annuity due. (3) Use a relatively
complicated and obtuse formula to find this same amount.20 We will focus on the first
two approaches.
We illustrate the spreadsheet approach in the chapter model, Ch04 Tool Kit.xlsx. The
spreadsheet model provides the most transparent picture, because it shows the value of
the retirement portfolio, the portfolio’s annual earnings, and each withdrawal over the
20-year planning horizon—especially if you include a graph. A picture is worth a
thousand numbers, and graphs make it easy to explain the situation to people who are
planning their financial futures.
To implement the calculator approach, we first find the expected real rate of return,
where rr is the real rate of return and rNOM the nominal rate of return. The real rate of return
is the return that we would see if there were no inflation. We calculate the real rate as:
Real rate rr 1 rNOM 1 Inflation − 1 0 (4-15)
1 06 1 03 − 1 0 0 029126214 2 9126214%
Using this real rate of return, we solve the annuity due problem exactly as we did earlier in
the chapter. We set the calculator to Begin Mode, after which we input N 20,
I YR real rate 2 9126214, PV 1000000, and FV 0; then we press PMT to get
$64,786.88. This is the amount of the initial withdrawal at Time 0 (today), and future
withdrawals will increase at the inflation rate of 3%. These withdrawals, growing at the
inflation rate, will provide the retiree with a constant real income over the next 20 years—
provided the inflation rate and the rate of return do not change.
In our example, we assumed that the first withdrawal would be made immediately.
The procedure would be slightly different if we wanted to make end-of-year withdrawals.
First, we would set the calculator to End Mode. Second, we would enter the same inputs
into the calculator as just listed, including the real interest rate for I/YR. The calculated
PMT would be $66,673.87. However, that value is in beginning-of-year terms, and because
inflation of 3% will occur during the year, we must make the following adjustment to find
the inflation-adjusted initial withdrawal:
Initial end-of -year withdrawal $66,673 87 1 Inflation
$66,673 87 1 03
$68,674 09
Thus, the first withdrawal at the end of the year would be $68,674.09; it would grow by 3%
per year; and after the 20th withdrawal (at the end of the 20th year), the balance in the
retirement fund would be zero.
We also demonstrate the solution for this end-of-year payment example in Ch04 Tool
Kit.xlsx. There we set up a table showing the beginning balance, the annual withdrawals,
the annual earnings, and the ending balance for each of the 20 years. This analysis
confirms the $68,674.09 initial end-of-year withdrawal derived previously.
20For example, the formula used to find the payment of a growing annuity due is shown below. If g
annuity growth rate and r nominal rate of return on investment, then:
PVIF of a growing annuity due PVIFGADue 1− 1 g 1 r N 1 r r g
PMT PV PVIFGADue
where PVIF denotes “present value interest factor.” Similar formulas are available for growing ordinary annuities.
180 Part 2 Fixed Income Securities
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

## Halaman PDF 218

```text
4-18b Example 2: Initial Deposit to Accumulate a
Future Sum
As another example of growing annuities, suppose you need to accumulate $100,000 in 10
years. You plan to make a deposit in a bank now, at Time 0, and then make 9 more
deposits at the beginning of each of the following 9 years, for a total of 10 deposits. The
bank pays 6% interest, you expect inflation to be 2% per year, and you plan to increase
your annual deposits at the inflation rate. How much must you deposit initially? First, we
calculate the real rate:
Real rate rr 1 06 1 02 − 1 0 0 0392157 3 9215686%
Next, because inflation is expected to be 2% per year, in 10 years the target $100,000
will have a real value of:
$100,000 1 0 02 10 $82,034 83
Now we can find the size of the required initial payment by setting a financial calculator to
the Begin Mode and then inputting N 10, I YR 3 9215686, PV 0, and
FV 82034 83. Then, when we press the PMT key, we get PMT 6 598 87. Thus, a
deposit of $6,598.87 made at time 0 and growing by 2% per year will accumulate to $100,000
by Year 10 if the interest rate is 6%. Again, this result is confirmed in the chapter’s Tool Kit.
The key to this analysis is to express I/YR, FV, and PMT in real, not nominal, terms.
SELF-TEST
Differentiate between a “regular” and a “growing” annuity.
What three methods can be used to deal with growing annuities?
If the nominal interest rate is 10% and the expected inflation rate is 5%, what is the expected
real rate of return? (4.7619%)
SUMMARY
Most financial decisions involve situations in which someone makes a payment at one point
in time and receives money later. Dollars paid or received at two different points in time are
different, and this difference is dealt with using time value of money (TVM) analysis.
• Compounding is the process of determining the future value (FV) of a cash flow or a
series of cash flows. The compounded amount, or future value, is equal to the beginning
amount plus interest earned.
• Future value of a single payment FVN PV 1 I N.
• Discounting is the process of finding the present value (PV) of a future cash flow or a
series of cash flows; discounting is the reciprocal, or reverse, of compounding.
• Present value of a payment received at the end of Time N PV
FVN
1 I N.
• An annuity is defined as a series of equal periodic payments (PMT) for a specified
number of periods.
• An annuity whose payments occur at the end of each period is called an ordinary
annuity.
• Future value of an ordinary annuity FVAN PMT
1 I N
I − 1
I .
Chapter 4 Time Value of Money 181
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

## Halaman PDF 219

```text
• Present value of an ordinary annuity PVAN PMT
1
I − 1
I 1 I N .
• If payments occur at the beginning of the periods rather than at the end, then we have an
annuity due. The PV of each payment is larger, because each payment is discounted back
1 year less, so the PV of the annuity is also larger. Similarly, the FV of the annuity due is
larger because each payment is compounded for an extra year. The following formulas can
be used to convert the PV and FV of an ordinary annuity to an annuity due:
PVAdue PVAordinary 1 I
FVAdue FVAordinary 1 I
• A perpetuity is an annuity with an infinite number of payments:
Value of a perpetuity PMT
I
• To find the PV or FV of an uneven series, find the PV or FV of each individual cash
flow and then sum them.
• If you know the cash flows and the PV (or FV) of a cash flow stream, you can
determine its interest rate.
• When compounding occurs more frequently than once a year, the nominal rate must be
converted to a periodic rate, and the number of years must be converted to periods:
Periodic rate IPER Nominal annual rate Periods per year
Number of Periods Years Periods per year
The periodic rate and number of periods is used for calculations and is shown on time lines.
• If you are comparing the costs of alternative loans that require payments more
than once a year, or the rates of return on investments that pay interest more than
once a year, then the comparisons should be based on effective (or equivalent) rates of
return. Here is the formula:
EAR EFF% 1 IPER M 1 0 1
INOM
M
M
1 0
• The general equation for finding the future value of a current cash flow (PV) for any
number of compounding periods per year is:
FVN PV 1 IPER Number of periods PV 1
INOM
M
MN
where
INOM Nominal quoted interest rate
M Number of compounding periods per year
N Number of years
• An amortized loan is paid off with equal payments over a specified period. An
amortization schedule shows how much of each payment constitutes interest, how
much is used to reduce the principal, and the unpaid balance at the end of each period.
The unpaid balance at Time N must be zero.
• A “growing annuity” is a stream of cash flows that grows at a constant rate for a
specified number of years. The present and future values of growing annuities can be
found with relatively complicated formulas or, more easily, with an Excel model.
• Web Extension 4A explains the tabular approach.
• Web Extension 4B provides derivations of the annuity formulas.
• Web Extension 4C explains continuous compounding.
182 Part 2 Fixed Income Securities
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

## Halaman PDF 220

```text
QUESTIONS
(4-1) Define each of the following terms:
a. PV; I; INT; FVN; PVAN; FVAN; PMT; M; INOM
b. Opportunity cost rate
c. Annuity; lump-sum payment; cash flow; uneven cash flow stream
d. Ordinary (or deferred) annuity; annuity due
e. Perpetuity; consol
f. Outflow; inflow; time line; terminal value
g. Compounding; discounting
h. Annual, semiannual, quarterly, monthly, and daily compounding
i. Effective annual rate (EAR or EFF%); nominal (quoted) interest rate; APR; periodic rate
j. Amortization schedule; principal versus interest component of a payment; amortized
loan
(4-2) What is an opportunity cost rate? How is this rate used in discounted cash flow analysis,
and where is it shown on a time line? Is the opportunity rate a single number that is used
to evaluate all potential investments?
(4-3) An annuity is defined as a series of payments of a fixed amount for a specific number of
periods. Thus, $100 a year for 10 years is an annuity, but $100 in Year 1, $200 in Year 2,
and $400 in Years 3 through 10 does not constitute an annuity. However, the entire series
does contain an annuity. Is this statement true or false?
(4-4) If a firm’s earnings per share grew from $1 to $2 over a 10-year period, the total growth
would be 100%, but the annual growth rate would be less than 10%. True or false? Explain.
(4-5) Would you rather have a savings account that pays 5% interest compounded semiannu￾ally or one that pays 5% interest compounded daily? Explain.
SELF-TEST PROBLEMS Solutions Shown in Appendix A
(ST-1) Assume that 1 year from now you plan to deposit $1,000 in a savings account that pays a
nominal rate of 8%.
a. If the bank compounds interest annually, how much will you have in your account
4 years from now?
b. What would your balance be 4 years from now if the bank used quarterly
compounding rather than annual compounding?
c. Suppose you deposited the $1,000 in 4 payments of $250 each at the end of Years 1,
2, 3, and 4. How much would you have in your account at the end of Year 4, based
on 8% annual compounding?
d. Suppose you deposited 4 equal payments in your account at the end of Years 1, 2, 3,
and 4. Assuming an 8% interest rate, how large would each of your payments have to
be for you to obtain the same ending balance as you calculated in part a?
(ST-2) Assume that 4 years from now you will need $1,000. Your bank compounds interest at an
8% annual rate.
a. How much must you deposit 1 year from now to have a balance of $1,000 at Year 4?
b. If you want to make equal payments at the end of Years 1 through 4 to accumulate
the $1,000, how large must each of the 4 payments be?
Future Value
Time Value of
Money
Chapter 4 Time Value of Money 183
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

## Halaman PDF 221

```text
c. If your father were to offer either to make the payments calculated in part b ($221.92)
or to give you a lump sum of $750 one year from now, which would you choose?
d. If you will have only $750 at the end of Year 1, what interest rate, compounded
annually, would you have to earn to have the necessary $1,000 at Year 4?
e. Suppose you can deposit only $186.29 each at the end of Years 1 through 4, but you
still need $1,000 at the end of Year 4. What interest rate, with annual compounding,
is required to achieve your goal?
f. To help you reach your $1,000 goal, your father offers to give you $400 one year from
now. You will get a part-time job and make 6 additional deposits of equal amounts
each 6 months thereafter. If all of this money is deposited in a bank that pays 8%,
compounded semiannually, how large must each of the 6 deposits be?
g. What is the effective annual rate being paid by the bank in part f?
(ST-3) Bank A pays 8% interest, compounded quarterly, on its money market account. The
managers of Bank B want its money market account’s effective annual rate to equal that of
Bank A, but Bank B will compound interest on a monthly basis. What nominal, or quoted,
rate must Bank B set?
PROBLEMS Answers Are in Appendix B
EASY PROBLEMS 1–8
If you deposit $10,000 in a bank account that pays 10% interest annually, how much will
be in your account after 5 years?
What is the present value of a security that will pay $5,000 in 20 years if securities of equal
risk pay 7% annually?
Your parents will retire in 18 years. They currently have $250,000, and they think they will
need $1 million at retirement. What annual interest rate must they earn to reach their
goal, assuming they don’t save any additional funds?
If you deposit money today in an account that pays 6.5% annual interest, how long will it
take to double your money?
You have $42,180.53 in a brokerage account, and you plan to deposit an additional $5,000 at
the end of every future year until your account totals $250,000. You expect to earn 12%
annually on the account. How many years will it take to reach your goal?
What is the future value of a 7%, 5-year ordinary annuity that pays $300 each year? If this
were an annuity due, what would its future value be?
An investment will pay $100 at the end of each of the next 3 years, $200 at the end
of Year 4, $300 at the end of Year 5, and $500 at the end of Year 6. If other
investments of equal risk earn 8% annually, what is this investment’s present value?
Its future value?
You want to buy a car, and a local bank will lend you $20,000. The loan would be
fully amortized over 5 years (60 months), and the nominal interest rate would be
12% with interest paid monthly. What is the monthly loan payment? What is the loan’s
EFF%?
Effective Annual
Rates
(4-1)
Future Value of a
Single Payment
(4-2)
Present Value of a
Single Payment
(4-3)
Interest Rate on a
Single Payment
(4-4)
Number of Periods of
a Single Payment
(4-5)
Number of Periods
for an Annuity
(4-6)
Future Value: Ordin￾ary Annuity versus
Annuity Due
(4-7)
Present and Future
Value of an Uneven
Cash Flow Stream
(4-8)
Annuity Payment
and EAR
184 Part 2 Fixed Income Securities
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

## Halaman PDF 222

```text
INTERMEDIATE PROBLEMS 9–29
Find the following values, using the equations, and then work the problems using a financial
calculator to check your answers. Disregard rounding differences. (Hint: If you are using a
financial calculator, you can enter the known values and then press the appropriate key to find
the unknown variable. Then, without clearing the TVM register, you can “override” the variable
that changes by simply entering a new value for it and then pressing the key for the unknown
variable to obtain the second answer. This procedure can be used in parts b and d, and in many
other situations, to see how changes in input variables affect the output variable.)
a. An initial $500 compounded for 1 year at 6%
b. An initial $500 compounded for 2 years at 6%
c. The present value of $500 due in 1 year at a discount rate of 6%
d. The present value of $500 due in 2 years at a discount rate of 6%
Use both the TVM equations and a financial calculator to find the following values. See
the Hint for Problem 4-9.
a. An initial $500 compounded for 10 years at 6%
b. An initial $500 compounded for 10 years at 12%
c. The present value of $500 due in 10 years at a 6% discount rate
d. The present value of $500 due in 10 years at a 12% discount rate
To the closest year, how long will it take $200 to double if it is deposited and earns the
following rates? [Notes: (1) See the Hint for Problem 4-9. (2) This problem cannot be
solved exactly with some financial calculators. For example, if you enter PV 200,
PMT 0, FV 400, and I 7 in an HP-12C and then press the N key, you will get
11 years for part a. The correct answer is 10.2448 years, which rounds to 10, but the
calculator rounds up. However, the HP10BII gives the exact answer.]
a. 7%
b. 10%
c. 18%
d. 100%
Find the future value of the following annuities. The first payment in these annuities is made
at the end of Year 1, so they are ordinary annuities. (Notes: See the Hint to Problem 4-9. Also,
note that you can leave values in the TVM register, switch to Begin Mode, press FV, and find
the FV of the annuity due.)
a. $400 per year for 10 years at 10%
b. $200 per year for 5 years at 5%
c. $400 per year for 5 years at 0%
d. Now rework parts a, b, and c assuming that payments are made at the beginning of
each year; that is, they are annuities due.
Find the present value of the following ordinary annuities (see the Notes to Problem 4-12).
a. $400 per year for 10 years at 10%
b. $200 per year for 5 years at 5%
c. $400 per year for 5 years at 0%
d. Now rework parts a, b, and c assuming that payments are made at the beginning of
each year; that is, they are annuities due.
a. Find the present values of the following cash flow streams. The appropriate interest
rate is 8%. (Hint: It is fairly easy to work this problem dealing with the individual
cash flows. However, if you have a financial calculator, read the section of the manual
that describes how to enter cash flows such as the ones in this problem. This will take
(4-9)
Present and Future
Values of Single
Cash Flows for
Different Periods
(4-10)
Present and Future
Values of Single
Cash Flows for
Different Interest
Rates
(4-11)
Time for a Lump
Sum to Double
(4-12)
Future Value of an
Annuity
(4-13)
Present Value of an
Annuity
(4-14)
Uneven Cash Flow
Stream
Chapter 4 Time Value of Money 185
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

## Halaman PDF 223

```text
a little time, but the investment will pay huge dividends throughout the course. Note
that, when working with the calculator’s cash flow register, you must enter CF0 0.
Note also that it is quite easy to work the problem with Excel, using procedures
described in the file Ch04 Tool Kit.xlsx.)
b. What is the value of each cash flow stream at a 0% interest rate?
Find the interest rate (or rates of return) in each of the following situations.
a. You borrow $700 and promise to pay back $749 at the end of 1 year.
b. You lend $700 and receive a promise to be paid $749 at the end of 1 year.
c. You borrow $85,000 and promise to pay back $201,229 at the end of 10 years.
d. You borrow $9,000 and promise to make payments of $2,684.80 at the end of each of
the next 5 years.
Find the amount to which $500 will grow under each of the following conditions.
a. 12% compounded annually for 5 years
b. 12% compounded semiannually for 5 years
c. 12% compounded quarterly for 5 years
d. 12% compounded monthly for 5 years
Find the present value of $500 due in the future under each of the following conditions.
a. 12% nominal rate, semiannual compounding, discounted back 5 years
b. 12% nominal rate, quarterly compounding, discounted back 5 years
c. 12% nominal rate, monthly compounding, discounted back 1 year
Find the future values of the following ordinary annuities.
a. FV of $400 each 6 months for 5 years at a nominal rate of 12%, compounded semiannually
b. FV of $200 each 3 months for 5 years at a nominal rate of 12%, compounded quarterly
c. The annuities described in parts a and b have the same total amount of money paid
into them during the 5-year period, and both earn interest at the same nominal rate,
yet the annuity in part b earns $101.75 more than the one in part a over the 5 years.
Why does this occur?
Universal Bank pays 7% interest, compounded annually, on time deposits. Regional Bank
pays 6% interest, compounded quarterly.
a. Based on effective interest rates, in which bank would you prefer to deposit your money?
b. Could your choice of banks be influenced by the fact that you might want to
withdraw your funds during the year as opposed to at the end of the year? In
answering this question, assume that funds must be left on deposit during an
entire compounding period in order for you to receive any interest.
Consider a $25,000 loan to be repaid in equal installments at the end of each of the next
5 years. The interest rate is 10%.
a. Set up an amortization schedule for the loan.
b. How large must each annual payment be if the loan is for $50,000? Assume that the
interest rate remains at 10% and that the loan is still paid off over 5 years.
Year Cash Stream A Cash Stream B
1 $100 $300
2 400 400
3 400 400
4 400 400
5 300 100
(4-15)
Effective Rate of
Interest
(4-16)
Future Value
for Various
Compounding
Periods
(4-17)
Present Value
for Various
Compounding
Periods
(4-18)
Future Value of an
Annuity for Various
Compounding
Periods
(4-19)
Effective versus
Nominal Interest
Rates
(4-20)
Amortization
Schedule
186 Part 2 Fixed Income Securities
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

## Halaman PDF 224

```text
c. How large must each payment be if the loan is for $50,000, the interest rate is 10%,
and the loan is paid off in equal installments at the end of each of the next 10 years?
This loan is for the same amount as the loan in part b, but the payments are spread
out over twice as many periods. Why are these payments not half as large as the
payments on the loan in part b?
Sales for Hanebury Corporation’s just-ended year were $12 million. Sales were $6 million
5 years earlier.
a. At what rate did sales grow?
b. Suppose someone calculated the sales growth for Hanebury in part a as follows:
“Sales doubled in 5 years. This represents a growth of 100% in 5 years; dividing 100%
by 5 results in an estimated growth rate of 20% per year.” Explain what is wrong with
this calculation.
Washington-Pacific (W-P) invested $4 million to buy a tract of land and plant some
young pine trees. The trees can be harvested in 10 years, at which time W-P plans to
sell the forest at an expected price of $8 million. What is W-P’s expected rate of
return?
A mortgage company offers to lend you $85,000; the loan calls for payments of $8,273.59
at the end of each year for 30 years. What interest rate is the mortgage company charging
you?
To complete your last year in business school and then go through law school, you will
need $10,000 per year for 4 years, starting next year (that is, you will need to withdraw the
first $10,000 one year from today). Your uncle offers to put you through school, and he
will deposit in a bank paying 7% interest a sum of money that is sufficient to provide the
four payments of $10,000 each. His deposit will be made today.
a. How large must the deposit be?
b. How much will be in the account immediately after you make the first withdrawal?
After the last withdrawal?
While Mary Corens was a student at the University of Tennessee, she borrowed $12,000
in student loans at an annual interest rate of 9%. If Mary repays $1,500 per year, then how
long (to the nearest year) will it take her to repay the loan?
You need to accumulate $10,000. To do so, you plan to make deposits of $1,250 per year—
with the first payment being made a year from today—into a bank account that pays 12%
annual interest. Your last deposit will be less than $1,250 if less is needed to round out to
$10,000. How many years will it take you to reach your $10,000 goal, and how large will the
last deposit be?
What is the present value of a perpetuity of $100 per year if the appropriate discount rate
is 7%? If interest rates in general were to double and the appropriate discount rate rose to
14%, what would happen to the present value of the perpetuity?
Assume that you inherited some money. A friend of yours is working as an unpaid intern at a
local brokerage firm, and her boss is selling securities that call for 4 payments of $50 (1 payment
at the end of each of the next 4 years) plus an extra payment of $1,000 at the end of Year 4. Your
friend says she can get you some of these securities at a cost of $900 each. Your money is now
invested in a bank that pays an 8% nominal (quoted) interest rate but with quarterly
compounding. You regard the securities as being just as safe, and as liquid, as your bank
deposit, so your required effective annual rate of return on the securities is the same as that on
your bank deposit. You must calculate the value of the securities to decide whether they are a
good investment. What is their present value to you?
(4-21)
Growth Rates
(4-22)
Expected Rate of
Return
(4-23)
Effective Rate of
Interest
(4-24)
Required Lump-Sum
Payment
(4-25)
Repaying a Loan
(4-26)
Reaching a Financial
Goal
(4-27)
Present Value of a
Perpetuity
(4-28)
PV and Effective
Annual Rate
Chapter 4 Time Value of Money 187
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

## Halaman PDF 225

```text
Assume that your aunt sold her house on December 31, and to help close the sale she took a
second mortgage in the amount of $10,000 as part of the payment. The mortgage has a
quoted (or nominal) interest rate of 10%; it calls for payments every 6 months, beginning on
June 30, and is to be amortized over 10 years. Now, 1 year later, your aunt must inform the
IRS and the person who bought the house about the interest that was included in the two
payments made during the year. (This interest will be income to your aunt and a deduction to
the buyer of the house.) To the closest dollar, what is the total amount of interest that was
paid during the first year?
CHALLENGING PROBLEMS 30–34
Your company is planning to borrow $1 million on a 5-year, 15%, annual payment, fully
amortized term loan. What fraction of the payment made at the end of the second year
will represent repayment of principal?
It is now January 1. You plan to make a total of 5 deposits of $100 each, one every 6 months,
with the first payment being made today. The bank pays a nominal interest rate of 12% but
uses semiannual compounding. You plan to leave the money in the bank for 10 years.
a. How much will be in your account after 10 years?
b. You must make a payment of $1,432.02 in 10 years. To get the money for this
payment, you will make five equal deposits, beginning today and for the following
4 quarters, in a bank that pays a nominal interest rate of 12% with quarterly
compounding. How large must each of the five payments be?
Anne Lockwood, manager of Oaks Mall Jewelry, wants to sell on credit, giving customers
3 months to pay. However, Anne will have to borrow from her bank to carry the accounts
receivable. The bank will charge a nominal rate of 15% and will compound monthly.
Anne wants to quote a nominal rate to her customers (all of whom are expected to pay on
time) that will exactly offset her financing costs. What nominal annual rate should she
quote to her credit customers?
Assume that your father is now 50 years old, plans to retire in 10 years, and expects to live for
25 years after he retires—that is, until age 85. He wants his first retirement payment to have
the same purchasing power at the time he retires as $40,000 has today. He wants all of his
subsequent retirement payments to be equal to his first retirement payment. (Do not let the
retirement payments grow with inflation: Your father realizes that if inflation occurs the real
value of his retirement income will decline year by year after he retires.) His retirement
income will begin the day he retires, 10 years from today, and he will then receive 24
additional annual payments. Inflation is expected to be 5% per year from today forward. He
currently has $100,000 saved and expects to earn a return on his savings of 8% per year with
annual compounding. To the nearest dollar, how much must he save during each of the next
10 years (with equal deposits being made at the end of each year, beginning a year from
today) to meet his retirement goal? (Note: Neither the amount he saves nor the amount he
withdraws upon retirement is a growing annuity.)
You want to accumulate $1 million by your retirement date, which is 25 years from
now. You will make 25 deposits in your bank, with the first occurring today. The
bank pays 8% interest, compounded annually. You expect to receive annual raises of
3%, which will offset inflation, and you will let the amount you deposit each year also
grow by 3% (i.e., your second deposit will be 3% greater than your first, the third will
be 3% greater than the second, etc.). How much must your first deposit be if you are
to meet your goal?
(4-29)
Loan Amortization
(4-30)
Loan Amortization
(4-31)
Nonannual
Compounding
(4-32)
Nominal Rate of
Return
(4-33)
Required Annuity
Payments
(4-34)
Growing Annuity
Payments
188 Part 2 Fixed Income Securities
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

## Halaman PDF 226

```text
SPREADSHEET PROBLEM
(4-35) Start with the partial model in the file Ch04 P35 Build a Model.xlsx from the textbook’s
Web site. Answer the following questions, using the spreadsheet model to do the
calculations.
a. Find the FV of $1,000 invested to earn 10% annually 5 years from now. Answer this
question first by using a math formula and then by using the Excel function wizard.
b. Now create a table that shows the FV at 0%, 5%, and 20% for 0, 1, 2, 3, 4, and 5 years.
Then create a graph with years on the horizontal axis and FV on the vertical axis to
display your results.
c. Find the PV of $1,000 due in 5 years if the discount rate is 10% per year. Again, first
work the problem with a formula and then by using the function wizard.
d. A security has a cost of $1,000 and will return $2,000 after 5 years. What rate of
return does the security provide?
e. Suppose California’s population is 30 million people and its population is expected to
grow by 2% per year. How long would it take for the population to double?
f. Find the PV of an ordinary annuity that pays $1,000 at the end of each of the next 5
years if the interest rate is 15%. Then find the FV of that same annuity.
g. How would the PV and FV of the above annuity change if it were an annuity due
rather than an ordinary annuity?
h. What would the FV and PV for parts a and c be if the interest rate were 10% with
semiannual compounding rather than 10% with annual compounding?
i. Find the PV and FV of an investment that makes the following end-of-year
payments. The interest rate is 8%.
j. Suppose you bought a house and took out a mortgage for $50,000. The interest rate is
8%, and you must amortize the loan over 10 years with equal end-of-year payments.
Set up an amortization schedule that shows the annual payments and the amount of
each payment that repays the principal and the amount that constitutes interest
expense to the borrower and interest income to the lender.
(1) Create a graph that shows how the payments are divided between interest and
principal repayment over time.
(2) Suppose the loan called for 10 years of monthly payments, 120 payments in all,
with the same original amount and the same nominal interest rate. What would
the amortization schedule show now?
MINI CASE
Assume that you are nearing graduation and have applied for a job with a local bank. The
bank’s evaluation process requires you to take an examination that covers several financial
analysis techniques. The first section of the test addresses discounted cash flow analysis. See
how you would do by answering the following questions.
Build a Model: The
Time Value of
Money
Year Payment
1 $100
2 200
3 400
resource
Chapter 4 Time Value of Money 189
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

## Halaman PDF 227

```text
a. Draw time lines for: (1) a $100 lump sum cash flow at the end of Year 2, (2) an
ordinary annuity of $100 per year for 3 years, and (3) an uneven cash flow stream of
−$50, $100, $75, and $50 at the end of Years 0 through 3.
b. (1) What’s the future value of an initial $100 after 3 years if it is invested in an account
paying 10% annual interest?
(2) What’s the present value of $100 to be received in 3 years if the appropriate interest
rate is 10%?
c. We sometimes need to find out how long it will take a sum of money (or something
else, such as earnings, population, or prices) to grow to some specified amount. For
example, if a company’s sales are growing at a rate of 20% per year, how long will it
take sales to double?
d. If you want an investment to double in 3 years, what interest rate must it earn?
e. What’s the difference between an ordinary annuity and an annuity due? What type of annuity
is shown below? How would you change the time line to show the other type of annuity?
100 100 100
0123
f. (1) What’s the future value of a 3-year ordinary annuity of $100 if the appropriate
interest rate is 10%?
(2) What’s the present value of the annuity?
(3) What would the future and present values be if the annuity were an annuity due?
g. What is the present value of the following uneven cash flow stream? The appropriate
interest rate is 10%, compounded annually.
01234
0 100 300 300 –50
h. (1) Define the stated (quoted) or nominal rate INOM as well as the periodic rate IPER.
(2) Will the future value be larger or smaller if we compound an initial amount more
often than annually—for example, every 6 months, or semiannually—holding the
stated interest rate constant? Why?
(3) What is the future value of $100 after 5 years under 12% annual compounding?
Semiannual compounding? Quarterly compounding? Monthly compounding?
Daily compounding?
(4) What is the effective annual rate (EAR or EFF%)? What is the EFF% for a nominal
rate of 12%, compounded semiannually? Compounded quarterly? Compounded
monthly? Compounded daily?
i. Will the effective annual rate ever be equal to the nominal (quoted) rate?
j. (1) Construct an amortization schedule for a $1,000, 10% annual rate loan with three
equal installments.
(2) During Year 2, what is the annual interest expense for the borrower, and what is
the annual interest income for the lender?
k. Suppose that on January 1 you deposit $100 in an account that pays a nominal (or
quoted) interest rate of 11.33463%, with interest added (compounded) daily. How
much will you have in your account on October 1, or 9 months later?
190 Part 2 Fixed Income Securities
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

## Halaman PDF 228

```text
l. (1) What is the value at the end of Year 3 of the following cash flow stream if the
quoted interest rate is 10%, compounded semiannually?
100 100 100
0123 Years
(2) What is the PV of the same stream?
(3) Is the stream an annuity?
(4) An important rule is that you should never show a nominal rate on a time line or
use it in calculations unless what condition holds? (Hint: Think of annual
compounding, when INOM EFF% IPER.) What would be wrong with your
answers to parts (1) and (2) if you used the nominal rate of 10% rather than
the periodic rate, INOM 2 10% 2 5%?
m. Suppose someone offered to sell you a note calling for the payment of $1,000 in
15 months. They offer to sell it to you for $850. You have $850 in a bank time deposit
that pays a 6.76649% nominal rate with daily compounding, which is a 7% effective
annual interest rate, and you plan to leave the money in the bank unless you buy the
note. The note is not risky—you are sure it will be paid on schedule. Should you buy
the note? Check the decision in three ways: (1) by comparing your future value if you
buy the note versus leaving your money in the bank; (2) by comparing the PV of the
note with your current bank account; and (3) by comparing the EFF% on the note
with that of the bank account.
Chapter 4 Time Value of Money 191
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

## Halaman PDF 229

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

