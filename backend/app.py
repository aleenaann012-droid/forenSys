from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "Backend is running"})

@app.route("/health")
def health():
    return jsonify({"message": "Flask API working fine"})

if __name__ == "__main__":
    app.run(debug=True)
