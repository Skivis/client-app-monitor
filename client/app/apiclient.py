import requests
import json
import platform
import psutil

from requests.exceptions import ConnectionError


class ApiClient(object):

    def __init__(self, client_id):
        self.base_url = "http://localhost:1337/"
        self.client_id = client_id
        self.notify_server()

    def notify_server(self):
        data = {}
        data['platform'] = platform.platform()
        data['node'] = platform.node()
        data['processor'] = platform.processor()
        data['system'] = platform.system()
        data['cores'] = psutil.cpu_count()
        data['client_id'] = self.client_id
        self.post(json.dumps(data, sort_keys=True), "clients")

    def post(self, data, url):
        endpoint = self.base_url + url
        try:
            return requests.post(endpoint, data=data)
        except ConnectionError as e:
            print "connection error", e
            return False
