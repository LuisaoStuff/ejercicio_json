########################################################################
#						      Librerías							       #
########################################################################

import json
from os import system

########################################################################
#						      Funciones							       #
########################################################################

def EliminarRepetidos(lista):	#	Recibe una lista y elimina los elementos repetidos.

	ListaSinRepetir = []
	for A in lista:
		if A not in ListaSinRepetir:
			ListaSinRepetir.append(A)
	return sorted(ListaSinRepetir)	#	Devuelve una lista de elementos únicos ordenada.

def LimpiarCadena(Cadena):	#	Esta función elimina algunos caracteres de una cadena. La uso sobre todo
							#	dentro de la función BuscadorDeJuegos(juego)
	CadenaLimpia=Cadena.upper().replace("-","").replace(" ","").replace("(","").replace(")","").replace(".","").strip()
	return CadenaLimpia

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
	Salida.close()
	system('rm salida.txt')

def Desinstalar_feh():

	system('whereis feh > salida.txt')
	clear(10)
	with open("salida.txt","r") as Salida:
		if Salida.readlines()[0]!='feh:\n':
			Afirmacion=['YES','Y','SI','S']
			Eleccion=input('	   Antes de salir, ¿desea desinstalar el paquete "feh"?	').upper()
			if Eleccion in Afirmacion:
				system('sudo apt-get remove -y feh')
	Salida.close()
	system('rm salida.txt')

def ListaPersonajes(Diccionario):
	Lista=[]
	for Personaje in Diccionario["characters"]:
		Lista.append(Personaje)

	return sorted(Lista)

def BuscarPersonaje(Busqueda,Lista1):
	for Personaje in Lista1:
		Coincidencia=LimpiarCadena(Personaje)
		if Coincidencia==Busqueda:
			
			return Personaje


def ContadorApariciones(Personaje,Diccionario):

	Total=Diccionario["characters"][BuscarPersonaje(Personaje,ListaPersonajes(Diccionario))]["comics"]["available"]
	return Total

def Categorias(Diccionario):

	Categorias=[]
	for Personaje in Diccionario["characters"]:
		
		for categoria in Diccionario["characters"][Personaje]["wiki"]["categories"]:
			print(categoria)
			Categorias.append(categoria)

	return EliminarRepetidos(Categorias)


########################################################################
#						   Código Principal							   #
########################################################################

with open("Personajes Marvel.json","r") as fichero:

	Diccionario = json.load(fichero)

	fehInstalado()

	while True:													############################
																#			Menú           #
		clear(0)												############################
		print('''\n\n	Elige una de las siguientes opciones:				

		1. Lista los nombres de todos los personajes
		2. Contador de apariciones en comics
		3. Personajes por categoría
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
			#s	Desinstalar_feh()
				clear(0)
				break

			elif opcion==1:
				clear(0)
				Lista=ListaPersonajes(Diccionario)
				for Personaje in Lista:
					print("			",Personaje)
				Pausa()
	
			elif opcion==2:
				clear(9)
				Busqueda=LimpiarCadena(input('''			    Introduce un personaje
		  	    > '''))
				Total=ContadorApariciones(Busqueda,Diccionario)
				print("		",BuscarPersonaje(Busqueda,ListaPersonajes(Diccionario)))
				print("		Apariciones >",Total,"\n")
				Pausa()
	
			elif opcion==3:
				
				clear(9)			
				for categoria in Categorias(Diccionario):
					print(categoria)
				Busqueda=LimpiarCadena(input('''			    Introduce un personaje
		  	    > '''))

'''										


			elif opcion==4:

			elif opcion==5:
'''