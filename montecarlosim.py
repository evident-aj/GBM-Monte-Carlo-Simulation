import yfinance as yf
import math as math
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.colors as clr 


while True:
    user_input = input("What stock would you like to analyze (e.g., AAPL): ")
    ticker_symbol = user_input.strip().upper()
    stock = yf.Ticker(ticker_symbol)
    info = stock.info
    name = info.get("longName", "N/A")
    past = stock.history(period="750d")['Close']
    if past.empty:
        print("No price data found for this ticker symbol.")
        continue
    else:
        break

pct_change_res = past.pct_change()
log_returns = np.log(1 + pct_change_res)

mean_daily_return = log_returns.mean()
daily_vol = log_returns.std()
dt = 1/750
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
    path = SimulateStock()
    all_paths.append(path)
    all_prices.append(path[-1])

cmp = plt.get_cmap('plasma')
color_norm = clr.Normalize(min(all_prices),max(all_prices))

plt.subplot(1, 2, 1)
for path in all_paths:
    color = cmp(color_norm(path[-1]))
    plt.plot(path, color=color, alpha=0.3)
plt.xlabel("Days")
plt.ylabel("Stock Price $")


plt.subplot(1, 2, 2)
counts, bin_edges, bars = plt.hist(all_prices, orientation='horizontal')
for i in range(len(bars)):
    midpoint = (bin_edges[i] + bin_edges[i + 1])/2
    bars[i].set_facecolor(cmp(color_norm(midpoint)))
plt.xlabel("Frequency") 

VaR = round(np.percentile(all_prices, 5), 2)

plt.suptitle(f"GBM Monte Carlo Simulation\nStock: {name}\nVaR: ${VaR}")


plt.tight_layout()
plt.show()






