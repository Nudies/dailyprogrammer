import socket
import select
import sys

class ChatServer(object):
        '''
        Simple chat server 
        '''
        def __init__(self, buf=1024):
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.buf = buf
                self.SOCKET_LIST = []
    
    
        def run(self, ip='127.0.0.1', port=8000, size=5):
                try:
                    self.sock.bind((ip, port))
                    self.sock.listen(size)
                    self.SOCKET_LIST.append(self.sock)
                    print 'Server running on %s:%s' % (ip, port)
                except:
                    print 'error'
                    self.sock.close()
                    sys.exit(1)
        
                while 1:
                    read_sockets, write_sockets, error_sockets = (
                        select.select(self.SOCKET_LIST, [], [], 0))
                    for sock in read_sockets:
                        if sock == self.sock:
                            conn, addr = self.sock.accept()
                            self.SOCKET_LIST.append(conn)
                            print 'Client %s:%s connected' % addr 
                        else:
                            try:
                                data = sock.recv(self.buf)
                                if data:
                                    self.speaker(sock, data)
                                else:
                                    self.SOCKET_LIST.remove(sock)
                                    print 'Client %s:%s disconnected' % addr
                                    self.speaker(sock, 'Client %s:%s disconnected' % addr)
                            except:
                                print 'error with %s:%s' % addr
                                self.speaker(sock, 'Client %s:%s disconnected' % addr)
                                
        
        def speaker(self, client_sock, msg):
                for sock in self.SOCKET_LIST:
                    if sock != self.sock and sock != client_sock:
                        try:
                            sock.send(msg)
                        except:
                            sock.close()
                            if sock in self.SOCKET_LIST:
                                self.SOCKET_LIST.remove(sock)
               

if __name__ == '__main__':
        server = ChatServer()
        server.run()
        server.sock.close()
