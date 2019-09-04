import sys
sys.stdin = open('퇴사_input.txt')


def backtrack(day, income):
    global ans
    ans = max(ans, income)
    if day > N:
        return
    if day + data[day][1] - 1 <= N:
        backtrack(day+data[day][1], income+data[day][2])
    backtrack(day+1, income)


N = int(input())
schedule = [0] * (N+1)
data = [(0, 0, 0)]
for i in range(1, N+1):
    Ti, Pi = map(int, input().split())
    data.append((i, Ti, Pi))

ans = 0
backtrack(1, 0)
print(ans)