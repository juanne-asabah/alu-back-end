#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    
    users_response = requests.get(f"{base_url}/users")
    if users_response.status_code != 200:
        exit(1)
    users_data = users_response.json()

    todos_response = requests.get(f"{base_url}/todos")
    if todos_response.status_code != 200:
        exit(1)
    todos_data = todos_response.json()

    user_map = {user.get("id"): user.get("username") for user in users_data}

    all_data = {}
    for user_id in user_map:
        all_data[str(user_id)] = []

    for task in todos_data:
        user_id = task.get("userId")
        if user_id in user_map:
            all_data[str(user_id)].append({
                "username": user_map[user_id],
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as file:
        json.dump(all_data, file)
