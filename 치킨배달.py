import sys
sys.stdin = open('치킨배달_input.txt')
import copy

def select(no, count):
    global min_distances
    if no >= K:
        if sum(check) == 0:
            return
        else:
            # for i in range(M):
            #     if check[i] == 1:
            #         temp = copy.deepcopy(data)
            #         temp[chickenlist[i][0]][chickenlist[i][1]] = 2
                    # visited = [[0 for _ in range(N)] for _ in range(N)]
            if count == M:
                for j in range(N):
                    for k in range(N):
                        if data[j][k] == 1:
                            print('j, k', j, k)
                            min_distance = 987654321
                            for i in range(K):
                                if check[i] == 1:
                                    print('치킨집', chickenlist[i][0], chickenlist[i][1])
                                    distance = abs(j-chickenlist[i][0]) + abs(k-chickenlist[i][1])
                                    print('거리', distance)
                                    if distance < min_distance:
                                        min_distance = distance
                            print('최소거리', min_distance)
                            # return
                            min_distances.append(min_distance)
                # print('j, k', j, k)
                # min_distances.append(min_distance)

                #     print(check[i], end=' ')
                # print()
            return

    check[no] = 1
    select(no+1, count+1)
    check[no] = 0
    select(no+1, count)

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
print(N, M)
print(data)


# visited = [[0 for _ in range(N)] for _ in range(N)]



chickenlist = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chickenlist.append([i, j])
print(chickenlist)
K = len(chickenlist)
check = [0] * K
# check = [(0, 0)] * len(chickenlist)
print(check)


min_distances = []

# print('check', check[0])
# for i in range(M):
#     data[check[i][0]][check[i][1]] = 0
select(0, 0)

print('?', min_distances)



'''
import sys
sys.stdin = open('치킨배달_input.txt')
import copy

def select(no, count):
    global min_distances
    if no >= K:
        if count == M:
            for i in range(K):
                print(check[i], end=' ')
            print()
        return

    check[no] = 1
    select(no+1, count+1)
    check[no] = 0
    select(no+1, count)

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
print(N, M)
print(data)






chickenlist = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chickenlist.append([i, j])
print(chickenlist)
K = len(chickenlist)
check = [0] * K

print(check)




select(0, 0)



'''