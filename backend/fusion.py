def fuse_scores(email_score, url_score, visual_score):
    return int(0.4 * email_score + 0.4 * url_score + 0.2 * visual_score)