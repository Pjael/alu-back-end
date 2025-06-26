#Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress

#!usr/bin.python3

import requests

class EmployeeToDoList():
    def todoList(self, employee_id):
        users = requests.get('https://jsonplaceholder.typicode.com/users').json()
        todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
        employee = next((user for user in users if user['id'] == employee_id), None)
        if not employee:
            print("Employee not found")
            return
        
        EMPLOYEE_NAME = employee['name']
        employee_tasks = [task for task in todos if task['userId'] == employee_id]
        TOTAL_NUMBER_OF_TASKS = len(employee_tasks)
        NUMBER_OF_DONE_TASKS = len([task for task in employee_tasks if task['completed']])
        
        done_tasks = [task for task in employee_tasks if task['completed']]
        print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in done_tasks:
            print(f"\t {task['title']}")
            
        # Replace 1 with any valid employee ID
            
if __name__ == "__main__":
    emp = EmployeeToDoList()
    emp.todoList(1)     