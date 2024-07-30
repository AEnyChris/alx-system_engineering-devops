#!/usr/bin/python3
"""
a Python script that, a user details into a CSV file
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    import json

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
    username = user_data.get("username")
    task_list = []

    for task in tasks:
        task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
                }
        task_list.append(task_dict)

    output_dict = {str(user_id): task_list}

    with open(f"{user_id}.json", 'w') as fp:
        json.dump(output_dict, fp)
