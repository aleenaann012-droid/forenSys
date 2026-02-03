from flask import Blueprint, request, jsonify

from visual.screenshots import analyze as visual_analyze
from visual.similarity import compare as similarity_compare
from fusion import fuse_scores

api_bp = Blueprint("api", __name__)


@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Backend running"})


@api_bp.route("/analyze", methods=["POST"])
def analyze_url():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    url = data["url"]

    visual_result = visual_analyze(url)
    similarity_result = similarity_compare(url)

    ml_score = 0.5  # placeholder

    final_score, verdict = fuse_scores(
        visual_result["visual_score"],
        similarity_result["similarity_score"],
        ml_score
    )

    response = {
        "url": url,
        "final_score": final_score,
        "verdict": verdict,
        "visual": {
            "flags": visual_result["flags"]
        },
        "similarity": {
            "matched_brand": similarity_result["matched_brand"]
        }
    }

    return jsonify(response)

@app.route("/")
def home():
    return {"message": "ForenSys Backend Running"}

