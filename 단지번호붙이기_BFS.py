import sys
sys.stdin = open('단지번호붙이기_input.txt')


def BFS(x, y):
    global house

    visited[x][y] = 1
    q = []
    q.append((x,y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay = q.pop(0)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if data[nx][ny] != 1:
                continue
            if data[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                house += 1
                q.append((nx, ny))




N = int(input())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
# print(data)
# print(visited)

count = 0
house_list = []

for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and visited[i][j] == 0:
            house = 1
            BFS(i, j)
            house_list.append(house)
            count += 1

house_list.sort()
print(count)
for i in house_list:
    print(i)