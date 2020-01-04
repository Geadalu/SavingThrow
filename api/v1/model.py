from mongoengine import *

class Character (Document):
    e_id = IntField(required=True, unique=True)
    name = StringField(required=True, max_length=20)
    hp = IntField(max_length=4)
    level = IntField(max_length=2)
    race = StringField(max_length = 20)
    character_class = StringField(max_length=40)
    alignment = StringField(max_length = 30)

class Game (Document):
    e_id = IntField(required=True, unique=True)
    name = StringField(required=True, max_length=40)
    description = StringField(max_length=300)
    characters = ListField(ReferenceField(Character))
    location = StringField(max_length=60)
    time = StringField(max_length=30)
    player_level = StringField(max_length=15)
    
class User (Document):
	e_id = IntField(required=True, unique=True)	
	name = StringField(max_length=12)
	email = EmailField(max_length=40)
	characters = ListField(ReferenceField(Character))
	games = ListField(ReferenceField(Game))