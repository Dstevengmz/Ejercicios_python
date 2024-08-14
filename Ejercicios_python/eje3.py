votantes=3
votos=0
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
# print("###################################")
# print("Ingrese 1 para cantidado Uno")
# print("Ingrese 2 para cantidado Dos")
# print("Ingrese 3 para cantidado Tres")
# print("Ingrese 4 para Voto en blanco")
# print("###################################")
print("clave ingrese 5 : ")

for i in range(votantes):
    print("###################################")
    print("Ingrese 1 para cantidado Uno")
    print("Ingrese 2 para cantidado Dos")
    print("Ingrese 3 para cantidado Tres")
    print("Ingrese 4 para Voto en blanco")
    print("###################################")
    votos=int(input(f"Ingrese el numero de su candidato, votante {i+1} :"))
    contador5=contador5+1
    while votos<1 or votos>5:
        print("Debes ingresar un numero entre (1 - 5)")
        votos=int(input(f"Ingrese el numero de su candidato, votante {i+1} :"))
    if(votos==1):
        contador1=contador1+1
    elif(votos==2):
        contador2=contador2+1
    elif(votos==3):
        contador3=contador3+1
    elif(votos==4):
        contador4=contador4+1
    else:
            print("Ingrese clave : ")
            clave=str(input("Ingrese la clave : "))
            if clave=="010101":
                 print("Votaciones terminadas.")
                 contador5=contador5-1
                 break
            elif(clave!="010101"):
                      print("Contraseña incorrecta")
                      clave=str(input("Ingrese la clave nuevamente: "))
                      print("Contraseña incorrrecta nuevamente")
                      clave=str(input("Ingrese la clave nuevamente: "))
                      contador5=contador5-1
            print("Imposible terminar sigamos votando")
            votos=int(input(f"Ingrese el numero de su candidato, votante {i+1} :"))
            contador5=contador5+1
                 
                
print(f"El resultado de votantes son : {contador5} , la suma de votantes 1 es : {contador1}, la suma de votantes 2 es : {contador2}, y la suma de votantes 3 es : {contador3}, y la suma de votos en blanco son : {contador4}")
