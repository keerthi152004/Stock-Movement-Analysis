import yfinance as yf

# Fetch historical stock price data
def get_stock_data(ticker, start_date, end_date, output_path):
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval='1h')
    stock_data = stock_data[['Open', 'Close']]
    stock_data.to_csv(output_path)
    print(f"Stock data saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    ticker = 'AAPL'  # Replace with your stock ticker
    start_date = '2024-01-01'
    end_date = '2024-11-01'
    output_path = 'data/stock_data.csv'  # Adjust path as needed

    get_stock_data(ticker, start_date, end_date, output_path)
