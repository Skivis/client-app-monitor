import time

from app.process import Process


class AppMonitor(object):

    def __init__(self, name):
        self.name = name
        self.interval = 1

    def monitor(self, process):
        process.update()
        # Log the state

    def run(self, interval):
        process = Process(self.name)

        while True:
            self.monitor(process)
            time.sleep(interval)
