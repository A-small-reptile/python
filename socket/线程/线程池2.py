import threading
import queue
import time
import contextlib

StopEvent=object()

class Threadpool:
         def __init__(self,max_num=10):
                  self.max_num=max_num
                  self.que=queue.Queue()
                  self.genrate_list=[]
                  self.free_list=[]
                  self.terminal=False
         def run_tp(self,func,args,callback=None):
                  if len(self.free_list)==0 and len(self.genrate_list)<len(max_num):
                           self.thread_num()
                  w=(func,args,callback,)
                  self.que.put(w)
         def thread_num(self,):
                  t=threading.Thread(target=func,)
                  t.start()
         def call_do(self):
                  current_thread=threading.current_thread()
                  self.genrate_list.append(current_thread)
                  event=self.que.get()
                  while event !=StopEvent:
                           func,args,callback=event
                           try:
                                    result=func(*args)
                                    status=True
                           except Exception as e:
                                    status=False
                                    result=e
                           if callback is not None:
                                    try:
                                             callback(status,result)
                                    except Exception as e:
                                            pass 
                           if self.terminal:
                                    event=StopEvent
                           else:
                                    with self.worker_state(self.free_list,current_thread):
                                             event=self.que.get()
                  self.genrate_list.remove(current_thread);
         def close(self):
                  num=len(self.genrate_list)
                  while num:                                                                                   
                           self.que.put(StopEvent)
                           num-=1
         def terminate(self):
                  self.terminal=True
                  while  self.genrate_list:
                           self.que.put(StopEvent)
                  self.que.empty()
         @contextlib.contextmanager
         def worker_state(self,freelist,val):
                  freelist.append(val)
                  try:
                           yield
                  finally:
                           freelist.remove(val)
def work(i):
         n=0
         while n<=i:
                  n+=1
                  print('work:',n)
pool=Threadpool()
for item in range(50):
         pool.run_tp(work,(item,))
pool.close()
