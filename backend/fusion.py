from config import EMAIL_WEIGHT, URL_WEIGHT, VISUAL_WEIGHT

def fuse_scores(email_score, url_score, visual_score):
    """
    email_score: int (0–100)
    url_score: int (0–100)
    visual_score: int (0–100)
    """

    final_score = (
        EMAIL_WEIGHT * email_score +
        URL_WEIGHT * url_score +
        VISUAL_WEIGHT * visual_score
    )

    return round(final_score, 2)
