import Analysis_funcs
import MC_funcs
import matplotlib.pyplot as plt
import seaborn

iter = 1000
days = 5
paths = 5000

x = Analysis_funcs.portfolio_analysis(iter,days,paths,["NVDA", "AAPL"],[25,50])
port = x[0]
initsum = x[1]
print(x[2])
print(x[3])
print(x[4])

MC_funcs.prob_tool(1,initsum+10,port,paths)

plt.figure()
plt.hist(port,bins = 60, density = True)
seaborn.kdeplot(port)
plt.axvline(x = initsum, c = 'lime')
plt.xlabel('Price')
plt.ylabel('Density')
plt.axvline(x = 85, color = 'red')
plt.title('Price Distribution')
plt.show()

