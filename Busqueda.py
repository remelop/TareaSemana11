def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j})."
    return f"El valor {valor} no se encontró en la matriz."
# Crear una matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
# Definir el valor a buscar
valor_a_buscar = 7
# Realizar la búsqueda e imprimir el resultado
resultado_busqueda = buscar_valor(matriz, valor_a_buscar)
print(resultado_busqueda)
