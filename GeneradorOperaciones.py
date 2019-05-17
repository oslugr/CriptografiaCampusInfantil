#
#
#	Programa que dado una operación benera el
#	Codigo de programación en python correspondiente
#
#
#


def f(x):
	x.upper()
	return {
		'+':'\n		letra_en_numero = letra_en_numero + ',
		'-':'\n		letra_en_numero = letra_en_numero - ',
		'*':'\n		letra_en_numero = letra_en_numero * ',
		'/':'\n		letra_en_numero = letra_en_numero / '
	}.get(x,0)


def f2(x,codigo):
	x=x.upper()
	return {
		'T':'\n\n	for i in range(0,8) :\n		'+ codigo +	'\n\n',
		'P':'\n\n	for i in range(1,8,2):\n		'+ codigo +	'\n\n',
		'I':'\n\n	for i in range(0,8,2):\n		'+ codigo +	'\n\n'
	}.get(x,0)


Codigo=[]


print ('El codigo de cada operacion tiene que ser XXX. \n\n')

print ('La primera X es la operacion que vamos a hacer. Puede ser: \n')
print ('+: sumar al codigo \n')
print ('-: restar al codigo \n')
print ('/: dividir al codigo \n')
print ('*: multiplicar al codigo \n\n')

print ('La segunda X es el numero con el que vamos a realizar la\noperacion anterior. Tiene que ser un numero entre 1 y 9 \n')

print ('La tercera X es a que digitos de la clave vamos a realizarles\nla operacion. Puede ser:')
print ('T: Todos los digitos \n')
print ('I: Los digitos impares \n')
print ('P: Los digitos pares \n')


fallo=True

for i in range(0,4):
	while fallo:
		print ('\n\nIntroduce el codigo de la operacion', i+1 , ': ')
		
		operacion = input()

		codigo='letra_en_numero = ord(codigo[i])'
		if len(operacion)!=3:
			print ('El codigo de cada operacion tiene que ser XXX.')
		else:
			if f(operacion[0])==0:
				print ("La primera X no se ha introducido bien")
			else:
				codigo+=f(operacion[0])
				if operacion[1]<'1' or operacion[1]>'9': 
					print ("La segunda X no se ha introducido bien")
				else:
					codigo+=operacion[1]
					codigo+='\n		codigo[i] = chr(letra_en_numero)'
					if f2(operacion[2],codigo)==0:
						print ("La tercera X no se ha introducido bien")
					else:
						codigo = f2(operacion[2],codigo)
						codigo+= '	return codigo,"'+operacion.upper()+'"\n\n'
						Codigo.append(codigo)
						fallo=False
	fallo=True


print ('\n\n\n')

for i in range(0,4):
	print ('Esta es la operacion ',i+1)
	print (Codigo[i])


print ('\n\n\n')



