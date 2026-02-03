import re
from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)

    # Feature 1: Length of the URL
    url_length = len(url)

    # Feature 2: Number of dots in the domain
    num_dots = parsed.netloc.count('.')

    # Feature 3: Uses HTTPS or not
    has_https = 1 if parsed.scheme == "https" else 0

    # Feature 4: Presence of '@' symbol
    has_at_symbol = 1 if '@' in url else 0

    # Feature 5: Number of hyphens in domain
    num_hyphens = parsed.netloc.count('-')

    # Feature 6: Suspicious words commonly used in phishing
    suspicious_words = ['login', 'verify', 'update', 'secure', 'account', 'bank']
    has_suspicious_word = 0
    for word in suspicious_words:
        if word in url.lower():
            has_suspicious_word = 1
            break

    return [
        url_length,
        num_dots,
        has_https,
        has_at_symbol,
        num_hyphens,
        has_suspicious_word
    ]