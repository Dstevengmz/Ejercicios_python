num=10
arreglo=[]
pares=[]
impares=[]
contador_pares=0
contador_impares=0
posiciones_pares=0
posiciones_impares=0

for i in range(num):
    valores=int(input(f"Ingrese el {i+1} valor : "))
    arreglo.append(valores)
    if valores%2==0:
        contador_pares=contador_pares+valores
        pares.append(valores)
    else:
        contador_impares=contador_impares+valores
        impares.append(valores)
        
    if i%2==0:
        posiciones_pares=posiciones_pares+valores
    else:
        posiciones_impares=posiciones_impares+valores

if pares:
    promedio_pares=contador_pares/len(pares)
else:
    promedio_pares=0

if impares:
    promedio_impares=contador_impares/len(impares)
else:
    promedio_impares=0

print(f"La suma de los pares es :{contador_pares}, y la suma de los impares es :{contador_impares} ")
print(f"EL promedio de los pares es : {promedio_pares}, y el promedio de los impares es : {promedio_impares}")
print(f"La suma de las posiciones pares son :{posiciones_pares}, y las posciones impares la suma es : {posiciones_impares}")