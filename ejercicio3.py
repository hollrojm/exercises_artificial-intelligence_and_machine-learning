# Calcular el area de un rectangulo

def calcular_area_rectangulo(base, altura):
    return base * altura

base = float(input('Intriduce la base del rectangulo: '))
altura  = float(input('Intriduce la altura del rectangulo: '))

print(f'El area del rectangulo segun su {base} y su {altura} es {calcular_area_rectangulo(base , altura)}')

