from __future__ import annotations
from fractions import Fraction
from typing import Union

Number = Union[int, Fraction]

class _PhiNumber:
    # Число вида a + b * sqrt(5)

    def __init__(self, a:Number = 0, b: Number = 0) -> None:
        self.a: Fraction = Fraction(a)
        self.b: Fraction = Fraction(b)

    @classmethod
    def phi(cls) -> "_PhiNumber":
        return(_PhiNumber(Fraction(1, 2), Fraction(1, 2)))
    

    def sign(self) -> int:
        a, b = self.a, self.b
        if a == 0 and b == 0:
            return 0
        if a >= 0 and b >= 0:
            return 1
        if a <= 0 and b <= 0:
            return -1
        d = a * a - 5 * b * b
        sa = 1 if a > 0 else -1
        return sa * (1 if d > 0 else -1)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, _PhiNumber):
            return NotImplemented
        return self.a == other.a and self.b == other.b
    
    def __lt__(self, other: "_PhiNumber") -> bool:
        return (self - other).sign() < 0
    
    def __le__(self, other: "_PhiNumber") -> bool:
        return (self - other).sign() <= 0
    
    def __gt__(self, other:"_PhiNumber") -> bool:
        return(self - other).sign() > 0
    
    def __ge__(self, other:"_PhiNumber") -> bool:
        return(self - other).sign() >= 0
    
    def __repr__(self) -> str:
        return f"_PhiNumber({self.a}, {self.b})"
    
    def __str__(self) -> str:
        if self.b == 0:
            return f"{self.a}"
        else:
            if self.a == 0:
                return f"{self.b}√5"
            else:
                if self.b > 0:
                    return f"{self.a} + {self.b}√5"
                else:
                    return f"{self.a} - {self.b}√5"