import threading

import time

done = False

def worker1():
    while True:
        print("task1")
        if done == True:
            break
        
def worker2():
    while True:
        print("task2")
        if done == True:
            break

t1 = threading.Thread(target=worker1, daemon=True)
t2 = threading.Thread(target=worker2, daemon=True)

t1.start()
t2.start()

input("press enter to quit")
done = True
    