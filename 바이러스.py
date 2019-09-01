import sys
sys.stdin = open('바이러스_input.txt')


def DFS(v):
    global count
    visited[v] = 1

    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            count += 1
            DFS(w)


N = int(input())
M = int(input())

G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

count = 0
DFS(1)
print(count)