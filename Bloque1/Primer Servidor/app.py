from flask import Flask

# 1. Creamos la aplicación
app = Flask(__name__)

# 2. Definimos la ruta principal
# Esto significa que cuando alguien ingrese a /, se ejecutará la función hola_mundo
@app.route('/')

# 3. Creamos la función que se ejecutará cuando accedamos a la ruta principal
def hola_mundo():
    # Devolvemos un mensaje en formato HTML
    return "<h1>¡Hola Mundo! Este es mi primer servidor con Python </h1>"

# 4. Iniciamos el servidor
if __name__ == '__main__':
    app.run(debug=True)
    #debug=True hace que el servidor se reinicie automáticamente cada vez que hagamos cambios en el código.

    # NOTA
    # Para poder utilizar el framework Flask, es necesario tenerlo instaldo
    # Se puede instalar utilizando "pin install flask" en la terminal.

    # Para ejecutar el servidor, simplemente ejecutamos este archivo con "python app.py" en la terminal. 
    # Toma en cuenta que debes estar en el directorio donde se encuentre tu archivo app.py   

