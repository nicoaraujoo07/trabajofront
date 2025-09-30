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
                    "fecha": "24 de Octubre de 2025",
                    "horario": "8am",
                    "lugar": "Tandil, Buenos Aires",
                    "tipo_carrera": "MTB Rural",
                    "modalidad_costo": {1: {"nombre": "Corta:" ,"valor": "10.000"},
                                        2: {"nombre": "Larga:" ,"valor": "25.000"}
                                        }
                    }
                }

lista = ["COMPROMISO SOCIAL: Organizamos actividades comunitarias, campañas solidarias y eventos abiertos para toda la comunidad.",

"FORMACION INTEGRAL: Más allá del entrenamiento físico, trabajamos aspectos como el liderazgo, el trabajo en equipo y la responsabilidad.",

"DIVERSIDAD DEPORTIVA: Contamos con múltiples disciplinas para todas las edades y niveles, desde iniciación hasta competición.",

"INFRAESTRUCTURA ADECUADA: Disponemos de espacios seguros, cómodos y en constante mejora para ofrecer la mejor experiencia posible.",

"EQUIPO HUMANO: Nuestro cuerpo técnico, profesores y voluntarios comparten una visión común basada en la empatía, la inclusión y el profesionalismo."]
    
lista2 = [
    ["Fútbol ⚽", "futbol.jpg"],
    ["Voley 🏐", "voley.jpeg"],
    ["Natación 🤽🏻‍♂️", "natacion.jpeg"],
    ["Golf ⛳", "golf.jpg"],
    ["Gimnasia artística 🤸🏻‍♀️", "gimnasia-artistica.jpeg"],
    ["Atletismo 🏃🏻‍➡️", "atletismo.jpeg"],
    ["Basquet 🏀", "basquet.jpeg"],
    ["Otros... ⭐", "otros.jpg"]
    ]
          

@app.route('/')
def index():
    ef_str = request.args.get("error_flag")
    if ef_str == "False":
        ef_str = False
    return render_template('index.html', datos=diccionario, lista=lista, deportes=lista2,error_flag=ef_str)

@app.route("/registro", methods=["GET", "POST"])
def registration():
    error_flag=request.args.get('error_flag')
    return render_template('registration.html', error_flag=error_flag)

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
        body="""Hola {nombre} {apellido}! Te has registrado exitosamente en la carrera en la modalidad {modalidad}. 
         - Tu DNI es {dni}. 
         - Enfermedades o condiciones médicas: {enfermedad}. 
        
        Nos vemos en la carrera!""".format(nombre=nombre, apellido=apellido, modalidad=modalidad, dni=dni, enfermedad=enfermedad)
    )
    try:
        mail.send(msg)
        return redirect(url_for("index", error_flag=False))
    except:
        return redirect(url_for("registration",error_flag=True))
if __name__ == '__main__':
    app.run("localhost", port="5001",debug=True)