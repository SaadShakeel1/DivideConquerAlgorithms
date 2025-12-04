from __future__ import annotations

import json
import pathlib
import time
from typing import Any, Dict, List

from src.algorithms import find_closest_pair, karatsuba_from_strings
from src.io_utils import load_integer_pair, load_points_from_file


def run_closest_pair(file_path: pathlib.Path) -> Dict[str, Any]:
    points = load_points_from_file(file_path)
    start = time.perf_counter()
    distance, point_a, point_b = find_closest_pair(points)
    elapsed = time.perf_counter() - start
    return {
        "file": str(file_path),
        "point_a": point_a,
        "point_b": point_b,
        "distance": distance,
        "elapsed_seconds": elapsed,
        "num_points": len(points),
    }


def run_integer_multiplication(file_path: pathlib.Path) -> Dict[str, Any]:
    a_str, b_str = load_integer_pair(file_path)
    start = time.perf_counter()
    product = karatsuba_from_strings(a_str, b_str)
    elapsed = time.perf_counter() - start
    return {
        "file": str(file_path),
        "digits_a": len(a_str.strip()),
        "digits_b": len(b_str.strip()),
        "product": str(product),
        "elapsed_seconds": elapsed,
    }


def main() -> None:
    base_dir = pathlib.Path(__file__).parent
    data_dir = base_dir / "data"

    point_files = sorted(data_dir.glob("points_set_*.txt"))
    int_files = sorted(data_dir.glob("ints_set_*.txt"))

    if not point_files or not int_files:
        raise FileNotFoundError("Run generate_datasets.py before applying algorithms.")

    results: Dict[str, List[Dict[str, Any]]] = {
        "closest_pair": [run_closest_pair(path) for path in point_files],
        "integer_multiplication": [run_integer_multiplication(path) for path in int_files],
    }

    results_path = data_dir / "results.json"
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)

    print(f"Wrote results to {results_path.resolve()}")


if __name__ == "__main__":
    main()


