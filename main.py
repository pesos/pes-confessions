import pymongo 
from flask import Flask
from pymongo import Connection

app = Flask(__name__)
app.debug = False

@app.route("/<confID>")
def landing(confID):
	collection = Connection()['conf']['b']
	cursor = collection.find({'confID': str(confID)})
	if cursor.count() == 0:
		return 'Confession #', confID, 'not found'
	return cursor[0]['message']

@app.route("/")
def default():
	collection = Connection()['conf']['a']
	cursor = collection.find({'confID': str(randrange(10, 180))})
	if cursor.count() == 0:
		return 'Refresh again!'
	return 'Random Confession \n' + cursor[0]['message']

@app.route("/random")
def rand():
	return default()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
