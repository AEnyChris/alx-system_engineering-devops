#!/usr/bin/python3
"""A script that returns the todo details of a user"""

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
todo_list = todo_json.json()

# Parse data to get information
empname = user_data["name"]
task_done = [task for task in todo_list if task["completed"] is True]
no_task_done = len(task_done)
total_tasks = len(todo_list)

# Information outuput
print(
        f"Employee {empname} is done with tasks({no_task_done}/{total_tasks})"
     )

for task in task_done:
    print(f"\t {task['title']}")
