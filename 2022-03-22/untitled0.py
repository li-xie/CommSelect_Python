import numpy as np
import pickle
rng = np.random.default_rng(1)
a = rng.random(1)
b = rng.random(1)
with open('randseed.pkl', 'wb') as f:
    pickle.dump(rng, f)
c = rng.random(1)
d = rng.random(1)
with open('randseed.pkl', 'rb') as f:
    rng2 = pickle.load(f)
e = rng2.random(1)
f = rng2.random(1)