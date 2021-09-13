#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her
TODO list progress.
Now exporting data in the JSON format!
And records all tasks from all employees!
"""
import requests
from sys import argv
import json


if __name__ == "__main__":
    user = requests.get("http://jsonplaceholder.typicode.com/users/").json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    filename = "todo_all_employees.json"

    with open(filename, "w") as f:
        dumpo = {ite2.get("id"): [{'task': i.get('title'),
                                   'completed': i.get('completed'),
                                   'username': i.get('username')} for i in todo
                                  if ite2.get("id") == i.get('userId')]
                 for ite2 in user}
        json.dump(dumpo, f)
