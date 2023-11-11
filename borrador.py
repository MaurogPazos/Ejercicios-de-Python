
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
    numeropi=float(3.141592)
    
    
areacirc=area_del_circulo()

print('Este es el menú de Área de los objetos: ')
print('1.- Area del Círculo')
print('2.- Area del Cuadrado')
print('3.- Area del Rectángulo')
print('4.- Salir')
seleccione_opcion=int(input('Seleccione una opción del menú: '))
while seleccione_opcion!=4:
    if seleccione_opcion==1:
        radio= print(int(input('Ingrese la medida del radio: ')))
        areacirculo=areacirc*(radio* radio)
        print('El area del círculo es: ' + str (areacirc))
    elif seleccione_opcion==2:
        print(int(input('Ingrese la medida de uno de los lados: ')))
        print(int(input('Ingrese la medida de otro de los lados: ')))
        print('El area del cuadrado es: ' + str (areacua))
    elif seleccione_opcion==3:
        print(int(input('Ingrese la medida de la base: ')))
        print(int(input('Ingrese la medida de la altura: ')))
        print('El area del rectangulo es: ' + str (arearect))
    else :
        print('Opción incorrecta!.')
    seleccione_opcion=int(input('Seleccione una opción del menú: '))
'''
#ejercicio 17 A
def cargar_numeros():
    lista_numeros=[]
    a=int(input('Ingrese los números, para finalizar ingrese el 0: '))
    while a != 0:
        lista_numeros.append(a)
        a=int(input('Ingrese los números, para finalizar ingrese el 0: '))    
    
    return lista_numeros
listarnum=cargar_numeros()
print(listarnum)
'''