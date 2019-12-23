from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response

class Game:

  def __init__(self, e_id, name, game, user):
		self.e_id = e_id		
		self.name = name
		self.players = players
		self.characters = characters

  game_list = [Game(1, 'Roshar en peligro', [1, 2], [1, 3])]
  
  #Listar todas las partidas
  @game_api.route('/v1/games/', methods=['GET'])
  def getGames():
    return jsonify({'Games: ':game_list})
  
  
  #Listar todos los atributos de una partida
  @game_api.route('/v1/games/<string:e_id>/', methods=['GET'])
  def getGame(e_id):
    for game in game_list:
      if game.get("e_id") == e_id:
        sub = 'Game '+user.get('name')+': '
        return jsonify({sub:game})
    abort(404)
  
  
  #Crear partida
  @games_api.route('/v1/games/', methods=['POST'])
  def postGame(e_id):
    if not request.json or not 'name' in request.json:
      abort(404)
    e_id = character_list[-1].e_id + 1
    name = request.json.get('name')
    players = request.json.get('players')
    characters = request.json.get('characters')
    game = Game(e_id, name, players, characters)
    game_list.append(game)	#ESTO NO SÉ SI ESTÁ BIEN
    return jsonify({'game':game}),201
  
  
  #Borrar partida