from __future__ import annotations

import pathlib

from src.data_generator import create_datasets


def main() -> None:
    base_dir = pathlib.Path(__file__).parent
    data_dir = base_dir / "data"

    point_sizes = [128, 144, 160, 176, 192, 208, 224, 256, 288, 320]
    int_sizes = [120, 132, 144, 156, 168, 180, 192, 210, 240, 270]

    create_datasets(point_sizes, int_sizes, data_dir)

    print(f"Created datasets in {data_dir.resolve()}")


if __name__ == "__main__":
    main()


