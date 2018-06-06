from socket  import *

sock=socket(AF_INET,SOCK_STREAM)
sock.bind(('',5050))
sock.listen(4)

while True:
          client,addr=sock.accept()
          print('connected ,begin talkging')
          while True:
                   data=client.recv(2048).decode('utf-8')
                   print('芝麻>',data)
                   in_con=input('我>')
                   if  not in_con:
                            print('请重新输入')
                            in_con=input('>')
                   client.send(in_con.encode('utf-8'))


                   
