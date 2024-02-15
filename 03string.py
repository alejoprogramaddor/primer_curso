#los trings 
my_name = "alejandro"
last_name = "aristizabal "
print(my_name)
print(last_name)

"""lo siguiente es para concatenar osea unir diferentes string y se utiliza
con el signo de + """
full_name = my_name + " " + last_name

print(full_name) 
'''si quieres utilizar un string con abreviaturas, por ejemplo 
en ingles , entonces lo que toca hacer es lo siguiente 

si es con una abreviatura , por ejemplo i'm alejandro , entonces se debe de poner 
en una cadena con doble '' comillas para poder que de (por ejemplo 
un string asi '' i'm alejandro '' y la otra es que sea de la siguiente forma 
cuando la necesita de doble comillas , entonces se crea el string con 
una sola comilla , por ejemplo ' yo soy ''alejandro'' ' y asi susesivamente )'''

'''hay tres formas de concatenar y son las siguientes '''
#ejemplo numero 1 
template = "hola, mi nombre es " + my_name + " y mi apellido es " + last_name 
print(template)
#ejemplo numero 2 
template = "hola, mi nombre es {} y mi apellido es {}".format(my_name, last_name)
print(template)
#ejemplo numero 3 y es el mas usado , recuerda poner 
# la f al principio la f es para informar que todo es string 
template = f"hola, mi nombre es {my_name} y mi apellido es {last_name}"
print(template)




