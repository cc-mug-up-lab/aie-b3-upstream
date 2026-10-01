def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("add requires integer arguments")
    return a + b


def multiply(a: int | float, b: int | float) -> int | float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("multiply requires numeric arguments")
    if a < 0 or b < 0:
        raise ValueError("negative numbers are strictly prohibited")
    result = a * b
    if abs(result) > 1_000_000:
        raise ValueError("multiplication overflow limit exceeded")
    return result
