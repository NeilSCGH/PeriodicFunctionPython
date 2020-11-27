from time import time

class PeriodicFunction():
    def __init__(self, function, interval):
        self.lastRunTime = time()
        self.interval = interval
        self.function = function

    def tryRun(self):
        if time() - self.lastRunTime >= self.interval:
            returnVal = self.function()#run the function
            self.lastRunTime = time()
            return True, returnVal
        return False, None