#!/usr/bin/python3
"""Returns information about a given employee's TODO list progress."""

import requests
import sys


def get_employee_todo_progress(emp_id):
    """Fetch and display TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, emp_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": emp_id}
    ).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    done_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done_count, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


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
