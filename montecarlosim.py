import yfinance as yf
import math as math
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.colors as clr 


while True:
    user_input = input("What stock would you like to analyze (e.g., AAPL): ")
    ticker_symbol = user_input.strip().upper()
    stock = yf.Ticker(ticker_symbol)
    past = stock.history(period="5y")['Close']
    if past.empty:
        print("No price data found for this ticker symbol.")
        continue
    else:
        break

pct_change_res = past.pct_change()
log_returns = np.log(1 + pct_change_res)

mean_daily_return = log_returns.mean()
daily_vol = log_returns.std()
dt = 1/252
current_price = past.iloc[-1]


def SimulateStock():
    drift = ((mean_daily_return - (daily_vol**2)/2) * dt)
    prices = [current_price]
    for i in range(1, 252 + 1):
        shock = daily_vol * np.random.normal() * math.sqrt(1/252)
        prices.append(prices[-1] * math.exp(drift + shock))
    return prices

all_paths = []
all_prices = []
for i in range(1000):
    all_paths.append(SimulateStock())
    all_prices.append(float(SimulateStock()[-1]))








