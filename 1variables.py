#Esto es un comentario de una sola line
""""Esto es un comentario de
varias lineas"""

#Inicializando variables
Nombre="Nombre del estudiante"
edad=58
Estado=True
Nota=5.0

#mostrar el contenido de las variables print()
print(Nombre)
print(edad)
print(Estado)
print(Nota)

#Que tipo de datos contiene cada variable
print(type(Nombre))
print(type(edad))
print(type(Estado))
print(type(Nota))

#Vamos a utilizar la funcion input para recoger datos por medio del teclado
Nombre=input("¿como te llamas? ")
edad=input("¿qué edad tienes? ")
Estado=input("¿en que Estado de encuentras? ")
Nota=input("cual es tu nota? ")

#para visualizar que guardamos en las variables anteriores
print("hola,",Nombre,"un gusto conocerte")
print("tu edad es:",edad)
print("tu estado es:",Estado)
print("tu nota es",Nota)