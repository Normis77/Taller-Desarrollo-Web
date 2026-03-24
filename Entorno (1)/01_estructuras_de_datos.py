# =============================================================================
# 01 - Estructuras de datos
# Listas, tuplas, sets y diccionarios: operaciones comunes y patrones utiles.
# =============================================================================


# -----------------------------------------------------------------------------
# LISTAS
# Ordenadas, mutables, permiten duplicados.
# -----------------------------------------------------------------------------

frutas = ["manzana", "banana", "cereza", "banana"]

frutas.append("mango")          # agregar al final
frutas.insert(1, "uva")         # insertar en posicion
frutas.remove("banana")         # elimina la primera ocurrencia
ultimo = frutas.pop()           # elimina y retorna el ultimo elemento

print(frutas)
print(f"Largo: {len(frutas)}")
print(f"Conteo de 'banana': {frutas.count('banana')}")

# Slicing: lista[inicio:fin:paso]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[2:7])     # [2, 3, 4, 5, 6]
print(numeros[::2])     # pares: [0, 2, 4, 6, 8]
print(numeros[::-1])    # invertida

# sorted() retorna una lista nueva; .sort() modifica en lugar
nombres = ["Carlos", "Ana", "Beatriz"]
print(sorted(nombres))              # orden alfabetico
print(sorted(nombres, reverse=True))


# -----------------------------------------------------------------------------
# TUPLAS
# Ordenadas, inmutables. Utiles para datos que no deben cambiar.
# -----------------------------------------------------------------------------

coordenada = (40.7128, -74.0060)    # latitud, longitud
lat, lon = coordenada               # desempaquetado

# Las tuplas de un solo elemento necesitan la coma
un_elemento = (42,)

# Desempaquetado con *
primero, *resto = (1, 2, 3, 4, 5)
print(primero)  # 1
print(resto)    # [2, 3, 4, 5]


# -----------------------------------------------------------------------------
# SETS
# No ordenados, sin duplicados. Utiles para membresía y operaciones de conjuntos.
# -----------------------------------------------------------------------------

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a & b)    # interseccion: {3, 4, 5}
print(a | b)    # union: {1, 2, 3, 4, 5, 6, 7}
print(a - b)    # diferencia: {1, 2}
print(a ^ b)    # diferencia simetrica: {1, 2, 6, 7}

# Caso practico: eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4]
sin_duplicados = list(set(lista_con_duplicados))
print(sin_duplicados)


# -----------------------------------------------------------------------------
# DICCIONARIOS
# Pares clave-valor. Desde Python 3.7 mantienen el orden de insercion.
# -----------------------------------------------------------------------------

persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso seguro con .get() evita KeyError
print(persona.get("nombre"))
print(persona.get("telefono", "no disponible"))  # valor por defecto

# Agregar o modificar
persona["email"] = "ana@ejemplo.com"
persona["edad"] = 31

# Iterar
for clave, valor in persona.items():
    print(f"  {clave}: {valor}")

# Metodos utiles
print(list(persona.keys()))
print(list(persona.values()))

# Fusionar diccionarios (Python 3.9+)
extra = {"pais": "España", "activo": True}
completo = persona | extra
print(completo)

# Diccionario por comprension
cuadrados = {n: n**2 for n in range(1, 6)}
print(cuadrados)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# -----------------------------------------------------------------------------
# PATRONES COMUNES
# -----------------------------------------------------------------------------

# Contar ocurrencias con un diccionario
texto = "abracadabra"
conteo = {}
for letra in texto:
    conteo[letra] = conteo.get(letra, 0) + 1
print(conteo)

# Lo mismo con collections.Counter
from collections import Counter
print(Counter(texto))

# defaultdict: evita tener que inicializar llaves
from collections import defaultdict

grupos = defaultdict(list)
datos = [("rojo", 1), ("azul", 2), ("rojo", 3), ("azul", 4)]
for color, valor in datos:
    grupos[color].append(valor)
print(dict(grupos))  # {'rojo': [1, 3], 'azul': [2, 4]}
