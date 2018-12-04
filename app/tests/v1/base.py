from ... import create_app
import unittest
import json




class BaseTestRedFlags(unittest.TestCase):

	def setUp(self):
		 
		self.app = create_app()
		self.app.testing = True
		self.client = self.app.test_client()

		self.data = {
			  "createdBy" : "Tom",
			  "location" : "45E, 24N",
			  "status" : "draft", 
			  "Images" : "image", 
			  "Videos" : "video",
			  "comment" : "whosmatternow"
			}

		self.data2 = {
			  "createdBy" : "mwaka", 
			  "location" : "45E, 29N",
			  "status" : "draft", 
			  "Images" : "image", 
			  "Videos" : "video",
			  "comment" : "whosmatternow"
			}

		self.data1 = {
			  "createdBy" : "Abram",
			  "location" : "5E, 9N",
			  "status" : "draft", 
			  "Images" : "image", 
			  "Videos" : "video",
			  "comment" : "whosmatternow"
			}

	def teardown():
		pass

if __name__ == '__main__':
	unittest.main()
