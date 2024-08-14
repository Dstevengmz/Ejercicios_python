class Empleado:

    def __init__(self):
        self.empleados=[]

    def Crear_Empleado(self,nombre,identificacion,cargo,nhtrabajadas,SalarioMensual,tarifahora):
        
        nuevo_empleado={"Nombre":nombre,"identificacion":identificacion,"cargo":cargo,"nhtrabajadas":nhtrabajadas,"TarifaHora":tarifahora,"SalarioMensual":SalarioMensual}
        self.empleados.append(nuevo_empleado)
        print("Empleado creado exitosamente con sus datos...")
        print("Los datos son : ")
        print(f"EL nombre del empleado es :{nombre}")
        print(f"EL identificacion es :{identificacion}")
        print(f"EL Cargo es :{cargo}")
        print(f"EL Horas trabajas son : {nhtrabajadas}")
        print(f"EL Tarifa por hora es :  {tarifahora}")
        print(f"EL Salario Mensual es :  {SalarioMensual}")
    
    def menu(self):
        while True:
            print("Ingrese 1 para crear empleado y calcular : ")
            print("Ingrese 2 para salir...")
            opcion=int(input("Ingres su opcion : "))
            if opcion==1:
                nombre=str(input("Ingres el nombre : "))
                identificacion=int(input("Ingrese su identificacion : "))
                cargo=str(input("Ingrese su cargo : "))
                nhtrabajadas=int(input("Ingrese el numero de horas trabajas en el mes: "))
                tarifahora=float(input("Ingrese el valor de tarifa por hora : "))
                SalarioMensual=nhtrabajadas*tarifahora
                self.Crear_Empleado(nombre,identificacion,cargo,nhtrabajadas,SalarioMensual,tarifahora)
            elif opcion==2:
                print("Exit")
                break
            else:
                print("La opcion ingresada es invalida.")


e=Empleado()
e.menu()