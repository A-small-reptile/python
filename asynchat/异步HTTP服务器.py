import asynchat asyncore socket
import os
import mimetypes
from http.client import responses

#该类继承自asyncore模块，仅处理接受事件
class async_http(aysncore.dispatcher):
         asyncore.dispatcher.__init__(self)
         self.create_socket(socket.AF_INET,socket.SOCK_STRAM)
         self.setsockopt(socket.SOL_SCOKET,socket.SO_REUSEADDR,1)
         self.bind(('',port))
         self.listen(5)

#处理异步的HTTP请求的类

class async_http_handler(asynchat.async_chat):
         def __init__(self,conn=None):
                  asynchat.async_chat.__init__(self.conn)
                  self.data={}
                  self.got_headler=False
                  self.set_terminator(b'\r\n\r\n')

         def collect_incoming_data(self,data):
                  if not self.got_headler:
                           self.data.append(data)

         def found_terminator(self):
                  self.got_headler=True
                  headler_data=b''.join(self.data)
                  headler_text=
                  
