### Diccionarios
# Ejemplo con horas de sueño
l_nombres = ['Ale Paez', 'Gabriela Camarillo', 'Emmanuel Cianca', 'Gilberto García', 'Liliana Juárez']
l_horas = [7, 6, 6, 3, 8]
# ejemplo1 = {
#     'keys': 'valor'
#     'Ale Paez' : {
#         'Horas de sueño': 7,
#         'Minutos al trabajo': 20
#     }
# }

horas_suenio_dict = {
    'Ale Paez': 7,
    'Gabriela Camarillo': 6,
    'Emmanuel Cianca': 6,
    'Gilberto García': 3,
    'Liliana Juárez': 8
}

# .items / Devuelve todos los elementos de un dict en una lista
for llave, valor in horas_suenio_dict.items():
    print(f'{llave} duerme {valor}')

# .keys / Devuelve todas las llaves de un dict
list(horas_suenio_dict.keys()) #Si se necesita tener las llaves como listas

for llave in horas_suenio_dict.keys() :
    print(f'{llave} duerme {horas_suenio_dict[llave]}')

# .values / Devuelve todos los valeros, aunque no queda claro a que llave pertenecen cada valor

suma_horas = 0
for valor in horas_suenio_dict.values() :
    print(valor)
    suma_horas += valor

print(f'El promedio de horas de sueño de los alumnos es: {suma_horas / len(horas_suenio_dict)}')

# .clear / Deja vacío el diccionario

# .copy / Crea una copia del dict

# .fromkeys / Crea un diccionario con un valor por default
horas_suenio_dict_2 = dict.fromkeys(['Artur', 'Oscar', 'Alex', 'Charlie'], 8)
print(horas_suenio_dict_2)

# horas_suenio_dict_2['Ale Paez'] -> KeyError: 'Ale Paez' no existe

## Consultas en Diccrionarios
# .get / Devuelve el valor de la llave, si no existe no devuelve nada
horas_suenio_dict_2.get('Ale Paez') # No devuelve nada porque Ale Paez no existe
horas_suenio_dict_2.get('Arturo')   # -> 8

# .pop / Elimina una llave junto con su valor
horas_suenio_dict_2.pop('Arturo')
print(horas_suenio_dict_2) # {'Oscar': 8, 'Alex': 8, 'Charlie': 8}

# .setdefault / Agrega un elemento
horas_suenio_dict_2.setdefault('Arturo', 7) # Agrega Arturo con 7 horas de sueño
# Parecido al get
horas_suenio_dict_2.setdefault('Arturo')
horas_suenio_dict_2.setdefault('Ale Paez') # Al igual que el get, no marca error

# .update / Recibe un diccionario
horas_suenio_dict_2.update({'Ale Paez', horas_suenio_dict['Ale Paez']})
print(horas_suenio_dict_2)
horas_suenio_dict_2['Ale Paez']
horas_suenio_dict_2['Gil'] = 10 # Gil no existe, lo crea y le asigna el valor de 10
horas_suenio_dict_2['Gustavo','No se encontró el nombre']

# Validar que la llave existe
if 'Gustavo' in horas_suenio_dict_2.keys() :
    print('Sabemos cuánto duerme Gus')
else :
    print('No sabemos cuánto duerme Gus')

### While
# while condicion: 
#     codigo

i = 0
while i < 11:
    print(i)
    i += 1

i = 0
while i < 10:
    i += 1
    print(i)

i = 0
while True:
    i += 1
    print(i)
    if i == 10:
        break

i = 0
while True:
    i += 1
    if i == 11 :
        break
    else:
        print(i)

# continue / Brinca a la siguiente iteración
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

i = 0
while i < 10:
    i += 2
    print(i)

# pass / omite la línea y pasa a la siguiente línea de código
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        pass
    print(i)

### zip / Permite crear diccionarios a partir de listas
dict(zip(l_nombres, l_horas))  # El primer argumento son las llaves, el segundo los valores

for i, j in zip(l_nombres, l_horas):
    print(f'{i} duerme {j} horas')

dict_ejercicio = {}

for llave, valor in zip(l_nombres, l_horas):
    dict_ejercicio.update({llave, valor})
    # dict_ejercicio.setdefault(llave, valor)
    # dict_ejercicio[llave] = valor

print(dict_ejercicio)

### for a in a zip()

[(i,j) for i, j in horas_suenio_dict_2.items()]

list(horas_suenio_dict_2.items())

### Mezclar diccionarios y listas
ejemplo_mixto = {'Arturo': {"Visión computacional": [10, 9, 7]}}
ejemplo_mixto['Arturo'] # -> {'Visión computacional': [10, 9, 7]}

### Pedir al usuario el nombre del alumno y los minutos que tarda su trabajo:
# Guardarlo en un diccionario, los nombres sono las llaves y los minutos son
# los valores, en enteros. El break es con un input "no" en el nombre del alumno
# Imprime el resultado de forma agradable

i = 'yes'
dict_exercise = {}
while i == 'yes':
    nombre = input('Ingrese el nombre del alumno: ')
    if (nombre.lower() == 'no'):
        i = 'no'
        break
    else:
        minutos = input('Ingrese el número de minutos que tarda en llegar a su trabajo: ')
        dict_exercise[nombre] = minutos
print(dict_exercise)

### Funciones
# def nombre_funcion(parametros):
#     codigo

def suma(x, y):
    return (x + y)

def resta(x, y):
    return (x - y)

def multiplicacion(x, y):
    return (x * y)

def division(x, y):
    if y == 0:
        print('No puedes dividir entre cero')
        return None
    return (x / y)

# def calculadora(x, y, operacion = 'suma') / Se asigna por default la operación suma. Deben ir al final de los parámetros
def calculadora(x, y, operacion):
    if operacion == 'suma':
        return(suma(x, y))
    if operacion == 'resta':
        return(resta(x, y))
    if operacion == 'multiplicacion':
        return(multiplicacion(x, y))
    if operacion == 'division':
        return(division(x, y))

# def calculadora('suma', x, y) / Marca error porque no sigue el orden declarado en los parámetros