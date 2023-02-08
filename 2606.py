n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    print(graph[a], graph[b])
cnt = 0
visited = [0] * (n + 1)


def dfs(start):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)

#
# 1 2 3 4 5 6
# [2 5] [1 3 5] [2] [] [1 2 6] [6]

