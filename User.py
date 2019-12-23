from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response

from Character import character_list

class User:
  
  def __init__(self, e_id, name, email, characters, games):
		self.e_id = e_id		
		self.name = name
		self.email = email
		self.characters = characters
		self.games = games
  

    
  user_list = [Usuario(1, 'Geadalu', 'lucia@savingthrow.com', ['Lightweaver', 'Ysera']),
  Usuario(2, "juanjoglvz", 'juanjo@savingthrow.com', ['Cancho'])]
    

  #Obtener la lista de los usuarios
  @user_api.route('/v1/users/', methods=['GET'])
  def getUsers():
    return jsonify({'Usuarios: ':user_list})


  #Crear un nuevo usuario
  @user_api.route('/v1/users/', methods=['POST'])
  def createUser():
    if not request.json or not 'email' in request.json:
      abort(404)
    e_id = user_list[-1].e_id + 1
    name = request.json.get('name')
    email = request.json.get('email')
    characters = request.json.get('characters')
    user = User(e_id, name, email, characters)
    user_list.append(user)	#ESTO NO SÉ SI ESTÁ BIEN
    return jsonify({'character':character}),201
      return abort(404)


  #Obtener los atributos de un usuario
  @user_api.route('/v1/users/<string:e_id>/', methods=['GET'])
  def getUser(e_id):
    for user in user_list:
      if user.get("e_id") == e_id:
        sub = 'User '+user.get('name')
        return jsonify({sub:user})
    abort(404)
    
   
  #Borrar usuario MIRAR PORQUE NO ESTOY SEGURA DE QUE ESTÉ BIEN
  @user_api.route('/v1/users/<string:e_id>/', methods=['DELETE'])
  def deleteUser(e_id):
    for user in user_list:
      if user.get("id") == e_id:
        sub = 'User '+user.get('name')
          return jsonify({sub:user})
    abort(404)
    
    
  #Obtener las partidas del usuario
  @user_api.route('/v1/users/<string:e_id>/games', methods=['GET'])
  def getUserGames(e_id):
    for user in user_list:
      if user['id'] == e_id:
        sub = user.get('name')+'\'s games:'
        return jsonify({'Games: ':user['games']})
    abort(404)
    
   
  #Obtener los personajes del usuario
  @user_api.route('/v1/users/<string:e_id>/characters', methods=['GET'])
  def getUserCharacters(e_id):
    for user in user_list:
      if user['id'] == e_id:
        return jsonify({'Characters: ':user['characters']})
    abort(404)
    
    
  #Crear nuevo personaje MIRAR PORQUE NO SÉ SI HAY QUE MOVERLO A CHARACTERS
  @user_api.route('/v1/users/<string:e_id>/characters', methods=['POST'])
  def postCharacter(e_id):
    if not request.json or not 'name' in request.json:
      abort(404)
    e_id = character_list[-1].e_id + 1
    name = request.json.get('name')
    game = request.json.get('game')
    user = request.json.get('user')
    character = Character(e_id, name, game, user)
    character_list.append(character)	#ESTO NO SÉ SI ESTÁ BIEN
    return jsonify({'character':character}),201


    
  @user_api.errorhandler(404)
  def not_found(error):
    return make_response(jsonify({'Error 404: ': 'We did not find your request... Throw perception!'}), 404)