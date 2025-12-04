from __future__ import annotations

import json
import math
import pathlib
import threading
import time
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from typing import Callable, Dict, List

from src.algorithms import find_closest_pair, karatsuba_from_strings
from src.io_utils import load_integer_pair, load_points_from_file


BASE_DIR = pathlib.Path(__file__).parent
DATA_DIR = BASE_DIR / "data"


class AlgorithmUI(ttk.Frame):
    def __init__(
        self,
        parent: ttk.Notebook,
        title: str,
        file_types: List[tuple[str, str]],
        handler: Callable[[pathlib.Path, Callable[[str], None]], Dict[str, str]],
    ) -> None:
        super().__init__(parent, padding=16)
        self.pack(fill=tk.BOTH, expand=True)
        self.file_types = file_types
        self.handler = handler
        self.selected_file: pathlib.Path | None = None

        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        ttk.Label(self, text=title, font=("Segoe UI", 14, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w"
        )

        self.file_label = ttk.Label(self, text="No file chosen", width=60)
        self.file_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=8)

        ttk.Button(self, text="Choose File", command=self.choose_file).grid(
            row=1, column=2, sticky="e"
        )

        self.run_button = ttk.Button(self, text="Run Algorithm", command=self.run_algorithm, state="disabled")
        self.run_button.grid(row=2, column=0, columnspan=3, sticky="ew")

        self.log = tk.Text(self, height=20, wrap=tk.WORD, state=tk.DISABLED, font=("Consolas", 10))
        self.log.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=(12, 0))

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.log.yview)
        scrollbar.grid(row=3, column=3, sticky="ns")
        self.log.configure(yscrollcommand=scrollbar.set)

    def choose_file(self) -> None:
        file_path = filedialog.askopenfilename(
            title="Select Input File",
            initialdir=DATA_DIR if DATA_DIR.exists() else BASE_DIR,
            filetypes=self.file_types,
        )
        if file_path:
            self.selected_file = pathlib.Path(file_path)
            self.file_label.config(text=self.selected_file.name)
            self.run_button.config(state="normal")
            self.clear_log()
            self.append_log(f"Selected file: {self.selected_file}")

    def run_algorithm(self) -> None:
        if not self.selected_file:
            messagebox.showwarning("No File", "Please select a valid input file first.")
            return

        self.run_button.config(state="disabled")
        self.append_log("Starting algorithm...")

        thread = threading.Thread(target=self._run_in_background, daemon=True)
        thread.start()

    def _run_in_background(self) -> None:
        start = time.perf_counter()
        try:
            def log_callback(msg: str) -> None:
                self.after(0, lambda: self.append_log(msg))
            results = self.handler(self.selected_file, log_callback)
        except Exception as exc:
            self.after(0, lambda: self._on_failure(exc))
            return
        elapsed = time.perf_counter() - start
        results["elapsed_ui"] = f"{elapsed:.6f} seconds (including UI overhead)"
        self.after(0, lambda: self._on_success(results))

    def _on_failure(self, exc: Exception) -> None:
        self.append_log(f"Error: {exc}")
        messagebox.showerror("Processing Error", str(exc))
        self.run_button.config(state="normal")

    def _on_success(self, results: Dict[str, str]) -> None:
        self.append_log("Algorithm completed successfully.\n")
        for key, value in results.items():
            self.append_log(f"{key}: {value}")
        self.run_button.config(state="normal")

    def append_log(self, text: str) -> None:
        self.log.configure(state=tk.NORMAL)
        self.log.insert(tk.END, text + "\n")
        self.log.configure(state=tk.DISABLED)
        self.log.see(tk.END)

    def clear_log(self) -> None:
        self.log.configure(state=tk.NORMAL)
        self.log.delete("1.0", tk.END)
        self.log.configure(state=tk.DISABLED)


