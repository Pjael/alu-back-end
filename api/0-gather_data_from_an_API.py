#!/usr/bin/python3

"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

from urllib import request, error 
import sys
import json

API_BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_json(url): #return parsed JSON data from a URL or raised an exception
    try: 
        with request.urlopen(url) as resp:
        # resp.read() returns bytes; decode using resp.headers.get_content_charset or utf-8 fallback
            charset = resp.headers.get_content_charset() or "utf-8" 
            data = resp.read().decode(charset)
            return json.loads(data)
    except error.HTTPError as e:
        #raise HTTPEroor so caller can decide how to handle it
        raise
    except error.URLError as e:
        raise
    
def main():
    if len(sys.argv) != 2:
        print("Usage: {} <EMPLOYEE_ID>".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    #validate integer argument
    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError()
    except ValueError:
        print("EMPLOYEE_ID must be a positive integer.", file=sys.stderr)
        sys.exit(1)
    
    user_url = f"{API_BASE_URL}/USERS/{employee_id}"
    todos_url = f"{API_BASE_URL}/TODOS?userId={employee_id}"
    
    try:
        user = fetch_json(user_url)
    except error.HTTPError as e:
        if e.code == 404:
            print(f"User with id {employee_id} not found.", file=sys.stderr)
            sys.exit(2)
        else:
            print(f"HTTP error fetching user: {e}", file=sys.stderr)
            sys.exit(3)
    except error.URLError as e:
        print(f"Network error fetching user: {e}", file=sys.stderr)
        sys.exit(4)
    
    #json placeholder returns an empty list for non-existing user(or 404);  ensures it contains a name
    if not user or "name" not in user: 
        print(f"User with id {employee_id} not found or no name returned.", file=sys.stderr)
        sys.exit(2)
    
    employee_name = user["name"]
    
    try:
        todos = fetch_json(todos_url)
    except error.HTTPError as e:
        print(f"HTTP error fetching TODOs: {e}", file=sys.stderr)
        sys.exit(5)
    except error.URLError as e:
        print(f"Network error fetching TODOs: {e}", file=sys.stderr)
        sys.exit(6)
        
    #todos should be a list
    if not isinstance(todos, list):
        print(f"Unexpected todos response format.", file=sys.stderr)
        sys.exit(7)
    total_tasks = len(todos)
    completed_tasks_list = [task for task in todos if task.get("completed") is True]
    completed_count = len(completed_tasks_list)
    
    #print output in the format required
    print(f"Empolyee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks_list:
        #each completed taks title on its own line with 1 tabulation and 1 space before the title
        title = task.get("title", "")
        print("\t" + title)

if __name__ == "__main__":
    main()