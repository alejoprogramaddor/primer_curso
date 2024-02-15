matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

#lo que podemos ver es una lista que tiene listas 

print(matriz[0])

#lo que nos va a decir es que tenemos una lista con los valores 1, 2, 3. sin embargo esto nos devuelve una lista en si , y se pueden 
# poner como si estuviera en corrdenadas , por ejemplo 

print(matriz[0][2])

# nos va a aparecer el numero 3 , por que el primer 0 es de la primera celda de arriba asia abajo y el segundo numero que es el 2 
# es la tercera celda que es de el 3 , por eso en la terminal aparece el 3 .

'''podemos empezar a hacer una iteraccion '''

for element in matriz:
    print(element)

'''nos va a aparecer toda la listas de la lista '''

for element in matriz:
    print(element)
    for item in element:
      print(item)

# en esta parte podemos ver que tenemos un ciclo sobre otro ciclo y a esto se le mmana un ciclo anidado  

#otra forma de verla es de la siguiente forma 

for pila in matriz:
    print(pila)
    for columna in pila:
      print(columna) 

