import sys
from collections import deque
sys.stdin = open('숨바꼭질_input.txt')


def BFS(x, time):
    global N, K, check, seconds
    dx = [-1, 1, 2]

    q = deque()
    q.append((x, time))

    while len(q) != 0:
        ax, time = q.popleft()

        if ax == K:
            seconds = time
            return

        for i in range(3):
            if i != 2:
                nx = ax + dx[i]
            else:
                nx = ax * dx[i]

            if nx >= 100001:
                continue
            elif 0 <= nx < 100001:
                if visited[nx] == 0:
                    visited[nx] = 1
                    q.append((nx, time + 1))


N, K = map(int, input().split())

dx = [-1, 1, 2]
visited = [0] * 100001
visited[N] = 1
seconds = 0
BFS(N, 0)
print(seconds)