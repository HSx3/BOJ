import sys
sys.stdin = open('토마토_input.txt')
from collections import deque

def BFS(x, y, days):
    global check, total

    q = deque()
    q = check

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay, days = q.popleft()
        visited[ax][ay] = 1
        total -= 1

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if data[nx][ny] == -1:
                continue
            if data[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, days+1))
    return days

M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
check = deque()
total = M*N
answer = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            check.append((i, j, 0))
        if data[i][j] == -1:
            total -= 1

answer = BFS(0, 0, 0)

if total:
    print(-1)
else:
    print(answer)
