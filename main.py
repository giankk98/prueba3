from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import xml.etree.ElementTree as ET
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DEFAULT_USERNAME = "USUARIO UDC"
DEFAULT_PASSWORD = "123"

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            session['username'] = username
            return jsonify({"success": True, "message": "Login successful"})
        else:
            return jsonify({"success": False, "message": "Login failed"})
    return render_template('login.html')

@app.route('/analyzeXML', methods=['POST'])
def analyze_xml():
    xml_content = request.form['xmlData']
    # Implementar lógica de análisis XML aquí
    return jsonify({"success": True, "message": "XML analyzed successfully"})

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)