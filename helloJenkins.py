import yfinance as yf


sq = yf.Ticker("SQ")
netflix = yf.Ticker("NFLX")

# get stock info
print(sq.info["symbol"] + ": " + str(sq.info["regularMarketPrice"]))
print(netflix.info["symbol"] + ": " + str(netflix.info["regularMarketPrice"]))