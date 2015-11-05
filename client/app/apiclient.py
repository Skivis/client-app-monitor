import requests
import json


class ApiClient(object):

    def __init__(self, client_id):
        self.base_url = "http://localhost:1337/"
        self.client_id = client_id
        self.notify_server()

    def notify_server(self):
        data = {"platform": "Windows", "client_id": self.client_id}
        self.post(json.dumps(data, sort_keys=True), "clients")

    def post(self, data, url):
        endpoint = self.base_url + url
        requests.post(endpoint, data=data)
