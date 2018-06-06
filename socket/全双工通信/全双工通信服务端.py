from socket import *


HOST=''
PORT=5050
server_addr=(HOST,PORT)


class Socket_server:
         def __init__(self,addr):
                  self.addr=addr
                  self.active=self.decorator()
         def _monitor(self):
                   if self.conn.recv(4096) !=None:
                           print('接收到数据')
                           data=self.conn.recv(4096)
                           print('客服端：',data.decode('utf-8'))
                   else:
                           print('没有接收到数据')
                           print('可以输入数据')
                           data=input('服务端：')
                           self.conn.send(data.encode('utf-8'))                
         def decorator(self):
                  sock=socket(AF_INET,SOCK_STREAM)
                  sock.bind((HOST,PORT))
                  sock.listen(5)
                  while True:
                           conn,addr=sock.accept()
                           self.conn=conn
                           if self.conn:
                                    print('已连接》》》')
                                    self._monitor()
        
                  
         
                                 
if __name__=="__main__":
         s=Socket_server(server_addr)
         
                                 
         
