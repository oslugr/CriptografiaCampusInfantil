# -*- coding: utf-8 -*-
#
#
#	Programa que dado una operación Genera el
#	Código de programación en python correspondiente
#
#	
#


def f(x): #Se usa para elegir el la primera operación, en caso de no escoger bien al operación se volverá a preguntar
	x.upper()
	return {
		'+':'\n		letra_en_numero = letra_en_numero + ',
		'-':'\n		letra_en_numero = letra_en_numero - ',
		'*':'\n		letra_en_numero = letra_en_numero * '
	}.get(x,0)


def f2(x,codigo): #Se usa para elegir la tercera operación, en caso de no escoger bien la operación se volverá a preguntar
	x=x.upper()
	return {
		'T':'\n\n	for i in range(0,8) :\n		'+ codigo +	'\n\n',
		'P':'\n\n	for i in range(1,8,2):\n		'+ codigo +	'\n\n',
		'I':'\n\n	for i in range(0,8,2):\n		'+ codigo +	'\n\n'
	}.get(x,0)


Codigo=[]


print ('El código de cada operación tiene que ser XXX. \n\n')

print ('	La primera X es la operación que vamos a hacer. Puede ser: \n')
print ('	+: sumar al código \n')
print ('	-: restar al código \n')
print ('	*: multiplicar al código \n\n')

print ('La segunda X es el numero con el que vamos a realizar la\noperación anterior. Tiene que ser un numero entre 1 y 9 \n')

print ('	La tercera X es a que dígitos de la clave vamos a realizarles la operación. Puede ser:')
print ('	T: Todos los dígitos \n')
print ('	I: Los dígitos impares \n')
print ('	P: Los dígitos pares \n')


fallo=True

for i in range(0,4):		#Bucle para realizar el numero de operaciones qeu se quiera
	while fallo:
		print ('\n\nIntroduce el codigo de la operacion', i+1 , ': ')
		
		operacion = input()

		codigo='letra_en_numero = ord(codigo[i])		#Se pasa la letra a número para poder realizar la operaciones'
		if len(operacion)!=3:
			print ('El codigo de cada operacion tiene que ser XXX.')
		else:
			if f(operacion[0])==0:		#Se introduce la primera cadena con la operacion
				print ("La primera X no se ha introducido bien")
			else:
				codigo+=f(operacion[0])
				if operacion[1]<'1' or operacion[1]>'9': 
					print ("La segunda X no se ha introducido bien")
				else:
					codigo+=operacion[1]
					codigo+='\n		codigo[i] = chr(letra_en_numero)		#Se devuelve el valor numerico para ponerlo como letra despues de las operaciones'
					if f2(operacion[2],codigo)==0:
						print ("La tercera X no se ha introducido bien")
					else:
						codigo = f2(operacion[2],codigo)
						codigo+= '	return codigo,"'+operacion.upper()+'"					#Devulve el codigo de la operacion\n\n'
						Codigo.append(codigo)
						fallo=False
	fallo=True


print ('\n\n\n')

for i in range(0,4):
	print ('Esta es la operacion ',i+1)
	print (Codigo[i])


print ('\n\n\n')


