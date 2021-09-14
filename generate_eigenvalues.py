import numpy as np
import typer
import matplotlib.pyplot as plt

from pathlib import Path


def random_matrix(n):
    return np.random.randn(n, n)


def generate(n, iters):
    vecs = random_matrix(n)
    eigenvalues = np.zeros((iters, n), dtype=np.complex64)
    for i_idx in range(iters):
        vals, vecs = np.linalg.eig(vecs)
        eigenvalues[i_idx] = vals
    return eigenvalues


def main(
    samples: int = 1,
    start_index: int = 0,
    dimension: int = 100,
    iterations: int = 1002,
    arrays_dir: Path = "arrays/"
    ):
    arrays_dir.mkdir(parent=True, exist_ok=True)

    for s_idx in range(start_index, start_index + samples):
        eigenvalues = generate(n, iters)

        filename = F"n_{dimension}_i_{iterations}_s_{s_idx}.npy"
        save_path = Path(arrays_dir, filename)
        np.save(save_path, eigenvalues)


if __name__ == "__main__":
    typer.run(main)
