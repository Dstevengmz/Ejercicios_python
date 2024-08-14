def calcular():
    num=10
    array=[]
    for i in range(num):
        valores=int(input(f"Ingrese el valor {i+1} : "))
        array.append(valores)
        ds=calcular_mayor(array)
    print("El numero mayor es : ",ds) 


def calcular_mayor(array):
    mayor=array[0]
    for i in array:
        if i>mayor:
            mayor=i
    return mayor
        
calcular()
    
    
#Otra forma de hacerlo:

# def calcular():   
#     numero=10
#     almacenar=[]
#     for i in range(numero):
#         xd=int(input("Ingrese los numeros : "))
#         almacenar.append(xd)
#         resultado=Num_mayor(almacenar)   
#     print("El numero mayor es : ",resultado) 
#     print("El arreglo tiene los numeros : ",almacenar)

# def Num_mayor(array):
#     mayor=max(array)
#     return mayor
    
# calcular()