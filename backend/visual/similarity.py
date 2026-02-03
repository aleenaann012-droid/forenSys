def compare(url):
    return {
        "similarity_score": 0.65 if url else 0.0,
        "reason": "Visual layout moderately similar to known brand"
    }