#not es para negar todas las operaciones utilizados en boleanos 
print(not True)

print(not False)

print('AND')
print('not True and True = ',not(True and True))
print('not True and false = ',not(True and False))
print('not False and True =',not(False and True))
print('not False and False =',not(False and False))

#en la terminal se invierte todo el operador logico de and 

stock = input('ingrese el numero de stok ')
stock = int(stock)
#recuerde que int representa numeros enteros , es decir 
#, positivos y negativos , no decimales 

print(not (stock >= 100 and stock <= 1000))
''' haca lo que va a a suceder es que como esta el not al principio 
entonces va a hacer lo contratio , si esta menos de 100 o mas de 1000
va a ser verdadero , de lo contraio esta en falso y lo podemos 
observar en la parte de la terminal '''

'''estas son las tablas de operadores logicos 
 
AND = solo si es verdadero y verdadero va a dar verdadero , del resto todo va a dar false 

True and True = True
True and False = False
False and False = False 
False and True  = False

0R = si solo uno tiene verdadero , siempre va a dar verdadero , a excepto de que los dos den false 

True or True = True
True or False = True
False or False = False 
False or True  = True

NOT = que es la forma de negar , en este caso por ejemplo 

not True = False 
not False = True 
 





'''