import sys
sys.stdin = open('연산자끼워넣기_input.txt')


def calc(temp, mix_o):
    global answer

    cal = 0
    if mix_o[0] == '+':
        cal = temp[0]+temp[1]
    elif mix_o[0] == '-':
        cal = temp[0]-temp[1]
    elif mix_o[0] == '*':
        cal = temp[0]*temp[1]
    elif mix_o[0] == '/':
        if temp[0] < 0:
            cal = abs(temp[0])//temp[1]
            cal = -(cal)
        else:
            cal = temp[0]//temp[1]

    i = 1
    while i != K:
        if mix_o[i] == '+':
            cal += temp[i+1]
        elif mix_o[i] == '-':
            cal -= temp[i+1]
        elif mix_o[i] == '*':
            cal *= temp[i+1]
        elif mix_o[i] == '/':
            if cal < 0:
                cal = abs(cal)//temp[i+1]
                cal = -(cal)
            else:
                cal //= temp[i+1]
        i += 1
    answer.append(cal)

def DFS(no):
    if no >= K:
        calc(numbers, a)
        return

    for i in range(0, K):
        if visited[i]:
            continue
        a[no] = operator_list[i]
        visited[i] = 1
        DFS(no+1)
        visited[i] = 0


N = int(input())
numbers = list(map(int, input().split()))
operator_num = list(map(int, input().split()))

operator_list = ''

for i in range(4):
    if i == 0:
        operator_list += '+' * operator_num[i]
    if i == 1:
        operator_list += '-' * operator_num[i]
    if i == 2:
        operator_list += '*' * operator_num[i]
    if i == 3:
        operator_list += '/' * operator_num[i]

answer = []
operator_list = list(operator_list)

K = len(operator_list)
a = [0] * K
visited = [0] * (K+1)
DFS(0)

print(max(answer))
print(min(answer))