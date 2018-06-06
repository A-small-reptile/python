import socket

def noblocking_way():
         sock=socket.socket()
         sock.setblocking(0)
         try:
                  sock.connect(('example.com',80))
         except BlockingIOError:
                  pass
         request='GET/HTTP/1.0\r\nHost:example.com\r\n\r\n'
         data=request.encode('ascii')
         while True:
                  try:
                           sock.send(data)
                           break
                  except OSError:
                           pass
         response=b''
         while True:
                  try:
                           chunk=sock.recv(2048)
                           while True:
                                    response +=chunk
                                    chunk=sock.recv(2048)
                                    break
                  except OSError:
                           pass
         return response
def sync_way():
         res=[]
         for i in range(10):
                  res.append(noblocking_way())
         return len(res)

if __name__=='__main__':
         conet=sync_way()
         print(conet)
                  
