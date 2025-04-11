class Calculadora:
    
    def suma(num1, num2):
        resultado = num1 + num2
        return resultado
    
    def resta(num1, num2):
        resultado = num1 - num2
        return resultado
    
    def multiplicacion(num1, num2):
        resultado = num1 * num2
        return resultado
    
    def division(num1, num2):
        if num2 == 0:
            return "Error: NO se puede divir por cero"
        num1 * num2
        
    def factorial(num):
        if num < 0:
            return "Error: NO se puede calcular el factorial de un numero negativo"
        
        elif num == 0 or num == 1:
            return 1
        
        else: 
            resultado = 1
            
            for i in range(2, int(num) +1):
                resultado *= i
            
            return resultado
        
    while True:
        print("\n===== OPERCAIONES BASICAS =====")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Factorial")
        print("6. Salir")
        
        opcion = input("\nSeleccione una operacion (1-6): ")
        
        if opcion == '6':
            print ("Gracias por utilizar el programa")
            break
        
        if opcion in ('1', '2','3', '4'):
            num1 = float(input('Ingrese el primer numero: '))
            num2 = float(input('Ingrese el segundo numero: '))
            
            if opcion == '1':
                resultado = suma(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = resta(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcion == '4':
                resultado = division(num1, num2)
                print(f"Resultado: {num1} / {num2} = {resultado}")
        elif opcion == '5':
            numfac= float(input('Ingrese numero para calcular factorial: '))
            print(f"Resultado: El factorial de {numfac} es {factorial(numfac)}")
        else:
            print("Opción no válida")
    