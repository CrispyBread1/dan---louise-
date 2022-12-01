def score_anouncer(final_score):
    if final_score["home_team"] > final_score["away_team"]:
        return "Home Win"
    elif final_score["home_team"] < final_score["away_team"]:
        return "Away Win"
    elif final_score["home_team"] == final_score["away_team"]:
        return "Draw"

def get_results(final_scores):
    announcemnt = []
    for scores in final_scores:
        result = score_anouncer(scores)
        announcemnt.append(result)
    return announcemnt

