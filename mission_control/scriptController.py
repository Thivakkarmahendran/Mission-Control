#imports
import os
import subprocess
from config import SCRIPT_DRIECTORY_PATH, AUTO_UPDATE_SCRIPTS



def getScripts():
    scripts = [f for f in os.listdir(SCRIPT_DRIECTORY_PATH)]
    scripts.remove(".DS_Store")
    scripts.remove("Mission-Control")
    return scripts

def updateAllScript():
    
    if not AUTO_UPDATE_SCRIPTS:
        print("AUTO_UPDATE_SCRIPTS disabled")
        return
        
    for script in getScripts():
        p = subprocess.Popen(["git", "pull"], cwd="{}/{}".format(SCRIPT_DRIECTORY_PATH, script))
        p.wait()


def runScript(script:str):
    p = subprocess.Popen(["git", "python", "app.py"], cwd="{}/{}".format(SCRIPT_DRIECTORY_PATH, script))