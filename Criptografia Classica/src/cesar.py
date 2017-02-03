#!/opt/plone/zinstance/bin/python3
# -*- coding: utf-8 -*-
from sys import argv
"""
	Cifragem e Decifragem com a Cifra de César
"""

chave = int(argv[2])

if(int(argv[1]) == 1):
	file = open(argv[3], 'r')
	data = file.read()
	file_cifrado = open('data/outputs/cesar_cifrado.txt', 'w')
	for l in data:
		k = int((ord(l) + chave) % 256)	
		cifra = chr(k)
		file_cifrado.write(cifra)
else:
	file_cifrado = open('data/outputs/cesar_cifrado.txt').read()
	file_decifrado = open('data/outputs/cesar_decifrado.txt', 'w')
	for l in file_cifrado:
		j = int((ord(l) - chave) % 256)
		decifra = chr(j)
		file_decifrado.write(decifra)
