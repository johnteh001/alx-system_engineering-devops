#!/usr/bin/python3
"""Export data to JSON for all employees"""

if __name__ == "__main__":
    import requests
    import json

    u_url = "https://jsonplaceholder.typicode.com/users/"
    api_url = "https://jsonplaceholder.typicode.com/todos/"
    users = requests.get(u_url).json()
    tasks = requests.get(api_url).json()
    task_record = {}
    for user in users:
        u_id = user.get("id")
        task_record['{}'.format(u_id)] = []
        for task in tasks:
            user_ID = task.get("userId")
            if user_ID == int(u_id):
                record = {}
                record['username'] = user.get('username')
                record['task'] = task.get("title")
                record['completed'] = task.get('completed')
                task_record[str(u_id)].append(record)

    with open("todo_all_employees.json", "w") as fil:
        data = json.dumps(task_record)
        fil.write(data)
