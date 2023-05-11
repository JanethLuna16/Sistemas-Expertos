"""
import string

def clean_string(s):
   
   # Esta funcion recibe una cadena de texto y elimina todos los caracteres especiales
   
    return s.translate(str.maketrans('', '', string.punctuation))

def adivinar_personaje(personajes):
  
  #  Esta funcion recibe una lista de diccionarios, cada uno representando un personaje con sus caracteristicas.
   #La funcion hace preguntas al usuario para adivinar en quien esta pensando el usuario.

    while len(personajes) > 1:
        pregunta = input("Haz una pregunta sobre el personaje (ej. Tiene pelo largo?): ")
        pregunta = clean_string(pregunta).lower()
        personajes = [p for p in personajes if isinstance(p[pregunta], bool) and p[pregunta]]
        print("Hay {} personajes que cumplen con esa caracteristica".format(len(personajes)))

    print("El personaje en quien estas pensando es: {}".format(personajes[0]["nombre"]))


personajes = [
    {
        "nombre": "Mario",
        "tiene_bigote": True,
        "usa_gorra": True,
        "es_rojo": True,
        "tiene_arma": False,
        "es_heroe": True,
        "es_villano": False
    },
    {
        "nombre": "Luigi",
        "tiene_bigote": True,
        "usa_gorra": True,
        "es_rojo": False,
        "tiene_arma": False,
        "es_heroe": True,
        "es_villano": False
    },
    {
        "nombre": "Pikachu",
        "tiene_bigote": False,
        "usa_gorra": False,
        "es_rojo": False,
        "tiene_arma": False,
        "es_heroe": True,
        "es_villano": False
    },
    {
        "nombre": "Sonic",
        "tiene_bigote": False,
        "usa_gorra": False,
        "es_rojo": True,
        "tiene_arma": False,
        "es_heroe": True,
        "es_villano": False
    },
    {
        "nombre": "Kirby",
        "tiene_bigote": False,
        "usa_gorra": False,
        "es_rojo": False,
        "tiene_arma": False,
        "es_heroe": True,
        "es_villano": False
    },
    {
        "nombre": "Donkey Kong",
        "tiene_bigote": False,
        "usa_gorra": False,
        "es_rojo": False,
        "tiene_arma": True,
        "es_heroe": True,
        "es_villano": False
    },
    {
        "nombre": "Bowser",
        "tiene_bigote": True,
        "usa_gorra": False,
        "es_rojo": False,
        "tiene_arma": True,
        "es_heroe": False,
        "es_villano": True
    },
    {
        "nombre": "Dr. Eggman",
        "tiene_bigote": True,
        "usa_gorra": True,
        "es_rojo": True,
        "tiene_arma": True,
        "es_heroe": False,
        "es_villano": True
    }
]
import random

def adivinar_personaje(personajes):
    pregunta = input("Haz una pregunta sobre el personaje que estas pensando: ")
    personajes = [p for p in personajes if isinstance(p[pregunta.lower()], bool) and p[pregunta.lower()]]
    if len(personajes) == 1:
        print("El personaje que estas pensando es:", personajes[0]['nombre'])
    elif len(personajes) > 1:
        adivinar_personaje(personajes)
    else:
        print("No conozco ningun personaje que cumpla esas caracteristicas.")
        jugar_nuevamente()

def jugar_nuevamente():
    respuesta = input("Quieres volver a jugar? (S/N): ")
    if respuesta.upper() == "S":
        jugar()
    else:
        print("Gracias por jugar!")

def jugar():
    print("Piensa en un personaje de la siguiente lista:")
    for index, personaje in enumerate(personajes):
        print(f"{index+1}. {personaje['nombre']}")
    adivinar_personaje(personajes)

jugar()
""" 
from turtle import clear
import mysql.connector
import string
# Función para obtener la lista de personajes desde la base de datos
def obtener_personajes():
    # Conectarse a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="adivinaquien"
    )

    # Crear cursor para ejecutar las consultas
    cursor = conn.cursor()

    # Ejecutar consulta para obtener la lista de personajes
    cursor.execute("SELECT * FROM personajes")

    # Obtener resultados y crear lista de personajes
    personajes = []
    for row in cursor.fetchall():
        personaje = {
            "nombre": row[1],
            "tiene_bigote": bool(row[2]),
            "usa_gorra": bool(row[3]),
            "es_rojo": bool(row[4]),
            "tiene_arma": bool(row[5]),
            "es_heroe": bool(row[6]),
            "es_villano": bool(row[7])
        }
        personajes.append(personaje)

    # Cerrar cursor y conexion
    cursor.close()
    conn.close()

    # Devolver lista de personajes
    return personajes

