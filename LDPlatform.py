import requests
import json


class LDPlatform:
    project_key = ""
    api_key = ""
    client_id = ""

    def __init__(self, api_key):
        self.api_key = api_key

    def create_project(self, project_key, project_name):
        self.project_key = project_key
        if self.project_exists(project_key):
            return
        payload = {"key": project_key, "name": project_name}

        res = requests.post(
            "https://app.launchdarkly.com/api/v2/projects",
            json=payload,
            headers={"Authorization": self.api_key, "Content-Type": "application/json"},
        )

        # client_id = "666b5cd5e16c371081d3ff33"
        items = json.loads(res.text)
        for e in items["environments"]:
            if e["key"] == "test":
                self.client_id = e["_id"]
                break

    def delete_project(self):
        res = requests.delete(
            "https://app.launchdarkly.com/api/v2/projects/" + self.project_key,
            headers={"Authorization": self.api_key},
        )

    def create_flag(
        self,
        flag_key,
        flag_name,
        variations=[],
        purpose=None,
        on_variation=0,
        off_variation=1,
        tags=[],
        migration_stages=0,
    ):
        if self.flag_exists(flag_key):
            return

        payload = {
            "key": flag_key,
            "name": flag_name,
            "clientSideAvailability": {
                "usingEnvironmentId": True,
                "usingMobileKey": True,
            },
        }

        if len(variations) > 0:
            payload["variations"] = variations

        if migration_stages > 0:
            payload["migrationSettings"] = {
                "contextKind": "user",
                "stageCount": migration_stages,
            }

        if purpose is None:
            payload["defaults"] = {
                "onVariation": on_variation,
                "offVariation": off_variation,
            }
        else:
            payload["purpose"] = purpose

        if len(tags) > 0:
            payload["tags"] = tags

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key,
        }
        response = requests.post(
            "https://app.launchdarkly.com/api/v2/flags/" + self.project_key,
            json=payload,
            headers=headers,
        )
        return response

    def add_release(self, flag_key):
        return

    def create_metric(
        self,
        metric_key,
        metric_name,
        event_key,
        metric_description="",
        kind="custom",
        numeric=False,
        success_criteria="LowerThanBaseline",
        unit="",
        exclude_empty_events=False,
        randomization_units="user",
        aggregation_type="average",
    ):
        payload = {
            "key": metric_key,
            "name": metric_name,
            "description": metric_description,
            "eventKey": event_key,
            "kind": kind,
            "isNumeric": numeric,
            "successCriteria": success_criteria,
            "eventDefault": {"disabled": exclude_empty_events},
            # "randomizationUnits": randomization_units,
            # "unitAggregationType": aggregation_type,
        }

        if numeric:
            payload["unit"] = unit

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key,
        }
        response = requests.post(
            "https://app.launchdarkly.com/api/v2/metrics/" + self.project_key,
            json=payload,
            headers=headers,
        )
        return response

    def create_metric_group(
        self, group_key, group_name, metrics, kind="funnel", description=""
    ):
        payload = {
            "key": group_key,
            "name": group_name,
            "description": description,
            "kind": kind,
            "maintainerId": "5f9b3b7b7f7b7d001f7b7f7b",
            "tags": ["coast"],
            "metrics": metrics,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key,
            "LD-API-Version": "beta",
        }
        response = requests.post(
            "https://app.launchdarkly.com/api/v2/projects/"
            + self.project_key
            + "/metric-groups",
            json=payload,
            headers=headers,
        )
        return response

    def project_exists(self, project_key):
        res = requests.get(
            "https://app.launchdarkly.com/api/v2/projects/" + project_key,
            headers={"Authorization": self.api_key},
        )
        data = json.loads(res.text)
        if "message" in data:
            return False
        return True

    def flag_exists(self, flag_key):
        res = requests.get(
            "https://app.launchdarkly.com/api/v2/flags/"
            + self.project_key
            + "/"
            + flag_key,
            headers={"Authorization": self.api_key},
        )
        data = json.loads(res.text)
        if "message" in data:
            return False
        return True

    def metric_exists(self, metric_key):
        return True

    def metric_group_exists(self, group_key):
        return True
