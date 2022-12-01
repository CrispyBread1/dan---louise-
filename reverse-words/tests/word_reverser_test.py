import unittest
from src.word_reverser import *

class TestWordReverse(unittest.TestCase):
    pass 

    # Have unit tests for the following sentences 
    def setUp(self):
        self.string1 = "Hello this is a test fantastic"
        self.string2 = "The cat was cute and he was called Azzazel"
        self.string3 = "Very cool hat"

    def test_string_1(self):
        reverse = spin_words(self.string1)
        self.assertEqual("olleH this is a test citsatnaf", reverse)
    
    def test_string_2(self):
        reverse = spin_words(self.string2)
        self.assertEqual("The cat was cute and he was dellac lezazzA", reverse)

    def test_string_3(self):
        reverse = spin_words(self.string3)
        self.assertEqual("Very cool hat", reverse)