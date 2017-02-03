#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
from sys import argv

"""
	Ataque usando texto em claro
"""

f_claro = open(argv[1], 'r')
claro = f_claro.read()

f_escuro = open(argv[2], 'r')
escuro = f_escuro.read()

chave = ord(escuro[0]) - ord(claro[0])

print("\nChave: " + str(chave) + '\n')
