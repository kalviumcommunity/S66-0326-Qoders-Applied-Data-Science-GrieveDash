"""Milestone demo: for and while loops for iterative data processing."""


def for_loop_examples() -> None:
    print("\n1) for loop over range")
    for i in range(1, 6):
        print(f"Processing batch {i}")

    print("\n2) for loop over list")
    issue_types = ["water", "roads", "garbage", "electricity"]
    for issue in issue_types:
        print(f"Reviewing issue type: {issue}")


def while_loop_examples() -> None:
    print("\n3) while loop with condition")
    pending = 3
    while pending > 0:
        print(f"Pending complaints remaining: {pending}")
        pending -= 1
    print("All pending complaints processed.")


def control_flow_examples() -> None:
    print("\n4) break and continue")
    complaints = ["resolved", "pending", "in_progress", "resolved", "pending"]
    for status in complaints:
        if status == "resolved":
            continue
        print(f"Handling status: {status}")
        if status == "in_progress":
            print("Encountered in_progress, stopping early.")
            break


def infinite_loop_prevention_example() -> None:
    print("\n5) preventing infinite loops")
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        print(f"Attempt {attempts + 1} of {max_attempts}")
        attempts += 1
    print("Loop stopped safely after max attempts.")


def run_demo() -> None:
    for_loop_examples()
    while_loop_examples()
    control_flow_examples()
    infinite_loop_prevention_example()


if __name__ == "__main__":
    run_demo()
