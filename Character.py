from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response


class Character:
  
  def __init__(self, e_id, name, game, user_name):
		self.e_id = e_id		
		self.name = name
		self.game = game
		self.user_name = user_name
  
  character_list = [ Character(1, 'Lightweaver', 1, 'Geadalu'),
  Character(2. 'Ysera', None, 'Geadalu'),
  Character(3, 'Cancho', 1, 'juanjoglvz')]
  
  character_api = Blueprint('character_api', __name__)
  
  #Obtener atributos de un personaje
  @character_api.route('/v1/character/<string:e_id>/', methods=['GET'])
  def getCharacterAttributes():
    for character in character_list:
      if character.get("e_id") == ident:
        sub = 'Character '+character.get('name')+": "
        return jsonify({sub:character})
    abort(404)
  
  #Obtener partida del personaje
  @character_api.route('/v1/characters/<string:e_id>/games', methods=['GET'])
  def getUserCharacters(e_id):
    for character in character_list:
      if user['id'] == e_id:
        sub = character.get('name')+'\'s game:'
        return jsonify({'Characters: ':user['characters']})
    abort(404)
  
  
  #Borrar personaje
