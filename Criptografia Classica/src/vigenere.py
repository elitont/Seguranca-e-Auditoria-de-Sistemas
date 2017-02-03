#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
from sys import argv
from itertools import cycle

key = str(argv[2])
key = [ord(i) for i in key]

if(int(argv[1]) == 1):
	file = open(argv[3], 'r')
	msg = file.read()
	cifra = '' 
	cifrado = open('data/outputs/vigenere_cifrado.txt', 'w')
	for (c,m) in zip(cycle(key), msg):
		k = chr(int(ord(m) + c) % 256)
		cifra += k
		cifrado.write(k)
else:
	cifra = open('data/outputs/vigenere_cifrado.txt', 'r').read()
	decifra = open('data/outputs/vigenere_decifrado.txt', 'w')
	for (c, m) in zip(cycle(key), cifra):
		k = chr(int(ord(m) - c) % 256)
		decifra.write(k)
