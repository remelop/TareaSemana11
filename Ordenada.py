def ordenar_fila(matriz, fila):
    # Verificamos si la fila está dentro de los límites de la matriz
    if fila < 0 or fila >= len(matriz):
        print("La fila especificada está fuera de los límites de la matriz.")
        return

    # Aplicamos el algoritmo de ordenación de Bubble Sort a la fila especificada
    for i in range(len(matriz[fila])-1):
        for j in range(len(matriz[fila])-1-i):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Matriz original
matriz_original = [
    [9, 3, 5],
    [2, 8, 1],
    [7, 4, 6]
]

# Copiamos la matriz original para no modificarla directamente
matriz_ordenada = [fila.copy() for fila in matriz_original]

# Fila a ordenar
fila_a_ordenar = 1  # Se ordenará la segunda fila (índice 1)

# Ordenamos la fila especificada en la matriz copiada
ordenar_fila(matriz_ordenada, fila_a_ordenar)

# Mostramos la matriz original y la matriz con la fila ordenada
print("Matriz original:")
imprimir_matriz(matriz_original)
print("\nMatriz con la fila ordenada:")
imprimir_matriz(matriz_ordenada)