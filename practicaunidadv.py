'''
#ejercicio 15
def area_del_cuadrado():
    lado1=int(input('Ingrese un lado del cuadrado: '))
    lado2=int(input('Ingrese el otro lado del cuadrado: '))
    areacuadrado=lado1*lado2
    return ('El area del cuadrado es: ' + str (areacuadrado))
areacua=area_del_cuadrado()

def area_del_rectangulo():
    base=int(input('Ingrese la medida de la base: '))
    altura=int(input('Ingrese la medida de la altura: '))
    arearectangulo=base*altura
    return ('El area del rectángulo es: '+ str (arearectangulo))
arearect=area_del_rectangulo()

def area_del_circulo():
    radio=int(input('Ingrese la medida del radio: '))
    numeropi= 3.141592
    areacirculo=numeropi*(radio*radio)
    return ('El area del circulo es: '+ str (areacirculo))
areacirc=area_del_circulo()

print('1.- Area del Círculo')
print('2.- Area del Cuadrado')
print('3.- Area del Rectángulo')
print('4.- Salir')
seleccione_opcion=int(input('Seleccione una opción del menú: '))
while seleccione_opcion!=4:
    if seleccione_opcion==1:
        print(area_del_circulo())
    elif seleccione_opcion==2:
        print(area_del_cuadrado())
    elif seleccione_opcion==3:
        print(area_del_rectangulo())
    else :
        print('Opción incorrecta!.')
    seleccione_opcion=int(input('Seleccione una opción del menú: '))

#ejercicio 17 a

def num_lista ():
    listanum=[]
    numeros=int(input('Ingrese números para agregar a la lista: '))
    while numeros!=0:
        listanum.append(numeros)
        numeros=(int(input('Ingrese números para agregar a la lista: ')))
    return listanum
listadenumeros=num_lista()
print(listadenumeros)

#práctica de condicionales
edad=int(input('Ingrese su edad: '))
if edad>=0 and edad<2:
    print('Es un bebé.')
elif edad>=2 and edad<13:
    print('Es un niño')
elif edad>=13 and edad<20:
    print('Es un adolescente')
else:
    print('Es un adulto')
'''
#práctica con While
suma=0
listanumeros=[]
numeros=int(input('Ingrese un número: '))
while numeros!=9999:
    listanumeros.append(numeros)
    suma= suma + numeros
    numeros=int(input('Ingrese un número: '))
print('El promedio de los números es: ' , suma/len(listanumeros))