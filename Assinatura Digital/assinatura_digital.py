#!/opt/plone/zinstance/bin/python3
# -*- coding: utf-8 -*-
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import binascii
import base64
import sys

opt = sys.argv[1]

if opt == 1:
	# text = sys.argv[2]
	print("criar assinatura digital")
else:
	print("validar assinatura digital")
