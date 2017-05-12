# -*- coding: utf-8 -*-
import queue,threading,time

q=queue.Queue()

def product(arg):
    while True:
        q.put(str(arg)+'包子')

def consumer(arg):
    while True:
        print arg,q.get()
        time.sleep(0)

for i in range(20):
    t=threading.Thread(target=product,args=(i,))
    t.start()
for j in range(10):
    t=threading.Thread(target=consumer,args=(j,))
    t.start()
