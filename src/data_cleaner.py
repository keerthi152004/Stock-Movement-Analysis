import pandas as pd
import re
import string

def clean_data(input_path, output_path):
    # Load the raw data
    df = pd.read_csv(input_path)

    # Step 1: Remove non-text messages (such as images, videos, etc.)
    df = df[df['text'].notna()]

    # Step 2: Remove duplicate messages
    df = df.drop_duplicates(subset='text', keep='first')

    # Step 3: Remove links (URLs) from the messages
    df['text'] = df['text'].apply(lambda x: re.sub(r'http\S+|www\S+|https\S+', '', x))

    # Step 4: Remove special characters and punctuation
    df['text'] = df['text'].apply(lambda x: re.sub(f"[{string.punctuation}]", '', x))

    # Step 5: Remove emojis (optional, can also remove non-English characters if needed)
    df['text'] = df['text'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', x))  # Remove non-ASCII characters (e.g., emojis)

    # Step 6: Remove extra whitespaces
    df['text'] = df['text'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

    # Step 7: Convert text to lowercase (normalization)
    df['text'] = df['text'].apply(lambda x: x.lower())

    # Step 8: (Optional) Remove stopwords (you can use nltk library to remove common words like "the", "is", etc.)
    stopwords = ['the', 'and', 'is', 'in', 'to', 'of', 'for', 'on', 'a', 'an', 'at', 'with', 'by', 'this', 'that']
    df['text'] = df['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stopwords]))

    # Save the cleaned data to a new CSV file
    df.to_csv(output_path, index=False)

    print(f"Data cleaned and saved to '{output_path}'!")

if __name__ == "__main__":
    input_path = 'data/raw_data.csv'      # Input file (raw data)
    output_path = 'data/cleaned_data.csv' # Output file (cleaned data)

    clean_data(input_path, output_path)
