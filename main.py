
# 백트래킹 (퇴각 검색)
# - 길을 가다가 이 길이 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행
# - 보통 재귀로 구현하며 조건이 맞지 않으면 종료한다.
# - DFS(깊이 우선 탐색) 기반



n, m = list(map(int, input().split()))

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

###########################Things to Learn##################################
#
# input().split()  >> 결과값: ['4', '4'] <class 'list'>
#
# map(function, iterable)
# 두 번째 매개변수로는 반복가능한 자료형(리스트, 튜플 등)이 옴
# map함수의 Return Value는 map object이기 때문에 해당 자료형을 list or tuple 형 변환 필요
# 함수의 동작은 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수
# 즉, map(적용시킬 함수, 적용할 값들)
#
# In the case of not using the MAP FUNTION,
#
# myList = [1,2,3,4,5]
#
# result1 = []
# ####for 반복문 이용####
# for val in myList:
#     #일일이 하나하나 리스트 요소에 접근해서 계산을 해서 리스트에 하나씩 또 append 해주어야 하는 번거로움 있음
#     result1.append(val+1)
# print(f'result1: {result1}')
#
# ####map함수이용####
# def add_one(n):
#     return n+1
#
# #자동적으로 리스트를 함수에 적용해서 map 객체를 반환
# result2 = list(map(add_one, myList))
# print(f'result2 : {result2}')