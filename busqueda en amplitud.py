from collections import deque

# Definir el grafo
grafo = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E', 'G'],
    'E': ['B', 'D', 'F', 'H'],
    'F': ['C', 'E', 'I'],
    'G': ['D', 'H', 'J'],
    'H': ['E', 'G', 'I', 'K'],
    'I': ['F', 'H', 'J', 'L'],
    'J': ['G', 'I', 'K', 'M'],
    'K': ['H', 'J', 'L'],
    'L': ['I', 'K', 'M'],
    'M': ['J', 'L']
}

# Definir la función de búsqueda en amplitud
def busqueda_amplitud(grafo, inicio, objetivo):
    # Inicializar la cola con el nodo de inicio
    cola = deque([inicio])
    
    # Inicializar el conjunto de nodos visitados y el diccionario de padres
    visitados = set()
    padres = {inicio: None}
    
    # Iterar hasta que se encuentre el objetivo o se agote la cola
    while cola:
        # Sacar el siguiente nodo de la cola y marcarlo como visitado
        nodo = cola.popleft()
        visitados.add(nodo)
        
        # Si se encontró el objetivo, reconstruir el camino y regresarlo
        if nodo == objetivo:
            camino = [nodo]
            padre = padres[nodo]
            while padre is not None:
                camino.append(padre)
                padre = padres[padre]
            camino.reverse()
            return camino
        
        # Encontrar todos los vecinos no visitados del nodo actual y agregarlos a la cola
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                cola.append(vecino)
                padres[vecino] = nodo
    
    # Si no se encontró el objetivo, regresar None
    return None

# Ejemplo de uso
inicio = 'A'
objetivo = 'M'
camino = busqueda_amplitud(grafo, inicio, objetivo)
print(camino)
