import joblib
import pandas as pd

# Load trained model
model = joblib.load("phish_model.pkl")

# Load dataset to get feature names
data = pd.read_csv("data/dataset.csv")

# Drop label column
feature_names = data.drop(columns=["Result"]).columns

# Get feature importance
importances = model.feature_importances_

# Combine and sort
feature_importance = sorted(
    zip(feature_names, importances),
    key=lambda x: x[1],
    reverse=True
)

print("Top Structural DNA Features:")
for feature, score in feature_importance[:10]:
    print(f"{feature}: {score:.4f}")