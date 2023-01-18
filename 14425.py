n, m = map(int, input().split())
s = [input() for i in range(n)]
cnt = 0

for i in range(m):
    word = str(input())

    if word in s:
        cnt += 1

print(cnt)