def closest_pair_handler(path: pathlib.Path, log_step: Callable[[str], None]) -> Dict[str, str]:
    points = load_points_from_file(path)
    log_step(f"Loaded {len(points)} points from file")
    log_step("=" * 50)
    log_step("ALGORITHM WORKING:")
    log_step("=" * 50)
    
    distance, point_a, point_b = find_closest_pair(points, log_step)
    
    log_step("=" * 50)
    log_step("RESULTS:")
    log_step("=" * 50)
    
    info: Dict[str, str] = {
        "input_points": str(len(points)),
        "file_path": str(path),
    }
    info["closest_point_a"] = f"{point_a}"
    info["closest_point_b"] = f"{point_b}"
    info["minimum_distance"] = f"{distance:.6f}"
    
    if len(points) <= 600:
        log_step("Verifying with brute force...")
        brute_distance = min(
            math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1])
            for i in range(len(points))
            for j in range(i + 1, len(points))
        )
        info["validation"] = (
            f"Brute force distance {brute_distance:.6f} "
            f"({'matches' if abs(brute_distance - distance) < 1e-6 else 'differs from'}) D&C result."
        )
        log_step(info["validation"])
    else:
        info["validation"] = "Brute force verification skipped due to dataset size."
        log_step(info["validation"])
    
    return info


def integer_multiplication_handler(path: pathlib.Path, log_step: Callable[[str], None]) -> Dict[str, str]:
    a_str, b_str = load_integer_pair(path)
    log_step(f"Loaded two numbers from file")
    log_step("=" * 50)
    log_step("ALGORITHM WORKING:")
    log_step("=" * 50)
    
    product_int = karatsuba_from_strings(a_str, b_str, log_step)
    
    log_step("=" * 50)
    log_step("RESULTS:")
    log_step("=" * 50)
    
    product = str(product_int)
    builtin = str(int(a_str.strip()) * int(b_str.strip()))
    
    info: Dict[str, str] = {
        "digits_a": str(len(a_str.strip())),
        "digits_b": str(len(b_str.strip())),
        "file_path": str(path),
    }
    info["karatsuba_product"] = product
    info["verification"] = (
        "Matches Python's built-in multiplication." if product == builtin else "Mismatch detected!"
    )
    log_step(f"Product: {product}")
    log_step(info["verification"])
    
    return info


def populate_dataset_panel(frame: ttk.LabelFrame, summary: Dict[str, List[dict]]) -> None:
    ttk.Label(frame, text="Available datasets:", font=("Segoe UI", 10, "bold")).grid(
        row=0, column=0, sticky="w"
    )

    text = tk.Text(frame, height=10, width=80, state=tk.NORMAL, wrap=tk.WORD)
    text.grid(row=1, column=0, sticky="nsew")
    frame.rowconfigure(1, weight=1)

    for entry in summary.get("closest_pair_files", []):
        text.insert(tk.END, f"[Closest Pair] {pathlib.Path(entry['file']).name} -> size={entry['size']}\n")
    for entry in summary.get("integer_multiplication_files", []):
        text.insert(
            tk.END,
            f"[Integer Multiplication] {pathlib.Path(entry['file']).name} -> digits={entry['size']}\n",
        )

    text.configure(state=tk.DISABLED)


def load_summary() -> Dict[str, List[dict]]:
    summary_path = DATA_DIR / "summary.json"
    if not summary_path.exists():
        return {"closest_pair_files": [], "integer_multiplication_files": []}
    with summary_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    root = tk.Tk()
    root.title("Divide-and-Conquer Algorithms Explorer")
    root.geometry("850x700")

    summary = load_summary()

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=16, pady=16)

    closest_tab = AlgorithmUI(
        notebook,
        "Closest Pair of Points",
        file_types=[("Point Dataset", "*.txt"), ("All Files", "*.*")],
        handler=closest_pair_handler,
    )
    notebook.add(closest_tab, text="Closest Pair")

    integer_tab = AlgorithmUI(
        notebook,
        "Large Integer Multiplication",
        file_types=[("Integer Dataset", "*.txt"), ("All Files", "*.*")],
        handler=integer_multiplication_handler,
    )
    notebook.add(integer_tab, text="Integer Multiplication")

    sidebar = ttk.LabelFrame(root, text="Dataset Reference", padding=12)
    sidebar.pack(fill=tk.BOTH, expand=False, padx=16, pady=(0, 16))
    populate_dataset_panel(sidebar, summary)

    root.mainloop()


if __name__ == "__main__":
    main()


