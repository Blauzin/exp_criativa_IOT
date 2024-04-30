# app.py
from flask import Flask, render_template
app= Flask(__name__)
## __name__ is the application name
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/sensors')
def sensors():
    sensores = ['Umidade', 'temperatura', 'luminosidade']
    return render_template("sensors.html", sensores=sensores)
@app.route('/actuators')
def sensors():
    actuators = ['Atuador 1', 'Atuador 2', 'Atuador 3' ]
    return render_template("actuators.html", actuators=actuators)