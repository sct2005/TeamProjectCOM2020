import unittest
import json

class TestExhibitLength(unittest.TestCase):

    def setUp(self):
        with open('../../backend/exhibits/data/seed/exhibits.json', 'w') as file:
            self.data = json.load(file)

        
        