# -*- coding: utf-8 -*-
import threading
import time

def threada(name):
    #加锁
    con.acquire()
    print ('%s: 你好啊...' % name)
    time.sleep(1)
    #通知其他线程
    con.notify()
    #等待其他线程notify通知，执行下边代码
    con.wait()
    print ('%s: 你说大黄是不是狗...' % name)
    time.sleep(1)
    con.notify()
    con.wait()
    print ('%s: 恩恩，我也是这样认为的...' % name)
    con.release()

def threadb(name):
    con.acquire()
    con.wait()
    print ('%s: 你也好啊...' % name)
    time.sleep(1)
    con.notify()
    con.wait()
    print ('%s: 不是啊，大黄是big yellow dog，简称BYD...' % name)
    time.sleep(1)
    con.notify()
    con.release()

con = threading.Condition()
threading.Thread(target=threadb, args=('胡远泽',)).start()  # 开辟线程
threading.Thread(target=threada, args=('马雪浩',)).start()