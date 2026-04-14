"""Milestone demo: defining and calling Python functions."""


def format_complaint(complaint_id: int, issue_type: str) -> str:
    return f"Complaint #{complaint_id} - {issue_type}"


def resolve_complaint(status: str) -> str:
    if status == "resolved":
        return "Already resolved."
    return "Marked as resolved."


def add_priority(base_priority: str, boost: bool) -> str:
    if boost:
        return "high"
    return base_priority


def scope_example() -> None:
    message = "local"
    print(f"Inside function, message = {message}")


def run_demo() -> None:
    print("\n1) Defining and calling a function")
    summary = format_complaint(101, "water")
    print(summary)

    print("\n2) Function with parameters and return value")
    result = resolve_complaint("pending")
    print(result)

    print("\n3) Parameters and arguments")
    updated_priority = add_priority("medium", boost=True)
    print(f"Updated priority: {updated_priority}")

    print("\n4) Basic function scope")
    message = "global"
    scope_example()
    print(f"Outside function, message = {message}")


if __name__ == "__main__":
    run_demo()
