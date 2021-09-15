import numpy as np
import typer
from matplotlib.colors import hsv_to_rgb

from pathlib import Path


def main(
    bins: int = 2160,
    lim: float = 1.42,
    filter_arrays: bool = True,
    dimension: int = 100,
    iterations: int = 1002,
    arrays_dir: Path = "arrays/"
    out_path: Path = "output/hist2d.npy"
    ):

    if filter_arrays:
        files = arrays_dir.glob(F"n_{dimension}_i_{iterations}_*.npy")
    else:
        files = list(arrays_dir.iterdir())
    arrays = np.stack([np.load(f) for f in files])

    hue = np.zeros((bins, bins))
    sat = np.ones((bins, bins))
    val = np.zeros((bins, bins))
    for dim in range(arrays.shape[-1]):
        hist, _, _ = np.histogram2d(
            arrays[...,dim].real.reshape(-1),
            arrays[...,dim].imag.reshape(-1),
            bins=bins,
            range=[[-lim, lim], [-lim, lim]],
            density=True
        )
        hue += hist * (dim + 1)
        val += hist
    
    hue -= hue.min()
    hue /= hue.max() + 1e-9
    val -= val.min()
    val /= val.max() + 1e-9

    rgb = hsv_to_rgb(np.stack([hue, sat, val], axis=-1))
    
    np.save(out_path, rgb)


if __name__ == "__main__":
    typer.run(main)

