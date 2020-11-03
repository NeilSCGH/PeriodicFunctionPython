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

def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")

myfnc1 = PeriodicFunction(f1, 3)
myfnc2 = PeriodicFunction(f2, 1)
myfnc3 = PeriodicFunction(f3, 10)

while 1:
    myfnc1.tryRun()
    myfnc2.tryRun()
    myfnc3.tryRun()