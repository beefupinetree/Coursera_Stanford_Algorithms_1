def partition(sub_array: list[int], pivot_index: int) -> list[int]:
    # put the pivot element in the first position
    p = sub_array[pivot_index]
    sub_array = swap(sub_array, 0, pivot_index)

    i = 1
    for j in range(1, len(sub_array)):
        if p > sub_array[j]:
            swap(sub_array, i, j)
            i += 1
    # move the pivot element to it's rightful place
    swap(sub_array, 0, i - 1)

    return sub_array, i - 1  # sub_array[: i - 1], sub_array[i:]


def swap(array: list[int], first_index: int, second_index: int) -> list[int]:
    array[first_index], array[second_index] = array[second_index], array[first_index]
    return array


def quicksort(array: list[int]) -> tuple[list[int], int]:  # ,count: int
    n = len(array)
    if n > 1:
        pi = 0  # Pivot Index
        array, pi = partition(array, pi)
        array[:pi], ops_left = quicksort(array[:pi])
        array[pi + 1 :], ops_right = quicksort(array[pi + 1 :])
        return array, ops_left + ops_right + n - 1
    else:
        return array, 0


if __name__ == "__main__":
    print(quicksort([3, 8, 2, 5, 1, 4, 7, 6]))
