import time
import uuid
import psutil

from psutil import AccessDenied
from psutil import NoSuchProcess

from app.logger import Logger
from app.process import Process
from app.utils import Timed


class AppMonitor(object):

    def __init__(self, config):
        self.name = config['name']
        self.limits = config['limits'].split(",")
        self.setup()

    def setup(self):
        client_id = uuid.uuid3(uuid.NAMESPACE_DNS, self.name)
        self.logger = Logger(str(client_id))

    def monitor(self, process):
        if not process.alive():
            raise NoSuchProcess(self.process_id)

        state = process.get_current_state()

        if state['cpu_percent'] < float(self.limits[0]):
            return

        level = "CAREFUL"

        if state["cpu_percent"] >= float(self.limits[1]):
            level = "WARNING"
        if state["cpu_percent"] >= float(self.limits[2]):
            level = "CRITICAL"

        status = state.copy()
        status.update(self.host_status())

        self.log(level, status)

    def host_status(self):
        # Add more stuff
        return { "system_cpu": psutil.cpu_percent() }

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
