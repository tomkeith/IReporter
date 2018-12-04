from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import RedFlagsModels



class RedFlags(Resource, RedFlagsModels):
	

	def __init__(self):
		self.db = RedFlagsModels()

	def post(self):
		data=request.get_json()
		createdBy=data['createdBy']
		location=data['location']
		comment = data['comment']

		resp = self.db.save_record(createdBy, location, comment)

		return make_response(jsonify(
			{
			"Message" : "RedFlag has been created",
			"status" : 201
			}), 201)

	def get(self):
		resp = self.db.get_all()

		return make_response(jsonify(
			{
			"RedFlag" : resp,
			"status" : 200
			}), 200)

	

class RedFlag(Resource, RedFlagsModels):
	"""docstring for RedFlag"""
	def __init__(self):
		self.db = RedFlagsModels()

	def get(self, num):
		resp = self.db.get_one(num)

		return make_response(jsonify(
			{
			"RedFlag" : resp,
			"status" : 201
			}), 201)

	def patch(self, num):
		try:
			int(num)
		except ValueError:
			return{
				'status': 404,
				'error': 'Valid id required'
			}
		editlocation = self.db.edit_location(num)
		return editlocation

	def patch(self, num):
		try:
			int(num)
		except ValueError:
			return{
				'status': 404,
				'error': 'Valid id required'
			}
		editcomment = self.db.edit_comment(num)
		return editcomment

	def delete(self, num):
		redflag = self.db.search(num)
		if redflag == None:
			return make_response(jsonify(
			{
			"RedFlag" : "RedFlag does not exist.",
			"status" : 404
			}), 404)
		self.db.destroy(redflag)
		success_message = {
			"id" : num,
			"message" : "RedFlag deleted successfully"
		}
		return make_response(jsonify(
			{
			"RedFlag" : success_message,
			"status" : 200
			}),)

		
	def put(self, num):
		resp = self.db.put_one(num)

		return make_response(jsonify(
			{
			"RedFlag" : resp,
			"status" : 200
			}), 200)

