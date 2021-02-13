### Repaso Clase 9

# Crear la clase AparatoElectronico

## Atributos
# Encendido (True, False)
# Marca
# Dimensiones
# estado_general (True, False)

## Métodos
# encender -> afecta Encendido
# descomponer -> afecta estado_general
# componer -> afecta estado_general
# apagar -> afecta Encendido

# Crear la clase Telefeno

## Atributos
# Encendido (True, False)
# Marca
# Dimensiones
# estado_general (True, False)
# estado_teclas (True, False)

## Métodos
# encender -> afecta Encendido
# descomponer -> afecta estado_general
# componer -> afecta estado_general
# apagar -> afecta Encendido
# descomponer -> afecta estado_teclas
# componer -> afecta estado_teclas

# Crear la clase Celular

## Atributos
# estado_wifi
# estado_red_gsm
# llamada = (True, False)

## Metodos
# conectar(, red = {wifi, gsm})
# desconectar(, red = {wifi, gsm})
# realizar_llamada()
# colgar()
# tomar_foto

class AparatoElectronico(object):
    def __init__(self, marca, dimensiones, encendido = True, estado_general = True):
        self.funciona = estado_general
        self.marca = marca
        self.dimensiones = dimensiones
        self.prendido = encendido
    def apagar(self):
        self.prendido = False
        print('El aparato electrónico se ha apagado')
    def encender(self):
        self.prendido = True
        print('El aparato electrónico se ha encendido')
    def descomponer(self):
        self.funciona = False
        print('El aparato electrónico se ha descompuesto')
    def componer(self):
        self.funciona = True
        print('El aparato electrónico funciona correctamente')


class Telefono(object):
    def __init__(self, marca, dimensiones, encendido = True, estado_general = True, estado_teclas = True):
        self.marca = marca
        self.dimensiones = dimensiones
        self.prendido = encendido
        self.funciona = estado_general
        self.funcionan_teclas = estado_teclas
    def apagar(self):
        self.prendido = False
        print('El teléfono ha sido apagado')
    def encender(self):
        self.prendido = True
        print('El teléfono ha sido encendido')
    def descomponer(self):
        self.funciona = False
        self.funcionan_teclas = False
        print('El teléfono y las teclas se ha descompuesto')
    def componer(self):
        self.funciona = True
        print('El teléfono funciona correctamente')
    def componer_teclas(self):
        self.funcionan_teclas = True

class Celular(object):
    def __init__(self, estado_wifi, estado_red_gsm, llamada = False):
        self.wifi = estado_wifi
        self.red = estado_red_gsm
        self.llamada = llamada
    def conectar_wifi(self):
        self.red = False
        self.wifi = True
        print('Se ha conectado al wifi correctamente')
    def usar_datos(self):
        self.wifi = False
        self.red = True
        print('Se ha conectado a la red gsm exitosamente')
    def llamar(self):
        self.llamada = True
    def colgar(self):
        self.llamada = False
    def tomar_foto(self):
        self.llamada = False

class Producto(object):
    carrito = 0
    def __init__(self, precio_inicial_sin_iva = 100, iva = 0.16):
        self.__precio_sin_iva = precio_inicial_sin_iva
        self.iva = iva
        self.__precio_con_iva = precio_inicial_sin_iva * (1 + iva)
        # self.precio_con_iva = self.precio_sin_iva * (1 + self.iva) // Otra forma de declarar la variable haciendo referencia a las variables ya existentes
        self.__calcular_totales()
    def modificar_precio(self, nuevo_precio_sin_iva):
        self.__precio_sin_iva = nuevo_precio_sin_iva
        self.__precio_con_iva = (1 + self.iva) * self.__precio_sin_iva
        self.__calcular_totales()
    def mostrar_precio_iva(self):
        print(self.__precio_con_iva)
    def comprar_una_unidad(self, unidades = 1):
        self.carrito += unidades
        self.__calcular_totales()
    def __calcular_totales(self):
        self.subtotal = self.__precio_sin_iva * self.carrito
        self.impuesto = self.subtotal * self.iva
        self.total = self.subtotal + self.impuesto
    def mostrar_totales(self):
        print(f'Has comprado {self.carrito} unidades, dando un subtotal de ${self.subtotal}, pagas de impuesto: {self.impuesto}, el total que vas a pagar es ${self.total}')

### Encapsulamiento
# Se utiliza para que un atributo no sea modificado fuera del objeto
# Se utiliza el doble guión bajo ej: __nombre_variable

producto1 = Producto(150)               # Se crea un producto de un precio sin iva de 150
print(producto1.comprar_una_unidad())   # Se compra 1 unidad de este producto
print(producto1.mostrar_totales())      # Se muestran los detalles de la compra
producto1.precio_sin_iva = 120          # Se intenta modificar el precio sin iva
producto1.calcular_totales()
print(producto1.mostrar_totales())
producto1.modificar_precio(170)

class Auto(object):
    def __init__(self):
        self.encendido = False
        self.__bombas_encendidas = False
        self.estado_general_auto = 'ok'
    def encender(self):
        self.__encender_bombas()
        self.encendido = True
    def __chequeo(self):
        pass
    def __encender_bombas(self):
        self.__bombas_encendidas = True
    def __apagar_bombas(self):
        self.__bombas_encendidas = False
    def mostrar_estado_auto(self):
        print(f'El auto se encuentra: {self.encendido}, con bombas encendidas: {self.__bombas_encendidas}, el estado general del auto es: {self.estado_general_auto}')

### Herencia
class Telefeno(AparatoElectronico):
    def __init__(self, encendido, marca, dimensiones, estado_general, estado_teclas):
        super().__init__(encendido, marca, dimensiones, estado_general) # Sobreescritura
        self.estado_teclas = estado_teclas
    def descomponer_teclas(self):
        self.estado_teclas = False
    def componer_teclas(self):
        self.estado_teclas = True
    def mostrar_estado(self):
        print(self.prendido,
            self.marca,
            self.dimensiones,
            self.funciona,
            self.estado_teclas
            )
    def mostrar_estado_anterior(self):
        super().mostrar_estado()

telefono1 = Telefeno(True, 'Sony', 'md', True, True)


### Overwriting