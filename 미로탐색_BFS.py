import sys
sys.stdin = open('미로탐색_input.txt')


def BFS(x, y, distance):
    global result

    q = []
    q.append((x, y, distance))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay, distance = q.pop(0)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if data[nx][ny] != 1:
                continue
            if nx == N-1 and ny == M-1:
                if result > distance+1:
                    result = distance+1
                    print(result)

            if data[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = distance+1
                q.append((nx, ny, distance+1))


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
# print(data)
# print(visited)

visited[0][0] = 1
result = 987654321
BFS(0, 0, 1)
# print(result)