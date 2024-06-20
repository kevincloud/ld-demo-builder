import requests
import json
import os

api_key = os.environ["LD_API_KEY"]
project_key = "cxld-raw-zoning"

exp_key = "ai-analysis-to-advisor"
exp_name = "AI Analysis to Advisor"
hypothesis = "We believe that by using more up to date AI models, we will increase customer conversions to contact their advisor."
primary_funnel_key = "ai-to-advisor-conversion"
flag_key = "config-ai-model"
attributes = ["plan", "beta", "metro", "net_worth"]


headers = {
    "Authorization": api_key,
    "Content-Type": "application/json",
    "LD-API-Version": "beta",
}

res = requests.post(
    "https://app.launchdarkly.com/api/v2/projects/"
    + project_key
    + "/environments/production/experiments",
    json={},
    headers=headers,
)

print(res.text)

# obj = json.loads(res.text)
# if "message" in obj:
#     print("Does not exist")
# else:
#     print("Exists!")


# curl -s -X GET \
#   'https://app.launchdarkly.com/api/v2/projects/platform-demo/release-pipelines/default-releases/releases' \
#   -H 'Authorization: api-XXX' \
#   -H 'LD-API-Version: beta'

# curl -s -X GET \
#   'https://app.launchdarkly.com/api/v2/projects/platform-demo/release-pipelines' \
#   -H 'Authorization: api-XXX' \
#   -H 'LD-API-Version: beta'

# curl -s -X GET \
#   'https://app.launchdarkly.com/api/v2/flags/cxld-raw-zoning/config-ai-model' \
#   -H 'Authorization: api-XXX'
