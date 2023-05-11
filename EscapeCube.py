import sys
import os
import time

class jugador:
    def __init__(self):
        self.nombre = ''
        self.sentimiento = ''
        self.signo_astrologico = ''
        self.posicion = 'suelo'
        self.ganar = False																																											
        self.resueltos = 0
jugador1 = jugador()


"""
Estas dentro de un cubo, y tienes que resolver cada parte de este para poder escapar, puedes moverte dentro de el.


Puedes viajar a una pared adyacente, pero no al otro lado. 
El juego te dirá que hay una brecha en el espacio, resolver paredes cambiará este sistema.

"""

#Variables constantes
DESCRIPCION = 'descripcion'
INFO = 'info'
PUZZLE = 'puzzle'
RESUELTO = False
LADO_ARRIBA = 'subir', 'avanzar'
LADO_ABAJO = 'bajar', 'atras'
LADO_IZQUIERDO = 'izquierda',
LADO_DERECHO = 'derecha',

room_solved = {'arriba': False, 'norte': False, 'suelo': False, 'este': False, 'oeste': False, 'sur': False,}


cubo = {
	'arriba': {
		DESCRIPCION: "Sientes una briza extraña, te das cuenta que estas caminando sobre las nubes.",
		INFO: "Mas extraño que eso es que... los pajaros te estan hablando \n  " ,
		PUZZLE: "Un pajaro intimidante se acerca y te dice lo siguiente: \n Veo sin ojos, vuelo sin alas, me muevo sin piernas, \n conjuro mas amor que cualquier amante y mas miedo que cualquier monstruo \n Soy astuto, despiadado y la mayoria de veces grande, los niños me adoran \n alfinal yo gobierno todo \n ¿Quien soy?",
		RESUELTO: "imaginacion",
		LADO_ARRIBA: 'norte',
		LADO_ABAJO: 'sur',
		LADO_IZQUIERDO: 'este',
		LADO_DERECHO: 'oeste',
	},
	'norte': {
		DESCRIPCION: "Te encuentras en una zona muy helada \n ves un iglu a la lejania, te acercas",
		INFO: "Te acabas de encontrar un yeti alfrente de ti " ,
		PUZZLE: "El yeti te pregunta... ¿Que muerdes sin dientes?", 
		RESUELTO: "hielo",
		LADO_ARRIBA: 'arriba',
		LADO_ABAJO: 'suelo',
		LADO_IZQUIERDO: 'oeste',
		LADO_DERECHO: 'este',
	},
	'suelo': {
		DESCRIPCION: "Te encuentras en un campo de flores bastante bonito.\n Aunque algo se siente raro, como si este fuera el centro del mundo.",
		INFO: "Una llave bastante grande y dorada, pero que aun asi puede pasar desapercibida\nse encuentra en medio del campo de flores.\nQue extrano.",
		PUZZLE: "La llave se encuentra dentro de la cerradura \npero esta oscurecido. \n  Parece que no gira.",
		RESUELTO: False, # Funcionara la llave despues de solucionar lo demas del rompecabezas?
		LADO_ARRIBA: 'norte',
		LADO_ABAJO: 'sur',
		LADO_IZQUIERDO: 'oeste',
		LADO_DERECHO: 'este',
	},
	'este': {
		DESCRIPCION: "Te encuentras en una cueva enorme y muy oscura \nse escucha ruido.",
		INFO: "Ves una silueta de persona tambien, \ntrae binoculares de vision nocturna.",
		PUZZLE: "La persona te ve y te pregunta,\n'¿Cuál es de los animales aquel que en su nombre tiene las cinco vocales?",
		RESUELTO: "murcielago",
		LADO_ARRIBA: 'norte',
		LADO_ABAJO: 'sur',
		LADO_IZQUIERDO: 'suelo',
		LADO_DERECHO: 'arriba',
	},
	'oeste': {
		DESCRIPCION: 'Te encuentras en una tipo de playa, estas confundid@.',
		INFO: 'Un hombre esta escondido entre la arena, te acercas .',
		PUZZLE: "El hombre te pregunta,\nLleva años en el mar y aún no sabe nadar.",
		RESUELTO: "arena",
		LADO_ARRIBA: 'norte',
		LADO_ABAJO: 'sur',
		LADO_IZQUIERDO: 'arriba',
		LADO_DERECHO: 'suelo',
	},
	'sur': {
		DESCRIPCION: "Te encuentras junto a un estanque tranquilo.\nUn anciano mira fijamente una mesa cercana.",
		INFO: "Saludas al anciano.\nÉl te hace señas para que mires la intrincada mesa de doce lados.",
		PUZZLE: "Cada lado de la mesa tiene un símbolo único,\n aunque todos te resultan familiares.\n ¿Con qué símbolo te sientas??",
		RESUELTO: "",#Tu signo zodiacal
		LADO_ARRIBA: 'suelo',
		LADO_ABAJO: 'arriba',
		LADO_IZQUIERDO: 'oeste',
		LADO_DERECHO: 'este',
	}

}


