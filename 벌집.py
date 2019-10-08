import sys
sys.stdin = open('벌집_input.txt')
import math

N = int(input())

# answer = math.ceil((N-1)/6)
answer = (N-1)//6
print(answer)