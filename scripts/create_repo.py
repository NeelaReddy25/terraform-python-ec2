import requests
import json
from dotenv import dotenv_values

config = dotenv_values(r"C:\devops\daws-78s\repos\terraform-python-ec2\scripts\.env")

# Configuration
github_token = config['github_token']
user_name = 'NeelaReddy25'
repo_name = 'terraform-python-ec2'
description = 'This repo is to discuss about python Useaccess'

# GitHub API URL for creating a repository with in an organisation
url = f'https://api.github.com/user/repos'

# Hraders and payload
headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github+json',
}
# This is the data we are sending to create repo
payload = {
    'name': repo_name,
    'description': description,
    'private': False # Set to True if you want to create a private repository
}

# Make the request to create a repository
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 201: # 201, Created. it means success
    print(f'Repository{repo_name}craeted successfully within {user_name}.')
    print(f'Repository URL:{response.json()["html_url"]}')
else:
    print(f'Failed to create repository in {user_name}. Status code: {response.status_code}')
    print(f'Response: {response.text}')