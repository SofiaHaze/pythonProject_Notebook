'''
호출 횟수 또한 피보나치 수열 따름
N      값  0   1   2   3   4   5
0호출횟수   1   0   1   1   2   3
1호출회수   0   1   1   2   3   5
'''

#0호출 횟수를 리스트로
fibo_0=[1, 0]
#1호출 횟수를 리스트로~
fibo_1=[0, 1]

T = int(input())

for i in range(T):
    N= int(input())

    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        for j in range(2, N+1):
            fibo_0.append(fibo_0[j-1] + fibo_0[j-2])
            fibo_1.append(fibo_1[j-1] + fibo_1[j-2])
            print(f"{fibo_0} {fibo_1}")

        print(f"{fibo_0.pop()} {fibo_1.pop()}")
        fibo_1=[0, 1]
        fibo_0=[1, 0]