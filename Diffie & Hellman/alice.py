import socket

HOST = ''
PORT = 5000 
DEST_HOST = '127.0.0.1' 
DEST_PORT = 5001 # Bob
SECRET_NUM = input("Numero secreto: ")
PUBLIC_BASE = input("Base: ")
PUBLIC_MOD = input("Mod: ")
PUBLIC_CALC = (PUBLIC_BASE ** SECRET_NUM) % PUBLIC_MOD
SECRET_KEY = 0

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((DEST_HOST, DEST_PORT))
msg = str(PUBLIC_BASE) + ' ' + str(PUBLIC_MOD) + ' ' + str(PUBLIC_CALC)
tcp.send (msg)
print "Mensagem enviada:", msg
tcp.close()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

con, mensagem = tcp.accept()
while True:
    msg = con.recv(1024)
    if not msg: break
    else:
        PUBLIC_CALC = int(msg)
    print "Bob:", msg
con.close()

SECRET_KEY = (PUBLIC_CALC ** SECRET_NUM) % PUBLIC_MOD
print "Chave secreta compartilhada com Bob: ", SECRET_KEY
tcp.close()
