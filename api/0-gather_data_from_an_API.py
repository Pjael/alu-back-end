#!/usr/bin/python3
"""Returns information about a given employee's TODO list progress."""

import requests
import sys


def get_employee_todo_progress(emp_id):
    """Fetch and display TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/{emp_id}").json()
    todos = requests.get(
        f"{base_url}/todos", params={"userId": emp_id}
    ).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    done_count = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({done_count}/{total_tasks}):"
    )

    for task in done_tasks:
        print("\t " + task.get("title"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(emp_id)
