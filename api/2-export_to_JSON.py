#!/usr/bin/python3
"""
This module exports an employee's TODO list records to a JSON file.

It takes an employee ID parameter from the command line, retrieves data
from a REST API, and formats the output into a nested JSON structure.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        sys.exit(1)
    todos_data = todos_response.json()

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_data = {str(employee_id): tasks_list}
    filename = f"{employee_id}.json"

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(json_data, file)

