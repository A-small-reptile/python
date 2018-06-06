import queue
import threading
import time

class Threadpool:
         def __init__(self,max_num=12):
                  self.queue=queue.Queue(max_num)
                  for i in range(max_num):
                           self.queue.put(threading.Thread)
         def get_thread(self):
                  return self.queue.get()
         def add_thread(self):
                  return self.queue.put(threading.Thread)
def func(pool,n):
         time.sleep(2)
         print(n)
         pool.add_thread()

p=Threadpool(10)
for i in range(1,20):
         thread=p.get_thread()
         t=thread(target=func,args=(p,i))
         t.start()
                  
