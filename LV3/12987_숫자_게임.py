from collections import deque


def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    qA = deque(A)
    qB = deque(B)
    if min(A) < max(B):
        while qB:
            numB = qB.popleft()
            for numA in qA:
                if numB > numA:
                    answer += 1
                    qA.popleft()
                    break
    else:
        for i in range(len(A)):
            if B[i] > A[i]:
                answer += 1

    return answer