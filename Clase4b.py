### Ejercicio 1
# 
#  Crear dos variables que representen dos productos, asignarle un precio
producto_uno = 265
producto_dos = 324.50

### Ejercicio 2 
# 
# Aplicarle iva (16% adicional del precio)
iva = 0.16
producto_uno_con_iva = producto_uno * (1 + iva)
producto_dos_con_iva = producto_dos * (1 + iva)
print("El precio del producto uno con iva: " + str(round(producto_uno_con_iva, 2)))
print("El precio del producto dos con iva: " + str(round(producto_dos_con_iva, 2)))

### Ejercicio 3
# 
#  Calcular el precio total de la compra de una pieza por producto
precio_total = (producto_uno + producto_dos) * (1 + iva)
print("El precio total de tu compra es: " + str(round(precio_total, 2)))

### Ejercicio 4
# 
#  Calcular el precio total de 4 piezas del producto 1 5 del producto 2
cantidad1 = input("Ingrese la cantidad de producto uno que desea comprar: ")
cantidad2 = input("Ingrese la cantidad de producto dos que desea comprar: ")
precio_total = ((producto_uno * int(cantidad1)) + (producto_dos * int(cantidad2))) * (1 + iva)
print("El precio total de tu compra es: " + str(round(precio_total, 2)))

### Ejercicio 5
# 
# Aplicar 2 operaciones con enteros
# Dados dos valores enteros ingresados por el usario,
# realizar dos operaciones (suma, resta, multiplicación o división)
# con dichos números e imprime el resultado utilzando un f-string
entero_uno = int(input("Ingrese un número entero: "))
entero_dos = int(input("Ingrese un segundo número: "))
suma = entero_uno + entero_dos
resta = entero_uno - entero_dos
print("Las operaciones que realizaste son: \n suma: " + str(suma) + "\n resta: " + str(resta))

### Ejericio 6
# 
# Aplicar 2 operaciones con flotantes
# Dados dos valores flotantes ingresados por el usario,
# realizar dos operaciones (suma, resta, multiplicación o división)
# con dichos números e imprime el resultado utilzando un f-string
flotante_uno = input("Ingrese un número flotante: ")
flotante_dos = input("Ingrese un segundo flotante: ")
division = float(flotante_uno) / float(flotante_dos)
multiplicacion = float(flotante_uno) - float(flotante_dos)
print("Las operaciones que realizaste son: \n division: " + str(division) + "\n multiplicacion: " + str(multiplicacion))


### Ejercicio 7
# 
# Aplicar 2 operaciones con strings
# Dados dos cadenas ingresados por el usario,
# realizar dos operaciones (suma, resta, multiplicación o división)
# con dichos números e imprime el resultado utilzando un f-string
cadena_uno = input("Ingrese una cadena de texto: ")
cadena_dos = input("Ingrese una segunda cadena de texto: ")
print("Si sumamos las dos cadenas anteriores se forma: " + cadena_uno + " " + cadena_dos)
print("Si multiplicamos la cadena uno por 5, se imprime 5 veces: \n" + (cadena_uno * 5))

# ### 
# nombre = "Carlos Aviles"
# otro_nombre = "Ale Paez"
# cadena = "Mi nombre es {}"
# print(cadena.format(nombre))
# print(cadena.format(otro_nombre))
# print((cadena.format(nombre).split(" ")))


### Crear una lista (l_nombres) con los nombres de 5 compañeros
l_nombres = ["Ale Paez", "Gabriela Camarillo", "Emmanuel Cianca", "Gilberto García", "Liliana Juárez"]
print(l_nombres)

### Crear una lista (l_dato) con el tiempo que tardan en llegar al trabajo
l_dato = [20, 0, 10, 35, 40]
print("minutos:", l_dato)

### Cambiar el tiempo (edad) del 3er compañero
l_dato[2] = 25
print(l_dato)

### mostrar los compañeros con menos de 26 años
l_modificado = [l_nombres[i] for i in range(len(l_nombres)) if l_dato[i] < 26]
print(l_modificado)

### Crear una lista con los compañeros de horas de sueño promedio
l_horas = [7, 6, 6, 3, 8]
print(l_horas)

### Seleccionar cuales compañeros duermen más de 8 horas
l_mas_horas = [l_nombres[i] for i in range(len(l_nombres)) if l_horas[i] > 8]

### Seleccionar cuales compañeros duermen menos de 8 horas
l_menos_horas = [l_nombres[i] if l_dato[i] < 4 else f"{l_nombres[i]} es vampiro" for i in range(len(l_nombres)) if l_horas[i] < 8]


### Aplicar 2 operaciones con bool
# < menor que
# > mayor que
# >= mayor o igual que
# <= menor o igual que

# and, &
# or, |

# True & True = True
print("True & True", True & True)
# True & False = False
print("True & False", True & False)
# False & True = False
print("False & True", False & True)
# False & False = False
print("False & False", False & False)

# True | True = True
print("True | True", True | True)
# True | False = True
print("True | False", True | False)
# False | True = True
print("False | True", False | True)
# False | False = False
print("False | False", False | False)

# if (expresion1 devuelve True, False):
#     codigo 1
# elif (expresion2 devuelve True, False):
#     codigo 2
# elif (expresion2 devuelve True, False):
#     codigo 3
# elif (expresion2 devuelve True, False):
#     codigo 4
# else:
#     codigo 5

# if condicion: 

### cuidado con el orden en esta caso nunca se va ejecutar
##  print("duermes muy poco")
##
horas_suenio = 7
if horas_suenio < 8:
    print("duermes muy poco")
elif horas_suenio < 4:
    print("eres un vampiro")
else:
    print("Que envidia")
    
### para corregirlo puedes cambiar el orden
horas_suenio = 7
if horas_suenio < 4:
    print("eres un vampiro")
elif horas_suenio < 8:
    print("duermes muy poco")
else:
    print("Que envidia")