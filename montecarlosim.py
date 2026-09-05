import yfinance as yf


while True:
    user_input = input("What stock would you like to analyze (e.g., AAPL): ")
    ticker_symbol = user_input.strip().upper()
    stock = yf.Ticker(ticker_symbol)
    past = stock.history(period="5y")
    if past.empty:
        print("No price data found for this ticker symbol.")
        continue
    else:
        break


