# crud lo que hace en las listas es crear , leer , cargar y eliminar parte de la lista , por ejemplo 

number = [1, 2, 3, 4, 5, 6]

print(number[:])
# asi se puede leer lo que esta en la lista 

# tambien se puede actualizar la lista , como por ejemplo 

number[-1] = 7 

print(number)
# haca lo que podemos observar es que se actualizo el ultimo caracter por otro valor y asi es que se puede actualizar 
#---------------------------------------------------------------

#de esta forma podemos hacer que agreguemos en el ultimo numero de la lista 
number.append(700)

print(number)

#------------------------------------------------------------------



# insert tambien se utiliza para poder agregar cualquier numero o cualquier caracter a una lista , por ejemplo 
# en donde va el 0 , hay esta poniendo en que parte de la lista lo desea agregar 

number.insert(0, 'un string en medio de una lista')

print(number)

#cuando se inserte algo en la lista el no lo va a remplazar , lo que va a pasar es que lo va a correr a el resto de la lista 

#-----------------------------------------------------------------------
# tambien podemos fucinar listas de la siguiente manera 

nueva_lista = [ 'alejandro', 'laura', 'flor', 'sebastian', 'jose alvaro ']

print(nueva_lista)

new_list = nueva_lista + number 

print(new_list)

# haca podemos observar de que en esta lista en la parte de la terminal se sumaron todas las dos listas que se requeria de nueva lista + number
#-------------------------------------------------------------------------

# como hacer para preguntar en que posicion esta un elemento 

print(nueva_lista.index('alejandro'))
 
index = nueva_lista.index('laura')

#en la parte de la terminal , me informa en que parte esta la lista 

print(index)

nueva_lista[index] = 'maria'

print(nueva_lista)

# asi es como se remplaza el laura por maria en la lista 

#-----------------------------------------------------------------------------

#ESTA ES LA FORMA EN LA CUAL SE ELIMINA O SE REMUEVE UN ELEMENTO DE LA LISTA 

nueva_lista.remove('alejandro')

print(nueva_lista)

# como podemos observar , ya no existe alejandro en la tabla , por que ya se retiro 

#---------------------------------------------------------------------------------------------------------

#OTRO QUE SE UTILIZA PARA ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA Y SE LLAMA POP , POR EJEMPLO 

nueva_lista.pop()

print(nueva_lista)

nueva_lista.pop(0)
print(nueva_lista)

# como podemos observar , en la nueva lista . pop ( se pone entre parentesis y se pone el numero de la posicion que desee eliminar )

#--------------------------------------------------------------------------------------------------------

# otra opsion para hacer en las listas es reverse y es para ponerlo alrevez por ejemplo 
 
nueva_lista.reverse()
print(nueva_lista)

#---------------------------------------------------------------------------------------------------
# ahora se utiliza es la funcion de sort para ordenar un lugar de la lista , como por ejemplo , 
#ponemos una lista desorganizada, pero ya en terminal estan organizados 


numbers = [1,4,8,3,6,5,6,8,2,8,5,0,7]

numbers.sort()
print(numbers)

#tambien sirve para string por numero alfabetico , poor ejemplo 

lista = ['al', 'ab', 'az' , 'ar', 'bc']

lista.sort()

print(lista)

#como podemos observar ya se organizo alfabeticamente 

# cuando hay una lista con string y numeros , hay si no funciona el metodo de sort , para que los organice 

'''cuando uno tiene tuplas no deja hacer modificaciones como si fuera una lista 
la diferencia de una lista a una tupla es que una tupla empieza con parentesis ()
encambio una tupla empieza con []'''


