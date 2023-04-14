#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""


if __name__ == '__main__':
    import requests
    import sys

    t = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + t)
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + t)

    employee = response.json()
    todos = todos.json()
    id = employee['id']
    name = employee['username']

    with open(f'{t}.csv', 'w') as file:
        for i in todos:
            Ta = i['completed']
            TASK_TITLE = i['title']
            TASK_COMPLETED_STATUS = i['completed']
            TASK_TITLE = i['title']
            file.write(
                f"\"{id}\",\"{name}\",\"{Ta}\",\"{TASK_TITLE}\"\n")