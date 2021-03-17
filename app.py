import os
from flask import Flask, render_template, request,send_from_directory
from werkzeug.utils import secure_filename 

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './files'


@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['archivo']
  filename = secure_filename(f.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # Retornamos una respuesta satisfactoria
  return "<h1>Archivo subido exitosamente</h1>"

@app.route("/upload/<filename>")
def get_file(filename):
    x = send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    print("imprimiendo info")
    print(x)
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True, port=5000)
