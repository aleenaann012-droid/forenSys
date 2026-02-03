import joblib
from features import build_features

model = joblib.load("backend/ml/phish_model.pkl")

def predict_phish_score(url, text):
    features = build_features(url, text).reshape(1, -1)
    return float(model.predict_proba(features)[0][1])