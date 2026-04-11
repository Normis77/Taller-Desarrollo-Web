from flask import Flask, render_template

# 1. Creamos la aplicación
app = Flask(__name__)
# 2. Definimos la ruta principal
@app.route('/')

# 3. Creamos la función que se ejecutará al acceder a la ruta principal
def inicio():
    # Datos de ejemplo para pasar a la plantilla anotados e un diccionario
    datos_usuario = {
        "nombre": "Estudiante",
        "curso": "Lenguajes"
    }
    # tareas para mostrar en la plantilla anotados en una lista
    tareas = ["Configurar Flask", "Crear Plantillas", "Aprender Jinja2"]
    
    # render_template busca el archivo en la carpeta /templates automáticamente
    # Pasa las variables para que Jinja2 las use en el HTML
    return render_template('index.html', usuario=datos_usuario, lista_tareas=tareas)

# 4. Iniciamos el servidor en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)

    # NOTA
    # Para ejecutar la aplicación, asegúrate de tener Flask instalado y luego ejecuta este script.
    # Ejecuta el comando: python app.py en la terminal, asegúrate de estar en el directorio correcto donde se encuentra este archivo
    # # Luego, abre tu navegador y ve a a la dirección dada

#En el código:
    # Para este caso la ruta es: @app.route('/')
    # y la vista es: def inicio():