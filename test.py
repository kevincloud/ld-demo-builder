import requests
import json
import os

api_key = os.environ["LD_API_KEY"]
project_key = "rustoleum"

payload = {
    "key": "default-releases",
    "name": "Default Releases",
    "phases": [

    ]
}

res = requests.post(
    "https://app.launchdarkly.com/api/v2/projects/"
    + project_key
    + "/release-pipelines",
    json=payload,
    headers={
        "Authorization": api_key,
        "Content-Type": "application/json",
        "LD-API-Version": "beta",
    },
)

obj = json.loads(res.text)
if "message" in obj:
    print("Does not exist")
else:
    print("Exists!")





curl -s -X GET \
  'https://app.launchdarkly.com/api/v2/projects/platform-demo/release-pipelines/default-releases' \
  -H 'Authorization: api-XXX' \
  -H 'LD-API-Version: beta'


