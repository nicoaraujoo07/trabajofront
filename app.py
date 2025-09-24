from flask import Flask, redirect, url_for, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_DEFAULT_SENDER'] = 'practicotrabajo74@gmail.com'
app.config['MAIL_USERNAME'] = 'practicotrabajo74@gmail.com'
app.config['MAIL_PASSWORD'] = 'vsug hlcz dpin dwvn'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)

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

@app.route("/registro", methods=["GET", "POST"])
def registration():
    return render_template('registration.html')

@app.route("/enviar_correo", methods=["POST"])
def enviar_correo():
    nombre = request.form['nombre']
    email = request.form['email']
    apellido = request.form['apellido']
    dni = request.form['dni']
    enfermedad = request.form['enfermedad']
    modalidad = request.form['modalidad']
    msg = Message(
        subject="Estás registrado!",
        sender="practicotrabajo74@gmail.com",
        #recipients=[email],
        recipients=[email],
        body="Hola {nombre} {apellido}, te has registrado exitosamente en la carrera en la modalidad {modalidad}. Tu DNI es {dni}. Enfermedades o condiciones médicas: {enfermedad}. Nos vemos en la carrera!".format(nombre=nombre, apellido=apellido, modalidad=modalidad, dni=dni, enfermedad=enfermedad)
    )
    mail.send(msg)
                           
if __name__ == '__main__':
    app.run(debug=True)
