import sys
sys.stdin = open('알파벳_input.txt')


def backtrack(x, y, check):
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
            backtrack(nx, ny, check+data[nx][ny])

R, C = map(int, input().split())
data = [list(map(str, input())) for _ in range(R)]
# print(data)
ans = 0
backtrack(0, 0, data[0][0])
print(ans)