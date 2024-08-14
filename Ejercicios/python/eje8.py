def palabra():
    cadena=str(input("Ingrese  la palabra : "))
    return cadena

def imprimir(cadena):
    print(cadena)

def invertir(palabra):
    invertirr=0
    invertirr=palabra[::-1]
    return invertirr

df=palabra()
d=invertir(df)
imprimir(d)
