#los if siempre se ejecutan sobre una operacion boleana por ejemplo 
if  True:
    print('debería ejecutarse')
if False:
    print('nunca se ejecuta')

pet = input('¿cual es tu mascota favorita?')

if pet =='perro':
    print('genial tienes buen gusto ')

if pet == 'gato':
    print('espero que tengas suerte')

stock = int(input('digita un numero '))

if stock >= 100 and stock <= 1000:
    print('el stock esta correcto')
# el else funciona es que si esa funcion no se cumple el if , entonces haga otra cosa  haga otra casa 
else:
    print('el stock es incorrecto ')
    
#tenemos una fucion entre los dos que se llama elif por ejemplo :
# esto a diferencia
#de siempre if , cuando lo vaya a buscar cuando se cumpla la condicion
# se deja de buscar , asi ahorraras tiempo  

pet = input('¿cual es tu mascota favorita?')

if pet =='perro':
    print('genial tienes buen gusto ')

elif pet =='gato':
    print('espero que tengas suerte')

elif pet == 'pez':
    print('super maravilloso')
    
else :
    print('no tienes ninguna mascota interesante')