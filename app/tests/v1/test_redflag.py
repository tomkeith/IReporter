import unittest
import json
from app.tests.v1.base import BaseTestRedFlags
from app.api.v1.redflags.models import redflags


class TestRedFlags(BaseTestRedFlags):
		
	
	def test_redflag_get(self):
		response = self.client.get('/api/v1/redflags')
		self.assertEqual(response.status_code, 200)

	def test_redflag_post(self):
		response = self.client.post('/api/v1/redflags', data=json.dumps(self.data), content_type='application/json')
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data)
		self.assertEqual(response.data)

	def test_redflag_patch(self):
		response = self.client.patch('/api/v1/redflags/1', data=json.dumps(self.data2), content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_redflag_delete(self):
		response = self.client.delete('/api/v1/redflags/1', content_type='application/json')
		self.assertEqual(response.status_code, 200)
		

	def test_redflag_get(self):
		response = self.client.get('/api/v1/redflags/1', data=json.dumps(self.data1), content_type='application/json')
		self.assertEqual(response.status_code, 201)



	def test_redflag_put(self):
		response = self.client.put('/api/v1/redflags/1', data=json.dumps(self.data1), content_type='application/json')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()


