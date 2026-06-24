from fractions import Fraction
from typing import Union

Number = Union[int, Fraction]

class _PhiNumber:
    # Число вида a + b * sqrt(5)

    def __init__(self, a:Number = 0, b: Number = 0) -> None:
        self.a: Fraction = Fraction(a)
        self.b: Fraction = Fraction(b)

    def __add__(self, other: "_PhiNumber") -> "_PhiNumber":
        # (a + b * sqrt(5)) + (c + d * sqrt(5)) = (a + c) + (b + d) * sqrt(5)
        return _PhiNumber(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other: "_PhiNumber") -> "_PhiNumber":
        # (a + b * sqrt(5)) - (c + d * sqrt(5)) = (a - c) + (b - d) * sqrt(5)
        return _PhiNumber(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other: "_PhiNumber") -> "_PhiNumber":
        # (a + b * sqrt(5)) * (c + d * sqrt(5)) = (ac + 5bd) + (ad + bc) * sqrt(5)
        return _PhiNumber(self.a * other.a + 5 * self.b * other.b, self.a * other.b + self.b * other.a)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _PhiNumber):
            return NotImplemented
        return self.a == other.a and self.b == other.b
    
    def __repr__(self) -> str:
        return f"_PhiNumber({self.a}, {self.b})"