from core import PeriodicFunction

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