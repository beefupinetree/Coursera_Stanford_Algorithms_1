import pytest
from assignment_1.karatsuba import karatsuba


@pytest.mark.parametrize(
    "int1, int2, expected",
    [
        (10, 10, 100),
        (100, 100, 10000),
        (5678, 1234, 7006652),
        (12389, 123, 1523847),
    ],
)
def test_karatsuba(int1: int, int2: int, expected: int) -> None:
    assert karatsuba(int1, int2) == expected
