# GBM-Monte-Carlo-Simulation

A stock price simulator built on Geometric Brownian Motion. Takes any ticker and a custom time frame, pulls historical data, and simulates 1000 possible future price paths. Color coded by final price, with a matching orientation-aligned histogram and 95% Value at Risk calculated.

<img width="1312" height="479" alt="Screenshot 2026-09-07 at 5 24 25 PM" src="https://github.com/user-attachments/assets/0dbaaffa-0843-4253-9f51-bd32c056c58c" />


## What it does
- Downloads historical price data for a user-specified ticker using yfinance, with input validation.
- Accepts a custom simulation length in days and handles non-numeric input.
- Retrieves the company name for use in the chart title.
- Calculates historical log returns, mean daily return, and daily volatility.
- Simulates 1,000 potential future price paths using Geometric Brownian Motion (GBM), each with an independent sequence of random shocks.
- Displays simulated paths alongside a histogram of final prices, with aligned price axes for easy comparison.
- Applies a shared color scale to paths and histogram bars based on final price, keeping both panels visually consistent.
- Estimates 95% Value at Risk (VaR) from the simulated final prices and displays it in the plot title.

## Why Use Geometric Brownian Motion?
Geometric Brownian Motion (GBM) provides a simple, efficient starting point for simulating stock prices. It combines an expected growth rate with random fluctuations to generate a range of possible outcomes.
  - Keeps prices positive: GBM models proportional changes, so simulated prices stay above zero.
  - Captures compounding: Price changes scale with the current stock price, reflecting percentage-based returns.
  - Uses historical data: Return and volatility estimates help calibrate the simulation.
  - Supports Monte Carlo analysis: Generating many possible paths helps visualize uncertainty and estimate potential downside risk.

GBM assumes constant drift and volatility, with independent, normally distributed log returns. Real markets can experience sudden jumps, changing volatility, and more extreme outcomes than the model captures, so it serves as a useful baseline rather than a reliable price predictor.

## What Value at Risk means here
The simulation uses numpy.percentile to calculate the 5th-percentile final price. Approximately 5% of simulated paths end below this price, while 95% end above it over the chosen simulation period.

This price threshold can be converted into 95% Value at Risk (VaR) per share:

**95% VaR = starting stock price − 5th-percentile final price**

For example, if the starting price is $100 and the 5th-percentile final price is $85, the estimated VaR is $15 per share. Under the model, approximately 5% of outcomes involve losses greater than $15. VaR is not a maximum possible loss, and its accuracy depends on the model’s assumptions.

## Stack
```
yfinance     — market data and company info
numpy        — GBM simulation, random normal generation, percentile calculation
math         — exponential and square root for the GBM update step
matplotlib   — dual-panel visualization with colormap and per-bar recoloring
```

## Usage
```bash
pip install yfinance numpy matplotlib
python montecarlosim.py
```
Enter any valid ticker and the number of days to simulate when prompted.

## How to read the chart
- Each line represents one possible stock price path over the selected number of trading days.
- Dark purple indicates lower final prices, while bright yellow indicates higher final prices.
- The histogram shows the distribution of final prices across all 1,000 simulations.
- Paths and histogram bars use the same color scale for easy comparison.
- The simulated paths generally spread out over time, reflecting increasing uncertainty.
