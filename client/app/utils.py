import time


class Timed(object):
    """Convenience context manager for timing stuff"""

    def __init__(self, interval=False):
        self.interval = interval

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        if self.interval:
            self.pause = self.interval - self.secs
            # TODO: When interval is small (i.e 1 sec), 'secs' gets a
            # negative value if what we're timing takes longer than
            # 'interval'. Gotta make sure that longer tasks maybe run on
            # their on thread.
            #
            # Quick fix for now, if 'secs' is negative, assign the
            # original 'interval' to it.
            if self.pause < 0:
                self.pause = self.interval
