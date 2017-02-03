from sys import argv

file = open(argv[1], 'r')
data = file.read()
chave = int(argv[3])

if(int(argv[2]) == 1):
	file_cifrado = open('../data/outputs/cesar_cifrado.txt', 'w')
	for l in data:
		k = int((ord(l) + chave) % 256)	
		cifra = chr(k)
		file_cifrado.write(cifra)
else:
	file_cifrado = open('../data/outputs/cesar_cifrado.txt').read()
	file_decifrado = open('../data/outputs/cesar_decifrado.txt', 'w')
	for l in file_cifrado:
		j = int((ord(l) - chave) % 256)
		decifra = chr(j)
		file_decifrado.write(decifra)
