from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

users = [
        
    {'id': 1,
     'name': u'Geadalu',
     'email': u'lucia@savingthrow.com',
     'characters':  ['Lightweaver', 'Ysera'],
     'games': [1]
    },

    {'id': 2,
     'nombreUsuario': u'juanjoglvz',
     'email': u'juanjo@savingthrow.com',
     'characters': ['Cancho'],
     'games':  [1, 2]
    }
    
]

games = [
        
      {'id': 1,
       'name': 'Roshar en peligro',
       'players': ['Geadalu', 'juanjoglvz'],
       'characters': ['Lightweaver', 'Cancho'],
       }    
]

characters = [
        {'id': 1,
         'name': 'Lightweaver',
         'game': 1,
         'user': 'Geadalu',
        },
         
         {'id': 2,
         'name': 'Ysera',
         'game': None,
         'user': 'Geadalu',
        },
             
        {'id': 3,
         'name': 'Cancho',
         'game': 1,
         'user': 'juanjoglvz',
        }
]


                                #USUARIOS
@app.route('/v1/users/', methods=['GET'])
def getUsers():
    return jsonify({'Usuarios':users})


@app.route('/v1/users/', methods=['POST'])
def createUser():
    return abort(404)


@app.route('/v1/users/<string:ident>/', methods=['GET'])
def getUser(ident):
    for user in users:
        if user.get("id") == ident:
            sub = 'Usuario '+user.get('name')
            return jsonify({sub:user})
    abort(404)
    
    
@app.route('/v1/users/<string:ident>/', methods=['DELETE'])
def deleteUser(ident):
    for user in users:
        if user.get("id") == ident:
            sub = 'Usuario '+user.get('name')
            return jsonify({sub:user})
    abort(404)
    
    
@app.route('/v1/users/<string:ident>/games', methods=['GET'])
def getGame(ident):
    for user in users:
        if user['id'] == ident:
            return jsonify({'Partidas: ':user['games']})
    abort(404)
    
    
@app.route('/v1/users/<string:ident>/characters', methods=['GET'])
def getCharacters(ident):
    for user in users:
        if user['id'] == ident:
            return jsonify({'Personajes: ':user['characters']})
    abort(404)
    
@app.route('/v1/users/<string:ident>/characters', methods=['POST']) #MIRAR EJEMPLO
def postCharacters(ident):
    for user in users:
        if user['id'] == ident:
            return jsonify({'Personajes: ':user['characters']})
    abort(404)


    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error 404: ': 'We did not find your request... Throw perception!'}), 404)
        
 
    
                                #PERSONAJES
                            
                            
                            
                        
                                #PARTIDAS
                            


@app.route('/')
 
def index():
     
    return "¡Bienvenid@ a SavingThrow! *tumbleweeds crawling around...*"

if __name__ == '__main__':
    app.run(debug=False)
