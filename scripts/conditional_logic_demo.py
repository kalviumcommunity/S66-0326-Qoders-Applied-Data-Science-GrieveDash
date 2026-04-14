"""Milestone demo: conditional statements for data logic."""


def basic_if_example(complaints_today: int) -> None:
    print("\n1) Basic if statement")
    if complaints_today > 20:
        print("High complaint volume detected.")


def if_else_example(status: str) -> None:
    print("\n2) if-else branching")
    if status == "resolved":
        print("Complaint is resolved.")
    else:
        print("Complaint is not resolved yet.")


def if_elif_else_example(priority: str) -> None:
    print("\n3) if-elif-else branching")
    if priority == "high":
        print("Escalate immediately.")
    elif priority == "medium":
        print("Assign to standard queue.")
    else:
        print("Track in low-priority queue.")


def logical_operator_examples(priority: str, status: str, resolution_time: int) -> None:
    print("\n4) Logical operators")

    if priority == "high" and status != "resolved":
        print("AND: High-priority unresolved complaint needs urgent action.")

    if status == "pending" or status == "in_progress":
        print("OR: Complaint is still active.")

    if not (resolution_time > 0):
        print("NOT: Resolution time is not greater than zero.")


def run_demo() -> None:
    basic_if_example(complaints_today=27)
    if_else_example(status="in_progress")
    if_elif_else_example(priority="medium")
    logical_operator_examples(priority="high", status="pending", resolution_time=0)


if __name__ == "__main__":
    run_demo()
