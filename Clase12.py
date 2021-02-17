class Poderosa(object):
    def __init__(self, tamanio = 10):
        self.tamanio = tamanio
    def __len__(self):
        print(f'tamaño {self.tamanio}')
    def __floordiv__(self, objeto2:Poderosa) -> int :
        if isinstance(objeto2, Poderosa):
            return(self.tamanio // objeto2.tamanio)
        else:
            print('La comparación tiene que hacerse con objetos de la clase Poderosa')
            return None

poderosa = Poderosa()
len(poderosa)
poderosa1 = Poderosa()
poderosa1.__floordiv__(poderosa)
poderosa1 // poderosa
poderosa1 // 1
poderosa1.__floordiv__(1)
### Operadores Binarios

### Crear la clase hogar, crearle por lo menos 3 métodos
### y tres atributos. Considera adicionalmente el atributo
### número de cuartos y el de superficie en m2

class Hogar(object):
    def __init__(self, n_rooms, m_squared, address):
        self.n_rooms = n_rooms
        self.m_squared = m_squared
        self.address = address
    def __len__(self):
        return(self.m_squared)
    def __add__(self, object2:Hogar) -> int:
        if isinstance(object2, Hogar) :
            return(self.n_rooms + object2.n_rooms)
        else:
            print('La comparación tiene que hacerse con objetos de la clase Poderosa')
            return None
    def show_address(self):
        print(f'La dirección es: {self.address}')


### Crear la clase Departamentos que hereda la clase hogar
### crearle por lo menos 3 métodos y atrubutos

class Departamento(Hogar):
    def __init__(self, n_rooms, m_squared, address, floor, price, balcony):
        super().__init__(n_rooms, m_squared, address)
        self.floor = floor
        self.price = price
        self.balcony = balcony
    def show_floor(self):
        print(f'El depa está en el piso {self.floor}')
    def show_price(self):
        print(self.price)
    def show_balcony(self):
        if self.balcony == True :
            print('El depa SI tiene balcón')
        else : 
            print('El depa NO tiene balcón')

### Utilizar __add__ en hogar que sume los cuartos de la casa o un departamento
### Utilizar __len__ para devolver las dimensiones de la casa o del depa

mi_casa = Hogar(3, 300,'Av. Madero, número 256, entre Morelos y Quevedo, colonia Buenos días')
mi_depa = Departamento(1, 90,'Av. Constitución, número 116, entre Benemérito y América, colonia Hola mundo', 6, 9000, False)
mi_casa.__len__()
mi_depa.__len__()
mi_casa + mi_depa
### Buscar la representación oficial de un string


### try

### else

### Ejercicios
#1
try:
    resultado = 10/0
except ZeroDivisionError:
    print('No se puede dividir entre cero')

#2
lista = [1, 2, 3, 4, 5]
try: 
    lista[10]
except IndexError:
    print('El índice que utilizó no existe')

#3
colores = {'rojo': red, 'verde': green, 'negro': black}
colores['blanco']

#4
resultado = 15 + '20'

error = True
try:
    x = 1
    x = x / 0
    error = False
except ZeroDivisionError:
    print('División entre cero')
else:
    x = x ** 2
finally:
    if error
        del x
    print('Siempre se ejecuta esto')


### Creación de paquetes, Python es poderoso por sus paquetes
### Organizar código
### Reutilizar código

### Calculadora
