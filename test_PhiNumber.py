import pytest
from fractions import Fraction
from PhiNumber import _PhiNumber as P


def test_creation():
    x = P(5, 0)
    assert (x.a, x.b) == (Fraction(5), Fraction(0))
    assert P.phi() == P(Fraction(1, 2), Fraction(1, 2))
 
def test_arithmetic():
    assert P(0, 1) * P(0, 1) == P(5, 0)    
    assert P.phi() * P.phi() == P.phi() + P(1, 0) 
    assert P(1, 2) + P(3, 4) == P(4, 6) 
    assert P(1, 2) - P(3, 4) == P(-2, -2) 
 
def test_exactness():
    third = P(Fraction(1, 3), 0)
    assert third + third + third == P(1, 0) 
 
def test_comparisons():
    assert (P(1, 0) < P.phi() < P(2, 0)) == True
    assert P(1, -1).sign() == -1           
    assert P(0, 0).sign() == 0 
 
 
if __name__ == "__main__":
    pytest.main()
