import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):
    
    def setUp(self):
        self.compound = CompoundInterest(100, 0, 10)
    
    # Tests
    

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    # def test_compound1(self):
    #     total = self.compound.compound_interest()
    #     self.assertEqual(732.81, total)



    # Should return 181.94 given 100 principal, 6 percent, 10 years
    # def test_compound2(self):
    #     total = self.compound.compound_interest()
    #     self.assertEqual(181.94, total)



    # # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    # def test_compound3(self):
    #     total = self.compound.compound_interest()
    #     self.assertEqual(149058.55, total)



    # Should return 0.00 given 0 principal, 10 percent, 1 year
    # def test_compound3(self):
    #     total = self.compound.compound_interest()
    #     self.assertEqual(0, total)



    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_compound3(self):
        total = self.compound.compound_interest()
        self.assertEqual(100, total)


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