def opciones_menu():
	
	opcion = input("> ")
	if opcion.lower() == ("jugar"):
		comienzo_juego()
	elif opcion.lower() == ("salir"):
		sys.exit()
	elif opcion.lower() == ("ayuda"):
		ayuda_menu()		
	while opcion.lower() not in ['jugar', 'ayuda', 'salir']:
		print("Error en el comando, intenta de nuevo.")
		opcion = input("> ")
		if opcion.lower() == ("jugar"):
			comienzo_juego()
		elif opcion.lower() == ("salir"):
			sys.exit()
		elif opcion.lower() == ("ayuda"):
			ayuda_menu()

def titulo_de_pantalla():
	
	
	os.system('clear')
	
	print('#' * 45)
	print('#   Bienvenido a este juego de adivinanzas  #')
	print("#               Proyecto final              #")
	print('#' * 45)
	print("                 .: Jugar :.                  ")
	print("                 .: Ayuda :.                  ")
	print("                 .: Salir :.                  ")
	opciones_menu()



def ayuda_menu():
	print("")
	print('#' * 45)
	print("~" * 45)
	print("Escribe un comando como 'moverme' y luego 'izquierda'")
	print("para navegar el mapa de este cubo de adivinanzas.\n")
	print("Entradas como 'mirar' o 'examinar' te permitirán")
	print("interactuar con el rompecabezas del cubo.\n")
	print("Este rompecabezas necesitara muchos comandos y")
	print("posibles respuestas de tu conocimiento fuera del juego.\n")
	print("Asegurate de escribir en minusculas.\n")
	print('#' * 45)
	print("\n")
	print('#' * 45)
	print(" Porfavor selecciona una opcion para continuar ")
	print('#' * 45)
	print("                 .: Jugar :.                  ")
	print("                 .: Ayuda :.                  ")
	print("                 .: Salir :.                  ")
	opciones_menu()



salir_del_juego = 'salir'

def imprimir_posicion():
	
	print('\n' + ('#' * (4 +len(jugador1.posicion))))
	print('# ' + jugador1.posicion.upper() + ' #')
	print('#' * (4 +len(jugador1.posicion)))
	print('\n' + (cubo[jugador1.posicion][DESCRIPCION]))

def importante():
	if jugador1.resueltos == 5:
		print("Algo en el mundo parece haber cambiado...")
	print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Que te gustaria hacer?")
	acciones = input("> ")
	acciones_aceptadas = ['moverme', 'caminar', 'andar', 'salir', 'inspeccionar', 'examinar', 'mirar', 'buscar']

	while acciones.lower() not in acciones_aceptadas:
		print("Accion desconocida, porfavor intenta de nuevo.\n")
		acciones = input("> ")
	if acciones.lower() == salir_del_juego:
		sys.exit()
	elif acciones.lower() in ['moverme', 'caminar', 'andar']:
		movimiento(acciones.lower())
	elif acciones.lower() in ['inspeccionar', 'examinar', 'mirar', 'buscar']:
		examinar()

def movimiento(misAcciones):
	preguntas = "A donde te gustaria "+misAcciones+" ?\n> "
	destino = input(preguntas)
	if destino == 'subir':
		mov_destino = cubo[jugador1.posicion][LADO_ARRIBA] 
		movimiento_jugador(mov_destino)
	elif destino == 'izquierda':
		mov_destino = cubo[jugador1.posicion][LADO_IZQUIERDO]
		movimiento_jugador(mov_destino)
	elif destino == 'derecha':
		mov_destino = cubo[jugador1.posicion][LADO_DERECHO]
		movimiento_jugador(mov_destino)
	elif destino == 'bajar':
		mov_destino = cubo[jugador1.posicion][LADO_ABAJO]
		movimiento_jugador(mov_destino)
	else:
		print("Comando invalido, intenta mejor usar estos comandos:\n arriba, bajar, izquierda, derecha .\n")
		movimiento(misAcciones)

def movimiento_jugador(mov_destino):
	print("\nTe acabas de mover hacia " + mov_destino + ".")
	jugador1.posicion = mov_destino
	imprimir_posicion()

def examinar():
	if room_solved[jugador1.posicion] == False:
		print('\n' + (cubo[jugador1.posicion][INFO]))
		print((cubo[jugador1.posicion][PUZZLE]))
		puzzle_respuesta = input("> ")
		checkpuzzle(puzzle_respuesta)
	else:
		print("No hay que ver aqui.")

