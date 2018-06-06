from socket import *
import select
import re

sock=socket.socket()
ADDR=('',6060)
sock.bind(ADDR)
sock.listen(5)
inputs=[sock]
clientdict={}
user='No name user'
roomnumber=0
print('Start the chat server')

while True:
     rs,ws,es=select.select(inputs,[],[])
     for i in rs:
          if i==sock:
               client,addr=sock.accept()
               inputs.append(client)
               clientdict[client]=[client,addr,user,roomnumber]
          else:
               try:
                    data=i.recv(4096)
                    matchname=re.match(r'(.+)\sjoin the server',data)
                    matchroom=re.match(r'Join the room(\d)',data)
                    if matchname:
                         print(data)
                         for x in inputs:
                              if x==sock or x==i:
                                   pass
                              else:
                                   if clientdict[x][2]=='No name user' or clientdict[x][3]==0:
                                        pass
                                   else:
                                        x.send(data)
                         username=matchname.group(1)
                         clientdict[i][2]=username
                         i.send('welcome ,%s'%username)
                    elif matchroom:
                         print('%s'%clientdict[i][2],data)
                         roomnumber=matchroom.group(1)
                         clientdict[i][3]=roomnumber
                         i.send('You join room %s '%roomnumber)
                         for x in inputs:
                              if x==sock or x==i:
                                   pass
                              else:
                                   if clientdict[x][3]==client[i][3]:
                                        x.send('%s join this room '%clientdict[i][2])
                         else:
                              senddata='%s said %s'%(clientdict[i][2],data)
                              for x in inputs:
                                   if x==sock or x==i:
                                        pass
                                   else:
                                        if clientdict[x][3]==clientdict[i][3]:
                                             x.send(senddata)
                              disconnected=False
                    except OSError:
                         disconnected=True
                    if disconnected:
                         leftdata='%s has left'%clientdict[i][2]
                         print leftdata
                         for x in inputs:
                              if x==sock or x==i:
                                   pass
                              else:
                                   x.send(senddata)
                         inputs.remove(i)
