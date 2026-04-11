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
    
    # EL CAMBIO ESTÁ AQUÍ: Le damos el nombre exacto a la base de datos
    db = client['mi_base_de_datos'] 
    
    # Seleccionamos una colección (como una "tabla")
    usuarios_coleccion = db['usuarios']
    
    print("¡Conexión exitosa a MongoDB Atlas!")
except Exception as e:
    print(f"Error al conectar: {e}")

# --- RUTAS DE TU SERVIDOR ---

@app.route('/')
def inicio():
    return "<h1>¡Tu servidor Flask está vivo!</h1> <p>Ve a http://127.0.0.1:5000/crear-usuario para probar la base de datos.</p>"

@app.route('/crear-usuario')
def crear_usuario():
    try:
        # Creamos un dato de prueba
        nuevo_usuario = {"nombre": "Miguel", "rol": "Programador Master"}
        
        # Lo guardamos en la nube!
        resultado = usuarios_coleccion.insert_one(nuevo_usuario)
        
        return jsonify({
            "status": "Exito",
            "mensaje": "¡Dato guardado en Atlas!",
            "id_mongo": str(resultado.inserted_id)
        })
    except Exception as e:
        return jsonify({"status": "Error", "detalle": str(e)}), 500

# 4. Arrancar el servidor
if __name__ == '__main__':
    app.run(debug=True)