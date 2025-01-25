import MC_funcs
import matplotlib.pyplot as plt
import seaborn
import numpy

# number formatting
def form_p(num):
    return f"{num:.2%}"
def form_b(num):
    return f"{num:.2f}"

# parameters and asset allocation
iter = 1000
days = 100
paths = 50000
AAPLalo = 250
MSFTalo = 500
NVDAalo = 130
initsum = AAPLalo + MSFTalo + NVDAalo

# turning on price level analysis (0 : off, 1 : > strike, 2 < strike)
type = 1
strike = 1000

# running simulations and loading data
AAPL = MC_funcs.asset_sim(iter,days,AAPLalo,paths,"Data/AAPL.xlsx")
MSFT = MC_funcs.asset_sim(iter,days,MSFTalo,paths,"Data/MSFT.xlsx")
NVDA = MC_funcs.asset_sim(iter,days,NVDAalo,paths,"Data/NVDA.xlsx")

# calling parameters [drift, volatility]
AAPLp = [form_p(AAPL[1]),form_p(AAPL[2])]
MSFTp = [form_p(MSFT[1]),form_p(MSFT[2])]
NVDAp = [form_p(NVDA[1]),form_p(NVDA[2])]

print('AAPL params = ', AAPLp) 
print('MSFT params = ', MSFTp)
print('NVDA params = ', NVDAp)   
print()

# analysis and charts
port = AAPL[0] + MSFT[0] + NVDA[0]
min = form_b(min(port))
max = form_b(max(port))
mean = sum(port)/paths
pgrowth = form_p(abs(initsum - mean)/mean)

print('Minimum of', min, ', Maximum of', max)
print('Initial Value: $',initsum)
print('Average Value: $',form_b(mean))
print('Growth: ',pgrowth)
print()

# P[portfolio > or < strike]
count = 0
sum = 0

if type == 0:
    pass
elif type == 1:
    for p in port:
        if p >= strike:
            count += 1
    prob = count/paths
    print(f"{prob:.2%}", "trade is ITM.") 
elif type == 2:
    for p in port:
        if p <= strike:
            count += 1
    prob = count/paths
    print(f"{prob:.2%}", "trade is ITM.")

plt.figure()
plt.hist(port,bins = 60, density = True)
seaborn.kdeplot(port)
plt.axvline(x = initsum, c = 'lime')
plt.xlabel('Price')
plt.ylabel('Density')
if type == 0:
    pass
else:
    plt.axvline(x = strike, color = 'red')
plt.title('Log-Norm Dist of Prices')
plt.show()


