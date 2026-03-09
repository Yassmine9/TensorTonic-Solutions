import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)

    n = len(rater1)

    p0 = np.sum(rater1 == rater2) / n

    labels = set(rater1) | set(rater2)

    pe = 0
    for label in labels:
        p1 = np.sum(rater1 == label) / n
        p2 = np.sum(rater2 == label) / n
        pe += p1 * p2

    if pe == 1:
        return 1.0

    return (p0 - pe) / (1 - pe)