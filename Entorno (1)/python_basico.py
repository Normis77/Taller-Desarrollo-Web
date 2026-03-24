# =============================================================================
# 00 - Lo basico de Python
# Variables, tipos de dato, operadores, condicionales y bucles.
# Este archivo es el punto de partida. No necesitas saber nada antes de esto.
# =============================================================================


# -----------------------------------------------------------------------------
# VARIABLES
# No se declara el tipo. Python lo detecta solo.
# El nombre debe empezar con letra o _ y no puede tener espacios.
# Convencion: usar snake_case (palabras en minuscula separadas por guion bajo).
# -----------------------------------------------------------------------------

nombre = "Carlos"
edad = 25
altura = 1.78
es_estudiante = True

# Puedes ver el tipo de cualquier variable con type()
print(type(nombre))         # <class 'str'>
print(type(edad))           # <class 'int'>
print(type(altura))         # <class 'float'>
print(type(es_estudiante))  # <class 'bool'>

# Asignacion multiple en una linea
x = y = z = 0

# Desempaquetado: asignar varios valores a la vez
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Intercambiar valores sin variable temporal (tipico de Python)
a, b = b, a
print(a, b)     # 2 1


# -----------------------------------------------------------------------------
# TIPOS DE DATO PRIMITIVOS
# -----------------------------------------------------------------------------

# int: numeros enteros, sin limite de tamanio
poblacion = 8_000_000_000   # el guion bajo es solo visual, no afecta el valor

# float: numeros con decimales
pi = 3.14159
precio = 19.99

# str: cadenas de texto, con comillas simples o dobles, equivalentes
saludo = "Hola"
despedida = 'Adios'

# Las cadenas multilínea usan triple comilla
parrafo = """
Esta es una cadena
que ocupa varias lineas.
"""

# bool: True o False (con mayuscula)
activo = True
eliminado = False

# None: representa la ausencia de valor (como null en otros lenguajes)
resultado = None
print(resultado)        # None
print(type(resultado))  # <class 'NoneType'>


# -----------------------------------------------------------------------------
# STRINGS: OPERACIONES COMUNES
# -----------------------------------------------------------------------------

mensaje = "  Hola, Mundo!  "

print(len(mensaje))             # largo incluyendo espacios
print(mensaje.strip())          # quitar espacios al inicio y al final
print(mensaje.lower())          # todo en minusculas
print(mensaje.upper())          # todo en mayusculas
print(mensaje.replace("Mundo", "Python"))
print("Hola" in mensaje)        # True - verificar si contiene una subcadena

# Formateo con f-strings (la forma recomendada desde Python 3.6)
nombre = "Ana"
edad = 30
print(f"Me llamo {nombre} y tengo {edad} anos.")
print(f"El doble de mi edad es {edad * 2}.")   # se puede poner expresiones

# Acceder a caracteres individuales por indice (empieza en 0)
texto = "Python"
print(texto[0])     # P
print(texto[-1])    # n  (indice negativo: cuenta desde el final)
print(texto[1:4])   # yth  (slicing: desde el indice 1 hasta el 3)


# -----------------------------------------------------------------------------
# CONVERSION DE TIPOS (CASTING)
# -----------------------------------------------------------------------------

numero_str = "42"
numero_int = int(numero_str)    # str -> int
numero_flt = float(numero_str)  # str -> float
de_vuelta  = str(numero_int)    # int -> str

print(numero_int + 8)   # 50  (ya es un numero, se puede operar)

# input() siempre retorna string, hay que convertir si se necesita numero
# edad_usuario = int(input("Cuantos anos tienes? "))


# -----------------------------------------------------------------------------
# OPERADORES
# -----------------------------------------------------------------------------

