# Ejercicio 1: Crear una lista de números del 1 al 10 y calcular la suma

num = int (input("Introduce el numero final de la lista:  "))
lista = list(range(1, num + 1))
result = sum(lista)

print(f'La suma de la lista hasta {num} es {result}')
