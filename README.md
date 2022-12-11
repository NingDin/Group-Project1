# Group-Project1
## Project Introduction
In this project, we are curious in several stock market related topics. While our main focus is to identify any potential correlations between tweets from major hedge fund managers and the stock market fluctuations, we are also interested to uncover any major correlation between the US and Canadian Stock Market.  We are looking to gather data through different channels and answer the questions by running sentiment analysis on the data. 

## Reaserch Questions to Answer
Is the US stock market and stock markets in other parts of the world correlated?
How do US hedgefundmanagers predict/correlate (using sentiment analysis) to the canadian or us market? What is the correlations between the tweets and the market? 
Do possitive or negative tweets have a greater correlation with the market?

## Team Members and Task Division
Scrum: Ning Ding
API: David John Chartrand
Data manipulation: Ning Ding
Visulization: David Haiming Wang

## Dataset to be used
Twitter API
Yahoo finance (Yfinance)

## Project Flow: 

## Part I: Data Sourcing, Gathering and Preparation:

## Stock Data
Ning located Yfinance from Github which allowed him to download stock prices for any given ticker from Yahoo Finance. Ning defined several functions to help narrow down the data by time frame, he also cleaned the data by dropping irrelevent values and columns and only keeping the stock prices. Ning retrieved the stock prices for two indexes: SPY (represents the US Stock Market) and ACWX (used to represent the other stock markets in the world). Ning created a column and using simple column manipulations to calculated the return of both stocks for each day.

## Twitter Analysis & API
David began the project ny narrowing down the accounts we looked at by looking at the accounts that Ning was following. David then created a DataFrame that incompassed these users ID, Username, and Name. I them created a random sample of the users and collected their twitter timeline from the last years. Then Ning create a script to use HuggingFace sentiment analysis to evaluate where the tweets were positive or negative to see if there was a correlation between the tweet sentiment and the S&P 500 stock price. 

## Part II: Data Manupulation and Creating Visualization

## SPY vs ACWX
In order to compare the relationship between the return of SPY and ACWX, Haiming merged previous created data frames from SPY and ACWX, also created line chart to show the return of both stocks over the years. Also created Scatter plot and used linear regression to discover the correlation between the two stock indexes. The result shows although over all the US Market has higher return on average (might also because the world market index ACWX was only incepted in 2008), the two markets has a strong positive correlation based on these two indexes, we obtained a pearson correlation coefficient of 0.80.

## SPY vs Twitter Sentiment Analysis Result:
Using David's results from the sentiment analysis, Haiming merged the analysis result (data frame) with the SPY return, he used hvplot to created a line chart showing the trends of both the sentiment score and the SPY return during the same time period. He also created a scatter plot and generated a linear regression showing very weak correlation between the two with a pearson coefficient of 0.02 only. Another factor to consider when looking at the result is the small sample size of the tweets we used to test the hypothesis


## Some Observations and Questions After looking at SPY
1. SPY daily return is not normalize distributed
2. SPY has fatter tail and negative skewed. which means negative out come thend to become more frequent and larger then a normal distribution applied
3. The daily up & down occurance tend to become 50/50 and evenly distributed. A 3 days consective positive return is rare; (based on 1993 data) a 6 days consecutive positive return is extremly rare: 98.08% consecutive upday below or equal 6 days. 

Questions based on these observations: Does each day's return has its independ probability? Does a 6-day consecutive return alwasys signals a immediate reversal? What about overlaping factors on 5 or 4 days? Since the occurance is less rare and comparable meanningful as well.

4. The rolling 5 days ATR suggest the true range of daily high-low is 1.616% compare rolling 50-years historical realize vol at 1.314% daily. The stock is at high vol regime; Maybe consider to work on setting risk management tight/adjust expectation based on current/forecast(catalyst) vol enviorment.
5.SPY vs rest of word:
SPY- us 500 major stock index
ACWX-ex US etf. reference at: factsheet: https://www.ishares.com/us/literature/fact-sheet/acwx-ishares-msci-acwi-ex-u-s-etf-fund-fact-sheet-en-us.pdf
General take away: SPY tend to outperform ACWX in majority of times; more effcient risk adjust return investment comapre to ACWX. To support claim base on following metrix: CAGR% spy 9.67% vs 0.86% Sharp 0.54 vs 0.13 combine with Sortino for downside SPY 0.83 VS ACWX0.24; Pearson correlation coefficient between SPY and ACWX is 0.80, showing a strong positive correlation.

  

