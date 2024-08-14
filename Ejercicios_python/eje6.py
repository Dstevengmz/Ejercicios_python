promedioprimaria=0
promediosegundaria=0
promediotecnico=0
promedioprofesional=0
promedioposgrado=0
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
personasdeundia=int(input("Ingrese el numero de personas que encuesto:"))

for i in range(personasdeundia):
    
    print("Ingrese su nivel de estudio.")
    print("######################################")
    print("Ingrese 1 Para estudios de primaria. ")
    print("Ingrese 2 Para estudios de segundaria.")
    print("Ingrese 3 Para estudios tecnicos.")
    print("Ingrese 4 Para estudios profesionales.")
    print("Ingrese 5 Para estudios de pregrado.")
    print("######################################")
    nivelstudio=int(input("Ingrese su opcion: "))

    if(nivelstudio<0 or nivelstudio>5):
        print("Error no puede ser menor a 0 y no puede ser mayor a 5 el numero a insertar")
    elif nivelstudio==1:
        contador1=contador1+nivelstudio
        print("la suma es : ",contador1)
        promedioprimaria=contador1/personasdeundia
    elif nivelstudio==2 :
        contador2=contador2+1
        promediosegundaria=contador2/personasdeundia
    elif nivelstudio==3 :
        contador3=contador3+1
        promediotecnico=contador3/personasdeundia
    elif nivelstudio==4 :
        contador4=contador4+1
        promedioprofesional=contador4/personasdeundia
    elif nivelstudio==5 :
        contador5=contador5+1
        promedioposgrado=contador5/personasdeundia

print(f"El promedio de nivel primaria es : {promedioprimaria:.2f}, el promedio de nivel de segundaria es :{promediosegundaria:.2f}, el promedio de nivel tecnico es:{promediotecnico:.2f}, el promedio de nivel profesional es : {promedioprofesional:.2f} y el promedio de nivel de posgrado es: {promedioposgrado:.2f} ")
   
