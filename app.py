import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Stock Market Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Market Analytics Dashboard")

stocks = {
    "Apple":"AAPL",
    "Microsoft":"MSFT",
    "NVIDIA":"NVDA",
    "Tesla":"TSLA",
    "Amazon":"AMZN",
    "Google":"GOOGL"
}

company = st.sidebar.selectbox(
    "Select Company",
    list(stocks.keys())
)

ticker = stocks[company]



start_date = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime("2020-01-01")
)

end_date = st.sidebar.date_input(
    "End Date",
    pd.to_datetime("today")
)

df = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    auto_adjust=True
)

if hasattr(df.columns, "droplevel"):
    try:
        df.columns = df.columns.droplevel(1)
    except:
        pass

df.reset_index(inplace=True)

df["Daily_Return"] = df["Close"].pct_change()

df["MA50"] = df["Close"].rolling(50).mean()
df["MA200"] = df["Close"].rolling(200).mean()

latest_price = df["Close"].iloc[-1]
highest_price = df["Close"].max()
lowest_price = df["Close"].min()
volatility = df["Daily_Return"].std()

st.subheader(f"{ticker} Performance Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Current Price",
    f"${latest_price:.2f}"
)

col2.metric(
    "Highest Price",
    f"${highest_price:.2f}"
)

col3.metric(
    "Lowest Price",
    f"${lowest_price:.2f}"
)

col4.metric(
    "Volatility",
    f"{volatility:.4f}"
)

st.markdown("---")

st.subheader("📊 Closing Price Trend")

st.line_chart(df.set_index("Date")["Close"])

st.subheader("📈 Moving Averages")

ma_df = df.set_index("Date")[["Close", "MA50", "MA200"]]

st.line_chart(ma_df)

st.subheader("📉 Daily Returns")

st.line_chart(
    df.set_index("Date")["Daily_Return"]
)

st.subheader("📦 Trading Volume")

st.bar_chart(
    df.set_index("Date")["Volume"]
)

st.subheader("📋 Dataset")

st.dataframe(df.tail(20))

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download CSV",
    csv,
    f"{ticker}_stock_data.csv",
    "text/csv"
)