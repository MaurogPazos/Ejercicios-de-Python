#ejercicio numero 1.
print('Se imprimirá la letra correspondiente a la posición del número ingresado.')
palabra=(input('Ingrese un texto: '))
numero=int(input('Ingrese un número:'))
if numero>0 and numero<len(palabra):
    print(palabra[numero-1])#número menos 1 ya que los strings se cuentan a partir de 0
else:
    print('No se ha podido realizar la tarea.')
#ejercicio numero 2.
tupla=('Mauro','Gabriel','Pazos','Ma','Pa')
def palabras_3(tupla):
    l=[]
    for palabras in tupla:
        if len(palabras)>=3:
            l.append(palabras)
    return l
print(palabras_3(tupla))
#ejercicio numero 3.
#funcion que cargue datos de vinos en una lista, fin de carga 'xxx'
#anio, nombre, tipo, valor.
def cargaDedatos():
    lista=[]
    print('La carga de datos finaliza al introducir(xxx).')
    nombre=(input('Ingrese el nombre del vino: '))
    while nombre!='xxx':
        anio=int(input('Ingrese el año: '))
        tipo=(input('Ingrese el tipo: '))
        valor=float(input('Ingrese el valor: '))
        lista.append([nombre,anio,tipo,valor])
        nombre=(input('Ingrese el nombre del vino: '))
    return lista
#cuantos vinos son mayores al año 2000
def contarMayores2000(lista):
    cont=0 #variable tipo contador
    for v in lista:
        if v[1] >=2000:
            cont=cont+1
    return cont
#cuantos vinos son 'Malbec'
def contarMalbec(lista):
    suma=0 #variable tipo suma
    for m in lista:
        if m[2]=='Malbec':
            suma=suma+m[3]
    return suma
#sacar promedio de los vinos entre 2010 y 2022.
def promedioVinos(lista):
    suma=0
    cont=0
    for v in lista:
        if v[1]>=2010 and v[1]<=2022:
            suma=suma+v[1]
            cont=cont+1
    if cont==0:
        return 0 #quiere decir que si al recorrer la lista no hay vinos con ese criterio
    else:
        return suma/cont
#zona del programa principal
vinos=cargaDedatos()

print('1.Contar vinos mayores al año 2000')
print('2.Contar cantidad de vinos tipo Malbec')
print('3.Promedio de vinos del año 2010-2022')
print('4.Salir')
opcionMenu=(input('Seleccione una opción del menú o 4 para salir: '))
while opcionMenu!='4':
    if opcionMenu=='1':
        print(contarMayores2000(vinos))
    elif opcionMenu=='2':
        print(contarMalbec(vinos))
    elif opcionMenu=='3':
        print(promedioVinos(vinos))
    else:
        print('Opción incorrecta.')
    opcionMenu=(input('Seleccione una opción del menú o 4 para salir: '))
    
 