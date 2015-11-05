import requests


class ApiClient(object):

    def __init__(self, client_id):
        self.base_url = ""
        self.client_id = client_id

    def send(self, data, url):
        endpoint = self.base_url + url
        requests.post(endpoint, data=None, json=None)
