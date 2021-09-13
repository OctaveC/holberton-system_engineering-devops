#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her
TODO list progress.
Now exporting data in the JSON format!
And records all tasks from all employees!
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get("http://jsonplaceholder.typicode.com/users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        user_tasks = {}
        for user_id in user:
            username = user_id.get("username")
            user_id = str(user_id.get("id"))
            todo = requests.get("http://jsonplaceholder.typicode.com/todos?" +
                                 "userId=" + user_id).json()
            task_list = []

            for task in todo:
                tasks_dict = {"task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": username}
                task_list.append(tasks_dict)

            user_tasks[user_id] = task_list

        json.dump(user_tasks, jsonfile)
