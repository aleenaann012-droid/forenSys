def url_phishing_score(url):
    if not url:
        return 0, "No URL provided"

    score = 0
    reason = "URL appears safe"

    if "@" in url or "-" in url:
        score = 80
        reason = "Suspicious URL pattern detected"

    return score, reason