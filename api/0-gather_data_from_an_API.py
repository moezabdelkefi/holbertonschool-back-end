#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
import sys


employee_id = sys.argv[1]
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code == 200:
    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)
    employee_name = todos[0]["userId"]
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
else:
    print(f"Error retrieving TODO list: {response.status_code}")
