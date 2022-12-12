import unittest, requests 
from app import app, db

class TestHomeRoute(unittest.TestCase):
    def test_home(self):
        res = requests.get('/')
        self.assertEqual(res.status_code, 200)