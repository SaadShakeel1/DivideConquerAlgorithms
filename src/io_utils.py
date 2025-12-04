from __future__ import annotations

import pathlib
from typing import List, Tuple

from .algorithms import Point


def load_points_from_file(path: str | pathlib.Path) -> List[Point]:
    path = pathlib.Path(path)
    with path.open("r", encoding="utf-8") as handle:
        raw = [line.strip() for line in handle if line.strip()]

    if not raw:
        raise ValueError(f"{path} is empty")

    points: List[Point] = []
    start_index = 0

    try:
        expected = int(raw[0])
        start_index = 1
    except ValueError:
        expected = None

    for chunk in raw[start_index:]:
        parts = chunk.split()
        if len(parts) != 2:
            raise ValueError(f"Bad line in {path}: {chunk}")
        x, y = map(float, parts)
        points.append((x, y))

    if expected is not None and expected != len(points):
        raise ValueError(f"Point count mismatch in {path}")

    return points


def load_integer_pair(path: str | pathlib.Path) -> Tuple[str, str]:
    path = pathlib.Path(path)
    with path.open("r", encoding="utf-8") as handle:
        numbers = [line.strip() for line in handle if line.strip()]

    if len(numbers) != 2:
        raise ValueError(f"{path} must contain exactly two integers")

    return numbers[0], numbers[1]


def ensure_directory(path: str | pathlib.Path) -> pathlib.Path:
    directory = pathlib.Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory.resolve()


