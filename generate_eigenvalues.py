import numpy as np
import typer
import matplotlib.pyplot as plt

from pathlib import Path
import uuid


def random_string():
    return uuid.uuid4().hex


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
    dimension: int = 100,
    iterations: int = 1002,
    arrays_dir: Path = "arrays/"
    ):
    arrays_dir.mkdir(parents=True, exist_ok=True)

    for s_idx in range(start_index, start_index + samples):
        eigenvalues = generate(dimension, iterations)

        filename = F"n_{dimension}_i_{iterations}_{random_string()}.npy"
        save_path = Path(arrays_dir, filename)
        np.save(save_path, eigenvalues)


if __name__ == "__main__":
    typer.run(main)
