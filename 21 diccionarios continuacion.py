persona = {
    'nombre': 'sebastian',
    'apellido': 'aristizabal',
    'edad': 24 ,
    'lenguajes': ['python', 'javascript'],
    'ciudad': 'medellin'
}

print(persona)

#podemos cambiar la informacion de la siguiente manera 

persona['nombre'] = 'rafael'

# tambien lo podemos modificar de la siguiente manera 

persona['edad'] -= 3

print(persona)
#---------------------------------------------------------------------------------------------------------

# SUMAR UN VALOR 

persona['ciudadd'] = 'bogota',

print(persona)

# tambien para agregar una mas es de la siguiente forma como es una lista podemos hacer lo siguiente 

persona['lenguajes'].append('c++')

print(persona)

# como podemos observar en lenguajes nos aumento otro idioma el cual le agregamos c++
#---------------------------------------------------------------------------------------------------
# para eliminar un atributo en el diccionario es de la sigueinte forma 

del persona['nombre']

print(persona)


# asi se elimina un atributo del dicionario otro metodo es el de pop 

persona.pop('edad')

print(persona)

#-----------------------------------------------------------------------------------------------------

#hay algo muy importante que podemos utilizar y eso se llama los ITEMS de un diccionario 

print('items')
print(persona.items())

#cuando le digo items en va a devolverme casi en un arrays en pares de tuplas 

print('keys')
print(persona.keys())

#si vemos los keys el lo unico que nos devuelve es una lista con los atributos que nos tenga el dicionario como por ejemplo 
#nombre, apellido, ciudad, edad , lenguajes , pero no muestra el resultado de cada una , por ejemplo de nombre y no aparece sebastian 

print('values')
print(persona.values())

#las values es para que le retorne una lista pero solo de los valores por ejemplo , sebastian aristizabal, 24 , devuelve una lista con todas las respuestas 


