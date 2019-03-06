########################################################################
#						      Librerías							       #
########################################################################

import json
from os import system

########################################################################
#						      Funciones							       #
########################################################################

def clear(Espaciado):	#	Pequeña funcion que simula un clear, además recibe un entero para centrar
						#	el texto que lo sigue a continuación.
	system('clear')
	print("\n"*Espaciado)

def Pausa():

	input('\n		  "Pusa enter" para volver al menú...')

def fehInstalado():

	system('whereis feh > salida.txt')
	clear(7)
	with open("salida.txt","r") as Salida:
		if Salida.readlines()[0]=='feh:\n':
			print('''		Parece que no tienes instalado el paquete "feh"
		Si desea que durante la ejecución de este python
		se puedan mostrar las imágenes de los personajes
		debería instalarlo.
				''')
			Afirmacion=['YES','Y','SI','S']
			Eleccion=input('		¿Desea instalar el paquete "feh"?	').upper()
			if Eleccion in Afirmacion:
				system('sudo apt-get install -y feh')
				Miniaturas=True
			else:
				Miniaturas=False
		else:
			Miniaturas=True

def Desinstalar_feh():

	system('whereis feh > salida.txt')
	clear(10)
	with open("salida.txt","r") as Salida:
		if Salida.readlines()[0]!='feh:\n':
			Afirmacion=['YES','Y','SI','S']
			Eleccion=input('	   Antes de salir, ¿desea desinstalar el paquete "feh"?	').upper()
			if Eleccion in Afirmacion:
				system('sudo apt-get remove -y feh')


########################################################################
#						   Código Principal							   #
########################################################################

with open("Personajes Marvel.json","r") as fichero:

	Diccionario = json.load(fichero)

	fehInstalado()

	Pausa()

	while True:

																############################
																#			Menú           #
		clear(0)												############################
		print('''\n\n	Elige una de las siguientes opciones:				

		1. Lista los nombres de todos los personajes
		2. Contador de apariciones en comics
		3. 
		4. 
		5. 
		0. Salir
			''')
		
		try:		#	Uso un try por si el usuario introduce un valor nulo o un caracter no entero. 

			opcion=int(input("\n		Opción:  "))

		except:		#	Error:

			print('\n		Debes introducir una opción válida')		
			Pausa()
		else:		#	Si introduce un entero ejecuta una de las siguientes opciones.

			if opcion==0:		#############
								#	Salir   #
				clear(0)		#############
				Desinstalar_feh()
				clear(0)
				break
'''
			elif opcion==1:

			elif opcion==2:											

			elif opcion==3:

			elif opcion==4:

			elif opcion==5:
'''