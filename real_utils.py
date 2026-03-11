# real_utils.py

def round_number(x: float, digits: int = 2) -> float:
    return round(x, digits)


def floor_number(x: float) -> int:
    return int(x) if x >= 0 or x == int(x) else int(x) - 1


def ceil_number(x: float) -> int:
    return int(x) if x == int(x) else int(x) + 1 if x > 0 else int(x)


def absolute_float(x: float) -> float:
    return abs(x)


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("0 ga bo‘lish mumkin emas")
    return a / b


def percentage(part: float, whole: float) -> float:
    if whole == 0:
        raise ZeroDivisionError("Butun qiymat 0 bo‘lishi mumkin emas")
    return (part / whole) * 100


def average(numbers: list) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def max_float(numbers: list) -> float:
    return max(numbers)


def min_float(numbers: list) -> float:
    return min(numbers)


def float_summary(numbers: list) -> dict:
    if not numbers:
        return {
            "count": 0,
            "sum": 0,
            "average": 0,
            "min": None,
            "max": None
        }

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": average(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }