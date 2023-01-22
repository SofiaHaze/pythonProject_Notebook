from sys import stdin
#파이썬 rstrip ()은 문자열의 지정된 문자열의 끝을 (기본값은 공백입니다) 삭제함
input = lambda: stdin.readline().rstrip()
#
# 맨 첫줄 Test case를 입력받을 때는 input()을 사용해도 무방합니다.
# 그러나 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.

if __name__ == "__main__":
   T = int(input())
   for _ in range(T):
       M = int(input())
       #sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아집니다.
        # 만약 3을 입력했다면, 3\n 이 저장되기 때문에, 개행문자를 제거해야 합니다.
        # 또한, 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 합니다.
        #
       nums = []

       #수열의 갯수가 10이상이면 두줄 이상을 입력값으로 받기위해 M // 10 + 1
       for _ in range(M // 10 + 1):
           nums += list(map(int, input().split()))
           # print(nums)
           # [1, 2, 3, 4, 5, 6, 7, 8, 9]
       print(M // 2 + 1)


       #nums 수열중 홀수번째 값일 떄 마다 중간값 출력
       for i in range(1, len(nums) + 1, 2):
           print(sorted(nums[:i])[i // 2], end=' ')
       print()