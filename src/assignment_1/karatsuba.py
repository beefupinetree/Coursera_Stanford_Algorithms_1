def karatsuba(int1: int, int2: int) -> int:
    n1 = len(str(int1))
    n2 = len(str(int2))
    if n1 == 1 or n2 == 1:
        return int1 * int2
    max_len = max(n1, n2)
    split_pos = max_len // 2
    a = int1 // 10 ** (split_pos)
    b = int1 % 10 ** (split_pos)
    c = int2 // 10 ** (split_pos)
    d = int2 % 10 ** (split_pos)

    z0 = karatsuba(b, d)
    z1 = karatsuba((a + b), (c + d))
    z2 = karatsuba(a, c)

    return (z2 * 10 ** (2 * split_pos)) + ((z1 - z2 - z0) * 10 ** (split_pos)) + (z0)
