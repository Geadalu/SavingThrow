from flask import Flask

from api.v1.Game import game_api
from api.v1.Character import character_api
from api.v1.User import user_api
from api.v1.model import *

from flask.json import JSONEncoder

from mongoengine import connect

'''class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Game):
            return {
                'e_id': obj.e_id, 
		'name': obj.name,
		'players': obj.players,
		'characters': obj.characters
            }
	if isinstance(obj, Character):
            return {
                'e_id': obj.e_id, 
		'name': obj.name,
		'game': obj.game,
		'user': obj.user
            }
	if isinstance(obj, User):
            return {
                'e_id': obj.e_id, 
		'name': obj.name,
		'email': obj.email,
		'characters': obj.characters,
		"games": obj.games
            }
        return super(MyJSONEncoder, self).default(obj)'''

app = Flask(__name__)
#app.json_encoder = MyJSONEncoder

# Blueprint
app.register_blueprint(game_api)
app.register_blueprint(user_api)
app.register_blueprint(character_api)

# MongoDB database
app.config['MONGODB_DB'] = 'SavingThrow'
connect(
    'SavingThrow',
    host='mongodb://localhost/SavingThrow',
    port=27017 
)



if __name__ == '__main__':
    app.run(debug=True)
