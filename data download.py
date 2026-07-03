import yfinance as yf

df = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2025-01-01",
    auto_adjust=True
)

# Flatten columns if Yahoo returns MultiIndex
if hasattr(df.columns, "droplevel"):
    try:
        df.columns = df.columns.droplevel(1)
    except:
        pass

df.reset_index(inplace=True)

df.to_csv(
    "data/aapl_stock_data.csv",
    index=False
)

print(df.head())