# Aritmeticos
print(10 + 3)   # 13  suma
print(10 - 3)   # 7   resta
print(10 * 3)   # 30  multiplicacion
print(10 / 3)   # 3.3333...  division (siempre retorna float)
print(10 // 3)  # 3   division entera (descarta decimales)
print(10 % 3)   # 1   modulo (resto de la division)
print(10 ** 3)  # 1000 potencia

# Asignacion compuesta (atajos)
contador = 0
contador += 1   # equivale a: contador = contador + 1
contador -= 1
contador *= 2
contador //= 1

# Comparacion: siempre retornan True o False
print(5 == 5)   # igual
print(5 != 3)   # diferente
print(5 > 3)    # mayor que
print(5 < 3)    # menor que
print(5 >= 5)   # mayor o igual
print(5 <= 4)   # menor o igual

# Logicos
print(True and False)   # False - ambos deben ser True
print(True or False)    # True  - al menos uno debe ser True
print(not True)         # False - niega el valor

# Caso practico: combinar comparaciones
x = 15
print(x > 10 and x < 20)   # True (x esta entre 10 y 20)
print(10 < x < 20)          # True (forma mas pythonica de escribir lo mismo)


# -----------------------------------------------------------------------------
# CONDICIONALES
# -----------------------------------------------------------------------------

temperatura = 28

if temperatura > 30:
    print("Hace mucho calor")
elif temperatura > 20:
    print("Temperatura agradable")
elif temperatura > 10:
    print("Un poco frio")
else:
    print("Hace frio")

# Condicional en una linea (operador ternario)
# valor_si_true  if  condicion  else  valor_si_false
estado = "mayor de edad" if edad >= 18 else "menor de edad"
print(estado)

# Truthy y Falsy: Python evalua ciertos valores como True o False
# Falsy: None, 0, 0.0, "", [], {}, set()
# Todo lo demas es Truthy

nombre = ""
if not nombre:
    print("El nombre esta vacio")   # se imprime porque "" es Falsy

lista = [1, 2, 3]
if lista:
    print("La lista tiene elementos")  # se imprime porque la lista no esta vacia


# -----------------------------------------------------------------------------
# BUCLES
# -----------------------------------------------------------------------------

# --- for: iterar sobre una secuencia ---

# Iterar sobre una lista
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)

# Iterar sobre un rango de numeros
# range(inicio, fin, paso) - el fin NO se incluye
for i in range(5):          # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i, end=" ")
print()

# enumerate: obtener indice y valor al mismo tiempo
frutas = ["manzana", "pera", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# zip: iterar sobre dos listas en paralelo
nombres = ["Ana", "Luis", "Maria"]
edades  = [25, 30, 22]
for nom, ed in zip(nombres, edades):
    print(f"{nom} tiene {ed} anos")

# Iterar sobre un string
for letra in "Hola":
    print(letra, end="-")
print()


# --- while: repetir mientras se cumpla una condicion ---

intentos = 0
limite = 3

while intentos < limite:
    print(f"Intento {intentos + 1}")
    intentos += 1

# Ejemplo clasico: pedir entrada hasta que sea valida
# (comentado para no bloquear la ejecucion)
# while True:
#     respuesta = input("Escribe 'si' o 'no': ").lower()
#     if respuesta in ("si", "no"):
#         break
#     print("Respuesta invalida, intenta de nuevo")


# --- break, continue y else en bucles ---

# break: salir del bucle inmediatamente
for n in range(10):
    if n == 5:
        break
    print(n, end=" ")
print()   # 0 1 2 3 4

# continue: saltar al siguiente ciclo sin ejecutar el resto
for n in range(10):
    if n % 2 == 0:
        continue    # saltar los pares
    print(n, end=" ")
print()   # 1 3 5 7 9

# else en un bucle: se ejecuta si el bucle termino SIN un break
# Es util para saber si se encontro algo o no
objetivo = 7
for n in range(5):
    if n == objetivo:
        print(f"Encontrado: {n}")
        break
else:
    print("No se encontro el objetivo")   # se imprime porque no hubo break


# -----------------------------------------------------------------------------
# BUENAS PRACTICAS BASICAS
# -----------------------------------------------------------------------------

# Nombres descriptivos: el codigo se lee mas que se escribe
# MAL:
x1 = 100
y1 = 0.16
z1 = x1 * (1 + y1)

# BIEN:
precio_base = 100
tasa_iva    = 0.16
precio_final = precio_base * (1 + tasa_iva)
print(f"Precio final: {precio_final}")

# Constantes: por convencion se escriben en MAYUSCULAS
MAX_INTENTOS = 3
PI = 3.14159
