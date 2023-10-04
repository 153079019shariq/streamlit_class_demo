import streamlit as st
import yfinance as yf

st.title("Welcome to stock market")   

import datetime
#ticker_symbol = 'AAPL'
ticker_symbol = st.text_input("Enter Stock Symbol","AAPL",)
#start_date = "2019-01-01"
#end_date   = "2022-12-31"
col1, col2 = st.columns(2)
with col1:
 start_date = st.date_input("Please enter Starting Date",datetime.date(2019,1,1))
with col2:
 end_date = st.date_input("Please enter End Date",datetime.date(2022,12,31))
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1mo",start=f"{start_date}",
                             end=f"{end_date}")

#st.dataframe(ticker_df)

col1, col2 = st.columns(2)
with col1:
  st.write("# Daily closing price")
  st.line_chart(ticker_df["Close"])

with col2:
  st.write("# Highest price")
  st.line_chart(ticker_df["High"])

