# Ejercicio 2: Crear una función que devuelva el cuadrado de un número

def numero_al_cuadrado(num):
    return num ** 2

num = int(input("Introduce un numeropara calcular su cuadrado: "))
print(f'El cuadrado de {num} es {numero_al_cuadrado(num)}')