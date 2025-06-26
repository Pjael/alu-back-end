#!/usr/bin/python3

"""Using what you did in the task #0, extend your Python script to export data
in the JSON format."""

import json
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

        user_id = employee_id
        username = employee['username']
        employee_tasks = [
            task for task in todos if task['userId'] == employee_id
        ]

        tasks_list = []
        for task in employee_tasks:
            tasks_list.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })
        data = {str(user_id): tasks_list}

        filename = f"{user_id}.json"
        with open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    emp = EmployeeToDoList()
    emp.todo_list(1)
