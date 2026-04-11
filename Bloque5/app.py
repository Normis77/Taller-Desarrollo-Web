# Importamos Flask: el framework que crea el servidor web.
# render_template: para dibujar las páginas HTML.
# request: para capturar lo que el usuario escribe en los formularios.
# redirect/url_for: para movernos entre las páginas de la aplicación.
from flask import Flask, render_template, request, redirect, url_for

# MongoClient: el conector oficial de Python para bases de datos MongoDB.
from pymongo import MongoClient

# ObjectId: MongoDB usa IDs especiales. 
# Esta herramienta traduce esos IDs para poder buscar o borrar componentes específicos.
from bson.objectid import ObjectId

# Inicializamos la aplicación Flask
app = Flask(__name__)

# ---------------------------------------------------------
# 1. CONEXIÓN A LA NUBE 
# ---------------------------------------------------------
# Esta URI es la "llave" de acceso a nuestra base de datos en la nube.
MONGO_URI = "mongodb+srv://admin_taller:PasswordTaller1@laboratoriodb.6u0rlwx.mongodb.net/?appName=LaboratorioDB"

# Creamos el cliente que mantendrá la comunicación con Atlas
client = MongoClient(MONGO_URI)

# Seleccionamos la Base de Datos 'LaboratorioDB' y la Colección 'componentes'
# Si no existen, MongoDB las creará automáticamente al insertar el primer dato.
db = client['LaboratorioDB']
coleccion = db['componentes']

# ---------------------------------------------------------
# RUTA: CATÁLOGO 
# ---------------------------------------------------------
@app.route('/')
def catalogo():
    # .distinct("categoria") obtiene una lista de todas las categorías registradas sin repetirlas .
    categorias_disponibles = coleccion.distinct("categoria")
    
    # Capturamos si el usuario seleccionó una categoría en el menú desplegable
    categoria_seleccionada = request.args.get('categoria')
    
    # Creamos un filtro vacío (traer todo)
    query = {}
    if categoria_seleccionada and categoria_seleccionada != "Todas":
        # Si eligió una, filtramos la búsqueda por esa categoría
        query = {"categoria": categoria_seleccionada}
    
    # Realizamos la búsqueda en la nube
    # Convertimos el resultado a una lista de Python para que el HTML pueda leerla.
    mis_componentes = list(coleccion.find(query).sort("nombre", 1))
    
    # Enviamos los datos a 'catalogo.html' para que se dibujen las tarjetas.
    return render_template('catalogo.html', 
                           lista=mis_componentes, 
                           categorias=categorias_disponibles,
                           seleccionada=categoria_seleccionada)

# ---------------------------------------------------------
# RUTA: VISTA DE REGISTRO 
# ---------------------------------------------------------
@app.route('/registro')
def registro():
    # Esta ruta simplemente muestra el formulario de ingreso.
    return render_template('registro.html')

# ---------------------------------------------------------
# OPERACIÓN: CREATE
# ---------------------------------------------------------
@app.route('/agregar', methods=['POST'])
def agregar():
    # Convertimos los valores de texto a números enteros para cálculos matemáticos.
    total = int(request.form['cantidad_total'])
    en_uso = int(request.form.get('en_uso', 0))
    
    # Creamos un 'Diccionario' con la estructura técnica del componente.
    # Usamos .upper() para estandarizar las categorías en mayúsculas.
    nuevo_item = {
        "nombre": request.form['nombre'],
        "categoria": request.form['categoria'].upper(),
        "subcategoria": request.form.get('subcategoria', '').upper(),
        "cantidad_total": total,
        "en_uso": en_uso,
        "disponibles": total - en_uso, 
        "especificaciones": request.form.get('especificaciones', ''),
        "imagen": request.form['imagen'],
        "datasheet": request.form.get('datasheet', '') 
    }
    
    # Ordenamos a MongoDB insertar este nuevo documento.
    coleccion.insert_one(nuevo_item)
    
    # Redirigimos al catálogo para confirmar visualmente el ingreso.
    return redirect(url_for('catalogo'))

# ---------------------------------------------------------
# OPERACIÓN: UPDATE
# ---------------------------------------------------------
@app.route('/editar/<id_item>', methods=['POST'])
def editar(id_item):
    # Capturamos los nuevos valores desde la tarjeta del catálogo.
    total = int(request.form['cantidad_total'])
    en_uso = int(request.form['en_uso'])
    
    # Actualizamos el documento que coincida con el ID único.
    # $set: indica a MongoDB que solo cambie estos campos específicos.
    coleccion.update_one(
        {"_id": ObjectId(id_item)}, 
        {"$set": {
            "cantidad_total": total,
            "en_uso": en_uso,
            "disponibles": total - en_uso
        }}
    )
    return redirect(url_for('catalogo'))

# ---------------------------------------------------------
# OPERACIÓN: DELETE
# ---------------------------------------------------------
@app.route('/eliminar/<id_item>')
def eliminar(id_item):
    # Buscamos por el ID único y lo removemos permanentemente de la colección.
    coleccion.delete_one({"_id": ObjectId(id_item)})
    
    # Regresamos al catálogo actualizado.
    return redirect(url_for('catalogo'))

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # debug=True permite ver errores en tiempo real y reinicia el servidor al guardar cambios.
    app.run(debug=True)