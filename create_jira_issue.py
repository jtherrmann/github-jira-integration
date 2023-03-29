import os

import requests
from requests.auth import HTTPBasicAuth

email = os.getenv('JIRA_EMAIL')
token = os.getenv('JIRA_TOKEN')

url = 'https://asfdaac.atlassian.net/rest/api/latest/issue/'

auth = HTTPBasicAuth(email, token)

payload = {
    "fields": {
       "project":
       {
          "key": "JTH"
       },
       "summary": "created from python",
       "description": "testing issue creation via REST API",
       "issuetype": {
          "name": "Task"
       }
   }
}

response = requests.post(url, json=payload, auth=auth)

response.raise_for_status()

print(response.json())
