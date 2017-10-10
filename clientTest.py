import unittest
import client
import json

class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.app = client.APPLICATION.test_client()

    def testGetAcceptAppJson(self):
        rv = self.app.get('/',headers={'Accept': 'application/json'})
        self.assertEqual(json.loads(rv.data), {'message': 'Good Morning'})
        self.assertEqual(rv.status_code, 200)

    def testGetNoAccept(self):
        rv = self.app.get('/')
        self.assertEqual(rv.data, '<p>Hello World</p>')
        self.assertEqual(rv.status_code, 200)

    def testGetNoAcceptWithNameParmaeter(self):
        rv = self.app.get('/?name=Eric')
        self.assertEqual(rv.data, '<p>Hello Eric</p>')
        self.assertEqual(rv.status_code, 200)
    
    def testGetNegativeCase(self):
        rv = self.app.get('/',headers={'Accept': 'application/yml'})
        self.assertEqual(json.loads(rv.data), {'message': 'Only accept application/json or no accept header'})
        self.assertEqual(rv.status_code, 400)

    def testPostAcceptAppJson(self):
        rv = self.app.post('/',headers={'Accept': 'application/json'})
        self.assertEqual(json.loads(rv.data), {'message': 'Good Morning'})
        self.assertEqual(rv.status_code, 200)

    def testPostNoAccept(self):
        rv = self.app.post('/')
        self.assertEqual(rv.data, '<p>Hello World</p>')
        self.assertEqual(rv.status_code, 200)

    def testPostNegativeCase(self):
        rv = self.app.post('/',headers={'Accept': 'application/yml'})
        self.assertEqual(json.loads(rv.data), {'message': 'Only accept application/json or no accept header'})
        self.assertEqual(rv.status_code, 400)

    def testPostNoAcceptWithNameParmaeter(self):
        rv = self.app.post('/?name=Eric')
        self.assertEqual(rv.data, '<p>Hello Eric</p>')
        self.assertEqual(rv.status_code, 200)

if __name__ == '__main__':
    unittest.main()

