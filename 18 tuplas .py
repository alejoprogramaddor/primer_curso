numbers = (1, 2, 3, 5)
string = ('salome', 'alejandro', 'laura', 'alejandro')

print(numbers)
print(type(numbers))

print(string)
print(type(string))

print('quien esta en la primera pocision 0 es el ', numbers[0])

print('quien esta en la ultima pocision -1 es igual a  ', numbers[-1])


'''cuando uno tiene tuplas no deja hacer modificaciones como si fuera una lista 
la diferencia de una lista a una tupla es que una tupla empieza con parentesis ()
encambio una tupla empieza con []'''

# lo que si podemos hacer es lo siguiente , para buscar en donde esta una parte de la lista es de la sigueinte forma 

print(string)

#como podemos recordar en la parte de index es para buscar en que parte esta el string alejandro 

print(string.index('alejandro'))

#en la parte de abajo nos muestra que count es para saber cuantas veces se repite un string 

print(string.count('alejandro'))

'''asi podemos convertir una tupla en una lista para poder hacer modificaciones en la lista
le ponemos list(y entre parentesis lo que quiere convertir ) '''

my_list = list(string)

print(my_list)

#asi podemos averiguar que tipo de dato es my_list 
print(type(my_list))

#asi podemos agregar algo en la lista , escojemos la ubicacion para que se ponga en el puesto 

my_list[1]= 'sofia'

print(my_list)

'''ya sabemos como convertirlo de una tupla a una lista , ahora convirtamos una lista a una tupla y es de la siguiente manera '''

my_tuple = tuple(my_list)

print(my_tuple)
print(type(my_tuple))








