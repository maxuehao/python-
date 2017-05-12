# -*- coding: utf-8 -*-
from multiprocessing import Pool
from time import ctime 
import time

def childprocess(name):
   print ('I am %s start %s...' % (name,ctime()))
   time.sleep(3)
   print ('I am %s stop %s...' % (name,ctime()))

if __name__ == '__main__':
   print ('I AM Parent start %s' % ctime())
   #创建线程池
   p = Pool(4)
   for i in range(4):
      p.apply_async(childprocess,args=(i,))
   p.close()
   p.join()
   print ("OK!")
