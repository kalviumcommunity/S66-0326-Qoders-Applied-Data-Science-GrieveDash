"""Milestone demo: array shape, dimensions, and index positions in NumPy."""

import numpy as np


def show_shapes() -> None:
    print("\n1) Array shape and dimensions")
    one_d = np.array([10, 20, 30, 40])
    two_d = np.array([[1, 2, 3], [4, 5, 6]])

    print(f"1D array: {one_d}")
    print(f"1D shape: {one_d.shape}, ndim: {one_d.ndim}")

    print(f"2D array:\n{two_d}")
    print(f"2D shape: {two_d.shape}, ndim: {two_d.ndim}")


def index_examples() -> None:
    print("\n2) Indexing examples")
    one_d = np.array([10, 20, 30, 40])
    two_d = np.array([[1, 2, 3], [4, 5, 6]])

    print(f"one_d[0] = {one_d[0]}")
    print(f"one_d[2] = {one_d[2]}")

    print(f"two_d[0, 0] = {two_d[0, 0]}")
    print(f"two_d[1, 2] = {two_d[1, 2]}")


def layout_visualization() -> None:
    print("\n3) Visualizing layout (rows and columns)")
    grid = np.array([[7, 8, 9], [10, 11, 12]])

    print("Grid:")
    print(grid)
    print("Row 0:", grid[0])
    print("Row 1:", grid[1])
    print("Column 0:", grid[:, 0])
    print("Column 2:", grid[:, 2])


def run_demo() -> None:
    show_shapes()
    index_examples()
    layout_visualization()


if __name__ == "__main__":
    run_demo()
