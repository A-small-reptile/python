from socket import *

sock=socket(AF_INET,SOCK_STREAM)
sock.connect(('localhost',5050))
print('可以开始聊天了')
while True:
         data=input('我>')
         sock.send(data.encode('utf-8'))
         s_con=sock.recv(2048)
         print('玉米>',s_con.decode('utf-8'))
