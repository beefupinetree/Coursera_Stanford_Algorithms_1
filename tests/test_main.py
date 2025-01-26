import pytest
from pathlib import Path
from assignment_1.karatsuba import karatsuba
from assignment_2.count_inversions import inversions
from assignment_3.Quicksort import quicksort
from assignment_4.minimum_cut import KargerMinCut


# @pytest.fixture
def read_file(file_path: str) -> list[int]:
    file = Path(file_path)  # "src/assignment_2/IntegerArray.txt"
    return open(file).readlines()


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


@pytest.mark.parametrize(
    "in_array, expected",
    [
        ([1, 4, 3], 1),
        ([3, 2, 1, 5], 3),
        ([2, 2, 2], 0),
    ],
)
def test_inversions(in_array: list, expected: int) -> None:
    assert inversions(in_array)[1] == expected


def test_inversions_with_file() -> None:
    input_file = "src/assignment_2/IntegerArray.txt"
    assert inversions(read_file(input_file))[1] == 2397819672


def test_quicksort_with_file() -> None:
    input_file = "src/assignment_3/QuickSort.txt"
    assert quicksort(read_file(input_file))[1] == 153461
    assert quicksort([3, 8, 2, 5, 1, 4, 7, 6])[1] == 15


def test_min_cut_with_file() -> None:
    input_file = "src/assignment_4/kargerMinCut.txt"
    assert KargerMinCut(read_file(input_file))[1] == 153461
