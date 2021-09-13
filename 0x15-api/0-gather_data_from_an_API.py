#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her
TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get("http://jsonplaceholder.typicode.com/users/" +
                        argv[1]).json()
    total = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId=" + argv[1]).json()
    todo = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId=" + argv[1] +
        "&completed=true").json()

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(todo), len(total)))
    for task in todo:
        print("\t " + task.get("title"))
