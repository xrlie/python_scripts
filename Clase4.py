### Continuación Clase 3

### for en listas
for i in range(10) :
    print(i)

lista_con_for = [i *100 for i in range(100)]

### if en listas
i = 100
[i for i in range(100) if i % 2 == 0] # obtener pares
# not, !=
[i for i in range(100) if not i % 2 == 0] # obtener impares
[i for i in range(100) if i % 2 != 0]     # obtener impares

### else en listas
x = [i if i % 2 == 0 else "No es par" for i in range(100) ]

### for usando listas
# a la lista anterior sumarle 1 a los números enteros
[i + 1 for i in x if isinstance(i,int)]
[i + 1 for i in x if i % 2 == 0] # error por tratar de usar módulo con un str
[x[i] + 1 for i in range(len(x)) if i % 2 == 0]

[i + 1 if isinstance(i, int) else x[i] for i in x] #error
[i + 1 if isinstance(i, int) else i for i in x]
[i if isinstance(i, int) else i + 1 for i in x]
[i if isinstance(i, int) else x[i] + 1 for i in x]