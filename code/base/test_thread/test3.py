import threading
import time

exitFlag = 0
datas = [0,0,0,0,0,0]
count = 1
class myThread(threading.Thread):
    def __init__(self, callback, name):
        threading.Thread.__init__(self)
        self.callback = callback
        self.name = name
    def run(self):
        print "Start:", self.name
        self.callback()
        print "End:", self.name
def change_datas():
    global count
    while True:
        for i in range(len(datas)):
            datas[i] = count
        count += 1
def print_datas():
    print datas

t1 = myThread(change_datas, "change_datas")
t2 = myThread(print_datas, "print_datas")

t1.start()
t2.start()

print "exit main thread"
