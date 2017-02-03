#!/opt/plone/zinstance/bin/python3
# -*- coding: utf-8 -*-
from sys import argv

file = open(argv[1], 'r')
fout = open('data/padroes.txt', 'w')
palavras = file.readlines()

all_padroes = {}

for w in palavras:
	w = w.replace("\n","")
	i = 0
	padrao = ''
	padrao_w = {}

	for c in w:
		if i == 0:
			padrao_w.update({c: i})
			padrao += str(i)
			i += 1
		else:
			if padrao_w.get(c) == None:
				padrao_w.update({c: i})
				padrao += str(i)
				i += 1
			else:
				padrao += str(padrao_w.get(c))
	
	all_padroes.update({w: padrao})
	fout.write(('{0:<20} {1:<20}'.format(w, padrao))+'\n')