def checkpuzzle(puzzle_respuesta):
	if jugador1.posicion == 'suelo':
		if jugador1.resueltos >= 5:
			endspeech = ("Sin hacer nada la llave giro.\nComenzo a llover.\nTodas las partes del cubo empezaron a romperse.\nLa luz comienza asomarse por los lados.\n has escapado!")
			for personaje in endspeech:
				sys.stdout.write(personaje)
				sys.stdout.flush()
				time.sleep(0.05)
			print("\nDELICIDADES!")
			sys.exit()
		else:
			print("Nada parece suceder...")
	elif jugador1.posicion == 'sur':
		if puzzle_respuesta == (jugador1.signo_astrologico):
			room_solved[jugador1.posicion] = True
			jugador1.resueltos += 1
			print("Has resolvido el rompecabezas, felicidades!")
			print("\nRompecabezas resueltos: " + str(jugador1.resueltos))
		else:
			print("Respuesta incorrecta, intenta de nuevo.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			examinar()
	else:
		if puzzle_respuesta == (cubo[jugador1.posicion][RESUELTO]):
			room_solved[jugador1.posicion] = True
			jugador1.resueltos += 1
			print("Has resolvido el rompecabezas, felicidades!")
			print("\nRompecabezas resueltos: " + str(jugador1.resueltos))
		else:
			print("Respuesta incorrecta, intenta de nuevo.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			examinar()

def main_game_loop():
	total_rompecabezas = 6
	while jugador1.ganar is False:
		
		importante()



def comienzo_juego():
	
	os.system('clear')

	
	pregunta1 = "Hola persona, cual es tu nombre?\n"
	for personaje in pregunta1:
		
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)
	nombre_jugador = input("> ")
	jugador1.nombre = nombre_jugador

	
	pregunta2 = "Mi querid@ amig@ " + jugador1.nombre + ", como te sientes?\n"
	for personaje in pregunta2:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)
	sentimiento = input("> ")
	jugador1.sentimiento = sentimiento.lower()

	#Adjetivos de sentimientos
	bien_adj = ['feliz', 'alegre', 'emocionado','emocionada', 'enamorado', 'optimizta', 'bien']
	hmm_adj = ['nose', '2-3', 'masomenos','vacio','neutro', 'meh']
	mal_adj = ['mal','triste','enojado','estresado','impulsivo', 'enojada', 'estresada']


	if jugador1.sentimiento in bien_adj:
		feeling_string = "Me alegra que te sientas"
	elif jugador1.sentimiento in hmm_adj:
		feeling_string = "Esta raro que te sientas asi"
	elif jugador1.sentimiento in mal_adj:
		feeling_string = "Disculpa, no sabia que te sentias asi"
	else:
		feeling_string = "No se como es esa emocion"

	#Combina lo de arriba
	question3 = "Bueno, " + jugador1.nombre + ", " + feeling_string + " " + jugador1.sentimiento + ".\n"
	for personaje in question3:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)

	#Preguntas
	question4 = "Ahora cuentame, cual es tu signo zodiacal?\n"
	for personaje in question4:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)

	
	print("#####################################################")
	print("# Porfavor escribe bien el nombre de tu signo.")
	print("# ♈ Aries (The Ram)")
	print("# ♉ Tauro (El toro)")
	print("# ♊ Geminis (Los gemelos)")
	print("# ♋ Cancer (El cangrejo)")
	print("# ♌ Leo (El leon)")
	print("# ♍ Virgo (The Virgin)")
	print("# ♎ Libra (La balanza)")
	print("# ♏ Escorpio (El escorpion)")
	print("# ♐ Sagitario (El centauro)")
	print("# ♑ Capricornio (La cabra)")
	print("# ♒ Acuario (The Water Bearer)")
	print("# ♓ Piscis (El pez)")
	print("#####################################################")
	signo_astrologico = input("> ")
	acceptable_signs = ['aries', 'tauro', 'geminis', 'cancer', 'leo', 'virgo', 'libra', 'escorpio', 'sagitario', 'capricornio', 'acuario', 'piscis']
	

	while signo_astrologico.lower() not in acceptable_signs:
		print("Ese no es un signo aceptable, porfavor intente de nuevo.")
		signo_astrologico = input("> ")
	jugador1.signo_astrologico = signo_astrologico.lower()

	
	speech1 = "Ah, " + jugador1.signo_astrologico + ", que interesante... Entonces.\n"
	speech2 = "Creo que es de donde debemos de partir, " + jugador1.nombre + ".\n"
	speech3 = "Que desafortunad@!.\n"  
	speech4 = "no me digas... no sabes donde estas?  Bueno...\n"
	speech5 = "Con suerte escaparas de este cubo, solo tienes que resolver el rompecabezas.\n"
	speech6 = "JA. JA.. JA...\n"
	for personaje in speech1:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)
	for personaje in speech2:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)
	for personaje in speech3:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.1)
	for personaje in speech4:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)
	for personaje in speech5:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.05)
	for personaje in speech6:
		sys.stdout.write(personaje)
		sys.stdout.flush()
		time.sleep(0.2)
	time.sleep(1)

	os.system('clear')
	print("################################")
	print("# Aqui empieza tu aventura... #")
	print("################################\n")
	print("Te encuentras en el centro de un extrano lugar.\nSParece ser que estas atrapado en un misterioso cubo.\n")
	print("Te das cuenta de que cada cara del cubo tiene un tema distinto.\nComo saldras de esto...\n")
	print("Notas que hay objetos parados a lado de las paredes.\nAcaso aqui no hay gravedad? aunque hay nubes...")
	main_game_loop()


titulo_de_pantalla()