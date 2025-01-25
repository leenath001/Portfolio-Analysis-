# Portfolio-Analysis-
Simulates portfolio performance using historical data and Geometric Brownian Motion assumption

(1) Param_Est.Param_Est(sheet)
*  File takes excel sheet as input and returns estimated drift (mu) and volatility (sig). Uses Parkinson volatility Estimator
*  Columns MUST be named 'dS/S' and 'ln(H/L)' for script to work

(2) MC_funcs.asset_sim(iter,days,allocation,paths,sheet)
*  iter : No. of GBM iterations wanted through specified time period.
*  days : No. of days.
*  allocation : Amt. ($) allocated to specific asset
*  paths : No. of simulations wanted. Reccomended 5000+

Output: 
*  asset_sim[0] : array (size = paths) of possible prices for asset
*  asset_sim[1] : estimated drift (mu)
*  asset_sim[2] : estimated vol (sig)

Portfolio_Ex:
*  Example using (2) to simulate movements of AAPL, MSFT, NVDA over 200 days
*  Script gives average portfolio price and plots potential returns
