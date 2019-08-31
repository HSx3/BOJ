import sys
sys.stdin = open('숨바꼭질_input.txt')


def DFS(no, x, cnt, time):
    global N, K
    dx = [-1, 1, 2]
    if no >= 3:
        time += 1
        if cnt == 1:
            if N == K:
                print(N)
                print(time)
            # for i in range(3):
            #     print(check[i], end=' ')
            # print()
        return
    for i in range(3):
        if i != 2:
            N = x + dx[i]
            check[no] = N
            DFS(no + 1, N, cnt+1, time)
            check[no] = 0
            DFS(no + 1, N, cnt, time)
        else:
            N = x * dx[i]
            check[no] = N
            DFS(no + 1, N, cnt + 1, time)
            check[no] = 0
            DFS(no + 1, N, cnt, time)
    # check[no] = N
    # DFS(no+1, N, cnt+1)
    # check[no] = 0
    # DFS(no+1, N, cnt)



N, K = map(int, input().split())

dx = [-1, 1, 2]
check = [0] * 3

DFS(0, N, 0, 0)