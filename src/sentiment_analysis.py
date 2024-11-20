import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(input_path, output_path):
    # Load the cleaned data
    df = pd.read_csv(input_path)

    # Drop rows where the 'text' column is missing or empty
    df = df[df['text'].notnull()]  # Remove NaN values
    df = df[df['text'].str.strip() != '']  # Remove empty strings

    # Initialize the VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Function to calculate the sentiment score
    def get_sentiment(text):
        # Ensure text is a string
        text = str(text)
        sentiment = analyzer.polarity_scores(text)
        return sentiment['compound']  # Compound score is the overall sentiment

    # Apply the sentiment analysis
    df['sentiment_score'] = df['text'].apply(get_sentiment)

    # Save the data with sentiment scores
    df.to_csv(output_path, index=False)
    print(f"Sentiment analysis completed. Results saved to '{output_path}'!")

if __name__ == "__main__":
    input_path = 'data/cleaned_data.csv'         # Input: cleaned data
    output_path = 'data/cleaned_data_with_sentiment.csv'  # Output: data with sentiment scores
    analyze_sentiment(input_path, output_path)
