"""Milestone demo: readable variable names and useful comments (PEP 8 basics)."""


def poor_vs_good_names() -> None:
    print("\n1) Poor vs good variable names")

    # Poor naming (vague and hard to read)
    x = 12
    y = 5
    z = x - y
    print(f"Poor naming result: {z}")

    # Good naming (clear intent)
    total_complaints = 12
    resolved_complaints = 5
    unresolved_complaints = total_complaints - resolved_complaints
    print(f"Good naming result: {unresolved_complaints}")


def useful_comments_example() -> None:
    print("\n2) Useful comments (explain intent)")

    raw_status = "In-Progress"

    # Normalize status values to keep downstream logic consistent
    normalized_status = raw_status.strip().lower().replace("in-progress", "in_progress")
    print(f"Normalized status: {normalized_status}")

    resolution_time_days = 0

    # Unresolved complaints should not have a positive resolution time
    if normalized_status != "resolved":
        resolution_time_days = 0

    print(f"Resolution time days: {resolution_time_days}")


def pep8_basics_example() -> None:
    print("\n3) PEP 8 basics (snake_case and constants)")

    # Constants use UPPER_CASE naming
    MAX_RETRY_ATTEMPTS = 3

    retry_attempt = 1
    while retry_attempt <= MAX_RETRY_ATTEMPTS:
        print(f"Attempt {retry_attempt} of {MAX_RETRY_ATTEMPTS}")
        retry_attempt += 1


def run_demo() -> None:
    poor_vs_good_names()
    useful_comments_example()
    pep8_basics_example()


if __name__ == "__main__":
    run_demo()
