import math


def is_prime(n: int):
    """#### For only `n` in ℕ and `n` > 2! """
    assert isinstance(n, int), "p, q must be in ℤ"
    n = abs(n)
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_relative_primes(p: int, q: int):
    """ For only p and q in ℤ """
    assert isinstance(p, int) and isinstance(q, int), "p, q must be in ℤ"
    return lcd(p, q) == 1


def mul[Number: (int, float)](p: Number, *args: Number)-> Number:
    for q in args:
        p *= q
    return p


def lcd(*args: int):
    """ Least common divison """
    return (round(mul(*args)) // math.lcm(*args)) or 1 # C implementation


class _Divisors(tuple[int, ...]):
    def __repr__(self):
        return f"{self.__class__.__name__}({self.origin})"
    #
    @property
    def origin(self):
        return self[0] * self[len(self) - 1] if len(self) > 1 else 0
    #
    @property
    def uppers(self):
        return tuple([n for n in self if  abs(n) > self._sqrt()])
    #
    @property
    def lowers(self):
        return tuple([n for n in self if  abs(n) < self._sqrt()])
    #
    def in_couples(self):
        lw = self.lowers
        up = self.uppers
        out: list[tuple[int, int]] = []
        for i in range(len(lw)):
            out.append((lw[i], up[len(lw) - 1 - i]))
        return out
    #
    def _sqrt(self):
        if not hasattr(self, "__sqrt"):
            self.__sqrt = math.sqrt(abs(self.origin))
        return self.__sqrt
    #
    def __iadd__(self, t2: tuple[int, ...]):
        return self.__class__(self[:len(self) // 2] + t2 + self[len(self) // 2:])
    #
    __add__ = __iadd__


def divisors(n: int) -> _Divisors:
    out = _Divisors()
    CONST = -1 if n < 0 else 1
    n = abs(n)
    i = 1
    while i*i <= n:
        if n % i == 0:
            if CONST == -1:
                out += ((i, CONST * n // i))
                out += ((CONST * i, n // i))
            else:
                out += ((i, n // i))
                out += ((-i, -(n // i)))
        i += 1
    return out


def prime_factors(n: int) -> list[int]:
    i = 2
    factors: list[int] = []
    while i*i <= abs(n):
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors += [i]
    if n > 1:
        factors += (n,)
    return factors


def median(v: list[int]) -> float | int:
    if len(v) % 2 == 0:
        return (v[len(v) // 2] + v[len(v) // 2 + 1]) / 2
    return v[len(v) // 2]


def human_readable(n: float, sep: str = ' ') -> str:
    integer, decimal = str(int(n)),  n - int(n)
    out = ""
    for i in range(len(integer) - 1, -1, -1):
        out = integer[i] + out
        if len(out.replace(sep, '')) % 3 == 0:
            out = sep + out
    if decimal:
        return out + str(decimal)[1:]  # xxx + .5
    return out
