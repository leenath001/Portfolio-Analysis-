def equity_data(ticker,period):
    
    import yfinance as yf
    import numpy as np
    import datetime

    today = datetime.date.today()
    specified_date = np.busday_offset(today,-period,roll = 'backward')
    today_str = str(today)
    specdate_str = str(specified_date)

    historical_data = yf.download(ticker,specdate_str,today_str)  # data for the last year
    return historical_data

def equity_bidask(ticker):

    import yfinance as yf

    equity = yf.Ticker(ticker)
    bid = equity.info['bid']
    ask = equity.info['ask']

    ba = 'Bid : {}, Ask : {}'.format(bid,ask)

    return ba, bid, ask

