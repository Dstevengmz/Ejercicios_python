#kilo de huevo
sumacalidad=0
Ngallinas=int (input("Ingrese el numero de gallinas : "))
print(f"Calcular calidad de las {Ngallinas} gallinas")
for i in range(Ngallinas):
    peso =float(input(f"Ingrese el peso de gallina {i+1}: "))
    altura=float(input(f"Ingrese la altura en centimetros {i+1}: "))
    huevos=float(input(f"Ingrese el numero de huevos de la gallina {i+1}: "))

    calidad=(peso*altura)/huevos
    sumacalidad+=calidad

    
    promedio_gallina_calidad=sumacalidad/Ngallinas

    if(promedio_gallina_calidad<=8):
        preciokilo=8*calidad
    elif(promedio_gallina_calidad>8 and promedio_gallina_calidad<15):
        preciokilo=1.00*calidad
    elif(promedio_gallina_calidad>=15):
        preciokilo=1.2*calidad

    print(f"Resultado del kilo de la gallina {i+1} es : ",preciokilo)
