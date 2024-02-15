text = 'ella sabe programar en python'
print('Javascript' in text )
print('Python' in text)

''' el in es  para buscar en el text si esta alguna palabra y nos responde
de una forma boleana , osea true o false '''

#acontinuación podemos hacer un ejercicio de condicionales con el texto 

if 'js' in text :
    print('no esta en el texto ')
else :
    print('si esta en el texto')
    
'''esta es otra funcion en la cual cuenta el tamaño de un string por ejemplo 
len examina el espacio de numero de caracteres que hay en un texto '''


size = len('alejandro')
print(size)

'''si utilizas espacios en el string tambien se va a contar , por ejemplo  '''

fono = len(text)
print(fono)

'''va a aparecer que fono es iguaal a 12 caracteristicas , ya que tiene 3 espacios mas en alejandro '''

'''para pasar todo un texto a mayuscula tambien podemos hacer lo siguiente
eso lo podemos hacer con el operador de UPPER()'''

print(text.upper())

'''para poner todo el texto en minuscula se pone la palabra lower asi como vamos a ver acopntinuacion '''

print(text.lower())

#tambien podemos poner para saber cuanto aparce una letra en especifico con la palabra count

print(text.count('a'))

#podemos obervar que en el texto hay 4 veces la letra a , por eso es que aparece en terminal 4 

'''tambien esta la forma de swapcase y sirve para que el text5o que este en minuscula pase a mayuscula y 
el texto que este en mayuscula pasa a minuscula por ejemplo '''

print(text.swapcase())

'''esrta otra funncion es para saber si el string termina en lo que esta buscando , por ejemplo '''

print(text.endswith('python'))

#este tambien se utiliza para hacer un remplazo en un string por ejemplo 

print(text.replace('python', 'go'))

text_2 = 'este es un titulo '

print(text_2)

# la otra funtion es capitalize y sirve para oner el primer caracter en mayuscula por ejemplo 

print(text_2.capitalize())

#tambien hay otra funciuon que se llama title lo que hgace es poner el inicio de todas las palabras del texto en mayuscula  por ejemplo 

print(text_2.title())

#tambien hya una funcion que se llama isdigit no dice si este texto es un digito  por ejemplo y nos va a responder como un boleano 

print(text_2.isdigit())

#nos va a aparecer en la terminal que es false , por que es un digito , pero vamos a cambiar la variable por un digito 

text_3 = "25696102014127"

print(text_3.isdigit())

# nos va a aparecer en la terminal que es true , por que es un numero 

'''algunos metodos nos va a cambiar el texto por mayusculas y niusculas y otras nos va a responder de forma booleana '''








