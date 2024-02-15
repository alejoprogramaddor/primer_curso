x = 3.3 
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)    

#para poder que y sea igual a 3.3 si mas decimales hacemos el siguiente ejercico 

y_str = format(y, ".2g")

# y_str (ese es el nombre que le damos a la variable  )
# format (es una funcion para ajuntar un parrafo  )
'''format(y, ".2g") = esto es para que el formato de solo dos digitos se pasa
el valor m que en este caso es y , para que el valor de y solo quede de 3.3 que son los digitos que necesito '''

print('string ya se convierte en', y_str)

#en este momento ya le quito toda esa precision decimal para ver que es verdad , se le hace una comparacion 

print(y_str == str(x))

#haca va una forma mas matematica 

print('*' * 10)

#esto lo que nos va a hacer es multiplicar ese * por 10 veces 

print(y, x)

# haca podemos obervar que la y es igual a 3.3000003 y x es igual a 3.3 y ya
#una del as formas es colocar una especie de tolerancia 

tolerance = 0.00001
print(abs(x - y) < tolerance) 
'''haca lo que estamos haciendo es abs significa absoluta  que estamos restando x 
menos y para sacar la diferencia  de esa presision decimal y ponemos el valor absoluto para que siempre 
de un valor positivo y luego tenemos un margen de error es decir una tolerancia entre esa posision '''

