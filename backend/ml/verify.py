import joblib
import pandas as pd

print("=== PHISH-DNA ML VERIFICATION START ===")

# 1. Load model
model = joblib.load("phish_model.pkl")
print("✔ Model loaded")

# 2. Load dataset
data = pd.read_csv("data/dataset.csv")
print("✔ Dataset loaded")

# 3. Check columns
print(f"✔ Dataset shape: {data.shape}")
print(f"✔ Label column exists: {'Result' in data.columns}")

# 4. Prepare sample input
X = data.drop(columns=["Result"])
y = data["Result"].map({-1: 1, 1: 0})

# 5. Run a sample prediction
sample = X.iloc[[0]]
pred = model.predict(sample)[0]
prob = model.predict_proba(sample)[0][1]

print("✔ Sample prediction ran")
print(f"   → Prediction (1=phishing): {pred}")
print(f"   → Phishing probability: {prob:.4f}")

# 6. Feature importance check
importances = model.feature_importances_
top_feature = X.columns[importances.argmax()]

print("✔ Feature importance accessible")
print(f"   → Top feature: {top_feature}")

print("\n=== ALL SYSTEMS WORKING ===")