import json

import requests
from erp_connector.utils.retryable_session import RetryableSession


class OneIntegrationClient:

    def __init__(self,erp_config):
        self.base_url = f'https://one-integration-{erp_config.env}-http-server.internal.cleartax.co'
        self.auth_token = erp_config.authToken
        self.x_erp_instance_id = erp_config.erpInstanceId

    def get_command(self):
        session = RetryableSession()
        url = f"{self.base_url}/api/one-integration/integration/command/get"
        headers = {
            "accept": "*/*",
            "x-clear-auth-token": self.auth_token,
            "x-erp-instance-id": self.x_erp_instance_id
        }

        try:
            response = session.get(url, headers=headers, timeout=45)
            response.raise_for_status()
            response_data = response.json()
            return response_data
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            raise Exception(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            raise Exception(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"An error occurred: {req_err}")

    def get_presign(self, file_name, command_id):
        session = RetryableSession()
        url = f"{self.base_url}/api/one-integration/integration/action/pre_sign?file_name={file_name}&command_id={command_id}"
        headers = {
            "accept": "*/*",
            "x-clear-auth-token": self.auth_token,
            "x-erp-instance-id": self.x_erp_instance_id,
            "fileContentType": "application/zip"
        }

        try:
            response = session.get(url, headers=headers, timeout=45)
            response.raise_for_status()
            response_data = response.json()
            return response_data
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            raise Exception(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            raise Exception(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"An error occurred: {req_err}")

    def upload_to_s3(self, upload_url, file_path):
        session = RetryableSession()
        headers = {
            'Content-Type': 'application/zip'
        }
        payload = open(file_path, 'rb')

        try:
            response = session.put(upload_url, headers=headers, data=payload, timeout=45)
            response.raise_for_status()
            if response.status_code != 200 and response.status_code != 201:
                print("s3 upload failure: ", response.text)
            return None
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            raise Exception(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            raise Exception(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"An error occurred: {req_err}")

    def post_command(self, presign_url, command_id):
        session = RetryableSession()
        url = f"{self.base_url}/api/one-integration/integration/command/send/result"
        headers = {
            "accept": "*/*",
            'Content-Type': 'application/json',
            "x-clear-auth-token": self.auth_token,
            "x-erp-instance-id": self.x_erp_instance_id
        }
        payload = json.dumps({
            "commandId": command_id,
            "metadata": {
                "s3Details": [
                    {
                        "url": presign_url
                    }
                ]
            }
        })

        try:
            response = session.post(url, headers=headers, data=payload, timeout=45)
            response.raise_for_status()
            response_data = response.json()
            return response_data
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            raise Exception(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            raise Exception(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"An error occurred: {req_err}")
