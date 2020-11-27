from core import PeriodicFunction

def f1():
    print("Each 1 second")
    return 42

def f2():
    print("Each 3 seconds")

def f3():
    print("Each 10 seconds")

myfnc1 = PeriodicFunction(f1, 1)
myfnc2 = PeriodicFunction(f2, 3)
myfnc3 = PeriodicFunction(f3, 10)

while 1:
    runned, returnVal = myfnc1l.tryRun()
    if runned: print(returnVal)

    myfnc2.tryRun()
    myfnc3.tryRun()