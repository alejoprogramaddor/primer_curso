#el ciclo FOR 

#el ciclo for se utiliza cuando ya se tiene un numero de elementos o interacciones dadas en la cual hay una condicional y
# hasta que se cumpla se va a ejecutar 

'''for element in range(1, 20):
    print(element)'''

#como podemos obervar en la terminal aparece un numero del 1 al 20 , por que nosotros le informamos desde donde empezar (1, 20) que es desde el 1 
#hasta el 20 sin necesidad de poner el += , si no que con range el automaticamente sube desde el 1 hasta el 20 
    
#vamos a crear una lista    
    
my_list = [23, 45, 67, 89, 43]

for element in my_list:          #esto significa que quiere iterar element en base de mi_list (estamos iterando bajo un conjunto dado es decir , la lista )
    print(element)

#la iteracion significa que es la repeticion de una ejecucion de un bloque de codigo siempre y cuando la condicion de bucle sea verdadera 
    
#tambien podemos iterar una tupla , y es de la siguiente manera 
    
my_tuple = ('alejo', 'camila', 'sebastian')
for cualquierNombre in my_tuple:
    print(cualquierNombre)

# tenemos el resultado en la terminal las dos iteraciones , tambien podemos iterar un diccionario de la siguiente manera 
    

product = {
    'name' : 'camisas',
    'price' : 100,
    'stock' : 55,
}

for element in product:
    print(element)    #lo que aparece en terminal son es las claves 

for element in product: 
    print(product[element])   #ahora si nos va a poner los valores 

for element in product:
    print(element, product[element])  #asi nos va a aparecer todo el diccionario 

# a esto es a lo que llamamos una lñista de diccionarios : 
    
people = [
    {
        'name' : 'nico',
        'age' : 24
    },
    {
        'name' : 'camila',
        'age' : 40
    }, 
    {
        'name' : 'andres',
        'age' : 82
    }
]

for person in people:
    print(person)


    




    

