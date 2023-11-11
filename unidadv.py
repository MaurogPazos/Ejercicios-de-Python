#simplifica por ejemplo la posibilidad de hacer un programa que devuelva la tabla de un n°x sin tener q hacer toda la tabla

contador=1
while contador<=10:
        print(5*contador)
        contador=contador+1

#como tomar lista de alumnos

lista=[]
contador=1
while contador <=3:
    nombre=input('Nombre ')
    comision=input('Comision ')
    lista.append([nombre,comision])
    contador=contador+1
print(lista)

lista=[]
nombre=input('Nombre ')
while nombre!='zzzz':
    comision=input('Comision ')
    lista.append([nombre,comision])
    nombre=input('Nombre ')
print(lista)
lista=[2,5,9,1,4]
suma=0
contador=1
while contador<=len(lista):
    suma=suma+lista[contador-1]
    contador=contador+1
print(suma)

#mismo que ejercicio anterior pero con utilización de for

lista=[2,5,9,1,4]
suma=0
for n in lista:
    suma=suma+n
print(suma)

