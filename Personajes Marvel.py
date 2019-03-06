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
	return Miniaturas

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
	try:
		for Personaje in Lista1:
			Coincidencia=LimpiarCadena(Personaje)
			if Coincidencia==Busqueda:
				return Personaje
	except:
		return 0

def ContadorApariciones(Personaje,Diccionario):
	try:
		Total=Diccionario["characters"][BuscarPersonaje(Personaje,ListaPersonajes(Diccionario))]["comics"]["available"]
	except:
		Total='No aparece'
	return Total

def Categorias(Diccionario):

	Categorias=[]
	for Personaje in Diccionario["characters"]:
		
		for categoria in Diccionario["characters"][Personaje]["wiki"]["categories"]:
			Categorias.append(categoria)	
	return EliminarRepetidos(Categorias)


def PersonajesPorCategoria(Diccionario,Categoria):
	Lista=[]
	CategoriaLimpia=LimpiarCadena(Categoria)
	for personaje in Diccionario["characters"]:

		for cat in Diccionario["characters"][personaje]["wiki"]["categories"]:
			Coincidencia=LimpiarCadena(cat)
			if Coincidencia==CategoriaLimpia:		
				personaje="			"+personaje+"/ Apariciones > "+str(Diccionario["characters"][personaje]["comics"]["available"])
				Lista.append(personaje)			
	return sorted(Lista)

def ListaEventos(Diccionario):
	Lista=[]
	for personaje in Diccionario["characters"]:
		for evento in Diccionario["characters"][personaje]["events"]["items"]:
			Lista.append(evento["name"])
	return EliminarRepetidos(Lista)

def PersonajesPorEvento(Diccionario,evento):
	Lista=[]
	for personaje in Diccionario["characters"]:
		if Diccionario["characters"][personaje]["events"]["available"]!=0:
			for event in Diccionario["characters"][personaje]["events"]["items"]:
				EventoL=LimpiarCadena(evento)
				Coincidencia=LimpiarCadena(event["name"])
				if Coincidencia==EventoL:		
					Lista.append(personaje)
	return Lista		

def Miniatura(Personaje,Diccionario):
	url=Diccionario["characters"][Personaje]["thumbnail"]["path"]
	extension=Diccionario["characters"][Personaje]["thumbnail"]["extension"]
	urlcompleta=url+'.'+extension
	return urlcompleta

def EventosP(Personaje,Diccionario):
	EncuentrosTotales=[]
	ListaDeEventos=ListaEventos(Diccionario)
	for evento in ListaDeEventos:
		for eventoPersonaje in Diccionario["characters"][Personaje]["events"]["items"]:
			if evento==eventoPersonaje["name"]:
				Encuentro=[]
				Encuentro.append(evento)
				ListaAV=PersonajesPorEvento(Diccionario,evento)
				ListaAV.pop(ListaAV.index(Personaje))	#Indexa la posicion del protagonista en el evento y lo elimina
				Encuentro.append(ListaAV)
				EncuentrosTotales.append(Encuentro)
	return EncuentrosTotales

def Heroe_Villano(Personaje,Diccionario):
	HV=['Heroes','Villains','Reformed Villains']
	for rol in Diccionario["characters"][Personaje]["wiki"]["categories"]:
		if rol in HV:
			return rol

########################################################################
#						   Código Principal							   #
########################################################################

with open("Personajes Marvel.json","r") as fichero:

	Diccionario = json.load(fichero)

	Miniaturas=fehInstalado()


	while True:													############################
																#			Menú           #
		clear(0)												############################
		print('''\n\n	Elige una de las siguientes opciones:				

		1. Lista los nombres de todos los personajes
		2. Contador de apariciones en comics
		3. Personajes por categoría
		4. Menú de eventos marvel
		5. Personaje, conocidos y enemigos
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
				clear(1)		
				Cat=Categorias(Diccionario)	
				for categoria in Cat:
					print("			",categoria)
				Busqueda=LimpiarCadena(input('''
			 Introduce una categoria
		  	 > '''))
				for linea in PersonajesPorCategoria(Diccionario,Busqueda):
						print(linea)
				Pausa()
				del Cat
			
			elif opcion==4:
				clear(1)
				Events=ListaEventos(Diccionario)
				for evento in Events:
					print("		",evento)
				Busqueda=LimpiarCadena(input('''
			 Introduce un evento
		  	 > '''))
				Participantes=PersonajesPorEvento(Diccionario,Busqueda)
				for participante in Participantes:
					print("		",participante)
				Pausa()

			elif opcion==5:
				Lista=ListaPersonajes(Diccionario)
				for Personaje in Lista:
					print("			",Personaje)
				Busqueda=LimpiarCadena(input('''			Introduce un personaje
		  	> '''))
				Personaje=BuscarPersonaje(Busqueda,ListaPersonajes(Diccionario))
				
				try:
					clear(0)
					print("	",Personaje,">>",Heroe_Villano(Personaje,Diccionario),"\n\n")
					ConocidosYEventos=EventosP(Personaje,Diccionario)
					for evento in ConocidosYEventos:
						
						print("\n	En el evento '"+evento[0]+"' coincidió con",len(evento[1]),"personajes:")
						for personajes in evento[1]:
							print("	-",personajes,">>",Heroe_Villano(personajes,Diccionario))
					
					if Miniaturas:
						print("\n\n			Cargando imagen...")
						system('feh -Za 125 --title "{}" {} &'.format(Personaje,Miniatura(Personaje,Diccionario)))
					Pausa()
				except:
					clear(10)
					input('	      Personaje inválido. Pulsa "enter para continuar..."')