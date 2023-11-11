#teóricamente no está mal, pero se usaría la palabra 'else', para no tener que poner la otra condición
'''
numero1=int(input('Ingrese un numero: '))
if numero1>0:
    print('Es positivo')
if numero1<0:
    print('Es negativo')
'''
#utilizando el condicional 'else'
'''
numero1=int(input('Ingrese un numero: '))
if numero1>0:
    print('Es positivo')
else :
    print('Es negativo')
'''
#uso de 'elif'
'''
numero1=int(input('Ingrese un numero: '))
if numero1>0:
    print('Es positivo')
elif numero1==0 :
    print('Es neutral')
else :
    print('Es negativo')
'''
#Solicite un numero por teclado del 1 al 5, e imprima su nombre en letras.
numero2=int(input('Ingrese un número del 1 al 5: '))
if numero2==1 :
    print('Uno')
elif numero2==2 : 
    print('Dos')
elif numero2==3 :
    print('Tres')
elif numero2==4 :
    print('Cuatro')
elif numero2==5 :
    print('Cinco')
else :
    print('No corresponde el valor')
    