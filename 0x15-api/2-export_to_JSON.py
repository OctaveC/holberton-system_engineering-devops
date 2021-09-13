#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her
TODO list progress.
Now exporting data in the JSON format!
"""
import json
import requests
from sys import argv



if __name__ == "__main__":
    user = requests.get("http://jsonplaceholder.typicode.com/users/" +
                        argv[1]).json()
    task_todo = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId=" + argv[1]).json()

    with open("{}.json".format(argv[1]), "w") as user_id:
        json.dump({argv[1]: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username')
        } for task in task_todo]}, user_id)
