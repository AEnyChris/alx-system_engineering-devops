#!/usr/bin/python3
"""
a Python script that, a user details into a CSV file
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    # Extract data from API
    user_id = argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos/"
    user_json = requests.get(user_url)
    todo_json = requests.get(todo_url)

    # Convert JSON data to Python objects
    user_data = user_json.json()
    tasks = todo_json.json()

    # Parse data to get information
    empname = user_data.get("name")
    task_done = [task for task in tasks if task.get("completed") is True]

    with open(f"{user_id}.csv", 'a') as fs:
        for task in tasks:
            fs.write('"{}","{}","{}","{}"\n'.format(
                user_id, empname, task.get("completed"), task.get("title")))
