def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("add requires integer arguments")
    return a + b


def multiply(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("multiply requires integer arguments")
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    # 物理冲突点：在同一位置新增了函数
    # 语义互斥点：Agent 要求除零抛错，这里偏偏要求返回 0
    if b == 0:
        return 0
    return a / b
