import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from features import build_features

df = pd.read_csv("data/phish_data.csv")

X = np.array([
    build_features(row["url"], row["text"])
    for _, row in df.iterrows()
])

y = df["label"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "backend/ml/phish_model.pkl")

print("✅ ML model trained & saved")