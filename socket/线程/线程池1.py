import queue
import threading
import time

class Threadpool:
         def default_queue(self,func):
                  for i in range(self.max_num):
                           self.que.put(func)
         def get_queue(self,):
                  return self.que.get(func)
         def add_queue(self,func):
                  return self.que.put(func)

def event(pool,func):
         lock.acquire()
         pool.que=queue.Queue()
         pool.max_num=10
         if  pool.que.empty():
                  pool.default_queue(func)
         else:
                  pool.get_queue()
         time.sleep(1)
         pool.add_queue(func)
         print('use time:',time.ctime())
         lock.release()
def func():
         a=0
         if a<100:
                  a+=1
                  print('fuc:',a)
         
p=Threadpool()
lock=threading.RLock()
for i in range(50):
         t=threading.Thread(target=event,args=(p,func))
         t.start()

         
