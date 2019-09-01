import sys
sys.stdin = open('보물섬_input.txt')
from collections import deque

def BFS(x, y, distance):

    q = deque()
    q.append((x, y, distance))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay, distance = q.popleft()

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if data[nx][ny] != 'L':
                continue
            if data[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = 99
                q.append((nx, ny, distance+1))
    return distance


N, M = map(int, input().split())
data = [list(map(str, input())) for _ in range(N)]

max_distance = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 'L':
            visited = [[0 for _ in range(M)] for _ in range(N)]
            visited[i][j] = 99
            check_distance = BFS(i, j, 0)
            if max_distance <= check_distance:
                max_distance = check_distance
print(max_distance)
