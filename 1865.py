# INF = float('inf')로 지정하면, 도로 없이 웜홀만 존재하는 그래프에서
# dis[goal] > dis[cur] + weight을 정확히 처리하지 못한다.
# 무한대 > 무한대 - T 꼴이 되어버려서, 분명 음의 사이클이 존재하는데, 없는 것으로 간주한다


# 그래서 거리 가중치를 초기화할때 사용할 변수인 INF는 문제 견적보고 적당히 큰 수로 만들어야한다
INF = 0xffffff

def bf(i: int):
    # i --> 시작 지점
    dis = [INF] * (N + 1)
    dis[i] = 0  # 시작위치의 거리 가중치 초기화

    # 뺑뺑이 있는지 찾기 위해서 N번 반복
    for cnt in range(N):
        for edge in edges:
            cur = edge[0]
            goal = edge[1]
            weight = edge[2]
            if dis[goal] > dis[cur] + weight:
                dis[goal] = dis[cur] + weight

                # 음의 사이클 존재
                if cnt == N - 1:
                    return True
    # 음수 사이클 없음
    return False


TC = int(input())

for tc in range(TC):
    N, M, W = map(int, input().split())
    # 그래프 인접 리스트
    edges = []
    # 도로 그래프 입력
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append([S, E, T])
        edges.append([E, S, T])
    # 웜홀 정보 입력
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append([S, E, -T])

    negative_cycle_exist = bf(1)
    # 음수 사이클이 존재하는지를 확인하는 것
    print('YES' if negative_cycle_exist else 'NO')



# 벨만 포드 알고리즘
# 그래프 상에 존재하는 두 노드 간의 최단 거리를 구하고 싶을 때 이용
# 다익스트라에서 할 수 없었던 음의 가중치도 계산 할 수 있도록 한 방식이지만 다익스트라보다 시간 복잡도가 높음

# 우선 벨만 포드 알고리즘에 대한 전제 조건
# 1. 최단 경로는 사이클을 포함할 수 없기 때문에, 최대 |V|-1개의 간선만 사용할 수 잇음
# 즉, 3개의 노드가 있을 때, 2개까지 간선만 허용한다는 의미
# 2. 최단 거리가 업데이트 되는 노드가 없어질 때 까지 계속해서 반복하여 구해주고, 음의 가중치로 인해 업데이트를 무한히 하게 되는 경우 탈출 시켜주어야 함
