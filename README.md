# Portfolio-Analysis-
Simulates portfolio performance using historical data and Geometric Brownian Motion (GBM) assumption. See functest.py for example of use case

Suppose that you have a portfolio consisting of AAPL, NVDA, GOOG, and META with 200 allocated to each, and you'd like to estimate your expected return for the week. This tool uses the GBM assumption and runs MC simulations to present the user with a distribution of returns.

(1) Master_Data_Entry.xlsx
*  To ensure accurate security simulation, we use historical data to glean estimates for return and volatility. Use https://www.nasdaq.com/market-activity/quotes/historical for data entry. Ensure time period is 1y. Sheet is formatted such that you can copy/paste data directly from download to sheet. Check last row to ensure data is correct. You may have to remove the last row. 
*  Columns MUST be named 'dS/S' and 'ln(H/L)' for script to work. Columns highlighted red indicate do not touch - sheet automatically performs calculations to be read by script. 

(2) Utilization of tool
*  Load Analysis_funcs and MC_funcs to your sheet. To ensure our excel shet reader works, load .xlsx files into a folder named Data. I reccomend creating a seperate folder [1] altogether for this tool, and then creating another folder within [1] titled Data. The .xlsx reader reads sheets within Data\[ticker] (for instance, references 'Data\NVDA')
*  Specify the number of discretizations (iter), length of time period (days), and number of MC simulations (paths). Also, specify the tickers and allocations to each
*  Sheets should ideally be named the ticker, and allocations should be indexed in the same place as tickers (for instance, tickers = ["AAPL","NVDA","GOOG","META"], alo = [200,200,200,200])

(3) Load parameters into Analysis_funcs.portfolio_analysis(iter,days,paths,tickers,alo)
*  The tool automatically takes the parameters specified in (2) and runs our simulation. There are 6 outputs, which will be specified below. 
*  [0] : The simulated portfolio of all stocks. Returns a (1 x paths) array of all possible portfolio values after specified time period.
*  [1] : Initial sum of portfolio before simulation. (sum(alo))
*  [2] : Minimum and maximum values of portfolio after simulation
*  [3] : Initial/Average value of portfolio. Takes expected value of [0].
*  [4] : Average growth using [3]
*  [5] : Value At Risk using 95% confidence

(4) More functionality in MC_funcs.prob_tool(type,K,prices,paths):
*  This tool gives you the probability that your portfolio ends above a specified price level. 
*  Type : 1 -> Prob[portfolio > K], 2 -> Prob[portfolio < K]
*  K : The specified price level
*  prices : the portfolio given by [0]
*  paths : the number of MC simulations run. 

Use histogram plotting tools to visualize portolio returns! Over short periods of time, density appears normal. Over longer periods, density represents log-normal behavior. 
*  Note that this model does not account for jumps, new information, etc... Using model over for extended periods of time is not reccomended and can provide inaccurate data.  
  
functest.py
*  Example using (3) to simulate movements of AAPL, NVDA, GOOG, META over 5 days. Portfolio allocates 200 to each. 
