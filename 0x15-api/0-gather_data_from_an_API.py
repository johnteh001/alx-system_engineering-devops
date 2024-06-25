#!/usr/bin/python3
"""Gather data from API"""

if __name__ == "__main__":
    import requests
    import sys

    u_id = sys.argv[1]
    u_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    user = requests.get(u_url).json()
    tasks = requests.get(api_url).json()
    user_name = user.get("name")
    task_done = 0
    total = 0
    task_names = []
    for task in tasks:
        user_ID = task.get("userId")
        if user_ID == int(u_id):
            total += 1
            if task.get("completed") is True:
                task_done += 1
                task_names.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(user_name,
          task_done, total))
    for n in task_names:
        print("\t {}".format(n))
