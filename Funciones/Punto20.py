print (" ")#Salto de linea
print ("Velazquez Mares Jesus Eliu")#Nombre del programador del codigo
print (" ")#Salto de linea
#Definimos "the_function" como una funcion al usar la palabra reservada "def"
def factorial(fac):
#Si fac es mayor que 0 entonces
  if(fac > 0):
    fact = fac + factorial(fac - 1)
    print(fact)
  else:
    fact = 0
  return fact

print("\n\nRecursion Example Results")
factorial(10)