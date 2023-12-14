import math
from fractions import Fraction as Fraction


def s(self: Fraction) -> str:
    return f"{self.numerator}/{self.denominator}"

Fraction.__str__ = s

def pol2(
    a: float,
    b: float,
    c: float
) -> tuple[Fraction | float, Fraction | float]:
    _a = Fraction(a)
    _b = Fraction(b)
    _c = Fraction(c)
    d: Fraction = _b**2 -4*_a*_c
    assert d >= 0, f"Disrciminant {d} < 0!"
    assert a != 0, "a != 0!"
    x1 = Fraction((-b+math.sqrt(d))/(2*a))
    x2 = Fraction((-b-math.sqrt(d))/(2*a))

    x1d = x1.as_integer_ratio()
    if (
        len(str(x1d[0])) >= 3 or len(str(x1d[1])) >= 3
        or x1 % 1 == 0
    ):
        x1 = x1.numerator / x1.denominator

    x2d = x2.as_integer_ratio()
    if (
        len(str(x2d[0])) >= 3 or len(str(x2d[1])) >= 3
        or x2 % 1 == 0
    ):
        x2 = x2.numerator / x2.denominator

    print("\n----------------")
    print(f"({-b} +- √{d})/{2*a}")
    print(f"{a}(x - {round(x1,3)})(x - {round(x2,3)})")
    print("----------------\n")
    return (x1, x2)