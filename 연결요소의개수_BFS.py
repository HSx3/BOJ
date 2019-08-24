import sys
sys.stdin = open('연결요소의개수_input.txt')


def BFS(v):
    visited[v] = 1
    q = []
    q.append(v)

    while len(q) != 0:
        t = q.pop(0)
        if not visited[t]:
            visited[t] = 1
            node[t-1] = 0
            if visited == [0] + [1]*N:
                return
            # print(t, end=' ')
        for i in range(len(G[t])):
            if G[t][i] == 1 and visited[i] == 0:
                q.append(i)




N, M = map(int, input().split())
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

node = list(range(1, N+1))
count = 0

for i in node:
    if node == [0]*N:
        break
    elif i != 0:
        node[i-1] = 0
        BFS(i)
        count += 1
print(count)