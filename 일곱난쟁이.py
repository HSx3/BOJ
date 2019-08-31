import sys
sys.stdin = open('일곱난쟁이_input.txt')


def DFS(no, nsum, count):
    global seven, flag
    if nsum > 100:
        return
    if no >= N:
        if nsum == 100 and count == 7:
            if flag == 0:
                flag = 1
                for i in range(N):
                    if check[i] != 0:
                        seven.append(check[i])
        return

    check[no] = data[no]
    DFS(no+1, nsum+check[no], count+1)
    check[no] = 0
    DFS(no+1, nsum, count)

N = 9
data = []
check = [0] * 9
seven = []
flag = 0

for i in range(9):
    data.append(int(input()))

DFS(0, 0, 0)
seven.sort()

for i in seven:
    print(i)