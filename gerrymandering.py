import sys
sys.stdin = open('input.txt','r')
n = int(input())
arr, nsum = [], 0
for _ in range(n):
    row = list(map(int, input().split()))
    nsum += sum(row)
    arr.append(row)
# print(arr)
# print(nsum)

# (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# x축은 0부터 n-2, y축은 1부터 n-1까지 가능
# d1과 d2를 1로 시작해서 d2를 하나씩 늘려간다.
# 범위를 벗어나면 d1을 증가시키고 다시 d2를 1부터 늘려가면서 가능한 모든 d1, d2를 검증한다

# 1 (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# 2 (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# 3 (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# 4 (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)

def divide(r, c, ans):
    for d1 in range(1, n):
        for d2 in range(1, n):
            lr, lc, rr, rc = r + d1, c - d1, r + d2, c + d2
            if rr == n - 1 or rc == n - 1: break
            br, bc = r + d1 + d2, c - d1 + d2
            if br >= n or bc >= n or bc < 0: break
            ans = min(ans, find_min(r, c, lr, lc, rr, rc, bc))
        #if r + d1 == n - 1 or c - d1 == -1: break
    return ans


def find_min(r, c, lr, lc, rr, rc, bc):
    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0

    d = 0
    for i in range(lr):
        for j in range(c + 1):
            if [i, j] == [r + d, c - d]:
                d += 1
                break
            cnt1 += arr[i][j]

    d = 1
    for i in range(rr + 1):
        for j in range(n - 1, c, -1):
            if [i, j] == [r + d, c + d]:
                d += 1
                break
            cnt2 += arr[i][j]

    d = 0
    for i in range(lr, n):
        for j in range(bc):
            if [i, j] == [lr + d, lc + d]:
                d += 1
                break
            cnt3 += arr[i][j]

    d = 1
    for i in range(rr + 1, n):
        for j in range(n - 1, bc - 1, -1):
            if [i, j] == [rr + d, rc - d]:
                d += 1
                break
            cnt4 += arr[i][j]

    cnt5 = nsum - cnt1 - cnt2 - cnt3 - cnt4
    max_cnt = max(cnt1, cnt2, cnt3, cnt4, cnt5)
    min_cnt = min(cnt1, cnt2, cnt3, cnt4, cnt5)
    return max_cnt - min_cnt

ans = sys.maxsize
for i in range(n-2):
    for j in range(1, n-1):
        ans = divide(i, j, ans)
print(ans)