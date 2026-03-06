def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    step=chunk_size-overlap
    i=0
    result=[]
    if (len(tokens)==0):
        return tokens
    elif (len(tokens)<chunk_size):
        result.append(tokens)
        return result
    else:
        for i in range(0,len(tokens),step):
            if(len(tokens[i:i+chunk_size])<chunk_size):
                break
            result.append(tokens[i:i+chunk_size])
    return result 