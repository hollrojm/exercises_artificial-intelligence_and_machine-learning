class NotasAlumno:
    
    def cal_nota_final(practica, problemas, teoria):
        return(practica *0.1) + (problemas * 0.5) + (teoria * 0.4)
    
    def validar_nota(nota):
        return 0 <= nota <= 10
    
    
    print("******* CÁLCULO DE NOTAS ****** ")
    
    while True:
        
        print("\n1. Calcular nota del Pelado")
        print("2. Salir")
        
        opcion = input("\nSeleccione una opción (1-2): ")
        
        if opcion == '2':
            print ('Hasta la vista Baby')
            break
        
        elif opcion == '1':
            nombre_alumno = input("\nIngrese el nombre del pelado: ")
            try:
                practica = float(input("Ingrese la nota práctica (0-10): "))
                if not validar_nota(practica):
                    print(("Error: La nota debe estar entre 0 y 10."))
                    continue
                problemas = float(input("Ingrese la nota de problemas (0-10): "))
                if not validar_nota(practica):
                    print(("Error: La nota debe estar entre 0 y 10."))
                    continue
                teoria = float(input("Ingrese la nota teórica (0-10): "))
                if not validar_nota(teoria):
                    print("Error: La nota debe estar entre 0 y 10.")
                    continue
            
                nota_final = cal_nota_final(practica, problemas, teoria)
            
            
                print(f"Alumno: {nombre_alumno}")
                print(f"Nota práctica (10%): {practica}")
                print(f"Nota problemas (50%): {problemas}")
                print(f"Nota teórica (40%): {teoria}")
                print(f"NOTA FINAL: {nota_final:.2f}")
            
            except ValueError:
                print('Error debe ingresar valores numericos para las notas')
                
        else:
            print('opcion no valida')