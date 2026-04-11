### Guía para principiantes: Flask + MongoDB Atlas



---

##  ¿Qué necesitas antes de empezar?

- Python instalado en tu computadora
- Una cuenta en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (es gratis)

---

##  PASO 1 — Preparar tu entorno de trabajo

Antes de escribir código, necesitamos crear un "espacio limpio" para nuestro proyecto. Esto se llama **entorno virtual** y sirve para que las librerías que instalemos no se mezclen con otros proyectos.

Abre tu terminal (Git Bash, PowerShell o CMD) y ejecuta estos comandos **uno por uno**:

```bash
# 1. Crear el entorno virtual
python -m venv venv

# 2. Activarlo
source venv/Scripts/activate
```

>  **¿Cómo sé que funcionó?** Verás que tu terminal ahora muestra `(venv)` al inicio. ¡Eso significa que el entorno está activo!

```bash
# 3. Instalar las librerías necesarias
pip install flask pymongo python-dotenv
```

Esto descargará automáticamente todo lo que necesitamos. Verás cómo se va descargando cada paquete.

![Instalación del entorno virtual y librerías](imagenes/1.png)

Una vez terminado, puedes verificar que todo quedó instalado con:

```bash
pip list
```

Deberías ver una lista con **Flask**, **pymongo** y **python-dotenv** entre otros.

![Lista de paquetes instalados](imagenes/2.png)

---

##  PASO 2 — Crear tu base de datos en la nube (MongoDB Atlas)

MongoDB Atlas es como un "Google Drive para datos". Es un servicio gratuito donde tu base de datos vive en internet para que puedas acceder a ella desde cualquier lugar.

### 2.1 Elegir el plan gratuito

Cuando creas un nuevo cluster, verás tres opciones. **Selecciona "Free"** (es el que tiene el círculo azul en la imagen).

- M10: De pago ($0.08/hora)
- Flex: De pago (desde $0.011/hora)
- **Free: ¡Gratis para siempre! ** ← Este es el que queremos

![Selección del plan gratuito en MongoDB Atlas](imagenes/3.png)

### 2.2 Configurar el cluster

Dale un nombre a tu cluster (por defecto es `Cluster0`, puedes dejarlo así) y elige el proveedor de nube. Para empezar, **AWS en N. Virginia** está perfecto.

![Configuración del nombre y proveedor del cluster](imagenes/4.png)

Luego haz clic en **"Create Deployment"**.

### 2.3 Configurar la seguridad — Crear tu usuario de base de datos

Aparecerá un panel para configurar la seguridad. Aquí hay dos pasos importantes:

**Paso 1:** Tu IP ya fue agregada automáticamente 

**Paso 2:** Crear un usuario para la base de datos. Escribe un **nombre de usuario** y una **contraseña** que puedas recordar. Luego haz clic en **"Create Database User"**.

>  **¡MUY IMPORTANTE!** Guarda esta contraseña en un lugar seguro. La necesitarás en el siguiente paso y **no la podrás ver de nuevo**.

![Creación del usuario de base de datos](imagenes/5.png)

Una vez creado el usuario, verás una palomita verde que confirma que todo está listo. Haz clic en **"Choose a connection method"**.

![Usuario creado exitosamente](imagenes/6.png)

### 2.4 Elegir cómo conectarte

Verás varias opciones de conexión. Selecciona **"Drivers"** (la primera opción), ya que vamos a conectarnos desde Python.

![Opciones de método de conexión](imagenes/7.png)

### 2.5 Obtener tu cadena de conexión

Asegúrate de que el driver seleccionado sea **Python** y la versión **3.12 or later**. Luego busca la **cadena de conexión** que se ve así:

```
mongodb+srv://TU_USUARIO:TU_CONTRASEÑA@cluster0.xxxxxxx.mongodb.net/?appName=Cluster0
```

**Copia esa cadena**, la usaremos en el siguiente paso.

![Cadena de conexión de MongoDB](imagenes/8.png)

### 2.6 Tu cluster está listo 

Regresa a la pantalla principal y verás tu **Cluster0** funcionando. El punto verde significa que está activo y listo para recibir datos.

![Cluster activo en MongoDB Atlas](imagenes/9.png)

### 2.7 (Opcional) Explorar la base de datos de ejemplo

Atlas viene con una base de datos de películas de ejemplo (`sample_mflix`). Puedes verla haciendo clic en **"Browse Collections"**. Sirve para practicar consultas.

![Explorador de colecciones en Atlas](imagenes/10.png)

---

##  PASO 3 — Crear los archivos de tu proyecto

En la carpeta de tu proyecto, crea estos **dos archivos**:

### Archivo 1: `.env` (el archivo de secretos)

Este archivo guarda información sensible como contraseñas. **Nunca lo subas a GitHub**.

Crea un archivo llamado `.env` y escribe:

```
MONGO_URI=mongodb+srv://TU_USUARIO:TU_CONTRASEÑA@cluster0.xxxxxxx.mongodb.net/?appName=Cluster0
```

