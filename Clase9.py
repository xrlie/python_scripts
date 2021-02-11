### Repaso de la clase 8

### Lambdas  // Funciones una sóla línea de código
suma = lambda x, y: x + y
resta = lambda x, y: x - y
division = lambda x, y: x / y if y != 0 else 'No puedes dividir entre cero'

# def suma(x, y):
#     return x + y

### Sintaxis de Clases
class Clase(object):
    pass

# Métodos
class Celular(object):
    def llamar(self):
        print('Iniciando llamada...')
    def colgar(self):
        print('Se terminó la llamada.')

mi_cel = Celular()

# Atributos
class Celular2(object):
    estado = '...en llamada...'
    marca = 'Nokia'
    def llamar(self):
        self.estado = '...en llamada...'
        print('Iniciando llamada')
    def colgar(self):
        self.estado = "en modo ahorro de energía"
        print("Se terminó la llamada")

mi_cel = Celular2()
mi_cel2 = Celular2()

# Constructor
class Celular3(object):
    def __init__(self, estado, marca):
        self.estado = estado
        self.marca = marca
    def llamar(self):
        self.estado = '...en llamada...'
        print('Iniciando llamada')
    def colgar(self):
        self.estado = "en modo ahorro de energía"
        print("Se terminó la llamada")

mi_cel = Celular3('Xiamoi', 'en modo ahorro de energía')
mi_cel2 = Celular3('Nokia', '...en llamada...')

# Self

# usar self.i como contador
class Acumulador(object):
    x = None
    def __init__(self, x = 0):
        self.x = x
    def sumar_una_unidad(self):
        self.x += 1
        return self.x
    def resta_una_unidad(self):
        self.x -= 1
    def mostrar_acumulador(self):
        print(self.x)

mi_acumulador = Acumulador()
mi_acumulador2 = Acumulador(3)

print('Mi acumulador uno es:', mi_acumulador.x)
print('Mi acumulador dos es:', mi_acumulador2.x)
print(mi_acumulador.sumar_una_unidad())
mi_acumulador.mostrar_acumulador()

# Ejercicio guiado, volver nuestro código de registro de usuarios visto en clase a la forma orientada a objetos


### Ejercicio en clase crea el objeto producto,
# a partir de diferentes métodos crea las siguientes acciones:
# Definir un precio sin iva inicial del producto                            // Done
# Modificar el precio actual del producto                                   // Done
# Mostrar precio con iva del producto                                       // Done
# Comprar un producto y agregar al carrito                                  // TODO
# Mostrar el subtotal de la cantidad de productos agregados al carrito      // TODO

class Producto(object):
    carrito = 0
    def __init__(self, precio_inicial_sin_iva = 100, iva = 0.16):
        self.precio_sin_iva = precio_inicial_sin_iva
        self.iva = iva
        self.precio_con_iva = precio_inicial_sin_iva * (1 + iva)
        # self.precio_con_iva = self.precio_sin_iva * (1 + self.iva) // Otra forma de declarar la variable haciendo referencia a las variables ya existentes
        self.calcular_totales()
    def modificar_precio(self, nuevo_precio_sin_iva):
        self.precio_sin_iva = nuevo_precio_sin_iva
        self.precio_con_iva = (1 + self.iva) * self.precio_sin_iva
        self.calcular_totales()
    def mostrar_precio_iva(self):
        print(self.precio_con_iva)
    def comprar_una_unidad(self, unidades = 1):
        self.carrito += unidades
        self.calcular_totales()
    def calcular_totales(self):
        self.subtotal = self.precio_sin_iva * self.carrito
        self.impuesto = self.subtotal * self.iva
        self.total = self.subtotal + self.impuesto
    def mostrar_totales(self):
        print(f'Has comprado {self.carrito} unidades, dando un subtotal de ${self.subtotal}, pagas de impuesto: {self.impuesto}, el total que vas a pagar es ${self.total}')

producto1 = Producto(200)
print(producto1.precio_sin_iva)
producto1.modificar_precio(150)
print(producto1.precio_sin_iva)
producto1.mostrar_precio_iva()
producto1.mostrar_totales()
producto1.comprar_una_unidad()
producto1.mostrar_totales()

