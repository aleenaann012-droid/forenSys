def email_phishing_score(email_body):
    score = 0
    reason = "No phishing indicators found"

    if "verify" in email_body.lower():
        score = 70
        reason = "Urgent verification language detected"

    return score, reason