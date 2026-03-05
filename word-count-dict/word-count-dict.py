def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    d=dict()
    for sentence in sentences:
        for word in sentence : 
            if word in d:
                d[word]+=1
            else:
                d[word]=1
    return d