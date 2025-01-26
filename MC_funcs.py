def asset_sim(iter,days,S0,paths,sheet):

    import pandas
    import numpy
    import matplotlib.pyplot as plt
    import math as m
    import random
    import seaborn
    import Param_Est

#########################

# input data into sheet, use function to estimate parameters
    params = Param_Est.Param_Est(sheet)

    mu = params[0]
    sig = params[1]

#########################

# 1 - PATH SIMULATION OF UNDERLYING (NORMAL SHOCKS, LOGN PRICES)

# estimation parameters, SPY(u .106 v .181)
    time = days/252
    dt = time/iter
    array = numpy.ones((paths, iter))
    array2 = numpy.ones((paths, iter))

# iterates through array and changes each entry (by iteration then path)
    for rowind, row in enumerate(array):
        for colind, entry in enumerate(row[1:iter+1]):
            entry = 1 + (mu * dt + sig * m.sqrt(dt) * numpy.random.randn())
            array[rowind,colind+1] = entry
            entry = array[rowind,colind+1]
            entry *= array2[rowind,colind]
            array2[rowind,colind+1] = entry

# prices from last iteration of each path, along with random sampling of shocks
    prices = S0 * array2[:,iter-1]
    randint = random.randint(0,iter)
    shocks = array[:,randint]

# price range
    evtot = (1/paths)*sum(prices)
    
    return prices, mu, sig

def prob_tool(type,K,prices,paths):
    
    count = 0
    sum = 0
    
    if type == 1:
        for p in prices:
            if p >= K:
                count += 1
        prob = count/paths
        return print(f"{prob:.2%}", "trade is ITM.") 
    elif type == 2:
        for p in prices:
            if p <= K:
                count += 1
        prob = count/paths
        return print(f"{prob:.2%}", "trade is ITM.")
        
def FI_sim(aloc,rate,days,paths):
    
    import numpy
    
    y = (aloc * (1 + rate)**(days/252))*numpy.ones(paths)
    
    return y