#Ejercicio 14 unidad v

def cargar_datos():
    equipos=[]
    nombre=input('Ingrese nombre del equipo (La carga finaliza cuando ingresa "zzz"): ')
    while nombre!='zzz':
        puntos=int(input('Ingrese los puntos: '))
        goles=int(input('Ingrese los goles: '))
        posicion=int(input('Ingrese la posición: '))
        equipos.append([nombre,puntos,goles,posicion])
        nombre=input('Ingrese nombre del equipo (La carga finaliza cuando ingresa "zzz"): ')
    return equipos
funcion=cargar_datos()
print(funcion)

def equipo_ultima_posicion (equipos):
    pos=-1
    equi=[]
    for e in equipos:
        if e [3]>pos:
            pos=e[3]
            equi=e
    return equi[2]

golesafavor=equipo_ultima_posicion(funcion)
print('Los goles del equipo de la última posición son: ' + str (golesafavor))

def equipo_primera_posicion (equipos):
    pos=-1
    equi=[]
    for e in equipos:
        if e [3]>pos:
            pos=e[1]
            equi=e
    return equi[0]

equipocampeon=equipo_primera_posicion(funcion)
print('El equipo campeón es: ' + str (equipocampeon))

def nombres_equipos(equipos):
    for x in equipos:
        print(x[0])
listaequipos=nombres_equipos(funcion)
print(listaequipos)

print('1. Goles a favor del último equipo')
print('2. Equipo Campeón')
print('3. Nombres de los equipos')
print('4. Salir')
opcion=int(input('Ingrese un número del 1 al 4: '))
while opcion!=4:
    if opcion==1:
        print(equipo_ultima_posicion(funcion))
    elif opcion==2:
        print(equipo_primera_posicion(funcion))
    elif opcion==3:
        print(nombres_equipos(funcion))
    else:
        print('Opción incorrecta: ')
    opcion=int(input('Ingrese un número del 1 al 4: '))