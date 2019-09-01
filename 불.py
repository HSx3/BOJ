import sys
sys.stdin = open('불_input.txt')
from collections import deque


def fire():
    
    for i in range(h):
        for j in range(w):
            q = deque()
            q.append()

def BFS(x, y, time):
    q = deque()
    q.append((x, y, time))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while len(q) != 0:
        ax, ay, time = q.popleft()
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if data[nx][ny] == '#' or data[nx][ny] == '*':
                continue
            if data[nx][ny] == '.':
                data[ax][ay] = '.'
                data[nx][ny] = '@'

                fire()




T = int(input())

for test_case in range(1, T+1):
    w, h = map(int, input().split())
    data = [list(map(str, input())) for _ in range(h)]
    print(data)

    for i in range(h):
        for j in range(w):
            if data[i][j] == '@':
                BFS(i, j, 1)
                break