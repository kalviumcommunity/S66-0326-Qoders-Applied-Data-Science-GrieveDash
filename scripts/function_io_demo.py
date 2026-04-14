"""Milestone demo: passing data into functions and returning results."""


def calculate_resolution_rate(resolved: int, total: int) -> float:
    if total == 0:
        return 0.0
    return round((resolved / total) * 100, 1)


def normalize_status(status: str) -> str:
    cleaned = status.strip().lower()
    if cleaned in {"in progress", "in-progress"}:
        return "in_progress"
    return cleaned


def summarize_issue(issue_type: str, count: int) -> str:
    return f"{issue_type}: {count} complaints"


def run_demo() -> None:
    print("\n1) Parameters and arguments")
    normalized = normalize_status("In-Progress")
    print(f"Normalized status: {normalized}")

    print("\n2) Returning values")
    rate = calculate_resolution_rate(resolved=12, total=20)
    print(f"Resolution rate: {rate}%")

    print("\n3) Using returned results")
    summary = summarize_issue("water", 8)
    print(summary)

    print("\n4) Reusing returned values in another call")
    status = normalize_status("Resolved")
    result = summarize_issue(status, 5)
    print(result)


if __name__ == "__main__":
    run_demo()
