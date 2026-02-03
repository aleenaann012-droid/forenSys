import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load dataset (already feature-engineered)
data = pd.read_csv("data/dataset.csv")

# 2. Separate features and label
# In this dataset, the label column is usually named 'Result'
X = data.drop(columns=["Result"])
y = data["Result"]

# Convert labels: -1 (phishing) → 1, 1 (legitimate) → 0
y = y.map({-1: 1, 1: 0})

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train interpretable model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# 6. Save model
joblib.dump(model, "phish_model.pkl")
print("Model saved as phish_model.pkl")