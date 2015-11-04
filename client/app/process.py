import psutil

from psutil import AccessDenied, NoSuchProcess


class Process(psutil.Process):

    def __init__(self, name):
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
        print self.cpu_percent(interval=None)
