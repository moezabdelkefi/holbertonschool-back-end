#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in the JSON format.
"""


import requests
import json
import sys

EMPLOYEE_ID = sys.argv[1]

# make the API call to get employee information
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}")
employee_data = response.json()
employee_name = employee_data["username"]

# make the API call to get TODO list for the employee
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}")
todo_list = response.json()

tasks = []
for task in todo_list:
    task_dict = {"task": task['title'], "completed": task['completed'], "username": employee_name}
    tasks.append(task_dict)

json_data = {EMPLOYEE_ID: tasks}

# write the JSON data to a file
filename = f"{EMPLOYEE_ID}.json"
with open(filename, mode='w') as json_file:
    json.dump(json_data, json_file, indent=4)

# count completed tasks
completed_tasks = [todo for todo in todo_list if todo["completed"]]
num_completed_tasks = len(completed_tasks)
total_num_tasks = len(todo_list)

print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

# print completed tasks
for task in completed_tasks:
    print(f"\t{task['title']}")
