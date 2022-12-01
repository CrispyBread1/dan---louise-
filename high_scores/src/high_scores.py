def get_latest_score(scores):
    return scores[-1]

def sort_scores(scores):
    return scores.sort(reverse = True)

def personal_best(scores):
    sort_scores(scores)
    return scores[0] 

def top_three_scores(scores):
    sort_scores(scores)
    list_amount = len(scores) 
    if list_amount < 3:
        three_list = scores[0:int(list_amount)]
    else: 
        three_list = scores[0:3]
    return three_list
    # three_list = scores[0:3]