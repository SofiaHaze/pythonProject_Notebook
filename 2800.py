# ✨ 입력
import sys
from itertools import combinations
input = sys.stdin.readline
stack = []
arr = input().rstrip()
glst = []
resarr = set()

# ✨ 괄호 쌍 위치 구하기
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(i)
    elif arr[i] == ')':
        s = stack.pop()
        glst.append((s,i))

# ✨ 조합을 이용해 괄호 제거하기
for i in range(1,len(glst)+1):
    for comb in combinations(glst,i):
        tmp = list(arr)
        for x in comb:
            tmp[x[0]] = ""
            tmp[x[1]] = ""
            resarr.add("".join(tmp))
for x in sorted(list(resarr)):
    print(x)