numero=int(input("Ingrese el numero : "))
if numero==0:
    print("El numero binario 0 : ")
else:
    binario=""
    while(numero>0):
        menosunnumero=numero%2
        binario=str(menosunnumero)+binario
        numero=numero//2
    print("El numero binario es : ",binario)