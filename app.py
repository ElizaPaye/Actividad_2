from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta_eventos_2026'

def crear_db():
    conn = sqlite3.connect("eventos.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inscritos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        telefono TEXT,
        evento TEXT,
        edad INTEGER,
        mensaje TEXT
    )
    """)

    conn.commit()
    conn.close()

crear_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    lista_eventos = [
        {
            'id': 1,
            'nombre': 'Día del Internet UPEA 2026 - Conferencias',
            'fecha': '10 de Mayo, 2026',
            'hora': '09:00 AM',
            'lugar': 'Auditorio UPEA - El Alto',
            'descripcion': 'Charlas sobre innovación, ciberseguridad, inteligencia artificial y el futuro de Internet.',
            'imagen': 'internet1.jpg',
            'precio': 'Gratuito',
            'cupos': 300,
            'categoria': 'Tecnología'
        },
        {
            'id': 2,
            'nombre': 'Día del Internet UPEA 2026 - Talleres',
            'fecha': '10 de Mayo, 2026',
            'hora': '02:00 PM',
            'lugar': 'Laboratorios UPEA',
            'descripcion': 'Talleres prácticos de programación, desarrollo web y redes.',
            'imagen': 'internet2.jpg',
            'precio': 'Gratuito',
            'cupos': 150,
            'categoria': 'Formación'
        },
        {
            'id': 3,
            'nombre': 'Día del Internet UPEA 2026 - Feria Tecnológica',
            'fecha': '10 de Mayo, 2026',
            'hora': '04:00 PM',
            'lugar': 'Patio Central UPEA',
            'descripcion': 'Exposición de proyectos, robots, apps y emprendimientos tecnológicos de estudiantes.',
            'imagen': 'internet3.jpg',
            'precio': 'Gratuito',
            'cupos': 500,
            'categoria': 'Innovación'
        },
    ]
    return render_template('eventos.html', eventos=lista_eventos)

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        evento = request.form.get('evento')
        edad = request.form.get('edad')
        mensaje = request.form.get('mensaje')

        # Validación básica
        if not nombre or not email or not evento:
            flash('Por favor completa los campos obligatorios.', 'error')
            return redirect(url_for('inscripcion'))

        # Guardar inscripción
        nueva_inscripcion = {
            'nombre': nombre,
            'email': email,
            'telefono': telefono,
            'evento': evento,
            'edad': edad,
            'mensaje': mensaje
        }
        conn = sqlite3.connect("eventos.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO inscritos (nombre, email, telefono, evento, edad, mensaje)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, email, telefono, evento, edad, mensaje))

        conn.commit()
        conn.close()

        flash(f'¡Inscripción exitosa, {nombre}! Te esperamos en el evento.', 'success')
        return redirect(url_for('gracias'))

    return render_template('inscripcion.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)