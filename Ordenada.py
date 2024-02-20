def ordenar_fila(matriz, fila):
    # Verificamos si la fila está dentro de los límites de la matriz
    if fila < 0 or fila >= len(matriz):
        print("La fila especificada está fuera de los límites de la matriz.")
        return

    # Aplicamos el algoritmo de ordenación de selección a la fila especificada
    for i in range(len(matriz[fila])):
        min_index = i
        for j in range(i+1, len(matriz[fila])):
            if matriz[fila][j] < matriz[fila][min_index]:
                min_index = j
        # Intercambiamos los elementos
        matriz[fila][i], matriz[fila][min_index] = matriz[fila][min_index], matriz[fila][i]

# Ejemplo de uso
matriz = [
    [9, 3, 5],
    [2, 8, 1],
    [7, 4, 6]
]
fila_a_ordenar = 1  # Se ordenará la segunda fila (índice 1)
ordenar_fila(matriz, fila_a_ordenar)

# Imprimimos la matriz después de ordenar la fila especificada
for fila in matriz:
    print(fila)