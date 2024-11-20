Stock Movement Prediction

This project involves predicting stock market movements based on sentiment analysis of messages from a Telegram channel. 
The workflow includes scraping data from Telegram, cleaning and preprocessing the data, performing sentiment analysis, and training a machine learning model to predict stock movements.


Table of Contents:
1.Introduction
2.Requirements
3.Project Structure
4.Usage


Introduction: 

This project predicts stock price movements based on sentiment derived from Telegram messages. 
It scrapes messages from a predefined Telegram channel, cleans and processes the text data, performs sentiment analysis, and finally trains a machine learning model using the stock price data to predict whether the stock price will go up or down.

Key Components:
Telegram Scraping: Scrapes messages from a target Telegram channel using Telethon.
Data Cleaning: Removes unwanted characters and cleans the scraped data.
Sentiment Analysis: Analyzes sentiment using VADER sentiment analysis.
Stock Data Integration: Merges sentiment data with stock price data to create a combined dataset.
Model Training: Trains a machine learning model (Random Forest) to predict stock movements.

Requirements
To run this project, you will need the following Python libraries:

pandas
yfinance
Telethon
vaderSentiment
scikit-learn
joblib


Install the necessary dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
requirements.txt:
txt
Copy code
pandas
yfinance
telethon
vaderSentiment
scikit-learn
joblib


Project Structure
The project is organized into the following structure:

bash
Copy code
Stock-Movement-Analysis/
│
├── data/                         # Folder to store raw and processed data
│   ├── raw_data.csv              # Raw scraped Telegram data
│   ├── cleaned_data.csv          # Cleaned data after preprocessing
│   ├── cleaned_data_with_sentiment.csv  # Data after sentiment analysis
│   ├── stock_data.csv            # Stock price data
│   ├── labeled_stock_data.csv    # Labeled stock movement data
│   ├── combined_data.csv         # Merged sentiment and stock data
│
├── model/                        # Folder to save trained models
│   ├── stock_movement_model.pkl  # Trained stock movement prediction model
│
├── src/                          # Source code
│   ├── data_cleaner.py           # Data cleaning script
│   ├── data_scraper.py           # Telegram data scraping script
│   ├── fetch_stock_data.py       # Fetch stock price data using yfinance
│   ├── label_stock_movements.py  # Label stock movements based on price changes
│   ├── merge_sentiment_and_stock.py  # Merge sentiment data with stock data
│   ├── sentiment_analysis.py     # Perform sentiment analysis on text data
│   ├── train_model.py            # Train machine learning model
│
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies



Usage
Step 1: Scrape Telegram Data
Run the script data_scraper.py to scrape messages from a Telegram channel.

bash
Copy code
python src/data_scraper.py
This will save the raw data into data/raw_data.csv.

Step 2: Clean the Data
Run the data_cleaner.py script to clean the scraped data.

bash
Copy code
python src/data_cleaner.py
The cleaned data will be saved as data/cleaned_data.csv.

Step 3: Perform Sentiment Analysis
Run the sentiment_analysis.py script to analyze sentiment of the messages using the VADER sentiment analysis tool.

bash
Copy code
python src/sentiment_analysis.py
The data with sentiment scores will be saved as data/cleaned_data_with_sentiment.csv.

Step 4: Fetch Stock Data
Run the fetch_stock_data.py script to download historical stock data using yfinance.

bash
Copy code
python src/fetch_stock_data.py
The stock data will be saved as data/stock_data.csv.

Step 5: Label Stock Movements
Run the label_stock_movements.py script to label stock movements based on the percentage change in stock prices.

bash
Copy code
python src/label_stock_movements.py
This will generate data/labeled_stock_data.csv.

Step 6: Merge Sentiment and Stock Data
Run the merge_sentiment_and_stock.py script to merge the sentiment data with the stock price data.

bash
Copy code
python src/merge_sentiment_and_stock.py
This will create a data/combined_data.csv file.

Step 7: Train the Model
Run the train_model.py script to train the machine learning model using the combined dataset.

bash
Copy code
python src/train_model.py
This will train a Random Forest model and save it as model/stock_movement_model.pkl.

Step 8: Predictions
Once the model is trained, you can use it to predict stock movements based on new data.





