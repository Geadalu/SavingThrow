from flask import Flask, jsonify, abort, make_response, Blueprint
import json
from mongoengine import errors

from api.v1.model import *

character_api = Blueprint('character_api', __name__)

#Listar personajes
@character_api.route('/v1/characters/', methods=['GET'])
def getCharacters():
    characters_list = []
    for character in Character.objects:
        characters_list.append(toJson(character))
    return jsonify({'characters': characters_list})
  
#Obtener atributos de un personaje
@character_api.route('/v1/characters/<int:character_id>/', methods=['GET'])
def getCharacter(character_id):
    character = Character.objects(e_id=character_id).exclude("id").get()
    if not character:
        abort(404)
    character = toJson(character)
    return jsonify({'character ': character})
 

#Create character
@game_api.route('/v1/games/', methods=['POST'])
def createCharacter():
    if not request.json or not 'name' in request.json:
        abort(404)
    if Character.objects:
        character = Character.objects.order_by('-e_id').first() # Last document created
        e_id = character.e_id + 1
    else:
        e_id = 1
      
    name = request.json.get('name')  
    hp = request.json.get('hp')
    level = request.json.get('level')
    race = request.json.get('race')
    character_class = request.json.get('character_class')
    alignment = request.json.get('alignment')

    character = Character(e_id, name, hp, level, race, character_class, alignment)

    try:
        character.save()
    except errors.NotUniqueError:
        error = 'Whoops! We can not have two characters with the same e_id, right?'
        return jsonify(error=error), 409

    character = toJson(character)
    return jsonify({'character created: ':character}),201

#Update character
@character_api.route('/v1/characters/<int:character_id>/', methods=['POST'])
def updateCharacter(character_id):
    if not request.json or not 'name' or not 'e_id' in request.json:
        abort(404)
    if Character.objects:
        try:
            character = Character.objects(e_id=request.get("e_id")).get() # User to modify
        except errors.DoesNotExist:
            error = 'Despite you are on stealth, we catched you. This character could not be found!'
            return jsonify(error=error), 409
    else:
        abort(404)
      
    name = request.json.get('name')
    hp = request.json.get('hp')  
    level = request.json.get('level')
    race = request.json.get('race')  
    character_class = request.json.get('character_class')
    alignment = request.json.get('alignment')

    character.update(
            name = name,
            hp = hp,
            level = level,
            race = race,
            character_class = character_class,
            alignment = alignment)
    

    character = toJson(character)
    return jsonify({'character updated: ':character}),200
    
   
#Borrar character 
@character_api.route('/v1/characters/<int:character_id>/', methods=['DELETE'])
def deleteCharacter(character_id):
    character = Character.objects(e_id=character_id).get()
    if not character:
        abort(404)
    character.delete()
    return jsonify({'deleted character: ': character}),200

@character_api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error 404: ': 'We did not find your request... Throw perception!'}), 404)

def toJson(object):
    objectToJson = object.to_json()
    objectData = json.loads(objectToJson)
    return objectData
    