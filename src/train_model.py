import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import pandas as pd

# Load the combined data
data = pd.read_csv('data/combined_data.csv')

# Create the Stock_Movement column based on Price_Change
data['Stock_Movement'] = data['Price_Change'].apply(lambda x: 1 if x > 0 else 0)

# Extract features (Price_Change) and labels (Stock_Movement)
features = data[['Price_Change']]  # Use any relevant features
labels = data['Stock_Movement']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, predictions)}")

# Classification Report
print("Classification Report:")
print(classification_report(y_test, predictions))

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Check if 'model' directory exists, if not, create it
if not os.path.exists('model'):
    os.makedirs('model')

# Save the trained model to a file
joblib.dump(model, 'model/stock_movement_model.pkl')

print("Model saved successfully!")
