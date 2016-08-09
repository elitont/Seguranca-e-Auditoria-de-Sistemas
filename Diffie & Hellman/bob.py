import socket

HOST = ''
PORT = 5001
DEST_HOST = '127.0.0.1'
DEST_PORT = 5000 # Alice
SECRET_NUM = input("Numero secreto: ")
PUBLIC_BASE = 0
PUBLIC_MOD = 0
PUBLIC_CALC = 0
SECRET_KEY = 0

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

client, mensagem = tcp.accept()
while True:
    msg = client.recv(4096)
    if not msg: break
    else:
        buf = msg.split(' ')
        PUBLIC_BASE = int(buf[0])
        PUBLIC_MOD = int(buf[1])
        PUBLIC_CALC = int(buf[2])
    print "Alice:", msg
client.close()
SECRET_KEY = (PUBLIC_CALC ** SECRET_NUM) % PUBLIC_MOD
tcp.close()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((DEST_HOST, DEST_PORT))
PUBLIC_CALC = (PUBLIC_BASE ** SECRET_NUM) % PUBLIC_MOD
msg = str(PUBLIC_CALC)
tcp.send (msg)
print "Mensagem enviada:", msg
tcp.close()

print "Chave secreta compartilhada com Alice: ", SECRET_KEY
