import numpy as np
import time

def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print(f'{f.__name__} function took {(time2-time1)*1000.0:.3f} ms')
        return ret
    return wrap

u = 1.1    
d = 1/u    
opttype = 'C' #option Type 'C' or 'P'

@timing
def binomial_tree_fast(K, T, S0, r, N, u, d, opttype='C'): 
    # Precompute constants
    dt = T / N
    q = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)

    # Initialize asset prices at maturity - Time step N
    S = S0 * d ** (np.arange(N, -1, -1)) * u ** (np.arange(0, N + 1, 1))

    # Initialize option values at maturity
    if opttype == 'C':
        C = np.maximum(0, S - K)
    else:
        C = np.maximum(0, K - S)

    # Step backwards through the tree
    for i in np.arange(N, 0, -1):
        C = disc * (q * C[1:i+1] + (1 - q) * C[0:i])

    return C[0]

# Example parameters
K = 100  # Strike price
T = 1    # Time to maturity
S0 = 100 # Initial stock price
r = 0.05 # Risk-free rate
N = 3    # Number of steps

# Call the function and print the result
result_fast = binomial_tree_fast(K, T, S0, r, N, u, d, opttype='C')
print("Option price is", result_fast)