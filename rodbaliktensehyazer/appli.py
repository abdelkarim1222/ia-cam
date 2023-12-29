from flask import Flask, render_template, request, jsonify
import os
import subprocess

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

# Définition de la page d'accueil de notre site
@app.route("/", methods=['GET', 'POST']) 
def home():
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
            return render_template("test1.html")
    else:
        return render_template("index.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            subprocess.run(["python", "driver_detector.py", "--shape_predictor", "shape_predictor_68_face_landmarks.dat"])
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        return render_template('contact.html')
    return render_template("index.html")

@app.route("/process_faces", methods=['POST'])
def process_faces():
    if request.method == 'POST':
        data = request.get_json()
        print("Received Faces:", data['faces'])
        # Vous pouvez ajouter un traitement supplémentaire ici
        return jsonify({'status': 'success'})

if __name__ == "__main__":
    app.run()
