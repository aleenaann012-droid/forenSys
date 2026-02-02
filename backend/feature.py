# Feature extraction for phishing detection (Structural DNA)

def extract_features(url):
    """
    Takes a URL string and returns a list of numerical features
    """

    url = url.lower()

    # 1. URL length
    url_length = len(url)

    # 2. Number of dots
    num_dots = url.count('.')

    # 3. Number of hyphens
    num_hyphens = url.count('-')

    # 4. Presence of '@' symbol
    has_at_symbol = 1 if '@' in url else 0

    # 5. HTTPS usage
    has_https = 1 if url.startswith('https') else 0

    # 6. Number of digits in URL
    num_digits = sum(char.isdigit() for char in url)

    # 7. Suspicious keywords
    suspicious_words = ['login', 'verify', 'update', 'secure', 'account', 'bank', 'free']
    has_suspicious_word = 1 if any(word in url for word in suspicious_words) else 0

    return [
        url_length,
        num_dots,
        num_hyphens,
        has_at_symbol,
        has_https,
        num_digits,
        has_suspicious_word
    ]