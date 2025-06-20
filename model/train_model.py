import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load EEG dataset
data = pd.read_csv('data/eeg.csv')  # Path to the EEG dataset
X = data.iloc[:, :-1]  # EEG signal values
y = data.iloc[:, -1]   # Label: 0 = non-seizure, 1 = seizure

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Save the trained model
joblib.dump(model, 'best_model.pkl')
