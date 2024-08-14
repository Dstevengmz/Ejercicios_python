def boletostotales():
    menu()  

def menu():
    personas = []
    while True:
        print("Ingrese 1 para comprar:")
        print("Ingrese 2 para salir:")
        x = int(input("Ingrese su opción: "))
        if x == 1:
            personas =comprar(personas)
        elif x == 2:
            imprimir(personas)
            print("Saliendo")
            break  
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")


def comprar(personas):
    ticket=5
    id =int(input("Ingrese su documento de identidad: "))
    personas.append(id)
    boletas=int(input("Ingrese el numero de boletas a comprar : "))
    if boletas<=ticket:
        print("Compra realizada exitosamente...")
        ticket=ticket-boletas
        print("Las boletas que quedan son : ",ticket)
        
def imprimir(array):
    print("Documentos de identidad ingresados:", array)


boletostotales()
