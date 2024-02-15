my_dict = {}

print(type(my_dict))

# en el type aparece dict que significa diccionario , solamente por ponerlo de esta forma de entre corchetes 

my_dict = {
    'name' : 'alejandro',
    'last name' : 'aristizabal',
    'age' : 27,
}

print(my_dict)

#para saber cuantos elementos hay en el diccionario ponemos el len por ejemplo 

print(len(my_dict))

# en la parte de la terminal va a aparecer 3 que significa que hay 3 caracteristicas en el diccionario 

# tambien podemos preguntar por algo en especifico de la siguientre manera 

print(my_dict['age'])

#en la terminal va a aparecer que es 27 


'''se puede hacer una consulta si existe un valor , si el valor existe , entonces aparecera el valor , en caso de que el valor no exixta ,
 lo que va a aparecer es none , que siginifica que no existe a direcencia de error por ejemplo  '''

print(my_dict.get('name'))

print(my_dict.get('edad'))

#como podemos observar en la parte de none significa que no esta en el my_dict es para buscar . 

# otra forma de saber si esta en el dicionario es esta 

print('avion' in my_dict)

#la repuesta debe de sar boleano , osea true o false 

#tambien podemos hacer otro ejercico 

print('age' in my_dict)




