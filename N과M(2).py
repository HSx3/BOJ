import sys
sys.stdin = open('N과M(2)_input.txt')


def DFS(no, count):
    if no >= N:
        if count == M:
            for i in range(N):
                if check[i] != 0:
                    print(check[i], end=' ')
            print()
        return
    check[no] = data[no]
    DFS(no+1, count+1)
    check[no] = 0
    DFS(no+1, count)

N, M = map(int, input().split())

data = list(range(1, N+1))
check = [0]*N

DFS(0, 0)