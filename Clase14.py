# Dates
import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.weekday())
print(x.strftime('%A'))

dir(x)
help(x)

print(f'{str(x.year)[2:4]}/{x.month}')

type(x)
x.strftime('%y/%m')
x.strftime('%Y/%m')
x.strftime('%Y/%b')

### Crear objeto datetime
import datetime

x = datetime.datetime(2020, 5, 17, 14, 30,12)
y = datetime.datetime(2020, 5, 18, 14, 30,12)
delta = y - x
y + delta
print(x)

### Referencias
# Para más detalle del strftime
# https://www.w3schools.com/python/python_datetime.asp
# https://docs.python.org/es/3/library/datetime.html

### Math
import math
math.ceil(3.00001)
math.floor(3.99999)
math.trunc(3.99999)
x = 10
y = -10
x + y
y = math.copysign(y, x)
y
x + y

def division(x, y):
    resultado = x / y if y != 0 else math.inf
    return(resultado)

### JSON

import json
json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
json.loads('["llave1", {"llave2":["test", null, 1.0, 2]}]')

### Abrir archivos
# archivo-salida.py
f = open ('holamundo.txt', 'wt') ### Importante ver wb
f.write('Hola Mundo')
f.close

f = open('test.json', 'r')
datos_json = json.load(f)
datos_json
f.close()

f = open('holamundo.txt', 'r')
mensaje = f.read()
f.close()
print(mensaje)

f = open('holamundo.txt', 'a')
f.write('\n' + 'Hola Mundo')
f.close()

f = open('test.json', 'wt')
f.write(json.dumps(datos_json, indent=4))
f.close

diccionario_nuevo = {
    "manzana": 12,
    "product1": 12
}

f = open('test.json', "a")
f.write("\n" + json.dumps(diccionario_nuevo, indent=4))
f.close

### Ejercicio para actualizar

json_temp = {
    "manzana": 12,
    "mango": 13
}

json.dumps(json_temp)

f = open("test.json", "wt")
f.write(json.dumps(json_temp, indent=4))
f.close()

f = open("test.json", 'a')
f.write(json.dumps({'pera':11}, indent=4))
f.close

f = open("test.json", "r")
var_temp_json = f.read()
f.close

json_temp = json.loads(var_temp_json)
json_temp.append({"pera": 11})
# json_temp.expent('pera': 11)
json_temp

f = open("test.json", "wt")
f.write(json.dumps({'pera':11}, indent=4))
f.close

### Ejercicio
x = datetime.datetime(2021, 2, 17, 30, 12)
x = datetime.datetime.now()
x
import pickle
f = open("fecha_actual.pkl", "wb")
pickle.dump(x, f)
f.close()

f = open("fecha_actual.pkl", "rb")
x_load = pickle.load(f)
f.close()
x_load