# Funcion para adivinar el personaje
def adivinar_personaje(personajes):
    pregunta = input("Menciona una caracteristica del personaje: ")
    respuesta = input("Es la respuesta afirmativa o negativa? (S/N): ")
    afirmativa = True if respuesta.upper() == "S" else False
    
    personajes = [p for p in personajes if p[pregunta.lower()] == afirmativa]
    
    # Agregar pistas negativas
    if afirmativa:
        pistas_negativas = input("Hay alguna caracteristica que el personaje NO debe tener? (S/N): ")
        while pistas_negativas.upper() == "S":
            pista = input("Que caracteristica NO debe tener el personaje?: ")
            personajes = [p for p in personajes if not p[pista.lower()]]
            pistas_negativas = input("Hay alguna otra caracteristica que el personaje NO debe tener? (S/N): ")
    
    if len(personajes) == 1:
        print("El personaje que estas pensando es:", personajes[0]['nombre'])
    elif len(personajes) > 1:
        adivinar_personaje(personajes)
    else:
        print("No conozco ningun personaje que cumpla esas caracteristicas.")
        jugar_nuevamente()

"""
    pregunta = input("Haz una pregunta sobre el personaje que estas pensando: ")
    personajes = [p for p in personajes if isinstance(p[pregunta.lower()], bool) and p[pregunta.lower()]]
    if len(personajes) == 1:
        print("El personaje que estas pensando es:", personajes[0]['nombre'])
    elif len(personajes) > 1:
        adivinar_personaje(personajes)
    else:
        print("No conozco ningun personaje que cumpla esas caracteristicas.")
        jugar_nuevamente()
 """
def agregar_personaje():
    # Conectarse a la base de datos
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="adivinaquien"
    )
    # Crear cursor para ejecutar las consultas
    cursor = conn.cursor()
    # Pedir al usuario los datos del nuevo personaje
    nombre = input("Ingresa el nombre del nuevo personaje: ")
    tiene_bigote = input("Tiene bigote? (S/N): ").upper() == "S"
    usa_gorra = input("Usa gorra? (S/N): ").upper() == "S"
    es_rojo = input("Es rojo? (S/N): ").upper() == "S"
    tiene_arma = input("Tiene arma? (S/N): ").upper() == "S"
    es_heroe = input("Es heroe? (S/N): ").upper() == "S"
    es_villano = input("Es villano? (S/N): ").upper() == "S"
    sql = "INSERT INTO personajes (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (nombre, tiene_bigote, usa_gorra, es_rojo, tiene_arma, es_heroe, es_villano)
    cursor.execute(sql, values)

    # Guardar los cambios en la base de datos
    conn.commit()

    # Cerrar cursor y conexion
    cursor.close()
    conn.close()
    print("Personaje agregado correctamente.")

# Funcion para mostrar el menu de opciones
def mostrar_menu():
    clear
    print("Seleccione una opcion:")
    print("1. Jugar")
    print("2. Agregar un nuevo personaje")
    print("3. Salir")
# Funcion principal del programa
def main():
    # Mostrar menu de opciones
    mostrar_menu()
    opcion = input()

    # Procesar la opcion seleccionada
    while opcion != "3":
        if opcion == "1":
            jugar()
        elif opcion == "2":
            agregar_personaje()
        else:
            print("Opcion invalida.")

        # Mostrar menu de opciones nuevamente
        mostrar_menu()
        opcion = input()

    print("Gracias por jugar!")

# Funcion para jugar de nuevo
def jugar_nuevamente():
    respuesta = input("Quieres volver a jugar? (S/N): ")
    if respuesta.upper() == "S":
        jugar()
    else:
        print("Gracias por jugar!")

# Funcion principal para iniciar el juego
def jugar():
# Obtener lista de personajes desde la base de datos
    personajes = obtener_personajes()

    print("Piensa en un personaje de la siguiente lista:")
    for index, personaje in enumerate(personajes):
        print(f"{index+1}. {personaje['nombre']}")
    adivinar_personaje(personajes)

    print("Piensa en un personaje de la siguiente lista:")
    for index, personaje in enumerate(personajes):
        print(f"{index+1}. {personaje['nombre']}")
    adivinar_personaje(personajes)
   
main()