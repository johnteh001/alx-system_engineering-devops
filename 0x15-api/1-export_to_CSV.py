#!/usr/bin/python3
"""Export data to CSV"""

if __name__ == "__main__":
    import requests
    import sys
    import csv

    u_id = sys.argv[1]
    u_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    user = requests.get(u_url).json()
    tasks = requests.get(api_url).json()
    task_record = []
    for task in tasks:
        user_ID = task.get("userId")
        if user_ID == int(u_id):
            record = []
            record.append(u_id)
            record.append(user.get("username"))
            record.append(str(task.get("completed")))
            record.append(task.get("title"))
            task_record.append(record)

    with open("{}.csv".format(u_id), "w") as fil:
        data = csv.writer(fil, quoting=csv.QUOTE_ALL)
        data.writerows(task_record)
