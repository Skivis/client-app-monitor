import time

from app.process import Process


class AppMonitor(object):

    def __init__(self, name):
        self.name = name
        self.interval = 1
        self.run()

    def monitor(self, process):
        process.update()

    def run(self):
        process = Process(self.name)

        while True:
            self.monitor(process)
            time.sleep(self.interval)
