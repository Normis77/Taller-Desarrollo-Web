import os
from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

# 1. Cargar la "llave" secreta desde el archivo .env
load_dotenv()

# 2. Inicializar el servidor Flask
app = Flask(__name__)

# 3. Configurar la conexión a MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")

try:
    # conectar al Cluster0
    client = MongoClient(MONGO_URI)
    
    # Seleccionamos la base de datos
    db = client['mi_base_de_datos'] 
    
    # Seleccionamos una colección (como una "tabla")
    usuarios_coleccion = db['usuarios']
    
    print("¡Conexión exitosa a MongoDB Atlas!")
except Exception as e:
    print(f"Error al conectar: {e}")

# --- RUTAS DE TU SERVIDOR (CRUD) ---

# Menú principal
@app.route('/')
def inicio():
    return """
    <h1>¡Tu CRUD en Flask está vivo! </h1> 
    <p>Haz clic en los enlaces para probar cada método en la base de datos:</p>
    <ul>
        <li><b>Crear:</b> <a href='/crear-usuario'>Agregar a "Ana" a la base de datos</a></li>
        <li><b>Leer:</b> <a href='/leer-usuarios'>Ver todos los usuarios guardados</a></li>
        <li><b>Actualizar:</b> <a href='/actualizar-usuario'>Ascender a "Miguel" a Jefe</a></li>
        <li><b>Borrar:</b> <a href='/borrar-usuario'>Eliminar a "Ana"</a></li>
    </ul>
    """

# CREATE (Crear un nuevo dato)
@app.route('/crear-usuario')
def crear_usuario():
    try:
        nuevo_usuario = {"nombre": "Ana", "rol": "Diseñadora"}
        resultado = usuarios_coleccion.insert_one(nuevo_usuario)
        
        return jsonify({
            "status": "Exito", 
            "mensaje": "¡Usuario Ana creado y guardado en la nube!", 
            "id_mongo": str(resultado.inserted_id)
        })
    except Exception as e:
        return jsonify({"status": "Error", "detalle": str(e)}), 500


# READ (Leer los datos)
@app.route('/leer-usuarios')
def leer_usuarios():
    try:
        # find() busca todos los documentos. Lo guardamos en una lista.
        usuarios_cursor = usuarios_coleccion.find()
        lista_usuarios = []
        
        for usuario in usuarios_cursor:
            # Convertimos el ID especial de Mongo a texto normal
            usuario['_id'] = str(usuario['_id'])
            lista_usuarios.append(usuario)
            
        return jsonify({
            "status": "Exito", 
            "total_usuarios": len(lista_usuarios), 
            "datos": lista_usuarios
        })
    except Exception as e:
        return jsonify({"status": "Error", "detalle": str(e)}), 500


# UPDATE (Actualizar un dato)
@app.route('/actualizar-usuario')
def actualizar_usuario():
    try:
        # 1. ¿A quién buscamos?
        filtro = {"nombre": "Miguel"} 
        # 2. ¿Qué le cambiamos?
        nuevos_datos = {"$set": {"rol": "Jefe de Programación"}} 
        
        resultado = usuarios_coleccion.update_one(filtro, nuevos_datos)
        
        if resultado.modified_count > 0:
            return jsonify({"status": "Exito", "mensaje": "¡Miguel fue actualizado a Jefe!"})
        else:
            return jsonify({"status": "Aviso", "mensaje": "No se hicieron cambios (quizás Miguel ya era Jefe o no existe)."})
    except Exception as e:
        return jsonify({"status": "Error", "detalle": str(e)}), 500


# DELETE (Borrar un dato)
@app.route('/borrar-usuario')
def borrar_usuario():
    try:
        # Buscamos y borramos a Ana
        resultado = usuarios_coleccion.delete_one({"nombre": "Ana"})
        
        if resultado.deleted_count > 0:
            return jsonify({"status": "Exito", "mensaje": "El usuario Ana fue eliminado para siempre."})
        else:
            return jsonify({"status": "Aviso", "mensaje": "No se encontró a Ana para borrarla."})
    except Exception as e:
        return jsonify({"status": "Error", "detalle": str(e)}), 500

# 4. Arrancar el servidor
if __name__ == '__main__':
    app.run(debug=True)