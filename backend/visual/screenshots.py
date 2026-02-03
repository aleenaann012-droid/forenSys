def analyze(url):
    return {
        "flags": ["login_page_detected"] if url else []
    }