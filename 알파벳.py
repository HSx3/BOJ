import sys
sys.stdin = open('알파벳_input.txt')


def DFS(x, y, check):
    global ans

    ans = max(ans, len(check))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if data[nx][ny] in check:
            continue
        if data[nx][ny] not in check:
            check.append(data[nx][ny])
            DFS(nx, ny, check)
            check.pop()


R, C = map(int, input().split())
data = [list(map(str, input())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
ans = 0
check = []
check.append(data[0][0])
visited[0][0] = 9
DFS(0, 0, check)
print(ans)
