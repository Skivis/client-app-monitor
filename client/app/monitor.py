import time
import sys

try:
    import psutil
except ImportError as e:
    print e, "(pip install psutil)"
    sys.exit()

from psutil import AccessDenied


class AppMonitor(object):

    def __init__(self, name):
        self.name = name
        self.interval = 1
        self.run()

    def monitor(self, process):
        print process.cpu_percent(interval=None)

        process.update()

    def get_process(self, name):
        for process in psutil.process_iter():
            try:
                if name in process.name():
                    return process.pid
            except AccessDenied as e:
                print "access denied", e

    def run(self):
        pid = self.get_process(self.name)
        process = psutil.Process(pid)

        while True:
            self.monitor(process)
            time.sleep(self.interval)
