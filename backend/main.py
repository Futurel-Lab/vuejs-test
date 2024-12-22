from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

#CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins":"http://localhost:8080","allow_headers":"Access-Control-Allow-Origin"}})

# hello world route testing

@app.route('/', methods=['GET'])
def greetings():
    return("Hello World")

@app.route('/shark', methods=['GET'])
def shark():
    return "🦈 Shark Attack 🦈"

GAMES = [
    {
        'title': 'PomoFarm',
        'genre': 'Focus',
        'played': True,
        'price': 4.99
    },
    {
        'title': 'Call of Duty: Black Ops 6',
        'genre': 'FPS',
        'played': True,
        'price': 69.99
    },
    {
        'title': 'Minecraft',
        'genre': 'SandBox',
        'played': True,
        'price': 26.99
    },
    {
        'title': 'FrostPunk 2',
        'genre': 'City Builder',
        'played': False,
        'price': 44.99
    },
    {
        'title': 'Cities Skylines: 2',
        'genre': 'City Builder',
        'played': True,
        'price': 59.99
    }
]

# GET route handler
@app.route('/games', methods=['GET'])
def get_games():
    return jsonify({
        'games': GAMES,
        'status': 'success'
        })


if __name__ == '__main__':
    app.run(debug=True)