### Pasos para crear un paquete
# 1 Crear una carpeta con el nombre del paquete
# 2 Crear un fichero con el nombre de __init__.py
# 3 Depositar tus funciones en un fichero con ese nombre

### ¿Cómo crear un subpaquete?
# 1 Crear una subcarpeta dentro de la carpeta creada anterior con el nombre del subpaquete
# 2 Crear un fichero con el nombre de __init__.py
# 3 Depositar tus funciones en un fichero con ese nombre

# TODO

# Recordemos como importar paquetes_
# import *paquete*
# import *paquete* as 'pkg'
# from *paquete* import 'function1', 'function2'
# from *paquete* import * (importa todo)

import package_python
package_python.suma(12, 13)
import package_python as pkg_py   # cambiar nombre al paquete para escribirlo más rápido.
pkg_py.suma(13, 14)
from package_python import suma   # importa únicamente las funciones que se utilizarán
suma(13, 14)
from package_python import *      # importa todo lo que esté dentro del paquete
suma(13, 14)

### Ejercicio 8
### Crear el paquete, my_python, con las siguientes funciones:
# hola_mundo() imprime "Hola Mundo"
# tipo(objeto) devuelve el tipo de objeto
# longitud(objeto) devuelve la longitud del objeto
# musica_favorita() # devuelve tu música favorita

# Probarlas
import my_python

import my_python as mp
mp.hola_mundo()

from my_python import musica_favorita
musica_favorita()
