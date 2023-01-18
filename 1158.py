
n, k = input().split()

arr = []
yose = []
index = 0 #제거할 인덱스

for i in range(1, int(n)+1):
    arr.append(i)
# arr = [i for i in range(1, int(n) + 1)]

# print(f'list : {arr}')
while arr:
    index = index + int(k) - 1
    if index >= len(arr):
        index %= len(arr)
    yose.append(str(arr.pop(index)))

print("<", ', '.join(yose), ">", sep='') #''공백없어주기

# 예시
# lst = ['a', 'b', 'c', 'd']
# print( ''.join(lst) ) # abcd
# print( ','.join(lst) ) # a,b,c,d
# print( '--'.join(lst) ) # a--b--c--d