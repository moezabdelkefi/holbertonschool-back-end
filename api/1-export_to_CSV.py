#!/usr/bin/python3

"""
This script retrieves information about a given employee's TODO list progress from a REST API.
It takes an integer employee ID as a command line argument and prints the progress information to the console.
It also exports the employee's TODO list to a CSV file with the format "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".
"""

import requests
import csv
import sys

EMPLOYEE_ID = sys.argv[1]

# make the API call to get employee information
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}")
employee_data = response.json()
employee_name = employee_data["name"]

# make the API call to get TODO list for the employee
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYEE_ID}")
todo_list = response.json()

# open a CSV file for writing
filename = f"{EMPLOYEE_ID}.csv"
with open(filename, mode='w', newline='') as csv_file:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    # write each task to the CSV file
    for task in todo_list:
        writer.writerow({
            'USER_ID': EMPLOYEE_ID,
            'USERNAME': employee_name,
            'TASK_COMPLETED_STATUS': str(task['completed']),
            'TASK_TITLE': task['title']
        })

# count completed tasks
completed_tasks = [todo for todo in todo_list if todo["completed"]]
num_completed_tasks = len(completed_tasks)
total_num_tasks = len(todo_list)

# print employee TODO list progress
print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_num_tasks}):")

# print completed tasks
for task in completed_tasks:
    print(f"\t{task['title']}")
