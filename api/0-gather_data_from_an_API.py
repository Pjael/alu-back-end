#!/usr/bin/python3

"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    sys.exit(1)

# Get the employee ID from command line argument and convert it to integer
try:
    emp_id = int(sys.argv[1])
except ValueError:
    print("Employee ID must be an integer.")
    sys.exit(1)
    
base_url = "https://jsonplaceholder.typicode.com"
user = requests.get(f"{base_url}/users/{emp_id}").json()
todos = requests.get(f"{base_url}/todos", params={"userId": emp_id}).json()

employee_name = user.get("name")
total_tasks = len(todos)
done_tasks = [task for task in todos if task.get("completed")]
done_count = len(done_tasks)
print(employee_name, done_count, total_tasks)

print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")

for task in done_tasks:
    print("\t " + task.get("title"))
