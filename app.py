from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
diccionario = {1: { "nombre": "Rally MTB 2025",
                    "organizador": "Club Social y Deportivo Unidos por el Deporte",
                    "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km …",
                    "fecha": "24 de Octubre de 2025",                        "horario": "8am",
                    "lugar": "Tandil, Buenos Aires",
                    "tipo_carrera": "MTB rural",
                    "modalidad_costo": {1: {"nombre": "Corta" ,"valor": "100"},
                2: {"nombre": "Larga" ,"valor": "200"}},
                    "Auspiciantes": ["ausp1","auspN"]}
                }

    
@app.route('/')
def index():
    return render_template('index.html', datos=diccionario)
def ir_registro():
    return redirect(url_for('registro'))
def ir_index():
    return redirect(url_for('index'))

@app.route("/registro")
def registration():
    return render_template('registro.html')
                           
if __name__ == '__main__':
    app.run(debug=True)
