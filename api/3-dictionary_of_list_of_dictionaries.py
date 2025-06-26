#!/usr/bin/python3
#Using what you did in the task #0, extend your Python script to export data in the JSON format.

import requests
import json

def export_all_employees_to_json():
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in todos if task['userId'] == user_id]
        tasks_list = []
        for task in user_tasks:
            tasks_list.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })
        data[str(user_id)] = tasks_list
            
    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4)
            
if __name__ == "__main__":
    export_all_employees_to_json()