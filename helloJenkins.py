import yfinance as yf


msft = yf.Ticker("SQ")

# get stock info
print(msft.info["symbol"] + ": " + str(msft.info["regularMarketPrice"]))