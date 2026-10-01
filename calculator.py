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

def divide(a: int | float, b: int | float) -> int | float:
    # 物理冲突点：在同一位置新增了函数
    # 语义互斥点：Agent 要求除零抛错，这里偏偏要求返回 0
    if b == 0:
        return 0
    return a / b
