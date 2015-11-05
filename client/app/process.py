import time
import psutil

from psutil import AccessDenied, NoSuchProcess


class Process(psutil.Process):

    def __init__(self, name):
        self.state = {}
        super(Process, self).__init__(self._pid(name))

    def _pid(self, name):
        for process in psutil.process_iter():
            try:
                if name in process.name():
                    return process.pid
            except AccessDenied as e:
                print "access denied", e

        raise NoSuchProcess(None, name=name, msg="process not found")

    def update(self):
        self.state = self.as_dict(attrs=[
            "cpu_percent", "memory_percent", "num_threads"])
        self.state['time'] = time.time()
