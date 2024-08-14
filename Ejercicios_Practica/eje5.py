def inicio():
    persona=4
    nombres=[]
    edades=[]
    generos=[]
    for i in range(persona):
        while True:
            try:
                nombre=str(input(f"Ingrese el nombre de la persona {i+1} : ")).lower()
                nombres.append(nombre)
                break
            except:
                print("Ingres un nombre valido.")
        while True:
            try:
                edad=int(input(f"Ingrese la edad de la persona {i+1} : "))
                edades.append(edad)
                break
            except:
                print("Ingrese una edad valida.")
        while True:
            try:
                genero=str(input(f"Ingrese genero de la persona {i+1} 'Masculino/Femenino' : ")).capitalize()
                if genero=="Masculino" or genero=="Femenino":
                    generos.append(genero)
                    break
                
                else:
                    print("Ingrese un genero valido ")
            except:
                print("Ingrese un genero valido.")
                
    #Mayor de edad
    mayor_edad(edades,nombres,generos)
    #Mayor de edad 
    # personas edad mayores a 20 años
    mayoresa20=personas_mayores_a_20_años(edades)
    imprimir_edad_mayores_a_20_años(mayoresa20)
    # personas edad mayores a 20 años
    #suma edades
    suma=suma_edades(edades,generos)
    imprimir_suma_edades(suma)
    #suma edades
    imprimir(persona,i,nombres,edades,generos)
         
def imprimir(personas,i,nombres,edades,generos):
    print("Resultados...\n")
    print("Nombre".ljust(15),"Edad".ljust(10),"Genero".ljust(15))
    for i in range(personas):
        ds=print(nombres[i].ljust(15),str (edades[i]).ljust(10),generos[i].ljust(15))
    return ds

def suma_edades(edades,generos):
    contador=0
    for i in range(len(generos)):
        if generos[i]=="Femenino":
            contador=contador+edades[i]
    return contador
    
def imprimir_suma_edades(suma):
    return print("La suma de edades de genero femenino es : \n",suma)
    
def personas_mayores_a_20_años(edades):
    contador=0
    for i in range(len(edades)):
        if(edades[i]>20):
            contador=contador+1
    return contador

def imprimir_edad_mayores_a_20_años(mayoresa20):
    return print("Las personas mayores a 20 años son : ",mayoresa20)
    
def mayor_edad(edades,nombres,generos):
    alguna_mayor=False
    print("\nLas personas mayores de edad son : ")
    print("Nombre".ljust(15),"edad".ljust(10),"Genero".ljust(15))
    for i in range(len(edades)):
            if edades[i]>=18:
                alguna_mayor=True
                print(nombres[i].ljust(15),str(edades[i]).ljust(10),generos[i].ljust(15))
                
    if not alguna_mayor:
        print("No hay personas mayores de edad : ")
    
    
inicio()