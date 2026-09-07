# GBM-Monte-Carlo-Simulation

A stock price simulator built on Geometric Brownian Motion. Takes any ticker and a custom time frame, pulls historical data, and simulates 1000 possible future price paths. Color coded by final price, with a matching orientation-aligned histogram and 95% Value at Risk calculated.

<img width="1250" height="480" alt="Screenshot 2026-09-07 at 4 49 19 PM" src="https://github.com/user-attachments/assets/155ff60b-9c6c-4162-a407-7c9ebec862fc" />

## What it does
- Downloads historical price data for any ticker via yfinance, with input validation
- Takes a custom number of simulation days as user input, with error handling for non-numeric input
- Pulls the company name (not just the ticker) to display in the chart title
- Calculates log returns, mean daily return, and daily volatility from historical data
- Simulates 1000 future price paths using GBM, each with a unique sequence of random shocks
- Renders a two-panel layout: simulated paths on the left, a histogram of final prices on the right, both sharing the same price axis orientation so the two visually align
- Color codes every path and every histogram bar by final price using the same colormap and normalization, so the two panels read as one consistent picture
- Calculates 95% Value at Risk from the simulated final prices and displays it directly in the plot title

## What Value at Risk means here
95% VaR is the price below which only 5% of the 1000 simulated outcomes fall, calculated directly from the simulated final price distribution using numpy.percentile. It's a plain-language answer to: across 1000 plausible futures, what's the worst price I should reasonably expect in 95% of them.

## Stack
'''
yfinance     — market data and company info
numpy        — GBM simulation, random normal generation, percentile calculation
math         — exponential and square root for the GBM update step
matplotlib   — dual-panel visualization with colormap and per-bar recoloring
'''

## Usage
'''
bash
pip install yfinance numpy matplotlib
python montecarlosim.py
'''
Enter any valid ticker and the number of days to simulate when prompted.

## How to read the chart
- The graph displays the possible future for each simulated stock over the chosen number of days
- Warmer colors indicate paths that ended at a lower final price, cooler colors indicate paths that ended higher
- The histogram shows the distribution of all 1000 final prices
- Every path on the graph widens over time because uncertainty compounds with the square root of time, not linearly
- The VaR figure marks the 5th percentile of simulated outcomes
