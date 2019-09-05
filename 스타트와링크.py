import sys
sys.stdin = open('스타트와링크_input.txt')


def DFS(no, count):
    global min_stat
    if no >= N:
        if count == N // 2:
            team_A = []
            team_B = []
            for i in range(N):
                if check[i] != 0:
                    team_A.append(check[i])
                else:
                    team_B.append(i + 1)
            # print('-------------')

            start_sum = 0
            link_sum = 0

            for i in range(N + 1):
                for j in range(N + 1):
                    if i != j:
                        if i in team_A and j in team_A:
                            start_sum += data[i - 1][j - 1]
                        if i in team_B and j in team_B:
                            link_sum += data[i - 1][j - 1]
            if min_stat > abs(start_sum - link_sum):
                min_stat = abs(start_sum - link_sum)
        return

    check[no] = player[no]
    DFS(no + 1, count + 1)
    check[no] = 0
    DFS(no + 1, count)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

player = list(range(1, N + 1))
check = [0] * N

min_stat = 987654321
DFS(0, 0)
print(min_stat)