>  Reemplaza `TU_USUARIO`, `TU_CONTRASEÑA` y la parte de `cluster0.xxxxxxx` con los datos reales que copiaste en el paso 2.5.

### Archivo 2: `app.py` (el servidor)

Crea un archivo llamado `app.py` con el siguiente código:

```python
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
    # Conectar al Cluster0
    client = MongoClient(MONGO_URI)
    
    # Seleccionar (o crear) una base de datos llamada 'mi_base_de_datos'
    db = client['mi_base_de_datos'] 
    
    # Seleccionar (o crear) una colección llamada 'usuarios'
    # Una colección es como una "tabla" en bases de datos tradicionales
    usuarios_coleccion = db['usuarios']
    
    print("¡Conexión exitosa a MongoDB Atlas!")
except Exception as e:
    print(f"Error al conectar: {e}")

# --- RUTAS DE TU SERVIDOR ---

@app.route('/')
def inicio():
    return "<h1>¡Tu servidor Flask está vivo!</h1><p>Ve a http://127.0.0.1:5000/crear-usuario para probar la base de datos.</p>"

@app.route('/crear-usuario')
def crear_usuario():
    try:
        # Creamos un dato de prueba
        nuevo_usuario = {"nombre": "Miguel", "rol": "Programador Master"}
        
        # Lo guardamos en la nube
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
```

### ¿Cómo debería verse tu carpeta?

```
mi-proyecto/
├── venv/               ← El entorno virtual (se crea solo)
├── imagenes/           ← Tus capturas de pantalla
├── app.py              ← Tu servidor 
├── .env                ← Tus contraseñas secretas 
└── manual.md           ← Esta guía 
```

---

##  PASO 4 — ¡Encender el servidor!

Con el entorno virtual activo (`(venv)` visible en la terminal), ejecuta:

```bash
python app.py
```

Si todo salió bien, verás algo así en la terminal:

![Servidor Flask corriendo con conexión exitosa](imagenes/11.png)

Los mensajes importantes son:
- ` ¡Conexión exitosa a MongoDB Atlas!` → Tu app se conectó a la nube
- `* Running on http://127.0.0.1:5000` → Tu servidor está encendido

> Para **detener** el servidor en cualquier momento, presiona `Ctrl + C`.

---

##  PASO 5 — Probar que todo funciona

Abre tu navegador y visita estas dos direcciones:

### Dirección 1: `http://127.0.0.1:5000`

Deberías ver el mensaje de bienvenida de tu servidor.

![Página principal del servidor Flask](imagenes/12.png)

### Dirección 2: `http://127.0.0.1:5000/crear-usuario`

Esta ruta crea un usuario de prueba y lo guarda en MongoDB Atlas. Deberías ver una respuesta en formato JSON como esta:

![Respuesta JSON al crear un usuario](imagenes/13.png)

Eso significa que el dato fue guardado exitosamente en la nube. ¡Felicitaciones! 🎉

---

##  PASO 6 — Verificar los datos en Atlas

Regresa a [cloud.mongodb.com](https://cloud.mongodb.com), ve a **Data Explorer** en el menú izquierdo, y navega hasta:

`Cluster0 → mi_base_de_datos → usuarios`

Ahí verás los documentos que guardaste desde tu aplicación. Cada vez que visites `/crear-usuario`, se agrega uno nuevo.

![Datos guardados visibles en MongoDB Atlas](imagenes/14.png)

---

##  Glosario rápido

| Término | ¿Qué significa en simple? |
|---|---|
| **Servidor** | Un programa que "escucha" y responde peticiones |
| **Flask** | La librería de Python que nos ayuda a crear servidores fácilmente |
| **MongoDB** | Una base de datos que guarda la info como objetos JSON |
| **Atlas** | La versión en la nube de MongoDB (gratis para empezar) |
| **Cluster** | El "contenedor" donde viven todas tus bases de datos en Atlas |
| **Colección** | Como una "tabla", es un grupo de documentos relacionados |
| **Documento** | Un registro individual de datos (como una fila en Excel) |
| **`.env`** | Archivo que guarda contraseñas y configuraciones secretas |
| **Entorno virtual** | Un espacio aislado para que las librerías de un proyecto no afecten a otros |

---

## Problemas comunes

**❌ "ModuleNotFoundError: No module named 'flask'"**
→ Asegúrate de tener el entorno virtual activo. Debes ver `(venv)` en tu terminal.

**❌ "Error al conectar" al iniciar el servidor**
→ Revisa que tu archivo `.env` tenga la URI correcta, sin espacios extra.

**❌ La página no carga en el navegador**
→ Verifica que el servidor esté corriendo (debes ver `Running on http://127.0.0.1:5000` en la terminal).

**❌ "IP not allowed"**
→ Ve a MongoDB Atlas → Network Access y agrega tu IP actual o usa `0.0.0.0/0` para permitir cualquier IP (solo para desarrollo).

---


