"""import pandas as pd

df = pd.read_csv("data/aapl_stock_data.csv")

print(df.head())

df["Daily_Return"] = df["Close"].pct_change()

print("Volatility:", df["Daily_Return"].std())
print("Highest Price:", df["Close"].max())
print("Lowest Price:", df["Close"].min())"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/aapl_stock_data.csv")

# Moving averages
df["MA50"] = df["Close"].rolling(50).mean()
df["MA200"] = df["Close"].rolling(200).mean()

plt.figure(figsize=(12,6))

plt.plot(df["Close"], label="Close Price")
plt.plot(df["MA50"], label="50 Day MA")
plt.plot(df["MA200"], label="200 Day MA")

plt.title("Apple Stock Price Analysis")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()

plt.savefig("images/stock_trend.png")

plt.show()