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
95% VaR is the price below which only 5% of the 1000 simulated outcomes fall, calculated directly from the simulated final price distribution using numpy.percentile. It's a plain-language answer to: across 1000 plausible futures, what's the worst price I should reasonably expect in 95% of them.

## Stack
```
yfinance     — market data and company info
numpy        — GBM simulation, random normal generation, percentile calculation
math         — exponential and square root for the GBM update step
matplotlib   — dual-panel visualization with colormap and per-bar recoloring
```

## Usage
```
bash
pip install yfinance numpy matplotlib
python montecarlosim.py
```
Enter any valid ticker and the number of days to simulate when prompted.

## How to read the chart
- The graph displays the possible future for each simulated stock over the chosen number of days
- Warmer colors indicate paths that ended at a lower final price, cooler colors indicate paths that ended higher
- The histogram shows the distribution of all 1000 final prices
- Every path on the graph widens over time because uncertainty compounds with the square root of time, not linearly
- The VaR figure marks the 5th percentile of simulated outcomes
