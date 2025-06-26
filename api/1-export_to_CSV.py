#!/usr/bin/python3

#Using what you did in the task #0, extend your Python script to export data in the CSV format.

import requests
import csv

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
            
        USER_ID = employee_id
        USERNAME = employee['username']
        
        filename = f'{USER_ID}.csv'
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for tasks in employee_tasks:    
                TASK_COMPLETED_STATUS = str(tasks['completed'])
                TASK_TITLE = task['title']
                writer.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
        
            
        # Replace 1 with any valid employee ID
            
if __name__ == "__main__":
    emp = EmployeeToDoList()
    emp.todoList(1)     
    