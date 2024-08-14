num=5
almacenar_numero=[]
suma=0
promedio=0
for i in range(num):
    x=int(input(f"Ingrese el {i+1} valor por favor : "))
    almacenar_numero.append(x)    
    suma=suma+x
    
promedio=suma/len(almacenar_numero)

if promedio in almacenar_numero:
    print("El promedio esta en el arreglo es : ", int(promedio))
else:
    print("No se encuentra el promedio en el arreglo.")
    

print("los numero que almaceno son : ",almacenar_numero)
print("La suma de los valores en el arreglo es : {} y el promedio es :{} ".format(suma,promedio))