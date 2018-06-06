import queue
import  threading

que=queue.Queue(10)

def s(i):
         que.get(i)
         print(que.qsize())

def d(i):
         
         g=que.put(i)
         print('del:',g ,'\n')

for i in range(1,13):
         t=threading.Thread(target=s,args=(i,))
         t.start()

for i in range(1,11):
         t=threading.Thread(target=d,args=(i,))
         t.start()
print('size',que.qsize())
