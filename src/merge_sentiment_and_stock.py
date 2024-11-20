import pandas as pd

# Merge sentiment and stock data based on timestamps
def merge_sentiment_and_stock(sentiment_path, stock_path, output_path):
    sentiment_data = pd.read_csv(sentiment_path, parse_dates=['date'], index_col='date')
    stock_data = pd.read_csv(stock_path, parse_dates=['Datetime'], index_col='Datetime')

    # Merge sentiment data with stock data
    combined_data = pd.merge_asof(sentiment_data.sort_index(), stock_data.sort_index(), left_index=True, right_index=True)
    combined_data.to_csv(output_path)
    print(f"Combined data saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    sentiment_path = 'data/cleaned_data_with_sentiment.csv'
    stock_path = 'data/labeled_stock_data.csv'
    output_path = 'data/combined_data.csv'

    merge_sentiment_and_stock(sentiment_path, stock_path, output_path)
