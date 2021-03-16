input = [i for i in range(100)]
n = 100


def _bin_search(lst, n, k):
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == k: return True
        if lst[mid] > k: hi = mid - 1
        else: lo = mid + 1
    return False


print(_bin_search(input, n, 28))
