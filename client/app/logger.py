from app.apiclient import ApiClient


class Logger(object):

    def __init__(self, client_id):
        self._log = []
        self.api_client = ApiClient(client_id)

    def log(self, level, state):
        state['level'] = level
        print state
        self._log.append(state)
