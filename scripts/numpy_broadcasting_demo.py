"""Milestone demo: understanding NumPy broadcasting with simple examples."""

import numpy as np


def scalar_broadcasting() -> None:
    print("\n1) Scalar to array broadcasting")
    values = np.array([10, 20, 30, 40])
    scalar = 5

    print(f"values shape: {values.shape}")
    print(f"values: {values}")
    print(f"values + {scalar}: {values + scalar}")
    print(f"values * {scalar}: {values * scalar}")


def one_d_broadcasting() -> None:
    print("\n2) Broadcasting between 1D arrays")
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])

    print(f"a shape: {a.shape}, b shape: {b.shape}")
    print(f"a + b: {a + b}")

    incompatible = np.array([1, 2])
    print(f"incompatible shape: {incompatible.shape}")
    try:
        _ = a + incompatible
    except ValueError as error:
        print(f"Incompatible example: {error}")


def two_d_one_d_broadcasting() -> None:
    print("\n3) Broadcasting between 2D and 1D arrays")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    row_adjustment = np.array([10, 20, 30])
    col_adjustment = np.array([100, 200])

    print(f"matrix shape: {matrix.shape}")
    print(f"row_adjustment shape: {row_adjustment.shape}")
    print("matrix + row_adjustment:")
    print(matrix + row_adjustment)

    print(f"col_adjustment shape: {col_adjustment.shape}")
    print("matrix + col_adjustment[:, None]:")
    print(matrix + col_adjustment[:, None])


def run_demo() -> None:
    scalar_broadcasting()
    one_d_broadcasting()
    two_d_one_d_broadcasting()


if __name__ == "__main__":
    run_demo()
