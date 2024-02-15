text = 'ella sabe python'

print(text[0])

#asi mostraria que el primer caracter es la E 

print(text[1])

#asi va a aparecer la posicion 2 que es la L 

size = len(text)

#print(text[size]) 

# en esta parte lo que va a aparecer es un error por que tenemos que calcular el tamaño - 1  por ejemplo 

print(text[size -1])

#nos va a aparecer que en el texto la ultima palabra es menos 1

'''en python lo que pasa con la ultima posicion de un string se puede busca poniendo un ( - 1 ) para poder ir a la n por ejemplo 
como podemos observar en la terminal , aparece que el -1 es igual a la letra n , que es la ultima en el string 
por ejemplo si fuera -2 seria la antepenultima , osea la o '''

print(text[-1])

# este es el metodo podemos sacar ciertas parte del textO slicing

print(text[0:5])
print(text[:10]) 

'''cuando no se pone la el numero , si no solo los dos puntos y despues el numero de cantidad del string ,
 es para que python lo coja directamente desde 0 '''

print(text[0:-1])

#como podemos observar , no nos aparece todo el texto en la linea , por que asi no se busca , es de la siguiente forma 

print(text[0:])
# ahora si el ejemplo anterior , si nos va a dar todo el texto , por que como fue dersde el principio , si no le ponemos 
#el numero final pyhton lo va a traducir como si fuera hasta el final del string 

print(text[:])

#tambien se puede este valor que significa desde el principio hasta el final 


