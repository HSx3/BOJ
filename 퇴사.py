import sys
sys.stdin = open('퇴사_input.txt')

N = int(input())
schedule = [0] * (N+1)
print(schedule)
# data = [(0, 0, 0)]
data = []
for i in range(1, N+1):
    Ti, Pi = map(int, input().split())
    data.append((i, Ti, Pi))
print(data)
# sort_data = sorted(data, key=lambda x:x[2], reverse=True)
# print(sort_data)
max_income = 0
income = 0
# i = N
# while i > 0:

for i in range(N, 0, -1):
    if data[i-1][0] + data[i-1][1]-1 <= N:
        print(i, schedule[data[i-1][0]:data[i-1][0]+data[i-1][1]])
        if 99 in schedule[data[i-1][0]:data[i-1][0]+data[i-1][1]]:
            continue
        else:
            for j in range(0, data[i-1][1]):
                schedule[data[i-1][0]+j] = 99
            income += data[i-1][2]
            # print(i)
            # print(schedule)
if max_income < income:
    max_income = income
print(max_income)
income = 0
schedule = [0] * (N+1)
for i in range(1, N):
    if data[i-1][0] + data[i-1][1]-1 <= N:
        print(i, schedule[data[i-1][0]:data[i-1][0]+data[i-1][1]])
        # print(data[i-1][0], data[i-1][0]+data[i-1][1])
        if 99 in schedule[data[i-1][0]:data[i-1][0]+data[i-1][1]]:
            continue
        else:
            for j in range(0, data[i-1][1]):
                schedule[data[i-1][0]+j] = 99
            income += data[i-1][2]
            print(schedule, income)
            # print(i)
            # print(schedule)

if max_income < income:
    max_income = income
print(max_income)
