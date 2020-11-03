"""
Source https://github.com/NeilSCGH/PeriodicFunctionPython
"""

from time import time

class PeriodicFunction():
    def __init__(self, function, interval):
        self.lastRunTime = time()
        self.interval = interval
        self.function = function

    def tryRun(self):
        if time() - self.lastRunTime >= self.interval:
            self.function()#run the function
            self.lastRunTime = time()