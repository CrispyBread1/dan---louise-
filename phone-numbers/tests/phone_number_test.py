import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):
    def test_create_phone_number_works(self):
        phone_number = create_phone_number(1234567890)
        self.assertEqual("(123) 456-7890", phone_number)

    def test_phone_number_doesnt_work(self):
        phone_number = create_phone_number(123456789)
        self.assertEqual(False, phone_number)