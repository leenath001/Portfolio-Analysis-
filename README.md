# Portfolio-Analysis-
Simulates portfolio performance using historical data and Geometric Brownian Motion (GBM) assumption. See functest.py for example of use case

Master_Data_Entry.xlsx
*  Use https://www.nasdaq.com/market-activity/quotes/historical for data entry. Ensure time period is 1y. Sheet is formatted such that you can copy/paste data directly from download to sheet. Check last row to ensure data is correct. 
*  Columns MUST be named 'dS/S' and 'ln(H/L)' for script to work. Columns highlighted red indicate do not touch.

(1) Param_Est.Param_Est(sheet)
*  File takes excel sheet as input and returns estimated drift (mu) and volatility (sig). Uses Parkinson volatility Estimator

(2) MC_funcs.asset_sim(iter,days,allocation,paths,sheet)
*  File uses GBM to run (paths) monte-carlo simulations over specified days. See Output
*  iter : No. of GBM iterations wanted through specified time period.
*  days : No. of days.
*  allocation : Amt. ($) allocated to specific asset
*  paths : No. of simulations wanted. Reccomended 10000+ for accuracy

Output: 
*    asset_sim[0] : array (size = paths) of possible prices for asset
*    asset_sim[1] : estimated drift (mu)
*    asset_sim[2] : estimated vol (sig)
  
(3) MC_funcs.prob_tool(type,K,prices,paths)
*  type : 1 indicates prices > K, 2 indicates prices < K
*  K : specific price wanted to analyze
*  prices : set this to asset_sim[0]
*  paths : same as above.
*  Upon calling (3), output prints automatically

(4) Analysis_funcs.portfolio_analysis(iter,days,paths,tickers,alo): 
* same variables as above except for:
* tickers : insert tickers verbatim in an array. Ex. ["NVDA"]. Datafile should be named ticker to ensure proper use of (1)
* alo : allocations to each stock. Ex. [50]

Output: 
*    portfolio_analysis[0] : array of possible prices for portfolio, takes allocations into account
*    portfolio_analysis[1] : initial value of portfolio before simulation
*    portfolio_analysis[2] : min/max of potential prices
*    portfolio_analysis[3] : average value of simulation
*    portfolio_analysis[4] : growth % (based on average)
  
functest.py
*  Example using (4) to simulate movements of AAPL, NVDA over 5 days
