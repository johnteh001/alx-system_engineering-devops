#!/usr/bin/python3
"""Export data to CSV"""

if __name__ == "__main__":
    import requests
    import sys
    import json

    u_id = sys.argv[1]
    u_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    user = requests.get(u_url).json()
    tasks = requests.get(api_url).json()
    task_record = {}
    task_record['{}'.format(u_id)] = []
    for task in tasks:
        user_ID = task.get("userId")
        if user_ID == int(u_id):
            record = {}
            record['username'] = user.get('username')
            record['completed'] = task.get('completed')
            record['task'] = task.get("title")
            task_record[u_id].append(record)

    with open("{}.json".format(u_id), "w") as fil:
        data = json.dumps(task_record)
        fil.write(data)
