import requests
import json
import os

TOKEN = os.environ['MY_TOKEN']

def check_token(token):
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get("https://api.github.com/user", headers=headers)

    if response.status_code == 200:
        print("Token is valid.")
        print("Token scopes:", response.json().get('scopes', 'No scopes found'))
    else:
        print("Token is invalid.")

def trigger_workflow(repo_owner, repo_name, token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/dispatches"
    headers = {
        "Accept": "application/vnd.github.everest-preview+json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "event_type": "trigger-event",
        "client_payload": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 204:
        print("Workflow triggered successfully!")
    else:
        print("Failed to trigger workflow:", response.status_code, response.text)

# Replace these values with your repo A owner, repo name, and personal access token
repo_owner = "TheFern2"
repo_name = "repoA"
token = TOKEN

check_token(token)

trigger_workflow(repo_owner, repo_name, token)
