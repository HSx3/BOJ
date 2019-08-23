import sys
sys.stdin = open('벽부수고이동하기_input.txt')


def DFS(x, y, distance, chance):
    global result
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if result < distance:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if data[nx][ny] != 0 and chance == 0:
            continue
        # chance 조건
        if data[nx][ny] != 0 and chance == 1:
            data[nx][ny] = 0
            visited[nx][ny] = 1
            DFS(nx, ny, distance+1, chance-1)
            data[nx][ny] = 1
            visited[nx][ny] = 0
            chance = 1
        # 클리어 조건
        if nx == N-1 and ny == M-1:
            visited[nx][ny] = 1
            distance += 1
            if result > distance:
                result = distance
            return
        if data[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            DFS(nx, ny, distance+1, chance)
            visited[nx][ny] = 0



N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
# print(N, M)
# print(data)
# print(visited)

result = 987654321
visited[0][0] = 1
DFS(0, 0, 1, 1)
if result == 987654321:
    print(-1)
else:
    print(result)