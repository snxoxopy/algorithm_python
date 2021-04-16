import sys
sys.stdin = open('input.txt','r')
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result = sys.maxsize


def maketeam(idx, cnt):
    if cnt == n // 2:
        global result
        start = 0  # 스타트팀합
        link = 0
        lst_start = []  # 담아서 비교
        lst_link = []
        for i in range(n):
            if visited[i]:
                lst_start.append(i)
            else:
                lst_link.append(i)
        print('lst_start', lst_start, 'lst_link', lst_link)

        for i in range(len(lst_start)):
            for j in range(len(lst_link)):
                #print('lst_start[%d] = %d, lst_start[%d] = %d' %(i, lst_start[i], j, lst_start[j]))
                print('arr[lst_start[%d]][lst_start[%d]] = %d' %(i, j, arr[lst_start[i]][lst_start[j]]))
                start += arr[lst_start[i]][lst_start[j]]
                link += arr[lst_link[i]][lst_link[j]]
        result = min(result, abs(start-link))
        return
        # 모두 더해서 두수의 차비교
    else:
        for i in range(idx, n):
            if not visited[i]:  # 팀정하기
                visited[i] = True
                print('visited[%d]=True' %i)
                maketeam(i, cnt+1)
                visited[i] = False


visited[0] = True  # 1을 팀에 넣고 시작한다 반으로 줄어든다.
maketeam(1, 1)
print(result)
