from flask import Flask, jsonify, abort, make_response, Blueprint
import json
from mongoengine import errors

from api.v1.model import *


game_api = Blueprint('game_api', __name__)
  
#Listar todas las partidas
@game_api.route('/v1/games/', methods=['GET'])
def getGames():
    games_list = []
    for game in Game.objects:
        games_list.append(toJson(game))
    return jsonify({'games': games_list})
  
  
#Listar todos los atributos de una partida
@game_api.route('/v1/games/<int:game_id>/', methods=['GET'])
def getGame(game_id):
    game = Game.objects(e_id=game_id)
    if not game:
        abort(404)
    game = toJson(game)
    return jsonify({'game ': game})
    
  
#Crear partida
@game_api.route('/v1/games/', methods=['POST'])
def createGame():
    if not request.json or not 'name' in request.json:
        abort(404)
    if Game.objects:
        game = Game.objects.order_by('-e_id').first() # Last document created
        e_id = game.e_id + 1
    else:
        e_id = 1
      
    name = request.json.get('name')  
    description = request.json.get('description')
    location = request.json.get('location')
    time = request.json.get('time')
    player_level = request.json.get('player_level')

    list_characters_identifiers = request.json.get('characters')
    list_characters = []
    for character_id in list_characters_identifiers:
        character = Character.objects(e_id=character_id)[0]
        list_characters.append(character)
    

    game = Game(e_id, name, description, list_characters, location, time, player_level)

    try:
        game.save()
    except errors.NotUniqueError:
        error = 'Whoops! We can not have two games with the same e_id, right?'
        return jsonify(error=error), 409

    game = toJson(game)
    return jsonify({'game created: ':game}),201
    
#Actualizar partida
@game_api.route('/v1/games/<int:game_id>/', methods=['POST'])
def updateGame(game_id):
    if not request.json or not 'e_id' or not 'name' in request.json:
        abort(404)
    if Game.objects:
        game = Game.objects.order_by('-e_id').first() # Last document created
        e_id = game.e_id + 1
    else:
        e_id = 1
      
    name = request.json.get('name')
    description = request.json.get('description')
    location = request.json.get('location')
    time = request.json.get('time')
    player_level = request.json.get('player_level')
    
    list_characters_identifiers = request.json.get('characters')
    list_characters = []
    for character_id in list_characters_identifiers:
        character = Character.objects(e_id=character_id)[0]
        list_characters.append(character)
    
    game.update(
            name = name,
            description = description,
            characters = list_characters,
            location = location,
            time = time,
            player_level = player_level)
    

    game = toJson(game)
    return jsonify({'game updated: ':game}),200
  
#Borrar partida
@game_api.route('/v1/games/<int:game_id>/', methods=['DELETE'])
def deleteGame(game_id):
    game = Game.objects(e_id=game_id).get()
    if not game:
        abort(404)
    game.delete()
    return jsonify({'deleted game: ': game}),200
  
@game_api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error 404: ': 'We did not find your request... Throw perception!'}), 404)

def toJson(object):
    objectToJson = object.to_json()
    objectData = json.loads(objectToJson)
    return objectData