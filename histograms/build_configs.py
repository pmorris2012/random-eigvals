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

def get_sample_steps(jobs, samples, n_start, n_end):
    count = jobs * samples
    lin_end = min(n_start + jobs, n_end)
    linsteps = np.linspace(n_start, lin_end, count)
    geomsteps = np.geomspace(1, n_end - lin_end + 1, count) - 1
    base_steps = linsteps + geomsteps
    return np.round(base_steps).astype(np.int32).reshape(jobs, samples)

def get_frame_dims(jobs, frames, strides_start, strides_end, sample_steps):
    frame_dims = np.zeros((jobs, frames * 2 - 1))
    for i, (start, end) in enumerate(zip(strides_start, strides_end)):
        frame_dims[:,i] = sample_steps[:,start:end].sum(axis=-1)
    return frame_dims

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
    sample_steps = get_sample_steps(jobs, samples, n_start, n_end)
    frame_dims = get_frame_dims(
        jobs, 
        frames, 
        strides_start, 
        strides_end, 
        sample_steps
    )

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
