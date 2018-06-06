import socketserver


addr=('',80)
class Myrequesthandler(socketserver.StreamRequestHandler):
         def handler(self):
                  data=self.rfile.readline()+self.clinet.address
                  yield data
                  d=self.wfile.write('你成功了')

recvtcp=socketserver.ThreadingTCPServer(addr,Myrequesthandler)
recvtcp.serve_forever()
