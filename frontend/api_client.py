def analyze_url(url):
    # TEMP placeholder until backend is ready
    return {
        "url": url,
        "final_score": 0.82,
        "verdict": "Phishing",
        "features": [
            {"name": "URL Length", "value": 78, "risk": "High"},
            {"name": "Domain Age", "value": "2 days", "risk": "High"}
        ]
    }