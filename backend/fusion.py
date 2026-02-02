from config import (
    VISUAL_WEIGHT,
    SIMILARITY_WEIGHT,
    ML_WEIGHT,
    PHISH_THRESHOLD
)


def fuse_scores(visual_score, similarity_score, ml_score):
    weighted_visual = visual_score * VISUAL_WEIGHT
    weighted_similarity = similarity_score * SIMILARITY_WEIGHT
    weighted_ml = ml_score * ML_WEIGHT

    final_score = weighted_visual + weighted_similarity + weighted_ml
    final_score = min(final_score, 1.0)

    verdict = "Phishing" if final_score >= PHISH_THRESHOLD else "Legitimate"

    return round(final_score, 2), verdict
