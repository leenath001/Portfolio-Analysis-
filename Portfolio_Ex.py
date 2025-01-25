import MC_funcs
import matplotlib.pyplot as plt
import seaborn

def form_p(num):
    return f"{num:.2%}"
    
def form_b(num):
    return f"{num:.2f}"

iter = 500
days = 200
paths = 10000
AAPLalo = 400
MSFTalo = 200
NVDAalo = 300

AAPL = MC_funcs.asset_sim(iter,days,AAPLalo,paths,"Data/AAPL.xlsx")
MSFT = MC_funcs.asset_sim(iter,days,MSFTalo,paths,"Data/MSFT.xlsx")
NVDA = MC_funcs.asset_sim(iter,days,NVDAalo,paths,"Data/NVDA.xlsx")

AAPLp = [form_p(AAPL[1]),form_p(AAPL[2])]
MSFTp = [form_p(MSFT[1]),form_p(MSFT[2])]
NVDAp = [form_p(NVDA[1]),form_p(NVDA[2])]

print('AAPL params = ', AAPLp) 
print('MSFT params = ', MSFTp)
print('NVDA params = ', NVDAp)  

port = AAPL[0] + MSFT[0] + NVDA[0]
mean = sum(port)/paths

print('Mean = ', form_b(mean))

plt.figure()
plt.hist(port,bins = 60, density = True)
seaborn.kdeplot(port)
plt.xlabel('Price')
plt.ylabel('Density')
plt.title('Log-Norm Dist of Prices')
plt.show()
