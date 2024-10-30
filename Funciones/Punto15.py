print (" ")#Salto de linea
print ("Velazquez Mares Jesus Eliu")#Nombre del programador del codigo
print (" ")#Salto de linea
#Definimos "the_function" como una funcion al usar la palabra reservada "def"
def the_function(Hola, /):
  print(Hola)
#Llamamos a la funcion 
#Pero si intenta enviar un argumento de palabra clave manda un error
the_function(Hola = "Hola Buenos Diaz")
pass