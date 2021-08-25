import json
import numpy as np
import typer


def get_frame_strides(samples, frames):
    return np.round(np.linspace(0, samples, frames + 1))[1:-1].astype(np.int32)

def main(
    name: str, 
    jobs: int = 8,
    frames: int = 30,
    samples: int = 100,
    n_start: int = 2,
    n_end: int = 20,
    bins_2d: int = 2160,
    bins_1d: int = 10000,
    blur: int = 9
    ):
    frame_strides = get_frame_strides(samples, frames)

    count = jobs * samples
    lin_steps = np.linspace(0, jobs, count - 1)
    geom_steps = np.geomspace(n_start - 1, n_end - lin_steps[-1] - 2, count - 1)
    base_steps = np.full(count, 1.0)
    base_steps[0] += 1
    base_steps[1:] += lin_steps + geom_steps
    base_steps = np.round(base_steps).astype(np.int32)

    for job_idx in range(jobs):
        job = {
            "name": name,
            "index": job_idx,
            "frames": frames
        }
    #json.dump()
    typer.echo(f"{base_steps}")


if __name__ == "__main__":
    typer.run(main)
