import requests
import json
import os

TOKEN = os.environ['MY_TOKEN']

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

trigger_workflow(repo_owner, repo_name, token)
