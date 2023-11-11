#Ejercicio 1
'''
numero1=int(input('Ingrese un numero: '))
if numero1>0:
    print('Es positivo')
elif numero1==0 :
    print('Es neutral')
else :
    print('Es negativo')
'''
#Ejercicio 2
'''
nombre=(input('Ingrese su nombre: '))
apellido=(input('Ingerse su apellido: '))
if nombre[0]==apellido[0]:
    print('Las iniciales de nombre y apellido son iguales')
else :
    print('Las iniciales no son iguales')
'''
#Ejercicio 3
'''
def es_divisible (m,n):
    if m%n ==0:
      return True
    else: 
        return False
print(es_divisible(556,6))
'''
#Ejercicio 4
'''
dias_semana=['Domingo','Lunes','Martes', 'Miercoles', 'Jueves','Viernes','Sabado']
ingrese_numero= int(input('Ingrese un numero:   '))
if ingrese_numero>=1 and ingrese_numero<=7 :
    print(dias_semana[ingrese_numero-1])
'''
#Ejercicio 5
pasajeros=int(input('Ingrese la cantidad de pasajeros: '))
if pasajeros==1 :
    print('Es convenientes viajar en: Bicicleta')
elif pasajeros==2 :
    print('Es conveniente viajar en: Moto')
elif pasajeros>2 and pasajeros <=4 :
    print('Es conveniente viaje en: Auto')   
elif pasajeros>4 and pasajeros <=12 :
    print('Es conveniente viajar en: Camioneta') 
elif pasajeros>12 and pasajeros <=40 :
    print('Es conveniente viajar en: Colecitvo') 
elif pasajeros>40 and pasajeros <=200 :
    print('Es conveniente viajar en: Avion') 
else :
    print('No es conveniente viajar')
