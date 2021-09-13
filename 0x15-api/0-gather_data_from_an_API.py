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
    mub_todo = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId=" + argv[1]).json()
    num_total = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId=" + argv[1] +
        "&completed=true").json()

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(num_todo), len(num_total)))
    for task in done:
        print("\t " + task.get("title"))
