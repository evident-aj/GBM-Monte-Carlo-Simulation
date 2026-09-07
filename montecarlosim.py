import math

import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

while True:
    user_input = input("What stock would you like to analyze (e.g., AAPL): ")
    ticker_symbol = user_input.strip().upper()
    user_days = input("How many days would you like to simulate?: ")
    stock = yf.Ticker(ticker_symbol)
    info = stock.info
    name = info.get("longName", "N/A")
    past = stock.history(period="750d")['Close']
    if past.empty:
        print("No price data found for this ticker symbol.")
        continue
    try:
        days = int(user_days)
        if days <= 0:
            print("Please enter a positive number of trading days.")
            continue
        break
    except ValueError:
        print("Invalid number of days.")
        continue
    

pct_change_res = past.pct_change()
log_returns = np.log(1 + pct_change_res)

mean_daily_return = log_returns.mean()
daily_vol = log_returns.std()
current_price = past.iloc[-1]


def SimulateStock():
    prices = [current_price]
    for i in range(days):
        shock = daily_vol * np.random.normal()
        next_price = prices[-1] * math.exp(mean_daily_return + shock)
        prices.append(next_price)
    return prices


all_paths = []
all_prices = []
for i in range(1000):
    path = SimulateStock()
    all_paths.append(path)
    all_prices.append(path[-1])

cmp = plt.get_cmap('plasma')
color_norm = clr.Normalize(min(all_prices),max(all_prices))
plt.style.use('dark_background')

ax_paths = plt.subplot(1, 2, 1)
for path in all_paths:
    color = cmp(color_norm(path[-1]))
    plt.plot(path, color=color, alpha=0.3)
plt.xlabel("Trading Days")
plt.ylabel("Stock Price $")


plt.subplot(1, 2, 2, sharey=ax_paths)
counts, bin_edges, bars = plt.hist(all_prices, orientation='horizontal')
for i in range(len(bars)):
    midpoint = (bin_edges[i] + bin_edges[i + 1])/2
    bars[i].set_facecolor(cmp(color_norm(midpoint)))
plt.xlabel("Frequency") 

var_95 = current_price - np.percentile(all_prices, 5)

plt.suptitle(f"GBM Monte Carlo Simulation\n"f"Stock: {name}\n"f"95% VaR per share ({days} trading days): ${var_95:.2f}")

plt.tight_layout()
plt.show()






