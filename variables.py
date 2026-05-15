#Esto es un comentario de una sola linea
"""Esto es un comentario de 
varias lineas"""

#inicializando variables
nombre="isabella del pilar peñafiel mayorga"
edad=14
estado=True
nota=5.0

#Mostrar el contenido de las variables print ()
print(nombre)
print (edad)
print(estado)
print(nota)

#que tipo de dato contiene cada variable.
print(type(nombre))
print(type(edad))
print(type(estado))
print(type(nota))

#Vamos a utilizar la funcion input para recoger datos por medio del teclado.
nombre=input("¿como te llamas?")
edad=input("¿que edad tienes?")
estado=input("¿en que estado estas?")
nota=input("¿cual es tu nota?")

#Para visualizar que guardamos en las variables anteriores
print("Hola,",nombre,"un gusto conocerte")
print ("Tu edad es:",edad)
print("Tu estado es:",estado)
print("Tu nota es:",nota)