import json

from requests import codes

from app.apiclient import ApiClient


class Logger(object):

    def __init__(self, client_id):
        self.client_id = client_id
        self._log = []
        self.api_client = ApiClient(client_id)

    def _count_log(self):
        if len(self._log) > 20:
            data = json.dumps(self._log)
            response = self.api_client.post(data, "logs")
            if response:
                if response.status_code == codes.ok:
                    self._log = []
            print response

    def log(self, level, state):
        if not self._log:
            self._log.append(self.client_id)
        else:
            state['level'] = level
            self._log.append(str(state))

        self._count_log()
