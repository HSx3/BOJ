import sys
sys.stdin = open('인구이동_input.txt')


def while_BFS(x, y):
    global flag
    while_visited = [[0 for _ in range(N)] for _ in range(N)]
    while_visited[0][0] = 999
    q = []
    q.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay = q.pop(0)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if while_visited[nx][ny] != 0:
                continue
            if while_visited[nx][ny] == 0:
                while_visited[nx][ny] = 999
                q.append((nx, ny))
            if L <= abs(data[nx][ny] - data[ax][ay]) <= R:
                flag = 0    # else로
                return

#
def off(check):
    global off_flag
    off_flag = 0
    total = 0
    country = len(check)
    for i in check:
        total += data[i[0]][i[1]]
    # print(total)
    move = total // country
    for i in check:
        data[i[0]][i[1]] = move

    for i in data:
        print(*i)
    print()



# 인구체크
def BFS(x, y):
    global check
    q = []
    q.append((x, y))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay = q.pop(0)

        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] != 0:
                continue
            if L <= abs(data[nx][ny]-data[ax][ay]) <= R and visited[nx][ny] == 0:
                visited[nx][ny] = 999
                check.append((ax, ay))
                check.append((nx, ny))
                q.append((nx, ny))

N, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
count = 0

while True:
    # while 조건
    flag = 1
    while_BFS(0, 0)
    if flag:
        break

    else:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        off_flag = 1
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    check = []
                    visited[i][j] = 999
                    BFS(i, j)
                    check = list(set(check))
                    if len(check) != 0:
                        off(check)
        print('--------')
        if off_flag == 0:
            count += 1
print(count)