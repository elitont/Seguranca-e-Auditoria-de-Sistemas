#!/opt/plone/zinstance/bin/python3
# -*- coding: utf-8 -*-
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii
import base64
import sys

opt = int(sys.argv[1])
text = open(sys.argv[2], 'r')

if opt == 1:
	text = text.read()
	hash = SHA256.new()
	hash.update(text.encode('utf-8'))
	sha256 = hash.digest()
	random_generator = Random.new().read
	key = RSA.generate(2048, random_generator)
	public_key = key.publickey()
	publickey_txt = public_key.exportKey("PEM")
	signature = public_key.encrypt(sha256, 32)

	file_key = open('cfg/chave_publica.pem', 'w')
	file_key.write(publickey_txt.decode('utf-8'))
	file_vldt = open('cfg/valida.in', 'w')
	file_vldt.write(str(text) + '\n' + str(sha256) + '\n')
	file_vldt.write(str(signature) + '\n' + str(publickey_txt))

else:

	all_text = text.readlines()
	text = all_text[0].replace('\n', '')
	signature_gerated = all_text[2].replace('\n', '')

	hash = SHA256.new()
	hash.update(text.encode('utf-8'))
	sha = hash.digest()

	public_key = RSA.importKey(open('cfg/chave_publica.pem').read())
	signature = public_key.encrypt(sha, 32)

	if str(signature) == str(signature_gerated):
		print("Ok!")
	else:
		print("Inválida!")
