### Recordatorio
# Python no tiene i++, pero...
print("Inicializando i con un valor de 1")
i = 1
print(i)
print("Sumando una unidad")
i += 1
print("El resultado es:", i)
# print("El resultado es: " + str(i))

texto_resultado = "El resultado es: {}"
texto_resultado.format(i) # Se ejecuta, se sustituye pero se regresa a su valor porque no se afecta a la variable
print(texto_resultado.format(i))
print(texto_resultado) # No se imprime porque el valor no se vio reflejado
texto_resultado = texto_resultado.format(i) # En esta línea se asigna el valor, por lo que ahora si se modifica
print(texto_resultado) # Ahora si se imprime el valor cambiado.

# también se pueden agregar los valores por medio de posición
j = 5
print("Tenemos dos valores: {} y {}")
cadena_rand = "Tenemos dos valores: {} y {}"
print(cadena_rand.format(i, j))

# Otra forma de agregar variables es declarándolas
cadena_rand2 = "Tenemos dos valores: {var1} y {var2}"
print(cadena_rand2.format(var1 = j, var2 = i))

# Una última modalidad para agregar valores son con los f-strings
### f-strings
x, y = 10, 29
print(f"Las coordenadas de tu posición son ({x}, {y})")

### Strings múltiples líneas
print('''
Cadena con
Múltiples
Líneas
''')

mi_empresa = "Rescatando Patitas"
objetivo = "ser un mediador para facilitar el proceso de adopción y así crear conciencia sobre la situación actual de los animales en situación de calle en"
pais = "Mexico"
producto1 = "Aplicación web con más de 10 mil animalitos esperando un hogar"
producto2 = "Conexión con todos las fundaciones de adopción cercanas a ti"
producto3 = "Las mejores promociones de nuestros patroncinadores"

print(f'''
Bienvenidos a {mi_empresa}
Nuestro objetivo como empresa es {objetivo} {pais}
Tenemos diferentes productos que ofrecer entre los cuales destacan:
1.- {producto1}
2.- {producto2}
3.- {producto3}
Esperamos que sea de tu agrado, te invitamos a compartir este mensaje entre tus contactos.
___Ayudando a regresar patitas a casa____
''')

### Funciones type, len
print("5 es un entero", type(5))
print("'5' es un string", type('5'))
print("True es un bool", type(True))
print("3.3333333 es un float", type(3.3333333))

# Ejemplo con variables
x = 5
print("5 es un entero", type(x))

len("Hola, hoy me siento....") # Regresa el tamaño de caracteres

### Obtener caractéres
sentimiento = "Hola, hoy me siento...."
sentimiento[:]

# Ejercicio Palíndromo
palindromo = "anita lava la tina"
print(palindromo)
print(palindromo[-1])

var_anecdota = "Hoy tuve mucho trabajo y estoy enfadado"
print(var_anecdota[0::2]) 

### string[1:11:2] La primer posición es donde comienza
### string[1:11:2] La segunda posición es donde termina
### string[1:11:2] La tercer posición es el tamaño del salto


### Métodos String

# .find() encontrar un texto
# .lower()
# .upper()
# .swapcase()
# .replace
# .split
# .join
# .isdigit()
# .isnumeric()
# .isdecimal()

### Ejercicio
texto_entrada = "12|13|14"
lista_texto_entrada = texto_resultado.split("|") # split espera como parámetro el c para dividir el texto
"|".join(lista_texto_entrada)

if lista_texto_entrada[0].isdigit():
    lista_texto_entrada[0] = int(lista_texto_entrada[0])