# Implementação dos trabalhos referentes a Criptografia Clássica

by Eliton Traverssini - <eliton.traverssini@gmail.com>

############################################################################################################

# Trabalho 6: 
	Implementar as 4 cifras de criptografia clássica discutidas em aula:
	*	Vigenere OK
	*	Cesar OK
	*	Transposição 
	*	Substituição


# Trabalho 7: 
	Implementar ataques com texto em claro para as 4 cifras implementadas no T6.
	*	Vigenere OK
	*	Cesar OK
	*	Transposição 
	*	Substituição

# Trabalho 8:
	Implementar ataque SEM O TEXTO em claro (força bruta), para as cifras de Vigener, Cesar e Transposição.
	*	Vigenere OK
	*	Cesar OK
	*	Transposição

# Trabalho 11:
	Implementar ataxo SEM O TEXTO em claro para a cifra de substituição.
	*	Substituição

############################################################################################################

# Uso:
	
	César:
	
	*	Cifrar:

			$ python src/cesar.py 1 <int(chave)> data/inputs/1.input

			ou

			$ python src/cesar.py 1 <int(chave)> <seu_arquivo>

	*	Decifrar:

			$ python src/cesar.py 2 <int(chave)>

	*	Ataque com texto em claro:
			
			$ python ataque/claro/cesar_ataque_claro.py data/outputs/cesar_decifrado.txt data/outputs/cesar_cifrado.txt

	*	Ataque por força bruta:

			$ python ataque/escuro/cesar_forca_bruta.py data/outputs/cesar_cifrado.txt

	*	Saídas:
			data/outputs/cesar_cifrado.txt
			data/outputs/cesar_decifrado.txt


##########################################################################################################
	Vigenere:
	
	*	Cifrar:
			$ python src/vigenere.py 1 <str(chave)> data/inputs/1.input

	*	Decifrar:

			$ python src/vigenere.py 2 <str(chave)>

	*	Ataque com texto em claro:

			$ python ataque/claro/vigenere_ataque_claro.py data/outputs/vigenere_decifrado.txt data/outputs/vigenere_cifrado.txt

	*	Ataque por força bruta:
			
			$ python ataque/escuro/vigenere_forca_bruta.py data/outputs/vigenere_cifrado.txt

	*	Saídas:
			data/outputs/vigenere_cifrado.txt
			data/outputs/vigenere_decifrado.txt


##########################################################################################################
	Transposição:
	
	*	Cifrar:

	*	Decifrar:

	*	Ataque com texto em claro:

	*	Ataque por força bruta:
	
	*	Saídas:


##########################################################################################################
	Substituição:
	
	*	Cifrar:

	*	Decifrar:

	*	Ataque com texto em claro:

	*	Ataque por força bruta:
	
	*	Saídas:
