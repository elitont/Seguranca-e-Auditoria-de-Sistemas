#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
import sys
from math import log
from bitarray import *

def adicionaPrefixos(xs, p):
    return dict((k, bitarray(p) + v) for (k,v) in xs.items())

class N:
    def __init__(self, x, f):
        self.x = x
        self.f = f
        self.l = None
        self.r = None

    def join(self, o):
        n = N(None, self.f + o.f)
        n.l = self
        n.r = o
        return n

    def coding(self):
        l = {}
        r = {}
        if self.x:
            return {self.x: bitarray()}
        if self.l: 
            l = self.l.coding()
        if self.r:
            r = self.r.coding()
        ret = {}
        ret.update(adicionaPrefixos(l, '0'))
        ret.update(adicionaPrefixos(r, '1'))
        return ret

    def __lt__(self, o):
        return self.f > o.f

    def __repr__(self):
        return "N(%s,%f)" % (self.x, self.f)

def huffmann(l):
    while(len(l) > 1):
        l.sort()
        a = l.pop()
        b = l.pop()
        c = a.join(b)
        l.append(c)
    return l.pop().coding()

def frequencia(texto): 
    ##Quantas vezes cada caracter apareceu no texto
    for c in texto:
        x = freq.get(c) or 0
        freq.update({c: x+1})
    
def entropia(texto, base):
    frequencia(texto)
    # p e a probabilidade de massa
    acum = 0
    for i in freq:
        p = float(freq[i]) / float(len(texto))
        acum += p * log(p, base)
    return -acum

def compHuffman(texto):
    l = []
    for i in freq:
        l.append(N(i, freq[i]))
    l.sort()
    arvore = huffmann(l)
    array = bitarray()
    for i in texto:
        array += arvore[i]
    return array.tobytes()

try:
    arq_name = sys.argv[1]
except:
    usage()

texto_orig = open(sys.argv[1], 'rb').read()
freq = {}
entropia_orig = entropia(texto_orig, 256)

texto_zip = compHuffman(texto_orig)
freq = {}
entropia_zip = entropia(texto_zip, 256)

open('data/texto_zip.out', 'wb').write(texto_zip)

print("Entropia do arquivo original: " + str(entropia_orig))
print("Entropia do arquivo compactado: " + str(entropia_zip))
