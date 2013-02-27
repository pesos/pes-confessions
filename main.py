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

	'''	
	conf = ''
	for obj in cursor:
		conf += obj['message']
		conf += '\n\n'

	return conf
	'''
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
