#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get employee information
    user = requests.get(f"{base_url}users/{user_id}").json()
    username = user.get("username")

    # Get employee todos
    todos = requests.get(f"{base_url}todos", params={"userId": user_id}).json()

    # Format the data
    data = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    # Write data to USER_ID.json
    filename = f"{user_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file)
