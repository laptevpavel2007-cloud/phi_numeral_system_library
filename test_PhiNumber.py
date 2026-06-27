import unittest
from fractions import Fraction
from PhiNumber import _PhiNumber as P
 
 
class TestPhiNumber(unittest.TestCase):
 
    def test_creation(self):
        x = P(5, 0)
        self.assertEqual((x.a, x.b), (Fraction(5), Fraction(0)))
        self.assertEqual(P.phi(), P(Fraction(1, 2), Fraction(1, 2)))
 
    def test_arithmetic(self):
        self.assertEqual(P(0, 1) * P(0, 1), P(5, 0))   
        self.assertEqual(P.phi() * P.phi(), P.phi() + P(1, 0)) 
        self.assertEqual(P(1, 2) + P(3, 4), P(4, 6))
        self.assertEqual(P(1, 2) - P(3, 4), P(-2, -2))
 
    def test_exactness(self):
        third = P(Fraction(1, 3), 0)
        self.assertEqual(third + third + third, P(1, 0)) 
 
    def test_comparisons(self):
        self.assertTrue(P(1, 0) < P.phi() < P(2, 0))
        self.assertEqual(P(1, -1).sign(), -1)           
        self.assertEqual(P(0, 0).sign(), 0)
 
 
if __name__ == "__main__":
    unittest.main()