#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import requests
import sys

EMPLOYEE_ID = sys.argv[1]

# make the API call to get employee information
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}")
employee_data = response.json()
employee_name = employee_data["name"]

response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}")
todo_list = response.json()

# count completed tasks
completed_tasks = [todo for todo in todo_list if todo["completed"]]
num_completed_tasks = len(completed_tasks)
total_num_tasks = len(todo_list)

# print employee TODO list progress
print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

# print completed tasks
for task in completed_tasks:
    print(f"\t{task['title']}")
