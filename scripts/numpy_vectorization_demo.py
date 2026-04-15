"""Milestone demo: vectorized NumPy operations vs Python loops."""

import numpy as np


def loop_vs_vectorized_arithmetic() -> None:
    print("\n1) Loop-based vs vectorized arithmetic")
    values = np.array([10, 20, 30, 40, 50])

    loop_result = []
    for value in values:
        loop_result.append((value * 2) + 5)
    loop_result = np.array(loop_result)

    vectorized_result = (values * 2) + 5

    print(f"Input values:         {values}")
    print(f"Loop result:          {loop_result}")
    print(f"Vectorized result:    {vectorized_result}")
    print(f"Results match:        {np.array_equal(loop_result, vectorized_result)}")


def vectorized_comparisons() -> None:
    print("\n2) Vectorized comparisons and conditions")
    resolution_days = np.array([1, 5, 12, 0, 8, 15])

    slow_cases = resolution_days > 7
    active_cases = resolution_days == 0

    print(f"Resolution days:      {resolution_days}")
    print(f"days > 7:             {slow_cases}")
    print(f"days == 0:            {active_cases}")


def shape_compatibility_check() -> None:
    print("\n3) Shape compatibility reminder")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(f"a shape: {a.shape}, b shape: {b.shape}")
    print(f"a + b: {a + b}")


def run_demo() -> None:
    loop_vs_vectorized_arithmetic()
    vectorized_comparisons()
    shape_compatibility_check()


if __name__ == "__main__":
    run_demo()
