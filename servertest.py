import unittest
import client
import json

class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = client.APPLICATION.test_client()

    def testGetAcceptAppJson(self):
        rv = self.app.get('/',headers={'Accept': 'application/json'})
        self.assertEqual(json.loads(rv.data), {'message': 'Good Morning'})

    def testGetNoAccept(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, '<p>Hello World</p>')
    
    def testGetNegativeCase(self):
        rv = self.app.get('/',headers={'Accept': 'application/yml'})
        self.assertEqual(json.loads(rv.data), {'message': 'Only accept application/json or no accept header'})

    def testPostAcceptAppJson(self):
        rv = self.app.post('/',headers={'Accept': 'application/json'})
        self.assertEqual(json.loads(rv.data), {'message': 'Good Morning'})

    def testPostNoAccept(self):
        rv = self.app.post('/')
        self.assertEqual(rv.data, '<p>Hello World</p>')

    def testPostNegativeCase(self):
        rv = self.app.post('/',headers={'Accept': 'application/yml'})
        self.assertEqual(json.loads(rv.data), {'message': 'Only accept application/json or no accept header'})

if __name__ == '__main__':
    unittest.main()

