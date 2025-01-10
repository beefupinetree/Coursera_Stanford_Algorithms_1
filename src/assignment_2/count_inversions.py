# with open("src/assignment_2/IntegerArray.txt") as f:
#     a = [int(x) for x in f]


def inversions(arr: list[int]):
    print(f"arr is {arr}")
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2

    p = arr[0:mid]
    a, inversion_p = inversions(p)
    print(f"a is {a}")

    q = arr[mid:]
    b, inversions_q = inversions(q)
    print(f"a is {a}, b is {b}")
    c, cross_inversions = _count_cross_inversions(a, b)

    num_inversions = inversion_p + inversions_q + cross_inversions
    return c, num_inversions


def _count_cross_inversions(p: list[int], q: list[int]):
    # and sort
    r = []
    print(f"p is {p}, q is {q}")
    i = 0
    j = 0
    num_inversion = 0
    while i < len(p) and j < len(q):
        if p[i] > q[j]:
            # if P[1] > Q[j], then P[k] > Q[k] for all  i < k <= len(P)
            # These are all inversions. It assumes that 'p' is sorted.
            num_inversion += len(p) - i
            r.append(q[j])
            j += 1
        else:
            r.append(p[i])
            i += 1

    if i < len(p):
        r.extend(p[i:])
    else:
        r.extend(q[j:])

    return r, num_inversion


if __name__ == "__main__":
    inversions([3, 2, 1, 5])
