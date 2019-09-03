import sys
sys.stdin = open('치킨배달_input.txt')

def select(no, count):
    global min_distances
    if no >= K:
        if sum(check) == 0:
            return
        else:
            if count == M:
                b = 0
                for j in range(N):
                    for k in range(N):
                        if data[j][k] == 1:
                            min_distance = 987654321
                            for i in range(K):
                                if check[i] == 1:
                                    distance = abs(j-chickenlist[i][0]) + abs(k-chickenlist[i][1])
                                    if distance < min_distance:
                                        min_distance = distance
                            b += min_distance
                min_distances.append(b)
            return

    check[no] = 1
    select(no+1, count+1)
    check[no] = 0
    select(no+1, count)

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

chickenlist = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chickenlist.append([i, j])

K = len(chickenlist)
check = [0] * K

min_distances = []
select(0, 0)

print(min(min_distances))