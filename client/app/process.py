import time
import psutil

from psutil import AccessDenied, NoSuchProcess


class Process(psutil.Process):

    def __init__(self, name):
        self.state = {}
        self.process_id = self.find_pid(name)
        super(Process, self).__init__(self.process_id)

    def find_pid(self, name):
        for process in psutil.process_iter():
            try:
                if name in process.name():
                    return process.pid
            except AccessDenied as e:
                print "access denied", e

        raise NoSuchProcess(None, name=name, msg="process not found")

    def get_current_state(self):
        state = self.as_dict(attrs=[
            "cpu_percent", "memory_percent", "num_threads"], ad_value="AD")
        state['time'] = time.time()
        return state

    def alive(self):
        return self.is_running()
