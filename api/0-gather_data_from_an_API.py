#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import json
import requests
from sys import argv

if __name__ == '__main__':
    resp_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    resp_users = requests.get('https://jsonplaceholder.typicode.com/users')

    todos_count = 0
    todos_done = 0
    for i in resp_todos.json():
        if i['userId'] == int(argv[1]):
            todos_count = todos_count + 1
            if i['completed'] is True:
                todos_done = todos_done + 1
    for i in resp_users.json():
        if i['id'] == int(argv[1]):
            emp = i['name']

    print(f"Employee {emp} is done with tasks({todos_done}/{todos_count}):")

    for i in resp_todos.json():
        if i['userId'] == int(argv[1]):
            if i['completed'] is True:
                print(f"\t {i['title']}")
