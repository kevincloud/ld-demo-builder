import requests
import os

api_key = os.environ["LD_API_KEY"]
project_key = "kevinc-coast-demo"

res = requests.delete(
    "https://app.launchdarkly.com/api/v2/projects/" + project_key,
    headers={"Authorization": api_key},
)

# res = requests.get(
#     "https://app.launchdarkly.com/api/v2/flags/" + project_key + "/" + flag_key,
#     headers={"Authorization": api_key},
# )

# obj = json.loads(res.text)
# if "message" in obj:
#     print("Does not exist")
# else:
#     print("Exists!")
