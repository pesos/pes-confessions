#!/usr/bin/env python

import facebook
import re
import pymongo
from pymongo import Connection

token = "166959483452298|gTCLDoLCM89lzRvjm_Ww2ThOfsU"

def getID(message):
	lines = message.split('\n')
	head = lines[0]
	number = re.findall(r'\d+', head)
	if len(number) > 0:
		return number[0]
	else:
		raise KeyError("Confession Number not found!")

def extract(data):
	collection = Connection()['conf']['b']
	for post in data:
		logger = {}
		try: 
			confID = getID(post["message"])
		except KeyError as k:
			print 'Error', k
			continue
		logger["confID"] = confID
		logger["message"] = post["message"]
		cursor = collection.find({'confID': str(confID)})
		if cursor.count() != 0:
			continue
		collection.insert(logger, safe=True)
		print 'Inserted', confID


def fetch():
	graph = facebook.GraphAPI(token)
	page = graph.get_object("613660905316922/posts", limit=300)
	data = page["data"]
	extract(data)

if __name__ == '__main__':
	fetch()
	
