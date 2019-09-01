import sys
sys.stdin = open('안전영역_input.txt')
import copy
from collections import deque

def BFS(x, y):
    q = deque()
    q.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay = q.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] != 0:
                continue
            if 0 < temp[nx][ny] <= 100 and visited[nx][ny] == 0:
                visited[nx][ny] = 999
                q.append((nx, ny))



N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

safezone = 0
top = 0

# 최대 높이 확인
for i in range(N):
    for j in range(N):
        if top < data[i][j]:
            top = data[i][j]
# print(top)
while top >= 1:
    safe = 0


    temp = copy.deepcopy(data)
    for i in range(N):
        for j in range(N):
            if temp[i][j] < top:
                temp[i][j] = 0

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # safe = 0
            if temp[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 999
                # temp[i][j] = 999
                BFS(i, j)
                safe += 1
                if safezone < safe:
                    safezone = safe
    top -= 1
    # print(safezone)
print(safezone)