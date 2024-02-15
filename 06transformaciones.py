name = "alejandro"
print(type(name))
name = 12 
print(type(name))
name = True
print(type(name))

'''podemos cambiar el tipo de variable por lo que queramos , ya sea un string , un boleano o un entero
tenemos que tener mucho cuidado con cambiar el tipo de variable como por ejemplo '''

print("nicolas " + "molina")

print(10 + 20)

'''no puedes hacer una suma de string con un numero , por ejemplo '''
print("alejandro ")

'''de inmediato nos va a aparecer un error por que tiene dos tipos de datos diferentes 
a excepto de que le ponga comillas a el numero para que lo guarde como otro string , por ejemplo '''

print("alejandro " + "27")

age = 12 
#print("mi edad es " + (age))
#va a salir un error por que age es un numero sin embargo , si lo desea sumar 
#lo debemos de convertir a un string por ejemplo 

print("mi edad es " + str(age))

'''como podemos observar ahora si podemos nos da en la terminal mi edad es 12 
No es que estemos cambiando el valor , si no que lo transformamos para poderlo utilizar en 
la funcion print '''

print(age)
#otra forma de cambiarlo de forma mas facil es la siguiente 

print(f"mi edad es {age}")
#podemos observar en terminal que aparece como si todo fuera un string 

age = input('escribe tu edad ')
print(type(age))
print(f'tu edad en 10 años sera {age}')

'''en este momento la edad va a ser un string por que impt siempre nos va a devolver es una cadena 
para transformar esto y pasarlo aun entero hacemos lo sigueinte '''

age = int(age)
age += 10 
print(f'tu edad en 10 años sera {age}')

''' haca emos convertido un numero a un string y un string a un numero '''
print(type(age))








