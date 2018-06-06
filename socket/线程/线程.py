import threading
import time


lock=threading.RLock()

def work(num,event,cond):
         with cond:
                  cond.wait()
                  num+=1
                  print(num)
                  print(time.ctime())
def work1(cond,num):
         with cond:
                  cond.wait()
                  num+=1
                  print(num)
                  print(time.ctime())
def work2(cond,num):
         with cond:
                  cond.wait()
                  num+=1
                  print(num)
                  print(time.ctime())
def prter(cond):
         with cond:
                  print('asda')
                  cond.notify(n=1)
                  print('asdafafa')
event_obj=threading.Event()
cond=threading.Condition()
for i in range(10):
         t1=threading.Thread(target=work,args=(2,event_obj,cond))
         t2=threading.Thread(target=prter,args=(cond,))
         t3=threading.Thread(target=work1,args=(cond,2))
         t4=threading.Thread(target=work2,args=(cond,2))
         t1.start()
         t2.start()
         
         t3.start()
         t4.start()
         

