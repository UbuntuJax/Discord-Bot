import time
t0 = time.time()
while 1:
    t_new = time.time()
    t_sub = t_new - t0
    #print(t_sub)
    if t_sub > 3:
        t0 = time.time()
        print("monkee")        