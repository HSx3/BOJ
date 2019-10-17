import sys
sys.stdin = open('DFS와BFS_input.txt')

def DFS(v):
    visited[v] = 1
    print(v, end=' ')

    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            DFS(w)

def BFS(v):
    visited = [0] * (N+1)

    q = []
    q.append(v)

    while len(q) != 0:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, N+1):
                if G[v][w] == 1 and visited[w] == 0:
                    q.append(w)


N, M, V = map(int, input().split())

G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1


DFS(V)
print()
BFS(V)
print()