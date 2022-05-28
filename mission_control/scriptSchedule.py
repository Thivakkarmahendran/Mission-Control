#imports
from apscheduler.schedulers.background import BackgroundScheduler
from scriptController import runScript, updateAllScript

"""
https://betterprogramming.pub/introduction-to-apscheduler-86337f3bb4a6

EXAMPLE:
sched = scriptSchedule()
"""

class scriptSchedule:
  
    sched = None
    
    def __init__(self):
       self.sched = BackgroundScheduler(daemon=False)
    
    def scheduleScript(self, script:str, days:int):
        self.sched.add_job(runScript(script),'interval',days=days)
        
    def scheduleAutoUpdate(self):
        self.sched.add_job(runScript(updateAllScript),'interval',days=1)
        
        
    def startSchedule(self):
        self.sched.start()
        
    def stopSchedule(self):
        self.sched.shutdown()
