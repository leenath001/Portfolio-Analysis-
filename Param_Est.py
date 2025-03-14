def Param_Est(ticker,start,end):

    import Data_Funcs as df
    import pandas as pd
    import numpy as np

    # mu 
    data = df.equity_data(ticker,start,end)
    close = data.loc[:,'Close']
    close = np.array([close])
    dS = np.diff(close,axis =1)
    extra = 0
    dS = np.append(dS,0)
    dS = dS[:,np.newaxis]
    x = dS/close
    mu = np.sum(x)

    # vol 
    H = data.loc[:,'High']
    L = data.loc[:,'Low']
    HLvec = np.log(H/L)**2
    volsum = np.sum(HLvec)
    volsumaj = np.array(volsum)
    volsumaj = volsumaj[0]
    denom = 4*len(HLvec)*np.log(2)
    v = volsumaj/denom
    vol = np.sqrt(v/len(HLvec))

    return mu, vol
