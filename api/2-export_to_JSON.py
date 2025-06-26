#!/usr/bin/python3
#Using what you did in the task #0, extend your Python script to export data in the JSON format.


import requests
import json

class EmployeeToDoList():
    def todoList(self, employee_id):
        users = requests.get('https://jsonplaceholder.typicode.com/users').json()
        todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
        employee = next((user for user in users if user['id'] == employee_id), None)
        if not employee:
            print("Employee not found")
            return
        
        USER_ID = employee_id
        USERNAME = employee['username']
        employee_tasks = [task for task in todos if task['userId'] == employee_id]
        
        tasks_list = []
        for task in employee_tasks: 
            tasks_list.append({
                "tasks": task['title'],
                "completed": task['completed'],
                "username": USERNAME
            })
        data = {str(USER_ID): tasks_list}
        
        #write to JSON file
        filename = f"{USER_ID}.json"
        with open(filename,"w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        
            
        
#for testing purposes, can Replace 1 with any valid employee ID      
if __name__ == "__main__":
    emp = EmployeeToDoList()
    emp.todoList(1)     
    