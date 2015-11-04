import sys

try:
    import psutil
except ImportError as e:
    print e, "(pip install psutil)"
    sys.exit()


class Process(psutil.Process):
    pass
