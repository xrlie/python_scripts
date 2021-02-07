### Una empresa tiene segmentado a sus clientes de la siguiente manera
## De edad menor a 18 años y compras mensuales mayores a 10,000 pesos
# se les llama: juniors
## De edad menor a 18 años y compras mensuales menores o igual 10,000 pesos
# se les llama: aficionados
## De edad mayor o igual a 18 años y compras mensuales mayores a 10,000 pesos
# se les llama: fifi
## De edad mayor o igual a 18 años y compras mensuales menores o igual a 10,000 pesos
# se les llama: chairos
## Todas las personas de más de 60 años se llamarán pejes
## Todas las personas que hagan compras mensuales mayores a 50,000 se llamarán Chava Iglesias JR
## Todas las personas de más de 60 años y hagan compras mensuales mayores a 50,000
edad_cliente = 27
nombre_cliente = "Fulanito"
compras_mensuales_cliente = 13000

if 60 >= edad_cliente >= 18 and 50000 >= compras_mensuales_cliente > 10000 :
    print('fifi')
elif 60 >= edad_cliente >= 18 and compras_mensuales_cliente <= 10000 :
    print('chairos')
elif edad_cliente < 18 and compras_mensuales_cliente > 10000 :
    print('juniors')
elif edad_cliente < 18 and compras_mensuales_cliente <= 10000 :
    print('aficionados')
elif edad_cliente >= 60 and compras_mensuales_cliente <= 50000 :
    print('pejes')
elif edad_cliente < 60 and compras_mensuales_cliente > 50000 :
    print('Chava Iglesias JR')
elif edad_cliente >= 60 and compras_mensuales_cliente > 50000 :
    print('mi abuelo favorito')

### Código más limpio
if edad_cliente >= 60 and compras_mensuales_cliente > 50000 :
    print('Mi abuelo favorito')
elif edad_cliente >= 60 :
    print('pejes')
elif compras_mensuales_cliente > 50000 :
    print('Chava Iglesias JR')
elif edad_cliente >= 18 and compras_mensuales_cliente > 10000 :
    print('fifi')
elif edad_cliente >= 18 :
    print('chairos')
elif edad_cliente < 18 and compras_mensuales_cliente > 10000 :
    print('juniors')
elif edad_cliente < 18 :
    print('aficionados')

for i in range(10) :
    print(i)

### A continuación se muestra una lista con los precios de las acciones diaro
### de nuestra empresa

precio_diario_promedio = [100, 60, 80, 90, 100, 120, 140]

### ¿Cuál es el precio promedio?
promedio = 0
for i in range(len(precio_diario_promedio)) :
    promedio += precio_diario_promedio[i]
    print(promedio)

print(promedio / len(precio_diario_promedio))

### ¿Cuántes vcees tomó el precio de 100?
# Método
x = precio_diario_promedio.count(100)
print(f'El número de coincidencias con 100 es: {x}')

# List comprehension
a = [ i for i in precio_diario_promedio if i == 100]
print(f'El número de coincidencias con 100 es: {len(a)}')

## Al analizar los datos, se descubrió que el precio de 60 era incorrecto
# el correcto era de 70
# cambiar el elemento 60 por un 70

#[precio_diario_promedio[i] = 70 for i in range(len(precio_diario_promedio)) if precio_diario_promedio[i] == 60]
precio_diario_promedio[1] = 70
print(precio_diario_promedio)

### Sets
A = {12, 15, 16, 17, 18}
B = {10, 4, 12, 4, 9, 15}
C = {10, 4}
D = {1, 2, 3}
# Union
A | B # = {4, 9, 10, 12, 15, 16, 17, 18}  ## Elementos que están en A o B

# Intersección
A & B # = {12, 15}     ## Elementos que están en A y B

# Diferencia
A - B # = {16, 17, 18} ## Elemenots que están en A y NO en B
B - A # = {9, 10, 4}   ## Elementos que están en B y NO en A

# Diferencia simétrica
A ^ B # = {16, 17, 18, 4, 9, 10} ## (Elementos que están en A y no están en B) UNIÓN (Elementos que están en B y no están en A)
C ^ D # = {1, 2, 3, 4, 10}       ## (Elementos que están en C y no están en D) UNIÓN (Elementos que están en D y no están en C)

# Subconjunto
C <= B # = True ## ¿Es C un subconjunto de B? // En otras palabras, todo lo que hay en C ¿está en B?

# Superconjunto
B >= C # = True ## ¿Es B un superconjunto de C? // En otras palabras, lo que tiene B ¿lo puedo encontrar en C?

# Métodos
# add ## Agregar un elemento
A.add(100)
A.add(11, 12, 100) # error
A.add([11, 12, 100]) # error

# update ## Agrega múltiples elementos
A.update([11, 12, 100])

# remove ## Elmina un determinado elemento, en caso de no encontrarlo manda un error
A.remove(11)
A.remove(102) # error

# discard ## Elimina un determinado elemento, en caso de no encontrarlo NO manda un error
A.discard(102) 

# pop ## Elimina un elemento de manera aleatoria
A.pop()

# clear ## Elimina todos los elementos del conjunto y se convierte en un conjunto vacio
A.clear()

a = frozenset(A)
print("Este es un frozen set:", a)