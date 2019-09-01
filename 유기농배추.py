import sys
sys.stdin = open('유기농배추_input.txt')


def DFS(x, y):
    visited[x][y] = 1

    stack = []
    stack.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(stack) != 0:
        ax, ay = stack.pop()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if data[nx][ny] == 0:
                continue
            if data[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))


T = int(input())

for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    data = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        u, v = map(int, input().split())
        data[v][u] = 1

    bug = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1 and visited[i][j] == 0:
                DFS(i, j)
                bug += 1

    print(bug)