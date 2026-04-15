"""Milestone demo: basic mathematical operations on NumPy arrays."""

import numpy as np


def element_wise_operations() -> None:
    print("\n1) Element-wise array operations")
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])

    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a + b: {a + b}")
    print(f"a - b: {a - b}")
    print(f"a * b: {a * b}")
    print(f"a / b: {a / b}")


def scalar_operations() -> None:
    print("\n2) Scalar operations")
    values = np.array([2, 4, 6, 8])

    print(f"values: {values}")
    print(f"values + 3: {values + 3}")
    print(f"values * 2: {values * 2}")
    print(f"values / 2: {values / 2}")


def list_vs_array_behavior() -> None:
    print("\n3) List vs array behavior")
    numbers_list = [1, 2, 3]
    numbers_array = np.array([1, 2, 3])

    print(f"list + list: {numbers_list + numbers_list}")
    print(f"array + array: {numbers_array + numbers_array}")


def shape_compatibility_note() -> None:
    print("\n4) Shape compatibility reminder")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(f"Compatible shapes: {a.shape} and {b.shape}")
    print(f"a + b: {a + b}")


def run_demo() -> None:
    element_wise_operations()
    scalar_operations()
    list_vs_array_behavior()
    shape_compatibility_note()


if __name__ == "__main__":
    run_demo()
