from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados dos cômodos
rooms = {
    'quarto': {
        'sensor': 'Sensor de luminosidade',
        'atuador': 'Interruptor'
    },
    'banheiro': {
        'sensor': 'Sensor de umidade',
        'atuador': 'Lâmpada inteligente'
    }
}

@app.route('/')
def home():
    return render_template('index.html', rooms=rooms)

@app.route('/room/<room_name>')
def room(room_name):
    room_data = rooms.get(room_name)
    if room_data:
        return render_template('room.html', room_name=room_name, room_data=room_data)
    else:
        return redirect(url_for('home'))

@app.route('/action/<room_name>/<device>')
def action(room_name, device):
    if device in rooms[room_name]:
        return f"{rooms[room_name][device]} ativado/a no {room_name}!"
    else:
        return redirect(url_for('room', room_name=room_name))

if __name__ == '__main__':
    app.run(debug=True)
