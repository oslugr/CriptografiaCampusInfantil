#
#
#	Programa que se modifica para añadir las operaciones de encriptacion.
#	Ademas se usa para que el equipo que tenga que resolverlo.
#
#
#
##################################################################################


def PrimeraEncriptacion(codigo):

	for i in range(0,8) :
		letra_en_numero = ord(codigo[i])
		letra_en_numero = letra_en_numero + 1
		codigo[i] = chr(letra_en_numero)

	return codigo,"+1t"

##################################################################################


def SegundaEncriptacion(codigo):

	for i in range(0,8) :
		letra_en_numero = ord(codigo[i])
		letra_en_numero = letra_en_numero + 1
		codigo[i] = chr(letra_en_numero)

	return codigo,"+1t"


##################################################################################


def TerceraEncriptacion(codigo):

	for i in range(0,8) :
		letra_en_numero = ord(codigo[i])
		letra_en_numero = letra_en_numero + 1
		codigo[i] = chr(letra_en_numero)

	return codigo,"+1t"

##################################################################################


def CuartaEncriptacion(codigo):

	for i in range(0,8) :
		letra_en_numero = ord(codigo[i])
		letra_en_numero = letra_en_numero + 1
		codigo[i] = chr(letra_en_numero)

	return codigo,"+1t"	

##################################################################################


codigo_inicial="11111111"



##################################################################################



import random




def f(x):
	return {
		1:'\nJajajajaja fallastes, te voy ganando.',
		2:'\nIntentalo de nuevo.',
		3:'\nUhhh que pena no has acertado.',
		4:'\nNo has acertado. :P '
	}.get(x,0)




codigo_final=list(codigo_inicial)

codigo1,a1=PrimeraEncriptacion(codigo_final)

Ordenes_final=a1

codigo2,a2=SegundaEncriptacion(codigo1)

Ordenes_final+=a2

codigo3,a3=TerceraEncriptacion(codigo2)

Ordenes_final+=a3

codigo4,a4=CuartaEncriptacion(codigo3)

Ordenes_final+=a4

codigo_final=''.join(codigo_final)







print ('\n\n\n\n')

print ('Este es la clave final. ',codigo_final)
print ('Podreis averiguar cual era la clave que introdujimos?\n')

print ('Las operaciones que hemos hecho son:', Ordenes_final,'\n\n\n')



fallo=True

while fallo:
	codigo_introducido = input("Introduce la clave de desactivacion: ")
	if codigo_inicial==codigo_introducido:

		print ("Enhorabuena. Has acertado la clave.")
		fallo=False
	else:
		print (f(random.randint(1,4)))




















