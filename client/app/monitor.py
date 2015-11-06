import time
import uuid
import psutil

from psutil import AccessDenied

from app.logger import Logger
from app.process import Process
from app.utils import Timed


class AppMonitor(object):

    def __init__(self, name):
        self.name = name
        self.setup()

    def setup(self):
        client_id = uuid.uuid3(uuid.NAMESPACE_DNS, self.name)
        self.logger = Logger(str(client_id))

    def monitor(self, process):
        process.update()
        if not process.is_running():
            return

        if process.state['cpu_percent'] > 50:
            level = "CAREFUL"

            status = process.state.copy()
            status.update(self.host_status())
            if process.state["cpu_percent"] > 70:
                level = "CRITICAL"
            if process.state["cpu_percent"] > 90:
                level = "WARNING"

            self.log(level, status)

    def host_status(self):
        # Add more stuff
        return {"system_cpu": psutil.cpu_percent()}

    def log(self, level, process):
        self.logger.log(level, process)

    def run(self, interval):
        process = Process(self.name)

        while True:
            try:
                with Timed(interval) as timed:
                    self.monitor(process)
                time.sleep(timed.interval)
            except psutil.Error as e:
                if isinstance(e, AccessDenied):
                    print "access denied:", e
