# Assinatura Digital

by Eliton Traverssini - <eliton.traverssini@gmail.com>

O programa lê um arquivo de texto e produz uma assinatura digital (1) ou valida uma assinatura já criada (2).

Uso:

	Gerar assinatura
		$ python3 assinatura_digital.py 1 data/text.in
		
		# ou
		
		$ python3 assinatura_digital.py 1 <seuarquivodetexto>

	Validar assinatura
		$ python3 assinatura_digital.py 2 cfg/valida.in

Obs: 
	Os arquivos "cfg/chave_publica.pem" e "cfg/valida.in" são usados para qualquer texto de entrada,
	alterando-se para cada texto diferente na geração de assinatura digital.