import asynchat
import asyncore

PORT=5050

class EndSession(Exception):
         pass

class ChatServer(asyncore.dispatcher):
         """聊天服务器"""

         def __init__(self,port):
                  asyncore.dispatcher.__init__(self)
                  #创建sockt
                  self.create_socket()
                  #设置socket 可重用
                  self.set_reuse_addr()
                  #监听端口
                  self.bind(('',port))
                  self.listen(5)
                  self.users={}
                  self.main_room=ChatRoom(self)

         def handler_accept(self):#获取新的套接字对象，并处理
                  conn,addr=self.accept()
                  ChatRoom(self,conn)
#聊天服务器的作用是通过asynccore.dispatcher来创建一个套接字对象，用于监听连接和传递数据


class ChatSession(asynchat.async_chat):
         """负责和客服端通信"""

         def __init__(self,server,sock):
                  asynchat.async_chat.__init__(self,scok)
                  self.server=server
                  self.set_terminator(b'\n') #设置分隔符
                  self.data=[]
                  self.name=None
                  self.enter=(LoginRoom(server))
         def enter(self,room):#进入房间
                  #从当前房间移除自身，然后添加到指定房间
                  try:
                           cur=self.room
                  except AttributeError:
                           pass
                  else:
                           cur.remove(self)
                  self.room=room
                  room.add(self)

         def collect_incoming_data(self,data):
                  #接收客服端的数据
                  self.data.append(data.decode('utf-8'))

         def found_terminator(self):
                  #当客服端的一条数据结束时的处理
                  line=''.join(self.data)
                  self.data=[]
                  try:
                           self.room.handler(self,line.encode('utf-8'))#对数据进行处理

                  except EndSession:
                           self.handler_close()
         def handler_close(self):                     
                  #当session关闭时，将进入LogoutRoom
                  asynchat.async_chat.handler_close(self)
                  self.enter(LogoutRoom(self.server))
#接收客户端数据，调用下一个函数处理数据和退出函数

class CommandHandler:
         """命令处理类"""

         def unknown(self,session,cmd):
                  #响应未知命令
                  #通过asynchat.async_chat.push方法发送消息
                  session.push(('Unknown command {} \n'.format(cmd)).encode('utf-8'))###向用户发出通知，未知的命令
                  
         def handler(self,session,line):
                  line=line.decode()
                  #命令处理
                  if not line.strip():
                           return
                  parts=line.split('',1)#将数据分开
                  cmd=parts[0]
                  try:
                           line=parts[1].strip()#判断数据是否为空
                  except IndexError:
                           line=''
                  #通过协议代码执行相应的方法
                  method=getattr(self,'do'+cmd,None)##########？？？？
                  try:
                           method(session.line)
                  except TypeError:
                           self.unknuown(session,cmd)
#处理命令 


class Room(CommandHandler):
         """包含多个用户的环境，负责基本的命令处理和广播"""

         def __init__(self,server):
                  self.server=server
                  self.sessions=[]
         def add(self,session):
                  #一个用户进入房间
                  self.sessions.append(session)
         def remove(self,session):
                  #一个用户离开房间
                  self.sessions.remove(session)
         def broadcast(self,line):
                  #向所有的用户发送指定消息
                  #使用asynchat.async_chat.push方法发送数据
                  for session in self.sessions:
                           session.push(line)
         def do_logout(self,sesion,line):
                  #退出房间
                  raise EndSession
#房间多用户的管理



class LoginRoom(Room):
         """处理登录用户"""
         def  add(self,session):
                  #用户连接成功的响应
                  Room.add(self,session)
                  #使用asynchat.async_chat.push 方法发送数据
                  session.push(b'Connect Success')
                  print()
         def do_login(self,session,line):
                  #用户登录逻辑
                  name=line.strip()
                  #获取用户名称
                  if not name:
                           session.push(b'UserName Empty')
                  #检查是否有同名用户
                  elif name in self.server.users:
                           session.push(b'UserName Exist')
                  #用户名检查成功后，进入主聊天室
                  else:
                           session.name=name
                           session.enter(self,server.main_room)
#登录后进入房间

class LogoutRoom(Room):
         """处理退出用户"""
         def add(self,session):
                  #从服务器中移除
                  try:
                           del self.server.users[session.name]
                  except KeyError:
                           pass
#登出房间

class ChatRoom(Room):
         """聊天用的房间"""
         def add(self,session):
                  #广播新用户进入
                  session.push(b'Login Success')
                  self.broadcast(session.name+'has entered the room.\n').encode('utf-8')#向在线的所用用户发出
                  self.server.users[session.name]=session
                  Room.add(self,session)
         def remove(self,session):
                  #广播用户离开
                  Room.remove(self,session)
                  self.broadcast(session.name+'has left the room.\n').encode('utf-8')
         def  do_say(self,session,line):
                  #客户端发送消息
                  self.broadcast((session.name+':'+line+'\n').encode('utf-8'))
         def do_look(self,seesion,line):
                  #查看在线用户
                  session.push(b'Online users:\n')
                  for  other in self.seeion:
                           session.push(other.name+'\n').encode('utf-8')
#房间的具体操作

if __name__=='__main__':
         s=ChatServer(PORT)
         try:
                  print('chat serve run at"0.0.0.0:{0}".format(PORT)')
                  asyncore.loop()
         except KeyboardInterput:
                           print('chat server exit')
                  
