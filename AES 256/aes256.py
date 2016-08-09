from Crypto import Random
from Crypto.Cipher import AES
from sys import argv

file = open(argv[1])
chave = file.read()
file.close()

file = open(argv[2])
texto = file.read()
file.close()

IV = Random.new().read(AES.block_size) # 16 bytes aleatorios

try:
	cipher = AES.new(chave, mode=AES.MODE_CFB, IV=IV)
except ValueError as error:
	print error
	exit(0)

cifrado = IV + cipher.encrypt(texto)
decifrado = cipher.decrypt(cifrado)[AES.block_size:]
print "\nTexto cifrado:\n", cifrado
print "\nTexto decifrado:\n", decifrado
