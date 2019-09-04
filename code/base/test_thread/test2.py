import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run(self):
        print "Start ", self.name
        print_time(self.name, self.counter, 5)
        print "Exiting ", self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print "%s: %s"%(threadName, time.ctime(time.time()))
        counter -= 1

t1 = myThread(1, "Thread-1", 1)
t2 = myThread(2, "Thread-2", 2)

t1.start()
t2.start()

print "exit main thread"
