import sys
sys.stdin = open('미로탐색_input.txt')


def DFS(x, y, distance):
    global flag, result
    # visited[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if result < distance:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if data[nx][ny] != 1:
            continue
        if nx == N-1 and ny == M-1:
            visited[nx][ny] = 1
            distance += 1

            if result > distance:
                result = distance
            # for i in visited:
            #     print(*i)
            # print()
            # print(distance)
            return
        if data[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = distance+1
            DFS(nx, ny, distance+1)
            visited[nx][ny] = 0


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

# print(data)
# print(visited)

# distance = 0
flag = 0

result = 987654321
visited[0][0] = 1
DFS(0, 0, 1)
print(result)