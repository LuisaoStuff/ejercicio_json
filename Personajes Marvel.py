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
													#######################################################
	system('whereis feh > salida.txt')				#	Comprueba  si  tienes instalado  el paquete feh   #
	clear(7)										#	para luego poder ejecutar el  comando. Si no lo   #
	with open("salida.txt","r") as Salida:			#	tienes instalado, te da la opcion de instalarlo   #
		if Salida.readlines()[0]=='feh:\n':			#######################################################
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

	system('whereis feh > salida.txt')					#############################################
	clear(10)											#	Al final del programa te da la opcion   #
	with open("salida.txt","r") as Salida:				#	de desinstalar el paquete feh 			#
		if Salida.readlines()[0]!='feh:\n':				#############################################
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
			Coincidencia=LimpiarCadena(Personaje)	#	Usa la funcion LimpiarCadena para "estandarizarla"
			if Coincidencia==Busqueda:				#	y que de esta forma la busqueda sea menos estricta
				return Personaje
	except:
		return 0

def ContadorApariciones(Personaje,Diccionario):
	try:
		Total=Diccionario["characters"][BuscarPersonaje(Personaje,ListaPersonajes(Diccionario))]["comics"]["available"]
	except:
		Total='No aparece'				#	Simplemente cuenta los comics que tiene un personaje concreto
	return Total

def Categorias(Diccionario):

	Categorias=[]
	for Personaje in Diccionario["characters"]:
		
		for categoria in Diccionario["characters"][Personaje]["wiki"]["categories"]:
			Categorias.append(categoria)	
	return EliminarRepetidos(Categorias)


def PersonajesPorCategoria(Diccionario,Categoria):
	Lista=[]												#####################################################
	CategoriaLimpia=LimpiarCadena(Categoria)				#	Devuelve una lista ordenada de los personajes   #
	for personaje in Diccionario["characters"]:				#	dentro de una categoría concreta				#
															#####################################################
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

def PersonajesPorEvento(Diccionario,evento):				#	Busca por el diccionario los personajes que tienen
	Lista=[]												#	un evento concreto dentro de events, y los mete en
	for personaje in Diccionario["characters"]:				#	una lista.
		if Diccionario["characters"][personaje]["events"]["available"]!=0:
			for event in Diccionario["characters"][personaje]["events"]["items"]:
				EventoL=LimpiarCadena(evento)
				Coincidencia=LimpiarCadena(event["name"])
				if Coincidencia==EventoL:		
					Lista.append(personaje)
	return Lista		

def Miniatura(Personaje,Diccionario):
	url=Diccionario["characters"][Personaje]["thumbnail"]["path"]				# Concatena los campos necesarios para
	extension=Diccionario["characters"][Personaje]["thumbnail"]["extension"]	# devolver una url de la miniatura
	urlcompleta=url+'.'+extension
	return urlcompleta

def EventosP(Personaje,Diccionario):			#	Recibe un personaje. Lee todos los eventos en los que ha estado
	EncuentrosTotales=[]						#	y los introduce en la funcion personajes por evento para crear
	ListaDeEventos=ListaEventos(Diccionario)	#	una lista de eventos y personajes
	for evento in ListaDeEventos:				#######################################################################
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

	Miniaturas=fehInstalado()	#	Comprueba que "feh" está instalado


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
				Desinstalar_feh()	#<<<<<<<<<<<<<<< Da la opción de desinstalar "feh"
				clear(0)
				break

			elif opcion==1:
				clear(0)							#################################################
				Lista=ListaPersonajes(Diccionario)	#	Lista los nombres de todos los personajes   #
				for Personaje in Lista:				#################################################
					print("			",Personaje)
				Pausa()
	
			elif opcion==2:				#	Cuenta el número de comics que tiene el personaje introducido
				clear(9)				#####################################################################
				Busqueda=LimpiarCadena(input('''			    Introduce un personaje
		  	    > '''))
				Total=ContadorApariciones(Busqueda,Diccionario)							#	Compara la cadena introducida
				print("		",BuscarPersonaje(Busqueda,ListaPersonajes(Diccionario)))	#	con la lista de todos los
				print("		Apariciones >",Total,"\n")									#	personajes y si lo encuentra
				Pausa()																	#	imprime el total de las apariciones
																						
			elif opcion==3:						################################
				clear(1)						#	Personajes por categoría   #
				Cat=Categorias(Diccionario)		################################
				for categoria in Cat:
					print("			",categoria)	#	Imprime la lista de categorías y pide una por teclado
				Busqueda=LimpiarCadena(input('''
			 Introduce una categoria
		  	 > '''))
				for linea in PersonajesPorCategoria(Diccionario,Busqueda):		# Imprime los personajes con esa
						print(linea)											# categoría
				Pausa()
				del Cat
			
			elif opcion==4:							##############################
				clear(1)							#	Menú de eventos marvel   #
				Events=ListaEventos(Diccionario)	##############################
				for evento in Events:
					print("		",evento)			#	Lista los eventos y pide uno por teclado
				Busqueda=LimpiarCadena(input('''
			 Introduce un evento
		  	 > '''))
				Participantes=PersonajesPorEvento(Diccionario,Busqueda)
				for participante in Participantes:		#	Lista los personajes que aparecen en ese evento
					print("		",participante)
				Pausa()

			elif opcion==5:								#	Personaje, conocidos y enemigos
				Lista=ListaPersonajes(Diccionario)		#######################################
				for Personaje in Lista:					
					print("			",Personaje)	#	Lista los personajes y pide uno por teclado
				Busqueda=LimpiarCadena(input('''			Introduce un personaje
		  	> '''))
				Personaje=BuscarPersonaje(Busqueda,ListaPersonajes(Diccionario))	#	Busca el personaje
				
				try:
					clear(0)
					print("	",Personaje,">>",Heroe_Villano(Personaje,Diccionario),"\n\n")	#	Coloca la etiqueta
					ConocidosYEventos=EventosP(Personaje,Diccionario)						#	Heroe/Villano/Reformado
					for evento in ConocidosYEventos:			#	Recorre la lista de Conocidos y eventos y la imprime
						
						print("\n	En el evento '"+evento[0]+"' coincidió con",len(evento[1]),"personajes:")
						for personajes in evento[1]:
							print("	-",personajes,">>",Heroe_Villano(personajes,Diccionario))
					
					if Miniaturas:		#	Si al principio del programa aceptaste las miniaturas o ya tenías el paquete
										#	ejecuta el comando feh para abrir una ventana con una imagen del personaje
						print("\n\n			Cargando imagen...")
						system('feh -Za 125 --title "{}" {} &'.format(Personaje,Miniatura(Personaje,Diccionario)))
					Pausa()
				except:
					clear(10)
					input('	      Personaje inválido. Pulsa "enter para continuar..."')