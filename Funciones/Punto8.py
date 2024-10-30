print (" ")#Salto de linea
print ("Velazquez Mares Jesus Eliu")#Nombre del programador del codigo
print (" ")#Salto de linea
#Definimos "the_function" como una funcion al usar la palabra reservada "def"
#Y usamos "**" si desconosemos la palabra clave a utilizar
def the_function(**si_no):
    print("Y ella dijo " + si_no["yo"])
#Llamamos a la funcion y la asignamos datos a los parametros
the_function(ella = "no", yo = "si")