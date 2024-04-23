# app.py
from flask import Flask

app= Flask(__name__)
@app.route('/')
def index():
    return """
    <html>
    <head>
    <title>Minha Casa</title>
    </head>
        <body>
            <h2>Minha Casa</h2>
            <h3>Acesse o menu:</h3>
            <ul>
            <li><a href="/sensors">Listar Sensores</a></li>
            <li><a href="/actuators">Listar Atuadores</a></li>
            </ul>
        </body>
</html>
"""

@app.route('/sensors')
def sensors():
    return "Listar Sensores"

@app.route('/actuators')

def actuators():
    return "Listar Atuadores"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)