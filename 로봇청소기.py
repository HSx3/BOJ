import sys
sys.stdin = open('로봇청소기_input.txt')


# 왼쪽 탐색
def search_left(x, y, direction):
    if d == 0:
        nx = r
        ny = c - 1
    elif d == 1:
        nx = r - 1
        ny = c
    elif d == 2:
        nx = r
        ny = c + 1
    elif d == 3:
        nx = r + 1
        ny = c

    return nx, ny, direction


# 뒤쪽 체크
def back(x, y, direction, all):
    if d == 0:
        nx = r + 1
        ny = c
    elif d == 1:
        nx = r
        ny = c - 1
    elif d == 2:
        nx = r - 1
        ny = c
    elif d == 3:
        nx = r
        ny = c + 1

    return nx, ny


# 모든 방향 탐색
def search_all(x, y, direction, check):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        check.append(data[nx][ny])
    return check


N, M = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

# print(N, M)
# print(r, c, d)
# print(data)

count = 0
while True:
    # 현재 위치 청소
    if data[r][c] == 0:
        data[r][c] = 2
        count += 1
    # 모든 방향 탐색
    all = search_all(r, c, d, [])

    # 뒤쪽 체크
    if all.count(1) == 4:
        nx, ny = back(r, c, d, all)
        # d
        if data[nx][ny] == 1:
            break
        # c
        elif data[nx][ny] == 2:
            r = nx
            c = ny

    elif all.count(1) == 3 and all.count(2) == 1:
        nx, ny = back(r, c, d, all)
        # d
        if data[nx][ny] == 1:
            break
        # c
        elif data[nx][ny] == 2:
            r = nx
            c = ny

    elif all.count(1) == 2 and all.count(2) == 2:
        nx, ny = back(r, c, d, all)
        # d
        if data[nx][ny] == 1:
            break
        # c
        elif data[nx][ny] == 2:
            r = nx
            c = ny

    elif all.count(1) == 1 and all.count(2) == 3:
        nx, ny = back(r, c, d, all)
        # d
        if data[nx][ny] == 1:
            break
        # c
        elif data[nx][ny] == 2:
            r = nx
            c = ny

    elif all.count(2) == 4:
        nx, ny = back(r, c, d, all)
        # d
        if data[nx][ny] == 1:
            break
        # c
        elif data[nx][ny] == 2:
            r = nx
            c = ny

    else:
        # 왼쪽 탐색
        nx, ny, d = search_left(r, c, d)

        # 2 - a
        if data[nx][ny] == 0:
            if d == 0:
                d = 3
            elif d == 1:
                d = 0
            elif d == 2:
                d = 1
            elif d == 3:
                d = 2
            # data[nx][ny] = 2
            r = nx
            c = ny

        # 2 - b
        elif data[nx][ny] == 1 or data[nx][ny] == 2:
            if d == 0:
                d = 3
            elif d == 1:
                d = 0
            elif d == 2:
                d = 1
            elif d == 3:
                d = 2

print(count)