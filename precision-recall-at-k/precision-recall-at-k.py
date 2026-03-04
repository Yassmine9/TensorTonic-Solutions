def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    p=0
    top_k=recommended[:k]
    resultat=[]
    for i in top_k :
        for j in relevant:
            if i==j:
                p+=1
    resultat.append(p/k)
    resultat.append(p/len(relevant))
    return resultat