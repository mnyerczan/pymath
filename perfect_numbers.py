def is_perfect_num(n: int) -> int:
    """
    >>> is_perfect_num(6)
    True
    >>> is_perfect_num(28)
    True
    >>> is_perfect_num(496)
    True
    >>> is_perfect_num(500)
    False
    """
    return sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

def perfect_numbers(max: int) -> list[int]:
    """
    >>> perfect_numbers(10)
    [6]
    >>> perfect_numbers(10**2)
    [6, 28]
    >>> perfect_numbers(496)
    [6, 28, 496]
    >>> perfect_numbers(10**3)
    [6, 28, 496]
    """
    res: list[int] = []
    for i in range(1, max + 1):
        if is_perfect_num(i):
            res.append(i)
    return res
