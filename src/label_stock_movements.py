import pandas as pd

def label_stock_movements(input_path, output_path):
    # Read the stock data
    stock_data = pd.read_csv(input_path, parse_dates=['Datetime'], index_col='Datetime')

    # Calculate daily percentage change
    stock_data['Price_Change'] = stock_data['Close'].pct_change(fill_method=None)

    # Label the movements: 1 for positive movement, 0 for negative/neutral movement
    stock_data['Movement'] = (stock_data['Price_Change'] > 0).astype(int)

    # Save the labeled data to a new CSV file
    stock_data.to_csv(output_path)
    print(f"Labeled stock data saved to {output_path}")

# Example usage
if __name__ == "__main__":
    input_path = "data/stock_data.csv"   # Path to the input CSV file
    output_path = "data/labeled_stock_data.csv"  # Path to the output labeled file

    label_stock_movements(input_path, output_path)
