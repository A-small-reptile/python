import socket
from concurrent import futures
import functools
import time

def decorator(func):
         @wraps(func)
         def wrappers(*args,**kw):
               starttime=time.ctime()
               result=self.func(*args,**kw)
               endtime=time.ctime()
               print('use time:%s'%(endtime-starttime))
               return func
         return wrappers

@decorator
def blocking_way():
         sock=socket.socket()
         sock.connect(('example.com',80))
         request='GET/HTTP/1.0\r\nHost:example.com\r\n\r\n'
         sock.send(request.encode('ascii'))
         response=b''
         chunk=sock.recv(4096)
         while chunk:
                  response +=chunk
                  chunk=sock.recv(4096)
         return response

def process_way():
         num=10
         with futures.ProcessPoolExecutor(num) as execytor:
                  futs={executor.submit(vblock_way) for i in range(10)}
         return len([fut.result() for fut in futs])
