import sys
sys.stdin = open('감시_input.txt')

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
print(data)

