from Crypto import Random
from Crypto.PublicKey import RSA
from sys import argv

file = open(argv[1])
texto = file.read()
file.close()

random_generator = Random.new().read
secret_key = RSA.generate(2**12, random_generator)
public_key = secret_key.publickey()

cifrado = public_key.encrypt(texto, 32)
decifrado = secret_key.decrypt(cifrado)
print "\nTexto cifrado (chave publica):\n", cifrado
print "\nTexto decifrado (chave privada):\n", decifrado
