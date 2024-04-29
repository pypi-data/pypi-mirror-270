from pathlib import Path


def basedir(suffix: str = None) -> Path:
    base_dir = Path.cwd()

    if suffix is not None:
        base_dir = base_dir / suffix

    return base_dir
