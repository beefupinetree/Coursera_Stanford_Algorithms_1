# with open("src/assignment_2/IntegerArray.txt") as f:
#     a = [int(x) for x in f]


def inversions(arr: list[int]):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2

    p = arr[0:mid]
    a, inversion_p = inversions(p)

    q = arr[mid:]
    b, inversions_q = inversions(q)
    c, cross_inversions = _count_cross_inversions(a, b)

    num_inversions = inversion_p + inversions_q + cross_inversions
    return c, num_inversions


def _count_cross_inversions(p: list[int], q: list[int]):
    r = []
    i = j = num_inversion = 0
    while i < len(p) and j < len(q):
        if p[i] > q[j]:
            # if P[1] > Q[j], then P[k] > Q[k] for all  i < k <= len(P)
            # These are all inversions. The claim emerges from the
            # property that P is sorted.
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
