#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her
TODO list progress.
Now exporting data in the CSV format!
"""
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get("http://jsonplaceholder.typicode.com/users/" +
                        argv[1]).json()
    task_todo = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId=" + argv[1]).json()
    user_id = str(user.get("id"))

    with open(user_id + ".csv", "w") as csv_file:
        username = user.get("username")
        user_id = user.get("id")

        for task in task_todo:
            csv_file.write('"{}","{}","{}","{}"\n'.
                           format(user_id, username, task.get("completed"),
                                  task.get("title")))
