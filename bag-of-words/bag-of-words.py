import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    result = [tokens.count(word) for word in vocab]
    return np.array(result,dtype=int)

                
