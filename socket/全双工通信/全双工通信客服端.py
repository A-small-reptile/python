from socket import *

HOST='localhost'
PORT=5050
BUFSIZE=2048
ADDR=(HOST,PORT)


class Conn:
         def fetch(self,addr):
                  self.sock=socket()
                  self.addr=addr
                  try:
                           self.sock.connect(self.addr)
                           self.send_conet()
                  except BlockingIOError:
                           pass
         def send_conet(self,): 
                  data=input('小白>')
                  self.sock.send(data.encode('utf-8'))
         def recv_conet(self):
                  chunk=self.sock.recv(2048)
                  print('服务端>',chunk)
                  
if __name__=='__main__':
        c=Conn()
        c.fetch(ADDR)
