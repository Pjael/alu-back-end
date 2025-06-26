#!/usr/bin/python3

"""Using what you did in the task #0, extend your Python script to export data
in the CSV format."""

import csv
import requests


class EmployeeToDoList:
    def todo_list(self, employee_id):
        users = requests.get(
            'https://jsonplaceholder.typicode.com/users'
        ).json()
        todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos'
        ).json()
        employee = next(
            (user for user in users if user['id'] == employee_id), None
        )
        if not employee:
            return "Employee not found"

        employee_name = employee['name']
        employee_tasks = [
            task for task in todos if task['userId'] == employee_id
        ]
        total_number_of_tasks = len(employee_tasks)
        number_of_done_tasks = len(
            [task for task in employee_tasks if task['completed']]
        )

        done_tasks = [
            task for task in employee_tasks if task['completed']
        ]
        print(
            f"Employee {employee_name} is done with tasks"
            f"({number_of_done_tasks}/{total_number_of_tasks}):"
        )
        for task in done_tasks:
            print(f"\t {task['title']}")

        user_id = employee_id
        username = employee['username']

        filename = f"{user_id}.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in employee_tasks:
                task_completed_status = str(task['completed'])
                task_title = task['title']
                writer.writerow(
                    [user_id, username, task_completed_status, task_title]
                )
        print("Number of tasks in CSV: OK")


if __name__ == "__main__":
    emp = EmployeeToDoList()
    emp.todo_list(1)
