# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
from time import ctime,sleep

def run(name):
   print ("run child process %s %s %s..."% (name,os.getpid(),ctime()))


if __name__=='__main__':
   # 创建父进程
   print("Parent process %s %s." %(os.getpid(),ctime()))
   # 创建子进程
   p = Process(target = run , args = ("text",))
   print ('Child process will start.')
   p.start()
   p.join()
   print('Child process end.')
