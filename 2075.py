import heapq
#데이터 정렬 된 상태로 저장하기 위해서 사용하는 파이썬 내장모듈
#heapq.heappop(heap) 하면 heap[0] out 
#heap:완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조

heap = []
n = int(input())

for _ in range(n):
    numbers = list(map(int, input().split())) #map 반환값 map 객체  list or tuple
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq. heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])
