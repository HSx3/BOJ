def DFS(v):
    visited[v] = 1

    u_list[v] = 0

    for w in range(1, N+1):
        if G[v][w]== 1 and visited[w] == 0:
            DFS(w)

N, M = map(int, input().split())
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N+1)

u_list = list(range(N+1))
for i in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

count = 0
for i in u_list:
    if i != 0:
        DFS(i)
        count += 1
print(count)