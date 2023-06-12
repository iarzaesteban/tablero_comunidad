from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'collaborative-community'
app.config['DATABASE'] = 'tablero_comunidad'
app.config['DB_USER'] = 'esteban'
app.config['DB_PASSWORD'] = '603007JC10209445'


@app.route('/')
def home():
    return 'Página de inicio'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verifica las credenciales en la base de datos
        conn = psycopg2.connect(database=app.config['DATABASE'],
                                user=app.config['DB_USER'],
                                password=app.config['DB_PASSWORD'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            # Iniciar sesión exitosa
            return '¡Inicio de sesión exitoso!'
        else:
            # Credenciales inválidas
            return 'Credenciales inválidas'
    
    # Renderizar el formulario de inicio de sesión
    return render_template('login.html')