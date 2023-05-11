from ast import Break
import mysql.connector
import random

sospechosos = ["Fernando", "Andrea", "Noe", "Maria", "Alan", "Veronica"]
armas = ["Bate de beisbol", "Cuerda", "Martillo", "Cuchillo", "Tubo de Plomo", "Pistola"]
habitaciones = [
    "Entrada",
    "Sala de estar",
    "Comedor",
    "Cocina",
    "Sala de musica",
    "Biblioteca",
    "Jardin",
    "Salon de juegos",
    "Habitacion de la Andrea",
    "Casa de Noe",
    "Patio",
    "Terraza",
    "wc"
]
hechos = {
    "Fernando": "Cocina",
    "Andrea": "Salon de juegos",
    "Noe": "Patio",
    "Maria": "Terraza",
    "Alan": "Jardin",
    "Veronica": "Entrada"
}
relaciones = {
    "Fernando": "Cuchillo",
    "Andrea": "Tubo de Plomo",
    "Noe": "Martillo",
    "Maria": "Bate de beisbol",
    "Alan": "Cuerda",
    "Veronica": "Pistola"
}

historia = {
    "Fernando": "Fernando es chef y mientras estaba haciendo la cena se escucharon unos gritos demasiodo fuertes, fue a investigar pero ya no habia nadie en la escena del crimen \n. Fue a buscar a sus amigos para informar que uno de ellos habia muerto, pero lo raro es que solo encontro a Noe en la sala de estar",
    "Andrea": "Todos estaban reunidos en la sala de estar, pero faltaban algunas personas... Cuando se escucharon gritos proveniente de la planta de arriba. Se sabe que Andre se estaba banando.\n  En el cadaver estaba Maria llorando desesperadamente al encontrar a su amigo muerto ",
    "Noe": "Janeth estaba jugando con sus perros en el jardin con Alan. Janeth fue por un juguete de su perrito pero ya no regreso. \n Segun las camaras Alan nunca se alejo del lugar en donde estaban pero si recibio una llamada  sospechosa de su amigo ",
    "Maria": "El papa de Andrea es jugador profesional de beisbol. Su papa es novio de Maria. Maria quiere a Andrea como su hija, pero Andrea no quiere a Maria.\n Toda la familia estaba reunida fuera de la casa cuando se escucharon gritos un poco cerca del lugar, cuando llegaron Andrea ya habia muerto",
    "Alan": " Alan, Fernando  y Noe son muy buenos amigos. Ellos invitaron a Janeth a plantar, se escucho que tocaron el timbre porque habia llegado Veronica. \n  Noe fue abrirle y Alan fue por un material que necesitaban, cuando llego Veronica ,Janeth ya habia muerto. Se desconoce donde se encuentra Fernando",
    "Veronica": "Cuando veronica fue a visitar a Alan, Noe , Janeth y Fernando , se dio cuenta que Janeth y Alan ya habian muerto. Se desconoce el paradero de Fernando"
}

def obtener_historia(culpable):
    return historia[culpable]

def obtener_arma(culpable):
    return relaciones[culpable]

def obtener_habitacion(culpable):
    return hechos[culpable]
def jugar():

    # Inicializar variables del juego
    culpable = random.choice(sospechosos)
    #arma = random.choice(armas)
    #habitacion = random.choice(habitaciones)
    pista_culpable = hechos[culpable]
    pista_arma = relaciones[culpable]
    pista_habitacion = historia[culpable]
    habitacion_sospechoso = obtener_habitacion(culpable)
    arma_sospechoso = obtener_arma(culpable)
    historia_sospechoso = obtener_historia(culpable)
    print("Bienvenido al juego de Clue. El objetivo del juego es determinar quien fue el asesino, con que arma y en que habitacion del castillo ocurrio el crimen.")
    print("Tienes 3 oportunidades para adivinar la combinacion correcta. Buena suerte!\n")
    print(historia_sospechoso)
    # Iniciar ciclo de juego
    for intento in range(3):
        print("Intento", intento+1)
       # print(culpable)
       # print(arma_sospechoso)
       # print(habitacion_sospechoso)
        # Pedir al usuario su teoria
        sospechoso = input("\n Quien crees que es el asesino? \n ( Fernando, Andrea, Noe, Maria, Alan, Veronica: ")
        arma_usada = input("\n Que arma crees que se uso? \n Elige entre Bate de beisbol, Cuerda, Martillo, Cuchillo, Tubo de Plomo, Pistola: ")
        lugar = input("\n En que habitacion crees que ocurrio el crimen? \n Elige entre Entrada, Sala de estar, Comedor, Cocina, Sala de musica, Biblioteca, Jardin, Salon de juegos, Habitacion de la Andrea, Casa de Noe, Patio, Terraza, wc): ")

        # Verificar si la teoría es correcta

        if sospechoso == culpable and arma_usada == arma_sospechoso and lugar == habitacion_sospechoso:
            print("Felicidades! Has encontrado al asesino, la arma y la habitacion correcta. Eres un detective excelente!")
            break
        else:
            print("Lo siento, tu teoria es incorrecta. A continuacion te dare una pista para ayudarte en tu siguiente intento.")

            # Dar una pista aleatoria al usuario
            pista_aleatoria = random.randint(1,3)
            if pista_aleatoria == 1:
                print("Pista: El asesino estuvo en la habitacion", pista_culpable)
            elif pista_aleatoria == 2:
                print("Pista: El arma usada pertenece al sospechoso", sospechoso)
            else:
                print("Pista: Esto fue lo que paso segun", sospechoso, ":", pista_habitacion)

    print("Fin del juego. Gracias por jugar.")

jugar()