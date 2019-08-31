import sys
sys.stdin = open('암호만들기_input.txt')


def DFS(no, length):
    global L

    if length > L:
        return

    if no >= C:
        if length == L:
            vc, cc = 0, 0
            password = ''
            for i in range(C):
                if check[i] != '0':
                    password += check[i]
                if check[i] in chk:
                    vc += 1
                if check[i] not in chk:
                    if check[i] != '0':
                        cc += 1
            if vc >= 1 and cc >= 2:
                password = ''.join(sorted(password))
                password_list.append(password)
        return

    check[no] = data[no]
    DFS(no+1, length+1)
    check[no] = '0'
    DFS(no+1, length)


L, C = map(int, input().split())
data = input().split()

check = ['0'] * C
chk = ['a', 'e', 'i', 'o', 'u']
password_list = []

DFS(0, 0)
password_list = sorted(password_list)
for i in password_list:
    print(i)