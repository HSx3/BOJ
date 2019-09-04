import sys
sys.stdin = open('스타트와링크_input.txt')

def stat(n, tX):
    global start_sum, link_sum

    link = 0
    if n >= 2:
        check_a = []
        check_b = []
        for i in range(0, (N//2)-1):

            if a[i] != 0:
                check_a.append(a[i])
                print(a[i], end=' ')
            if b[i] != 0:
                check_b.append(b[i])
                print(b[i], end=' ')
                # print('check', a[i] - 1, a[i + 1] - 1, data[a[i] - 1][a[i + 1] - 1])
                # start += data[a[i]-1][a[i+1]-1]
                # print('start', start)
        print()
        # print(calc(check_a, check_b))
        start_sum += calc(check_a, check_b)[0]
        link_sum += calc(check_a, check_b)[1]
        print('start_sum', start_sum, link_sum)
        return
    for i in range(len(tX)):
        if check_A[i]:
            continue
        check_A[i] = 1
        # check_B[i] = 1
        a[n] = tX[i]
        # b[n] = tB[i]
        stat(n+1, tX)
        check_A[i] = 0
        # check_B[i] = 0

def calc(X):
    # global min_stat
    stat_sum = 0
    link = 0
    for i in range(0, len(X), 2):
        print(data[X[i]-1][X[i+1]-1])
        # print(data[B[i]-1][B[i+1]-1])
        stat_sum += data[X[i]-1][X[i+1]-1]
        # link += data[B[i]-1][B[i+1]-1]
    return stat_sum



def DFS(no, count):
    if no >= N:
        if count == N//2:
            team_A = []
            team_B = []
            for i in range(N):
                if check[i] != 0:
                    team_A.append(check[i])
                else:
                    team_B.append(i+1)
            stat(0, team_A)
            stat(0, team_B)
            print('-------------')
            # for i in range(N):
            #     print(check[i], end=' ')
            # print()
        return
    check[no] = player[no]
    DFS(no+1, count+1)
    check[no] = 0
    DFS(no+1, count)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
# print(data)
player = list(range(1, N+1))
check = [0] * N
a = [0]*(N//2)
b = [0]*(N//2)
check_A = [0]*(N//2)
check_B = [0]*(N//2)
start_sum = 0
link_sum = 0
min_stat = 987654321
DFS(0, 0)
print('최소값', min_stat)