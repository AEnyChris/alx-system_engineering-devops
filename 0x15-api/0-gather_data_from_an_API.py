#!/usr/bin/python3
"""
a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

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
    empname = user_data.get("name")
    task_done = [task for task in todo_list if task.get("completed") is True]
    no_task_done = len(task_done)
    total_tasks = len(todo_list)

    # Information outuput
    print("Employee {} is done with tasks({}/{}):".format(
            empname, no_task_done, total_tasks))

    for task in task_done:
        print(f"\t {task['title']}")
