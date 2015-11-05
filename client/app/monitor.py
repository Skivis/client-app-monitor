import time
import uuid

from app.logger import Logger
from app.process import Process


class AppMonitor(object):

    def __init__(self, name):
        self.name = name
        self.interval = 1
        self.setup()

    def setup(self):
        client_id = uuid.uuid3(uuid.NAMESPACE_DNS, self.name)
        self.logger = Logger(client_id)

    def monitor(self, process):
        process.update()
        # TODO: some checking to determine whether to log
        # process state and if so, what severity
        self.log("CRITICAL", process.state)

    def log(self, level, process):
        self.logger.log(level, process)

    def run(self, interval):
        process = Process(self.name)

        while True:
            self.monitor(process)
            time.sleep(interval)
