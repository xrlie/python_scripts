### Listas
# Listas ? <- por qué ### o #

mi_primer_lista = [1, 3.1416, "Hola Mundo"]

### Asigno la referencia a Y
x = [1, 2] #Se crea la variable x, con una
# [1,2]
y = x
x[0] = 0
print(x)

### Asigno el valor a Y
x = [1, 2] #Se crea la variable x, con una
# [1,2]
y = x.copy()
x[0] = 0
print(y)

# append
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.append(mi_lista_2)
print("Resultado de hacer append de una lista [1,2,3] con [1,3]:", mi_lista_1)
## imprime : [1, 2, 3, [1,3]]

#extend
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.append(mi_lista_2)
print("Resultado de hacer extend de una lista [1,2,3] con [1,3]:", mi_lista_1)
## imprime : [1, 2, 3, 1, 3]

### Crear mi documentación
# ctrl + } # Sublime, notebooks
# ctrl + shift + 7 # VS
""" omite este código """ # puedes usar strings

#remove
mi_lista_1.remove(2) # Elimina el primer 2
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
mi_lista_1.append(mi_lista_2)

### Ejemplo de eliminación de varios elementos
ejemplo_emma = [1, 2, 3, [1, 3]]
print(ejemplo_emma)
ejemplo_emma.remove([1, 3])
print(ejemplo_emma)
ejemplo_emma.remove(3)
print(ejemplo_emma)

### ¿Cómo elimino un elemento de una lista dentro de otra lista?
ejemplo_mario = [1, 2, 3, [1, 3]]
ejemplo_mario[3].remove(1)

#index
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [1, 3]
#[1, 2, 3, [1, 3]]
mi_lista_1.index(3)
mi_lista_1.index([1, 3])
mi_lista_1 = [1, 2, 3, [1, 3], 3]
print(mi_lista_1.index(3))

#count
mi_lista_1.count(3)

#reverse
mi_lista_1 = [1, 2, 3, [1, 3], 3]
mi_lista_1[::-1] # Invierte la lista
mi_lista_1.reverse() # Invierte la lista
mi_lista_1[::-1].reverse() # Doble negación, no se invierte.

#insert
mi_lista_1.insert(2, "texto") # Agrega información en la posición indicada, sin eliminar la que ya se encuentra ahí

#pop
mi_lista_1.pop(2)

#sort
mi_lista_1.pop(3)
mi_lista_1.sort()

#copy
#map
#len
#
# #del


### Índices, otra vez!!
#[inicio:(fin - 1):salto]
x = [1, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1]
x[::] #todos los elementos
x[1::] #del elemento 1 al len(x) - 1
x[1:len(x):] #del elemento 1 al len(x) - 1

x[len(x) - 1] #último elemento
x[-1] #último elemento
x[len(x) - 1 :]

### for en listas