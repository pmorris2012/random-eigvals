import json
from pathlib import Path
import numpy as np
import typer


def get_frame_strides(samples, frames):
    strides = np.linspace(0, samples, frames + 1)
    strides = np.round(strides)[1:-1].astype(np.int32)
    strides = list(map(int, strides))
    strides_start = [0] * frames + strides
    strides_end = strides + [samples] * frames
    return strides_start, strides_end

def main(
    name: str, 
    jobs: int = 8,
    frames: int = 30,
    samples: int = 100,
    n_start: int = 2,
    n_end: int = 20,
    bins_1d: int = 10000,
    bins_2d: int = 2160,
    blur: int = 9,
    configs_dir: str = "configs"
    ):
    strides_start, strides_end = get_frame_strides(samples, frames)

    count = jobs * samples
    linsteps = np.linspace(0, jobs, count - 1)
    geomsteps = np.geomspace(n_start - 1, n_end - linsteps[-1] - 1, count - 1)
    base_steps = np.full(count, 1.0)
    base_steps[0] += n_start - 1
    base_steps[1:] += linsteps + geomsteps
    sample_steps = np.round(base_steps).astype(np.int32).reshape(jobs, samples)

    frame_dims = np.zeros((jobs, frames * 2 - 1))
    for i, (start, end) in enumerate(zip(strides_start, strides_end)):
        frame_dims[:,i] = sample_steps[:,start:end].sum(axis=-1)

    for job_idx in range(jobs):
        job = {
            "name": name,
            "index": job_idx,
            "frames": frames,
            "sample_dims": list(map(int, sample_steps[job_idx])),
            "partial_frame_dims": list(map(int, frame_dims[job_idx])),
            "strides_start": strides_start,
            "strides_end": strides_end,
            "bins_1d": bins_1d,
            "bins_2d": bins_2d,
            "blur": blur
        }

        out_path = Path(configs_dir, f"{name}-{job_idx}.json")
        with open(out_path, "w") as f:
            json.dump(job, f, sort_keys=True, indent=4)

    typer.echo(f"wrote {name}-[job_idx].json to {configs_dir}")


if __name__ == "__main__":
    typer.run(main)
