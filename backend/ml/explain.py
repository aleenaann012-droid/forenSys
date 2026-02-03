import joblib
import pandas as pd

print("Explainability script started...")

# Load trained model (from project root)
model = joblib.load("phish_model.pkl")
print("Model loaded.")

# Load dataset to get feature names
data = pd.read_csv("data/dataset.csv")
print("Dataset loaded.")

# Separate feature names
feature_names = data.drop(columns=["Result"]).columns

# Extract feature importance
importances = model.feature_importances_

# Combine and sort
feature_importance = sorted(
    zip(feature_names, importances),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Structural DNA Features:")
for feature, score in feature_importance[:10]:
    print(f"{feature}: {score:.4f}")

# ---- Human-readable explanation mapping ----

explanation_map = {
    "Prefix_Suffix": "The URL uses suspicious prefixes or suffixes, a common phishing tactic.",
    "Request_URL": "The page loads resources from external or untrusted domains.",
    "SFH": "The form submission behavior is abnormal or points to an unsafe endpoint.",
    "Links_pointing_to_page": "The site has very few inbound links, indicating low trust or a newly created domain.",
}

print("\nHuman-readable Structural DNA explanation:")

printed = False
for feature, score in feature_importance[:5]:
    if feature in explanation_map:
        print(f"- {explanation_map[feature]}")
        printed = True

# Fallback (VERY IMPORTANT)
if not printed:
    print("- The URL shows multiple structural patterns commonly associated with phishing websites.")