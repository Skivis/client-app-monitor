import argparse
from psutil import NoSuchProcess
from app.monitor import AppMonitor


parser = argparse.ArgumentParser(description='Client app monitor')

parser.add_argument('-n', '--name', help='Name of the process to monitor, i.e "Skype"', required=True)
parser.add_argument('-l', '--limits', help='Limits % for log levels "CAREFUL", WARNING & "CRITICAL i.e "50,70,90"', default="50,70,90")
args = vars(parser.parse_args())

try:
    AppMonitor(args).run(1)
except NoSuchProcess as e:
    print "process not found:", e.name
