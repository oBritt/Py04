

def square(x: int | float) -> int | float:
    """squaring a number"""
    return x * x


def pow(x: int | float) -> int | float:
    """exponatiating number by itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        """inner function"""
        nonlocal count
        nonlocal x
        x = function(x)
        return x

    return inner
