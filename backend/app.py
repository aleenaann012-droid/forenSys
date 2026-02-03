from flask import Flask
from api.routes import api_bp

app = Flask(__name__)

# Register all API routes
app.register_blueprint(api_bp)

# Root route (only place where app.route is allowed)
@app.route("/")
def home():
    return {"message": "ForenSys Backend Running"}

if __name__ == "__main__":
    app.run(debug=True)