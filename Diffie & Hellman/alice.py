import socket
import thread

HOST = ''
PORT = 5000 
DEST_HOST = '127.0.0.1' 
DEST_PORT = 5001 # Bob
SECRET_NUM = input("Numero secreto: ")
PUBLIC_BASE = input("Base: ")
PUBLIC_MOD = input("Mod: ")
PUBLIC_CALC = (PUBLIC_BASE ** SECRET_NUM) % PUBLIC_MOD
SECRET_KEY = 0



def sender(tcp):
    tcp.connect((DEST_HOST, DEST_PORT))
    # sep = '\n'
    print "Conectado com Bob."
    msg = str(PUBLIC_BASE) + ' ' + str(PUBLIC_MOD) + ' ' + str(PUBLIC_CALC)
    print "enviando: ", msg
    tcp.send (msg)
    
    tcp.close()
    print "Envio pronto."

def receiver(con):
    i = 1
    while i <= 1:
        msg = con.recv(1024)
        if not msg: break
        else:
            i += 1
            PUBLIC_CALC = int(msg)

        print "Bob:", msg
    con.close()
    SECRET_KEY = (PUBLIC_CALC ** SECRET_NUM) % PUBLIC_MOD
    print "Chave secreta compartilhada com Bob: ", SECRET_KEY
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
