import sys
sys.stdin = open('N과M(4)_input.txt')


def DFS(no, k):
    if no >= M:
        for i in range(N):
            if b[i] != 0:
                print(b[i], end=' ')
        print()
        return
    for i in range(k, N+1):
        b[no] = i
        DFS(no + 1, i)


N, M = map(int, input().split())

data = list(range(1, N+1))
b = [0] * N
check = [0] * N

DFS(0, 1)