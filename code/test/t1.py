import datetime

time1 = datetime.datetime.now()
print (time1)
for i in range(1000):
    for j in range(1000):
        for t in range(1000):
            pass
time2 = datetime.datetime.now()
print (time2)
print (time2-time1)
