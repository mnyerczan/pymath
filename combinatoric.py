import typing as _t



#
# itertools.permutations
#
def permutations[T](iterable: _t.Iterable[T], r: int | None) -> _t.Generator[tuple[T, ...], _t.Any, None]:
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r   # permutation group
    if r > n:
        return
    indices = list(range(n))    # Indexek
    cycles = list(range(n, n-r, -1))  # ???
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def factorial(n: int) -> int:
    return n * factorial(n - 1) if n > 1 else 1


def f_variations(n: int) -> list[list[bool]]:
    """
    >>> from pprint import pp
    >>> pp(f_variations(1))
    [[True], [False]]
    >>> pp(f_variations(4))
    [[True, True, True, True],
     [True, True, True, False],
     [True, True, False, True],
     [True, True, False, False],
     [True, False, True, True],
     [True, False, True, False],
     [True, False, False, True],
     [True, False, False, False],
     [False, True, True, True],
     [False, True, True, False],
     [False, True, False, True],
     [False, True, False, False],
     [False, False, True, True],
     [False, False, True, False],
     [False, False, False, True],
     [False, False, False, False]]
    """
    out: list[list[bool]] = [[] for _ in range(2**n)]  # Reference!
    for i in range(n):  # vertikalis
        counter = 0
        lim: int = 2**n / 2**(i + 1)     # Helyiérték szerinti csoportméret
        # kiszámítása: ..., 8, 4, 2
        for j in range(len(out)):  # Horozontális
            counter += 1
            out[j].append(counter <= lim)
            if counter == 2*lim:
                counter = 0
    return out


def bool_variations(n: int) -> _t.Generator[tuple[bool, ...], _t.Any, None]:
    """
    # Test
    >>> for v in bool_variations(1): print(v)
    (True,)
    (False,)
    >>> for v in bool_variations(3): print(v)
    (True, True, True)
    (True, True, False)
    (True, False, True)
    (True, False, False)
    (False, True, True)
    (False, True, False)
    (False, False, True)
    (False, False, False)
    """
    # Initial values of output
    # [..., True, True, True]
    values = [True for _ in range(n)]
    # Reverse indices
    # i. e. [..., 2, 1, 0]
    r_idxs = range(n - 1, -1, -1)
    # Values of powers of two
    # i. e. [..., 4, 2, 1]
    masses: list[int] = [2**i for i in r_idxs]
    yield tuple(values)
    for i in range(1, 2**n, 1):
        for j in r_idxs:
            if i % masses[j] == 0:
                values[j] = not values[j]
        yield tuple(values)


def variations[T](
    iterable: _t.Iterable[T],
    k: _t.Optional[int] = None,
    repetitive: bool = True
) -> _t.Iterable[tuple[T, ...]]:
    """
    ## Definition
    ... later
    >>> v = variations([1, 2, 'a'])
    >>> next(v)
    (1, 1, 1)
    >>> next(v)
    (1, 1, 2)
    >>> for _ in range(15): r = next(v)
    >>> for _ in range(5): next(v)
    (2, 'a', 'a')
    ('a', 1, 1)
    ('a', 1, 2)
    ('a', 1, 'a')
    ('a', 2, 1)
    >>> from pprint import pp
    >>> pp(list(variations([1,2,3,1,1,4],k=4, repetitive=False))[10:-8])
    [(2, 4, 1, 3),
     (2, 4, 3, 1),
     (3, 1, 2, 4),
     (3, 1, 4, 2),
     (3, 2, 1, 4),
     (3, 2, 4, 1)]
    >>> pp(list(variations([1, 2, 'a', 2, 4, 5, 6, 8, 7, 9, 10], k=13, repetitive=False)))
    []
    """
    assert isinstance(iterable, _t.Iterable), "Please Iterable, you fucking dickhead!!!"
    assert isinstance(k, (int)) or k is None, "Please int or None, you fucking dickhead!!!"
    assert isinstance(repetitive, bool), "Please bool, you fucking dickhead!!!"
    # If repetition not allowed
    if not repetitive:
        iterable = list(set(iterable))
    POOL = tuple(set(iterable))
    # (x axes), length of each series
    N = k if k else len(tuple(iterable))
    # For performance reason
    if not repetitive and k and k > len(tuple(iterable)):
        return
    # Counter indicies, which items how many changes.
    indicies = [0 for _ in range(N)]
    # Reverse indices, for number places i. e. [..., 2, 1, 0]
    R_IDXS = range(N - 1, -1, -1)
    # Values of powers of two i. e. [..., 4, 2, 1]
    MASSES: list[int] = [len(POOL)**i for i in R_IDXS]
    f0 = lambda: tuple([POOL[i] for i in indicies])
    # CHECK: Item(tuple) must be not redundand if r != None
    def f1(item: tuple[T,...]) -> bool:
        return repetitive or len(set(item)) == N
    if f1(res:=f0()):
        yield res
    # (y axes), count of all cases
    pool_len = len(POOL)
    for i in range(1, pool_len**N , 1):
        for j in R_IDXS:
            # Calculate by place value
            if i % MASSES[j] == 0:
                if indicies[j] == pool_len - 1:
                    indicies[j] = 0
                else:
                    indicies[j] += 1
        if f1(res:=f0()):
            yield res


def f(*args: int, **kw_args: _t.Any):
     return  list(args) + [int(e) for e in kw_args.values()]


def run(pred: _t.Callable[[bool], bool]):
    kys = pred.__annotations__.keys()
    argnum = len(kys) - 1 if "return" in kys else len(kys)
    for args in bool_variations(argnum):
        if not pred(*list(args)):
            print(f"{pred.__name__} {args} -> False")
            return
    print(f"{pred.__name__} -> True")


def is_p(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
