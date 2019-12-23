from flask import Flask

from api.v1.games import game_api, Game 
from api.v1.characters import character_api, Character 
from api.v1.users import user_api, User

from flask.json import JSONEncoder

class MyJSONEncoder(JSONEncoder):
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
        return super(MyJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

# Blueprint
app.register_blueprint(game_api)
app.register_blueprint(character_api)
app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run(debug=False)
