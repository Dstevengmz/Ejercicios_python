class Programa:
    usuarios=[]
    
    def __init__(self,nombre,identificacion):
        self.nombre=nombre
        self.identificacion=identificacion
        Programa.usuarios.append(self)
        
        
    def Crear_Usuario(usuario):
        
        
        
    def Menu(usuario):
        print("...Menu...")
        print("Ingrese 1 para crear usuario")
        print("Ingrese 2 para salir")
        x=int(input("Ingrese su opcion : "))
        if x==1:
            print("Ingrese nombre : ")
            nombre=str(input())
            print("Ingrese la identificacion : ")
            id=int(input())            
    