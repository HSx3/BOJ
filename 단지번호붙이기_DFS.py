import sys
sys.stdin = open('단지번호붙이기_input.txt')


def DFS(x, y):
    global house
    # 방문체크
    visited[x][y] = 1
    # 가구수 체크
    house += 1

    # 우, 좌, 하, 상
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 벽처리
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        # 단지 아닌 경우
        if data[nx][ny] != 1:
            continue
        if data[nx][ny] == 1 and visited[nx][ny] == 0:
            DFS(nx, ny)

N = int(input())

data = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

count = 0
house_list = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and visited[i][j] == 0:
            house = 0
            DFS(i, j)
            count += 1
            house_list.append(house)
print(count)
house_list.sort()
for i in house_list:
    print(i)