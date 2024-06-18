import requests
import json
import os

TOKEN = os.environ['MY_TOKEN']
GITHUB_REF = os.environ.get('GITHUB_REF', '')

def check_token(token):
    print(f"Token starts with: {token[:5]}")
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get("https://api.github.com/user", headers=headers)

    if response.status_code == 200:
        print("Token is valid.")
        print("Token scopes:", response.json().get('scopes', 'No scopes found'))
    else:
        print("Token is invalid.")

def trigger_workflow(repo_owner, repo_name, token, tag):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/dispatches"
    headers = {
        "Accept": "application/vnd.github.everest-preview+json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "event_type": "trigger-event",
        "client_payload": {
            "version_tag": tag
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

# Extract the tag from GITHUB_REF
if GITHUB_REF.startswith('refs/tags/'):
    version_tag = GITHUB_REF[len('refs/tags/'):]
else:
    version_tag = 'unknown'

check_token(token)

trigger_workflow(repo_owner, repo_name, token, version_tag)
