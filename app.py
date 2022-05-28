#imports
from mission_control.scriptSchedule import scriptSchedule
from mission_control.scriptController import *


sched = None


def intializeScheduler():
    global sched
    sched = scriptSchedule()
    sched.scheduleAutoUpdate()
    sched.scheduleScript("Stock-Analyser", 1)
    sched.startSchedule()


def main():
    print("***** Starting Mission Control ***** \n")
    intializeScheduler()

if __name__ == '__main__':
    main()
    