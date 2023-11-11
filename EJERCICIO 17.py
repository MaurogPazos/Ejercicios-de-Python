'''
a) Definir una función que permita el ingreso de números por 
teclado hasta ingresar el 0, y retorne esa lista. 
'''
#Zona de funciones.
def ingresoNumeros():
    lista=[]
    print('La carga de números finaliza al ingresar 0.')
    numero=int(input('Digite un número para ingresar a la lista(entero): '))
    while numero!=0:
        lista.append(numero)
        numero=int(input('Digite un número para ingresar a la lista(entero): '))
    return lista
'''
b) Definir una función que reciba como parámetro 
una lista de números y retorne como resultado el promedio.
'''
def promedioNumeros(lista):
    suma=0 #acumulador
    cantidad=len(lista)
    for numero in lista:
        suma=suma+numero
        promedio=suma/cantidad
    return promedio
'''
c) Definir una función que reciba como parámetro una lista
de números y retorne como resultado la suma de los números.
'''
def sumaNumeros(lista):
    suma=0 #acumulador
    for numero in lista:
        suma=suma+numero
    return suma
'''
d) Definir una función que reciba como parámetro una lista de números
y retorne el número más grande de la lista (máximo).
'''
def numeroMax(lista):
    maximo=lista[0]
    for numero in lista:
        if numero>maximo:
            maximo=numero
    return maximo
'''
e) Definir una función que reciba como parámetro una lista de números y 
retorne el número más pequeño de la lista (mínimo). 
'''
def numeroMin(lista):
    minimo=lista[0]
    for numero in lista:
        if numero<minimo:
            minimo=numero
    return minimo
'''
f) Definir una función denominada porcentaje, que tenga 2 parámetros formales, que representan el total y 
un valor y retorna el porcentaje de ese valor respecto del total. 
'''
def porcentaje(valor,total):
    respectoTotal=(valor*100)/total
    return respectoTotal
'''
Zona principal del Programa
'''
listaNumeros=ingresoNumeros()

print('1. Ver el promedio de los números ')
print('2. Ver la suma de los números ')
print('3. Ver el número máximo ')
print('4. Ver el número mínimo')
print('5. Calcular porcentaje ')
print('6. Salir ')
seleccionOpcion=(input('Seleccione una opción del menú: '))
while seleccionOpcion!='6':
    if seleccionOpcion=='1':
        prom= promedioNumeros(listaNumeros)
        print(prom)
    elif seleccionOpcion=='2':
        resultadoSuma= sumaNumeros(listaNumeros)
        print(resultadoSuma)
    elif seleccionOpcion=='3':
        numax= numeroMax(listaNumeros)
        print(numax)
    elif seleccionOpcion=='4':
        numin= numeroMin(listaNumeros)
        print(numin)
    elif seleccionOpcion=='5':
        totali=float(input('Ingrese un número: '))
        valori=float(input('Ingrese otro número: '))
        porcen= porcentaje(valori,totali)
        print(porcen)
    else:
        print('La opción es incorrecta.')
    seleccionOpcion=(input('Seleccione una opción del menú: '))

