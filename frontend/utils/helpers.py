import re

def is_valid_url(url):
    pattern = r"https?://[^\s]+"
    return re.match(pattern, url)