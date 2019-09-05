import sys
sys.stdin = open('연산자끼워넣기_input.txt')


def backtrack(base, idx, add, sub, mul, div):
    global N, mmax, mmin
    if idx == N:
        mmax = max(base, mmax)
        mmin = min(base, mmin)
        return
    else:
        if add:
            backtrack(base + numbers[idx], idx+1, add-1, sub, mul, div)
        if sub:
            backtrack(base - numbers[idx], idx+1, add, sub-1, mul, div)
        if mul:
            backtrack(base * numbers[idx], idx+1, add, sub, mul-1, div)
        if div:
            backtrack(int(base / numbers[idx]), idx+1, add, sub, mul, div-1)


N = int(input())
numbers = list(map(int, input().split()))
operator_num = list(map(int, input().split()))

mmax = -987654321
mmin = 987654321

backtrack(numbers[0], 1, operator_num[0], operator_num[1], operator_num[2], operator_num[3])
print(mmax)
print(mmin)