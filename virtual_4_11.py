
def cargar_datos():
    lista=[]
    num=int(input("ingrese un numero, finalizar operacion con el numero 0: "))
    while num != 0:
        lista.append(num)
        num=int(input("ingrese un numero, finalizar operacion con el numero 0: "))
    return lista

def promedio(x):
    suma=0
    cont=0
    for n in x:
        suma=suma + n
        cont=cont + 1
    return suma / cont

def suma(x):
    suma=0
    for n in x:
        suma=suma + n
    return suma

def maximo(x):
    max= -9999
    for n in x:
        if max < n:
            max= n
    return max

def minimo(x):
    min= 9999
    for n in x:
        if min > n:
            min = n
    return min

def porcentaje(total,valor):
    
    return valor*100/total

nums=cargar_datos()

print("-"*119)
print("menu de opciones")
print("-"*119)
print("1. Ver el promedio de los numeros")
print("2. Ver la suma de los numeros")
print("3. Ver la cantidad de numeros")
print("4. Ver el numero maximo")
print("5. Ver el numero minimo")
print("6. Calcular porcentaje")
print("7. Salir")
print("")
opcion=int(input("Ingrese una opcion de 1 al 7: "))
print("")
while opcion != 7:
    if opcion == 1:
        print("el promedido es: " + str(promedio(nums)))
    elif opcion == 2:
        print("la suma de los numeros es de: " + str(suma(nums)))
    elif opcion == 3:
        print("esta es la cantidad de numeros: " + str(len(nums)))
    elif opcion == 4:
        print("El numero maximo es: " + str(maximo(nums)))
    elif opcion == 5:
        print("el minimo es: " + str(minimo(nums)))
    elif opcion == 6:
        a=int(input("ingrese un total: "))
        b=int(input("ingrese un valor: "))
        print(porcentaje(a,b))
    else:
        print("opcion incorrecta")
    print("")
    print("-"*80)
    print("menu de opciones")
    print("-"*80)
    print("1. Ver el promedio de los numeros")
    print("2. Ver la suma de los numeros")
    print("3. Ver la cantidad de numeros")
    print("4. Ver el numero maximo")
    print("5. Ver el numero minimo")
    print("6. Calcular porcentaje")
    print("7. Salir")
    opcion=int(input("Ingrese una opcion de 1 al 7: "))
print("adios")