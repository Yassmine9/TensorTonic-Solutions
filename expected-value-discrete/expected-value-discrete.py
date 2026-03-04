import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if (np.allclose(sum(p),1.0,rtol=1e-6, atol=1e-8)):
    
        s=0
        for i in range(len(x)):
           s+=x[i]*p[i] 
        return s
    else:
        raise ValueError
