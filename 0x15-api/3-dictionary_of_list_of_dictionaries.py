#!/usr/bin/python3
"""
a Python script that extracts a user details into a JSON file
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    import json

    # Extract data from API
    user_url = f"https://jsonplaceholder.typicode.com/users/"
    todo_url = f"https://jsonplaceholder.typicode.com/todos/"
    user_json = requests.get(user_url)
    todo_json = requests.get(todo_url)

    # Convert JSON data to Python objects
    users = user_json.json()
    todos = todo_json.json()

    # Parse data to get information
    output_dict = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                task_dict = {
                        "username": user.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed")
                        }
                task_list.append(task_dict)
        output_dict[str(user.get("id"))] = task_list

    with open("todo_all_employees.json", 'w') as fp:
        json.dump(output_dict, fp)
