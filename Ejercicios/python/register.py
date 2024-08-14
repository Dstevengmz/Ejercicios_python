class Registrar:
    def __init__(self):
        self.usuarios=[]

    def Crear_usuario(self,nombre,apellido,usuariox,correo,clave,confirmar_clave):
        for usuario in self.usuarios:
            if usuario['usuariox']==usuariox:
                print(f"EL usuario {usuariox} ya esta creado")
                return False

        nuevo_usuario={"nombre":nombre,"apellido":apellido,"correo":correo,"usuariox":usuariox,"clave":clave,"Confirmar_clave":confirmar_clave}
        self.usuarios.append(nuevo_usuario)
        print("Usuario creado exitosamente...")

    def Login(self,usuariox,clave):
        for usuario in self.usuarios:
            if usuario['usuariox']==usuariox and usuario['clave']==clave:
                print("Bienvenido Login correcto")
                return True
        
        print("Usuario incorrecto...")
        return False
                
    def menu(self):
        while True:
            print("Ingrese 1 para registrar usuario : ")
            print("Ingrese 2 para login : ")
            print("Ingrese 3 para salir : ")
            opcion=int(input("Ingrese su opcion : "))

            if opcion==1:
                print("Registro de usuarios : ")
                nombre=str(input("Ingrese su nombre : "))
                apellido=str(input("Ingrese su apellido : "))
                usuariox=str(input("Ingres su usuario : "))
                correo=str(input("Ingrese su correo : "))
                clave=str(input("Ingres su clave : "))
                confirmar_clave=str(input("Confirmar clave : "))
                self.Crear_usuario(nombre,apellido,usuariox,correo,clave,confirmar_clave)
                
            elif opcion==2:
                print("Ingresar a la plataforma : ")
                usuariox=str(input("Ingrese el usuario : "))
                clave=str(input("Ingrese la clave : "))
                self.Login(usuariox,clave)
            elif opcion==3:
                print("Exit")
                break
            else:
                print("Su opcion no es valida...")


registro=Registrar()
registro.menu()


    

        