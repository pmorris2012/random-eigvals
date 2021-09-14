import numpy as np
import typer
import matplotlib.pyplot as plt
from pathlib import Path




def main(
    samples = 1, 
    n = 100, 
    iterations = 1002,
    arrays_dir: Path = "arrays/"
    ):
    arrays_dir.mkdir(parent, )=True, exist_ok=True)


mies = np.zeros((n, n))
for i in tqdm.tqdm(range(1, n + 1, 10)):
    for j in tqdm.tqdm(range(samples), desc=str(i)):
        vecs = np.random.randn(i, i)
        for _ in range(skip_iters):
            vals, vecs = np.linalg.eig(vecs)
        for k in range(iters):
            vals, vecs = np.linalg.eig(vecs)
            mies[i-1,:i] += np.abs(vals)
mies /= iters * samples
for i in range(1, n):
    plt.plot(np.arange(1, n-i+1), mies[:n-i,i])
plt.yscale('symlog')
plt.show()
