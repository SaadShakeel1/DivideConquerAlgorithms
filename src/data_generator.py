from __future__ import annotations

import random
import pathlib
from typing import Iterable, Tuple

from .io_utils import ensure_directory


def random_points(count: int, bounds: Tuple[int, int]) -> Iterable[Tuple[float, float]]:
    low, high = bounds
    for _ in range(count):
        yield random.uniform(low, high), random.uniform(low, high)


def save_point_files(out_dir: pathlib.Path, counts: Iterable[int], bounds: Tuple[int, int]) -> None:
    for index, count in enumerate(counts, start=1):
        file_path = out_dir / f"points_set_{index}.txt"
        with file_path.open("w", encoding="utf-8") as handle:
            handle.write(f"{count}\n")
            for x, y in random_points(count, bounds):
                handle.write(f"{x:.6f} {y:.6f}\n")


def random_number(num_digits: int) -> int:
    lower = 10 ** (num_digits - 1)
    upper = (10 ** num_digits) - 1
    return random.randint(lower, upper)


def save_integer_files(out_dir: pathlib.Path, sizes: Iterable[int]) -> None:
    for index, digits in enumerate(sizes, start=1):
        file_path = out_dir / f"ints_set_{index}.txt"
        with file_path.open("w", encoding="utf-8") as handle:
            handle.write(f"{random_number(digits)}\n")
            handle.write(f"{random_number(digits)}\n")


def create_datasets(point_sizes: Iterable[int], int_sizes: Iterable[int], out_dir: pathlib.Path | str) -> None:
    target_dir = ensure_directory(out_dir)
    save_point_files(target_dir, point_sizes, (-1000, 1000))
    save_integer_files(target_dir, int_sizes)


