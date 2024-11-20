import yfinance as yf

# Fetch historical stock price data
def fetch_stock_data(ticker, start_date, end_date, interval='1d'):
    # Download stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

    # Display the first few rows
    print(stock_data.head())

    return stock_data

# Example usage
if __name__ == "__main__":
    ticker = "AAPL"  # Stock ticker symbol (e.g., 'AAPL' for Apple, 'MSFT' for Microsoft)
    start_date = "2024-01-01"  # Start date of historical data
    end_date = "2024-11-01"    # End date of historical data
    interval = "1d"            # Time interval ('1d', '1h', '1wk', etc.)

    stock_data = fetch_stock_data(ticker, start_date, end_date, interval)

    # Save the data to a CSV file
    stock_data.to_csv("data/stock_data.csv")
    print("Stock data saved to data/stock_data.csv")
