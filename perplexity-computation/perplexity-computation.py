def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    logp=0
    N=len(actual_tokens)
    for i in range(N):
        p=prob_distributions[i][actual_tokens[i]]
        logp+=math.log(p)
    H=-(logp/N)
    return (math.exp(H))