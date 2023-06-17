import mysql.connector
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Establecer conexión con la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cancer_mama"
)

# Crear tabla de pacientes
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        edad INT,
        sintomas VARCHAR(255)
    )
''')

# Crear tabla de resultados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS resultados (
        id INT AUTO_INCREMENT PRIMARY KEY,
        paciente_id INT,
        resultado VARCHAR(255),
        FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
    )
''')

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

# Función para agregar un nuevo paciente a la base de datos
def agregar_paciente(nombre, edad, sintomas):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="cancer_mama"
    )
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pacientes (nombre, edad, sintomas) VALUES (%s, %s, %s)
    ''', (nombre, edad, sintomas))
    conn.commit()
    cursor.close()
    conn.close()

# Función para obtener todos los pacientes de la base de datos
def obtener_pacientes():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="cancer_mama"
    )
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM pacientes
    ''')
    pacientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return pacientes

# Función para agregar un resultado al paciente en la base de datos
def agregar_resultado(paciente_id, resultado):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="cancer_mama"
    )
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO resultados (paciente_id, resultado) VALUES (%s, %s)
    ''', (paciente_id, resultado))
    conn.commit()
    cursor.close()
    conn.close()




# Obtener los datos de entrenamiento
datos_entrenamiento = [
    [30, "Si","Si", "Maligno"],
    [32, "No","No", "Benigno"],
    [35, "No","No", "Benigno"],
    [40, "Si","Si", "Maligno"],
    # Agrega más datos de entrenamiento aquí
]

# Dividir los datos en características (X) y etiquetas (y)
X = [[dato[0], dato[1] ,dato[2]] for dato in datos_entrenamiento]
y = [dato[3] for dato in datos_entrenamiento]

# Realizar codificación one-hot de las características categóricas
enc = OneHotEncoder()
X_encoded = enc.fit_transform(X).toarray()

# Crear el clasificador de árbol de decisiones
clasificador = DecisionTreeClassifier()

# Entrenar el clasificador
clasificador.fit(X_encoded, y)

def predecir_resultado(edad, bulto,hinchazon):
    paciente = [[edad, bulto,hinchazon]]
    paciente_encoded = enc.transform(paciente).toarray()
    resultado = clasificador.predict(paciente_encoded)[0]
    return resultado

def hacer_preguntas():
    respuestas = []
    preguntas = [
        "Cual es tu edad?",
        "Tienes algun bulto en el pecho?",
        "Aumento del grosor o hinchazon de una parte de la mama?"
        # Agrega más preguntas aquí
    ]

    for pregunta in preguntas:
        respuesta = input(pregunta + " ")
        respuestas.append(respuesta)

    return respuestas

# Obtener las respuestas del usuario
respuestas_usuario = hacer_preguntas()

# Obtener la edad y la presencia/ausencia de bulto del usuario
edad_paciente = int(respuestas_usuario[0])
bulto_presente = respuestas_usuario[1]
hinchazon_paciente = respuestas_usuario[2]



# Verificar si el paciente está en los datos de entrenamiento
paciente_presente = False
for dato in datos_entrenamiento:
    if dato[0] == edad_paciente and dato[1] == bulto_presente and dato[2] == hinchazon_paciente:
        paciente_presente = True
        break

# Agregar el paciente a los datos de entrenamiento si no está presente
if not paciente_presente:
    datos_entrenamiento.append([edad_paciente, bulto_presente,hinchazon_paciente, "Desconocido"])
    X = [[dato[0], dato[1] , dato [2]] for dato in datos_entrenamiento]
    y = [dato[3] for dato in datos_entrenamiento]
    X_encoded = enc.fit_transform(X).toarray()
    clasificador.fit(X_encoded, y)

# Realizar la predicción del resultado
resultado_prediccion = predecir_resultado(edad_paciente, bulto_presente, hinchazon_paciente)

# Mostrar el resultado de la predicción
if resultado_prediccion == "Maligno":
    print("Tienes un posible caso de cancer de mama. Se recomienda consultar a un medico.")
else:
    print("No presentas indicios de cancer de mama. Sin embargo, es importante realizar examenes regulares.")

