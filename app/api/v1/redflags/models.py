from flask_restful import Resource
from flask import jsonify, make_response, request
import datetime



redflags = []

class RedFlagsModels():
	"""docstring for RedFlagsModels"""
	def __init__(self):
		self.db = redflags


	def save_record(self, createdBy, location, comment):
		payload = {
		  'id' : len(self.db)+1,
		  'createdOn' : datetime.datetime.now().strftime('%I:%M%p %B %d, %Y'),  
		  'createdBy' : createdBy, 
		  'type' : "redflag",       
		  'location' : location,   
		  'status' : "draft",     
		  'Images' : "images", 
		  'Videos' : "videos",
		  'comment' : comment
		
		}

		self.db.append(payload)

		return self.db
	
	
	def get_all(self):
		return self.db

	
		
