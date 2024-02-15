

# siclos en while , que significa mientras que es muy parecido a if , es el siguiente , vamos  a hacer un ejercicio primero de if 

'''
while True: 
  print('se ejecuto')  

'''

'''counter = 0
while counter <10 :
    counter+=1
    print(counter) 

    la importancia de identar es que se necesitan los espacio para poder que haga parte del ciclo while , si no le pone los espacio al principio del while 
    entonces le va a aparecer un error , tiene que ser tal cual '''

'''asi podemos hacer un ciclo que se puede repetir 10 veces por que a medida que se ejecuta va a sumar uno hasta que se cumpla el ciclo 
osea hasta que llegue a 10 ''' 

'''como podemos observar , el ciclo se detiene siempre y cuando se cumpla la funtion es decir hasta que llegue hasta 10 '''


'''counter = 0
while counter < 20:
    counter +=1
    if counter == 15:
      break
    print(counter)
'''
 
'''como podemos observar el break es una forma forzada de romper el ciclo '''


counter = 0

while counter <20:
   counter +=1
   if counter <15:
    continue
   print(counter)
   print(counter)
   print(counter)



'''lo que hace continue es pasarlo automaticamente a la siguiente iteracion y no lo va a volver a poner desde 0 
si no que le va a volver a aparecer desde la siguiente interacion , en este caso desde el 15'''



