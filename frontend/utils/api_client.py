import requests

API_URL = "http://127.0.0.1:5000/analyze"

def analyze(email_body, url):
    payload = {
        "email_body": email_body,
        "url": url
    }
    response = requests.post(API_URL, json=payload)
    return response.json()