num =None
contador=0
contador1=0
while num!=0:
    num=int(input("Ingrese el numero : "))
    if num!=0:
        if(num%2==0):
            contador+=num
            #print("La suma es : ",contador)
        else:
            contador1+=num
        #print("La suma es  : ",contador1)

    print(f"El numero ingresado es : {num} ")

print("Resultado")
print("Termino por que ingresaste el '0' ")
print(f"El resultado de la suma de numeros pares es : {contador} y la suma de los numeros impares es {contador1}")
