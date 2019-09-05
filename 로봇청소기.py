import sys
sys.stdin = open('로봇청소기_input.txt')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

print(N, M)
print(r, c, d)
print(data)

