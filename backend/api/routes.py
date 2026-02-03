from flask import Blueprint, request, jsonify

from visual.screenshots import analyze as visual_analyze
from visual.similarity import compare as similarity_compare
from fusion import fuse_scores

api_bp = Blueprint("api", __name__)


@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Backend running"})


from flask import Blueprint, request, jsonify
from urllib.parse import urlparse

from visual.visual_dna import visual_analyze
from visual.similarity import similarity_compare
from ml.email_model import email_phishing_score
from ml.url_model import url_phishing_score
from fusion import fuse_scores

api_bp = Blueprint("api", __name__)

@api_bp.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Input data required"}), 400

    email_body = data.get("email_body", "")
    url = data.get("url", "")

    if not email_body and not url:
        return jsonify({"error": "Email or URL required"}), 400

    # -------- EMAIL ANALYSIS --------
    email_score, email_reason = email_phishing_score(email_body)

    # -------- URL ANALYSIS --------
    url_score, url_reason = url_phishing_score(url)

    domain = urlparse(url).netloc if url else "N/A"

    # -------- VISUAL DNA --------
    visual_result = visual_analyze(url)
    similarity_result = similarity_compare(url)

    visual_result["flags"]
    visual_similarity = similarity_result["similarity_score"]
    visual_reason = similarity_result["reason"]

    # -------- FINAL FUSION --------
    final_score = fuse_scores(
        email_score,
        url_score,
        visual_similarity * 100
    )

    response = {
        "email_phishing_score": email_score,
        "email_reason": email_reason,
        "url_phishing_score": url_score,
        "url_reason": url_reason,
        "domain": domain,
        "visual_similarity": visual_similarity,
        "visual_reason": visual_reason,
        "final_score": final_score
    }

    return jsonify(response)

@app.route("/")
def home():
    return {"message": "ForenSys Backend Running"}

