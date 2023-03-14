from collections import deque

def bfs_grafo(grafo, inicio, objetivo):
    """
    Realiza una búsqueda en amplitud para encontrar la ruta más corta entre dos nodos en un grafo.

    :param grafo: el grafo representado como un diccionario donde las claves son los nodos y los valores son las listas de nodos adyacentes
    :param inicio: el nodo inicial
    :param objetivo: el nodo objetivo
    :return: una lista que representa la ruta más corta desde el nodo inicial hasta el nodo objetivo, o None si no se encuentra una ruta
    """
    queue = deque()
    queue.append(inicio)

    # Creamos un diccionario para almacenar el nodo anterior de cada nodo en el camino desde el nodo inicial
    parents = {inicio: None}

    # Creamos un diccionario para almacenar la distancia desde el nodo inicial hasta cada nodo visitado
    distance = {inicio: 0}

    while queue:
        current = queue.popleft()

        if current == objetivo:
            path = [objetivo]
            while parents[path[-1]] is not None:
                path.append(parents[path[-1]])
            return path[::-1]

        for vecino in grafo[current]:
            if vecino not in parents:
                parents[vecino] = current
                distance[vecino] = distance[current] + 1
                queue.append(vecino)

    return None

# Ejemplo de uso
grafo = {
    'Calle A': ['Calle B', 'Calle C'],
    'Calle B': ['Calle D', 'Calle E'],
    'Calle C': ['Calle F'],
    'Calle D': [],
    'Calle E': ['Calle F'],
    'Calle F': []
}

inicio = 'Calle B'
objetivo = 'Calle F'
ruta_mas_corta = bfs_grafo(grafo, inicio, objetivo)

if ruta_mas_corta:
    print(f"La ruta más corta desde {inicio} hasta {objetivo} es: {ruta_mas_corta}")
else:
    print(f"No se encontró una ruta desde {inicio} hasta {objetivo}")
