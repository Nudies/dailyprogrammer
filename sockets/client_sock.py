import socket
import threading


LOCK = threading.Lock()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))
NAME = raw_input('User Name: ')

def sender():
    data = ''
    while data != 'q':
        data = raw_input('')
        s.send('%s: %s' % (NAME, data))
    s.close()
    return


def reader():
    while 1:
        print s.recv(1024)
       
       
send_thread = threading.Thread(target=sender)
recv_thread = threading.Thread(target=reader)
send_thread.start()
recv_thread.start()
