from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app, resources={r"/*": {"origins":"http://localhost:8080","allow_headers":"Access-Control-Allow-Origin"}})

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
    },
     {
        'title': 'Nuclear Nightmare',
        'genre': 'Co-op Horror',
        'played': False,
        'price': 2.79
    }
]

# GET & POST route handler
@app.route('/games', methods=['GET', 'POST'])
def get_games():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
            'price': post_data.get('price')
            })
        response_object['message'] = 'Game added!'
    else:
        response_object['games'] = GAMES
        
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=True)