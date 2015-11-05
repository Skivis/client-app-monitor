import time
import uuid

from app.logger import Logger
from app.process import Process


class AppMonitor(object):

    def __init__(self, name):
        self.name = name
        self.setup()

    def setup(self):
        client_id = uuid.uuid3(uuid.NAMESPACE_DNS, self.name)
        self.logger = Logger(str(client_id))

    def monitor(self, process):
        process.update()

        if process.state['cpu_percent'] < 1:
            return

        if process.state["cpu_percent"] > 10:
            level = "WARNING"
        elif process.state["cpu_percent"] > 20:
            level = "CRITICAL"
        else:
            level = "CAREFUL"

        process.state['time'] = time.time()

        self.log(level, process.state)

    def log(self, level, process):
        self.logger.log(level, process)

    def run(self, interval):
        process = Process(self.name)

        while True:
            self.monitor(process)
            time.sleep(interval)
