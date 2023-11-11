'''
Ejercicio 17.
a) Definir una función que permita el ingreso de números 
por teclado hasta ingresar el 0, y retorne esa lista. 
'''
#Zona de funciones:
def armadoLista():
	lista=[]
	print('La carga de números a la lista, finaliza al ingresar 0')
	numero=int(input('Ingrese un número por teclado (entero): '))
	while numero!=0:
		lista.append(numero)
		numero=int(input('Ingrese un número por teclado (entero): '))
	return lista
'''
b) Definir una función que reciba como parámetro una lista de números y 
retorne como resultado el promedio.
'''
def promedioNumeros(lista):
	suma=0 #acumulador
	cantidad=len(lista)
	for numero in lista:
		suma=suma+numero
		promedio=suma/cantidad
	return promedio
promedionumeros=promedioNumeros(lista)
