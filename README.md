# GBM-Monte-Carlo-Simulation

A stock price simulator built on Geometric Brownian Motion. Takes any ticker and a custom time frame, pulls historical data, and simulates 1000 possible future price paths. Color coded by final price, with a matching orientation-aligned histogram and 95% Value at Risk calculated.

<img width="1250" height="480" alt="Screenshot 2026-09-07 at 4 49 19 PM" src="https://github.com/user-attachments/assets/155ff60b-9c6c-4162-a407-7c9ebec862fc" />

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
- The graph displays the possible future for each simulated stock over the chosen number of days
- Warmer colors indicate paths that ended at a lower final price, cooler colors indicate paths that ended higher
- The histogram shows the distribution of all 1000 final prices
- The simulated paths generally spread out over time, reflecting increasing uncertainty about future prices
- The VaR figure marks the 5th percentile of simulated outcomes
