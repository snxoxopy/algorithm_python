# https://www.acmicpc.net/problem/9012

# 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO
# 이해: 5분
# 풀이: 15분
# 구현: 25분
# Debug: 3분
import sys
import timeit

sys.stdin = open("input.txt", "r")


# 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다.
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
# 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

t = int(sys.stdin.readline())
print(t)

lst_prths = [list(map(str, sys.stdin.readline().strip('\n'))) for _ in range(t)]

print(lst_prths)

# 주소 접근
t_start = timeit.default_timer()

for i in range(t):
    res = []
    for j in range(len(lst_prths[i])):
        if lst_prths[i][j] == "(":
            res.append(lst_prths[i][j])
        elif lst_prths[i][j] == ")":
            if res: res.pop()
            else:
                res.append(1)
                break
    #print(res)
    ans = "NO" if res else "YES"
    print(ans)

t_end = timeit.default_timer()

print("소요시간 %f[ms]" %((t_end - t_start)*1000))

# index 접근
t_start = timeit.default_timer()

for prth in lst_prths:
    res = []
    for j in prth:

        if j == "(":
            res.append(j)
        else:
            if res: res.pop()
            else:
                res.append(1)
                break
    #print(res)
    ans = "NO" if res else "YES"
    print(ans)

t_end = timeit.default_timer()

print("소요시간 %f[ms]" %((t_end - t_start)*1000))


# 객체? 접근
# len(append) == len(pop) -> VPS

#ans = "YES" if res == True else "NO"