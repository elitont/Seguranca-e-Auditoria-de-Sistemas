#!/opt/plone/zinstance/bin/python3
# -*- coding: utf-8 -*-
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii
import base64
import sys

opt = int(sys.argv[1])

if opt == 1:
	text = open(sys.argv[2], 'r+').read()
	hash = SHA256.new()
	hash.update(text.encode('utf-8'))
	sha_256 = hash.digest()

	random_generator = Random.new().read
	key = RSA.generate(2048, random_generator)
	public_key = key.publickey()
	str_public_key = public_key.exportKey("PEM")
	str_private_key = key.exportKey("PEM")
	signature = public_key.encrypt(sha_256, 32)

	fkey = open('cfg/chave_publica.pem', 'w')
	fkey.write(str_public_key.decode('utf-8'))

	fout = open('cfg/valida.in', 'w')
	fout.write(str(text) + '\n' + str(sha_256) + '\n')
	fout.write(str(signature) + '\n' + str(str_public_key))

else:
	print("validar assinatura digital")
