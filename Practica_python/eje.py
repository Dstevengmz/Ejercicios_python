def digitos_iguales(numero):
    # Verificar que el número sea de dos dígitos
    if numero < 10 or numero > 99:
        return False
    
    # Obtener los dígitos del número
    decenas = numero // 10
    unidades = numero % 10
    
    # Comprobar si los dígitos son iguales
    if decenas == unidades:
        return True
    else:
        return False

# Solicitar al usuario ingresar un número entero de dos dígitos
while True:
    try:
        numero = int(input("Ingrese un número entero positivo de dos dígitos: "))
        if numero >= 10 and numero <= 99:
            break
        else:
            print("El número ingresado no es de dos dígitos. Inténtelo nuevamente.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Llamar a la función y mostrar el resultado
if digitos_iguales(numero):
    print(f"Los dos dígitos del número {numero} son iguales.")
else:
    print(f"Los dos dígitos del número {numero} son diferentes.")
