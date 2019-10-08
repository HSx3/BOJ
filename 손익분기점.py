import sys
sys.stdin = open('손익분기점_input.txt')

A, B, C = map(int, input().split())

if B >= C:
    answer = -1
else:
    answer = A//(C-B) + 1
print(answer)