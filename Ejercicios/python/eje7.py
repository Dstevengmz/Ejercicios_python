contador=0
n=int(input("Ingrese el numero de valores, 'N' : "))
for i in range(n):
    num=int(input("Ingrese el numero : "))
    contador=contador+num
print("La suma es : ",contador)