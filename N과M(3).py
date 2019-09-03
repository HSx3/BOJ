import sys
sys.stdin = open('N과M(3)_input.txt')


def DFS(no):
    if no >= M:
        for i in range(N):
            if b[i] != 0:
                print(b[i], end=' ')
        print()
        return
    for i in range(N):
        check[i] = 1
        b[no] = data[i]
        DFS(no + 1)
        check[i] = 0


N, M = map(int, input().split())

data = list(range(1, N+1))
b = [0] * N
check = [0] * N

DFS(0)