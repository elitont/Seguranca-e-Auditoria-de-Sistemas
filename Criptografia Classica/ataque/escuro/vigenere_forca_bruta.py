#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
from itertools import cycle
from sys import argv
import itertools

"""
    Ataque por força bruta, sem texto em claro
"""

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

data = open(argv[1], 'rb').read()

words_english = open('data/words_example.in', 'rb').read()
words_english = words_english.split()

chaves_invalidas = []

for i in range(1, 4):
	r = itertools.product(chars, repeat=i)
	for i in r:
		key = [-ord(j) for j in i]
		msg_decifrada = bytes((c + m) % 256 for (c, m) in zip(cycle(key), data))
		all_word = msg_decifrada.split()
		
		words = []
		for word in all_word[0:30]:
			if word in words_english:
				words.append(word)

		if(len(words) > 5):
			open('data/outputs/vigenere_decifrado.txt', 'wb').write(msg_decifrada)
