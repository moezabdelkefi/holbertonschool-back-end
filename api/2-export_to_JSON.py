#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import json
import requests
import sys
if __name__ == '__main__':
    t = sys.argv[1]
    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + t)
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + t)
    employee = response.json()
    todos = todo.json()
    id = employee['id']
    name = employee['username']
    lis = {}
    m = []
    lis[t] = m
    for i in todos:
        p = {}
        p["task"] = i['title']
        p["completed"] = i['completed']
        p["username"] = name
        m.append(p)
    with open(f'{t}.json', 'w') as file:
        json.dump(lis, file)