from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_eventos_2025'

# Lista para guardar inscritos (en un proyecto real usarías una base de datos)
inscritos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    lista_eventos = [
        {
            'id': 1,
            'nombre': 'Conferencia de Innovación Tech 2025',
            'fecha': '15 de Agosto, 2025',
            'hora': '09:00 AM',
            'lugar': 'Centro de Convenciones La Paz',
            'descripcion': 'El evento tecnológico más grande de Bolivia. Speakers internacionales, talleres prácticos y networking con los mejores profesionales del área.',
            'imagen': 'tech.jpg',
            'precio': 'Gratuito',
            'cupos': 200,
            'categoria': 'Tecnología'
        },
        {
            'id': 2,
            'nombre': 'Festival de Música Andina Fusión',
            'fecha': '22 de Septiembre, 2025',
            'hora': '06:00 PM',
            'lugar': 'Plaza Murillo, La Paz',
            'descripcion': 'Una noche mágica fusionando ritmos andinos con música contemporánea. Artistas locales e internacionales en un escenario único.',
            'imagen': 'musica.jpg',
            'precio': 'Bs. 50',
            'cupos': 500,
            'categoria': 'Música'
        },
        {
            'id': 3,
            'nombre': 'Workshop de Emprendimiento 2025',
            'fecha': '10 de Octubre, 2025',
            'hora': '08:00 AM',
            'lugar': 'Hotel Presidente, La Paz',
            'descripcion': 'Aprende de emprendedores exitosos, valida tu idea de negocio y conecta con inversionistas. ¡Tu idea puede cambiar el mundo!',
            'imagen': 'emprendimiento.jpg',
            'precio': 'Bs. 150',
            'cupos': 100,
            'categoria': 'Negocios'
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
        inscritos.append(nueva_inscripcion)

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