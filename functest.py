import Analysis_funcs
import MC_funcs
import matplotlib.pyplot as plt
import seaborn

iter = 500
days = 30
paths = 50000

tick = ["VOO","TSPA"]
alo = [250,400]

x = Analysis_funcs.portfolio_analysis(iter,days,paths,tick,alo)
port = x[0]
initsum = x[1]
print()
print(x[2])
print()
print(x[3])
print()
print(x[4])
print()
print(x[5])
print()

MC_funcs.prob_tool(1,5000,port,paths)

plt.figure()
plt.hist(port,bins = 60, density = True)
seaborn.kdeplot(port)
plt.axvline(x = initsum, c = 'lime')
plt.xlabel('Price')
plt.ylabel('Density')
#plt.axvline(x = 85, color = 'red')
plt.title('Price Distribution')
plt.show()

