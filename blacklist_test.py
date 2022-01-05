import time
var = 1
x = []
while 1:
    x.append(var)
    var+=1
    if len(x) == 3:
        x.pop(0)
    print(x)
    time.sleep(1)