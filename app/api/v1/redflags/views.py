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
			"data" : resp,
			"status" : 201
			}), 201)

	def get(self):
		resp = self.db.get_all()

		return make_response(jsonify(
			{
			"data" : resp,
			"status" : 200
			}), 200)

	


	

