# int_utils.py

def is_even(n: int) -> bool:
    return n % 2 == 0


def is_odd(n: int) -> bool:
    return n % 2 != 0


def is_positive(n: int) -> bool:
    return n > 0


def is_negative(n: int) -> bool:
    return n < 0


def absolute_value(n: int) -> int:
    return abs(n)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial manfiy son uchun aniqlanmagan")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))


def digit_count(n: int) -> int:
    return len(str(abs(n)))


def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else 0


def power(base: int, exp: int) -> int:
    return base ** exp


def is_perfect_number(n: int) -> bool:
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


def to_binary(n: int) -> str:
    return bin(n)[2:] if n >= 0 else "-" + bin(abs(n))[2:]


def to_octal(n: int) -> str:
    return oct(n)[2:] if n >= 0 else "-" + oct(abs(n))[2:]


def to_hexadecimal(n: int) -> str:
    return hex(n)[2:] if n >= 0 else "-" + hex(abs(n))[2:]