import sys
sys.stdin = open('연결요소의개수_input.txt')

def DFS(v):
    visited[v] = 1

    # u_list[v] = 0

    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            DFS(w)


N, M = map(int, input().split())
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N+1)
u_list = list(range(N+1))
for i in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

count = 0
# for i in range(1, N+1):
#     if visited[i] == 0:
#         DFS(i)
#         count += 1
# print(count)
for i in u_list:
    if i != 0:
        DFS(i)
        count += 1
print(count)


# 반복문
# def DFS(v):
#     stack = []
#     stack.append(v)
#     visited[v] = 1
#
#     # u_list[v] = 0
#     # print('c', u_list)
#     # print(v, end=' ')
#
#     while len(stack) > 0:
#         # print('1', stack)
#         prev = v
#         for w in range(1, N+1):
#             if G[v][w] == 1 and visited[w] == 0:
#                 stack.append(w)
#                 # print('2', stack)
#                 v = w
#                 u_list[v] = 0
#                 visited[w] = 1
#                 if visited == [0] + [1]*N:
#                     return
#                 # print(visited)
#                 # print(v, end=' ')
#                 break
#         if prev == v:
#             v = stack.pop()
#
#
# N, M = map(int, input().split())
# G = [[0 for _ in range(N+1)] for _ in range(N+1)]
# visited = [0] * (N+1)
# # print(G)
# # print(visited)
#
# u_list = list(range(N+1))
# # print(u_list)
# for i in range(M):
#     u, v = map(int, input().split())
#     G[u][v] = 1
#     G[v][u] = 1
# # print(G)
#
# count = 0
# for i in u_list:
#     # print(i, u_list)
#     if i == 0:
#         continue
#     if i != 0:
#         DFS(i)
#         # print()
#         count += 1
# print(count)