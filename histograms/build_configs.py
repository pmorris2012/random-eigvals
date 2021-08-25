import typer


def main(
    name: str, 
    jobs: int = 8,
    fpj: int = 30,
    samples: int = 100,
    n_start: int = 2,
    n_end: int = 20,
    bins_2d: int = 2160,
    bins_1d: int = 10000,
    blur: int = 9
    ):
    typer.echo(f"Saved configs.")


if __name__ == "__main__":
    typer.run(main)
