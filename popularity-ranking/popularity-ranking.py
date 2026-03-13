def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    result=[]
    for i in range(len(items)):
        v=items[i][1]
        a=v*items[i][0]
        b=min_votes*global_mean
        result.append((a+b)/(v+min_votes))
    return result
        