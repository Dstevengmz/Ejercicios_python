dinero=[]
suma_pal_promedio=0
promedio=0
dias_semana=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
for dia in dias_semana:
    while True:
        try:
            valor=int(input(f"Ingrese el valor del dia {dia} : "))
            dinero.append(valor)
            suma_pal_promedio=suma_pal_promedio+valor
            break
        except:
            print("Debe ingresar valores enteros ")
        
promedio=suma_pal_promedio/len(dias_semana)
    
#print(len(dias_semana))
#print(dinero)
print(suma_pal_promedio)
print(f"Promedio es : {promedio:.2f} ")