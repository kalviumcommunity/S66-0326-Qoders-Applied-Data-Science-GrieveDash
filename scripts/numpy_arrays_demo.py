"""Milestone demo: creating NumPy arrays from Python lists."""

import numpy as np


def create_arrays() -> None:
    print("\n1) Creating arrays from lists")
    one_d_list = [1, 2, 3, 4, 5]
    two_d_list = [[1, 2, 3], [4, 5, 6]]

    one_d_array = np.array(one_d_list)
    two_d_array = np.array(two_d_list)

    print(f"1D array: {one_d_array}")
    print(f"2D array:\n{two_d_array}")


def inspect_properties() -> None:
    print("\n2) Inspecting array properties")
    sample = np.array([10, 20, 30])

    print(f"shape: {sample.shape}")
    print(f"dtype: {sample.dtype}")
    print(f"ndim: {sample.ndim}")


def basic_operations() -> None:
    print("\n3) Basic array operations")
    values = np.array([1, 2, 3, 4])
    print(f"values: {values}")
    print(f"values + 2: {values + 2}")
    print(f"values * 3: {values * 3}")


def list_vs_array() -> None:
    print("\n4) List vs array behavior")
    numbers_list = [1, 2, 3]
    numbers_array = np.array([1, 2, 3])

    print(f"list + list: {numbers_list + numbers_list}")
    print(f"array + array: {numbers_array + numbers_array}")


def run_demo() -> None:
    create_arrays()
    inspect_properties()
    basic_operations()
    list_vs_array()


if __name__ == "__main__":
    run_demo()
