import socket
import thread
import time

HOST = ''
PORT = 5000 
DEST_HOST = '127.0.0.1' 
DEST_PORT = 5001 # Bob

def sender(tcp):
    tcp.connect((DEST_HOST, DEST_PORT))
    
    print "Conectado com Bob."
    msg = raw_input()
    while msg <> '\x18': # CTRL+X
        tcp.send (msg)
        msg = raw_input()
    tcp.close()
    print "Desconectado."

def receiver(con):
    while True:
        msg = con.recv(1024)
        if not msg: break
        print "Bob:", msg
    con.close()
    thread.exit()

t = raw_input("Connect? (S/N): ")
if t == 'N':
    exit(0)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sender
thread.start_new_thread(sender, tuple([tcp,]))
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

while True:
    con, mensagem = tcp.accept()
    # receiver
    thread.start_new_thread(receiver, tuple([con,]))
tcp.close()
