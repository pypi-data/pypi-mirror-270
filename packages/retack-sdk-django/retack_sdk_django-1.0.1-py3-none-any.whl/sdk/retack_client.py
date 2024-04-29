import json
import requests

class RetackClient:
    def __init__(self, retack_config):
        self.retrack_config = retack_config

    async def report_error_async(self, error, stack_trace, user_context=None):
        # Base URL
        base_url = "https://api.dev.retack.ai"
        endpoint = "/observe/error-log/"

        headers = {
            "Content-Type": "application/json",
            "ENV-KEY": self.retrack_config.api_key
        }

        body = {
            "title": error,
            "stack_trace": str(stack_trace),
            "user_context": user_context.to_json() if user_context else None
        }

        try:
            response = requests.post(base_url + endpoint, headers=headers, json=body)
            response.raise_for_status()
            return True
        except Exception as e:
            print("Unable to report error to Retack AI.")
            print(e)
            return False

class ErrorReportRequest:
    def __init__(self, error, stack_trace, user_context=None):
        self.error = error
        self.stack_trace = stack_trace
        self.user_context = user_context

class RetackConfig:
    def __init__(self, api_key):
        self.api_key = api_key

class UserContext:
    def __init__(self, username, extras):
        self.username = username
        self.extras = extras

    def to_json(self):
        return json.dumps(self.__dict__)
