
'''
설탕 배달_ 백준]
<접근법>
상근 배달 N킬로그램, 봉지 3K, 5K
최대한 적은 봉지의 수 들고 가려함,
ex. 18KG => 3K 6개, 5K 3개+3K 1개
N= 5*p + 3*q,  15, 30 45 50
    1)N이 5로 나눠질 경우
    2)N이 5과 3의 조합으로 나눠 담을 수 있을 경우
    3)N이 3으로 나눠질 경우
    4)5와 3으로는 나눠지지 않을 경우
18 = 5+5+5+3 : 4
4 = 3 ... 1 : -1(나눠지지 않을 경우)
6 = 3+3 : 2
9 = 3+3+3 : 3
11 = 5+3+3 : 3
'''

import sys


# N = map(int, sys.stdin.readline())
N = int(sys.stdin.readline())
p=0
Ans = 0
if N % 5 == 0:
    Ans = N // 5

else:
    while N >= 0:
        N-=3
        p+=1
        if N%5 ==0:
            Ans = p+(N//5)
            break
        elif N==1 or N==2:
            Ans = -1
            break
        elif N==0:
            Ans = 0
            break

print(Ans)