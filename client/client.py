import time
import sys

try:
    import psutil
except ImportError as e:
    print e, "(pip install psutils)"
    sys.exit()

from psutil import AccessDenied


class Monitor(object):

    def __init__(self, name):
        print "asd"
        self.name = name
        self.interval = 1
        self.run()

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
            print process.cpu_percent(interval=1)
            time.sleep(self.interval)


if __name__ == "__main__":
    Monitor("Skype")
