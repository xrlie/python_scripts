### Crear una clase lista
# Crear método append()
# Crear método extend()
# Crear método pop()

class ListaPersonalizada(object):
    def __init__(self, *valores):
        self.__lista_interna = []
        for i in valores:
            self.__lista_interna.append(i)
    def __str__(self):
        aux = "["
        for i in self.__lista_interna:
            aux += str(i) + ","
        aux += "]"
        return(aux)
    def extend(self, lista):
        for i in lista:
            self.__lista_interna.append(i)
    def append(self, lista):
        self.__lista_interna.append(lista)
    def pop(self, elemento_consultado):
        [elemento for elemento in self.__lista_interna if elemento != elemento_consultado]

lista = ListaPersonalizada(1,3,4,5,6)
print(lista)
lista.append([3,4,5,6]) # -> [1,3,4,5,6, [3,4,5,6]]
lista.extend([3,4,5,6]) # -> [1,3,4,5,6, [3,4,5,6]]
lista.pop(3)
print(lista)

### Polimorfismo

### Crear la clase diccionario
# Crear método get()
# Crear método

### Transportes
## Atributos
# Marca
# Dimensiones
# Capacidad

class Transportes(object):
    def __init__(self, marca, dimensiones, capacidad):
        self.marca = marca
        self.dimensiones = dimensiones
        self.capacidad = capacidad
    def desplazamiento(self):
        print('Se está moviendo el transporte')

### Terrestres
## Atributos
# Número de llantas
# Tipo de terreno de desplazamiento

class Terrestres(Transportes):
    def __init__(self, marca, dimensiones, capacidad, n_llantas, terreno):
        super().__init__(marca, dimensiones, capacidad)
        self.n_llantas = n_llantas
        self.terreno = terreno
    def desplazamiento(self):
        print('Se está moviendo el terrestre')

# Desplazamiento
# print('Se está moviendo ')

### Autos
# A/C
# Rin

class Autos(Terrestres):
    def __init__(self, marca, dimensiones, capacidad, n_llantas, terreno, a_c, inch_rin):
        super().__init__(marca, dimensiones, capacidad, n_llantas, terreno)
        self.a_c = a_c
        self.inch_rin = inch_rin
    def desplazamiento(self):
        print('Se está moviendo el auto')

### Motos
# Caballito
# Rebasar en corto espacio

class Motos(Terrestres):
    def __init__(self, marca, dimensiones, capacidad, n_llantas, terreno):
        super().__init__(marca, dimensiones, capacidad, n_llantas, terreno)
    def caballito(self):
        print('La moto está realizando un caballito')
    def rebasar(self):
        print('La moto está rebasando en un espacio corto')
    def desplazamiento(self):
        print('Se está moviendo el auto')

class Entero():
    def __init__(self, x):
        self.x = x
    def __add__(self, externo):
        return(self.x + externo.x)

entero1 = Entero(10)
entero2 = Entero(8)
entero1 + entero2

class Cadena():
    def __init__(self, x):
        self.x = str(x)
    def __add__(self, externo):
        return(self.x + externo.x)

cadena1 = Cadena(10)
cadena2 = Cadena(8)
cadena1 + cadena2