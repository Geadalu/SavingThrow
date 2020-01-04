from flask import Flask, jsonify, abort, make_response, Blueprint
import json
from mongoengine import errors
import pymongo

from api.v1.model import *

user_api = Blueprint('user_api', __name__)
 
#Obtener la lista de los usuarios
@user_api.route('/v1/users/', methods=['GET'])
def getUsers():
    users_list = []
    for user in User.objects.exclude("id"):
        users_list.append(toJson(user))
    return jsonify({'users': users_list})


#Obtener los atributos de un usuario
@user_api.route('/v1/users/<int:user_id>/', methods=['GET'])
def getUser(user_id):
    user = User.objects(e_id=user_id).exclude("id").get()
    if not user:
        abort(404)
    user = toJson(user)
    return jsonify({'user ': user})

#Crear un nuevo usuario
@user_api.route('/v1/users/', methods=['POST'])
def createUser():
    if not request.json or not 'email' or not 'name' in request.json:
        abort(404)
    if User.objects:
        user = User.objects.order_by('-e_id').first() # Last document created
        e_id = user.e_id + 1
    else:
        e_id = 1
      
    name = request.json.get('name')  
    email = request.json.get('email')

    list_characters_identifiers = request.json.get('characters')
    list_characters = []
    for character_id in list_characters_identifiers:
        character = Character.objects(e_id=character_id)[0]
        list_characters.append(character)
    
    list_games_identifiers = request.json.get('games')
    list_games = []
    for game_id in list_games_identifiers:
        game = Game.objects(e_id=game_id)[0]
        list_games.append(game)
    
    user = User(e_id, name, email, list_characters, list_games)

    try:
        user.save()
    except errors.NotUniqueError:
        error = 'Whoops! We can not have two users with the same e_id, right?'
        return jsonify(error=error), 409

    user = toJson(user)
    return jsonify({'user created: ':user}),201

#Actualizar usuario
@user_api.route('/v1/users/<int:user_id>/', methods=['POST'])
def updateUser(user_id):
    if not request.json or not 'email' or not 'name' or not 'e_id' in request.json:
        abort(404)
    if User.objects:
        try:
            user = User.objects(e_id=request.get("e_id")).get() # User to modify
        except errors.DoesNotExist:
            error = 'Wait... Who is this? This user could not be found!'
            return jsonify(error=error), 409
    else:
        abort(404)
      
    name = request.json.get('name')  
    email = request.json.get('email')
    
    list_characters_identifiers = request.json.get('characters')
    list_characters = []
    for character_id in list_characters_identifiers:
        character = Character.objects(e_id=character_id)[0]
        list_characters.append(character)
    
    list_games_identifiers = request.json.get('games')
    list_games = []
    for game_id in list_games_identifiers:
        game = Game.objects(e_id=game_id)[0]
        list_games.append(game)
    

    user.update(
            name = name,
            email = email,
            characters = list_characters,
            games = list_games)
    

    user = toJson(user)
    return jsonify({'user updated: ':user}),200
    
   
#Borrar usuario
@user_api.route('/v1/users/<int:user_id>/', methods=['DELETE'])
def deleteUser(user_id):
    user = User.objects(e_id=user_id).get()
    if not user:
        abort(404)
    user.delete()
    return jsonify({'deleted user: ': user}),200
    

@user_api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error 404: ': 'We did not find your request... Throw perception!'}), 404)

def toJson(object):
    objectToJson = object.to_json()
    objectData = json.loads(objectToJson)
    return objectData