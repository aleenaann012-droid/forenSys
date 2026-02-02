# Train phishing detection model (Structural DNA)

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from features import extract_features


# 1. Load dataset
# Dataset must have columns: 'url' and 'label'
data = pd.read_csv("../data/raw/phishing.csv")

# 2. Extract features
X = data['url'].apply(extract_features).tolist()
y = data['label']

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# 5. Save trained model
joblib.dump(model, "phish_model.pkl")

print("✅ Model trained and saved as phish_model.pkl")
