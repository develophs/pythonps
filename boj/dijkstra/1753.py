from sys import stdin
from collections import defaultdict
import heapq

if __name__ == '__main__':
    # 간선의 갯수 E
    # 정점의 갯수 V
    # 기본적인 우선순위 큐의 메소드 logV

    # 모든 정점들이 서로 연결되어 있을경우 시간복잡도가 가장 크다.
    # 정점을 모두 방문하고 연결되어 있는 간선을 한번 씩 확인한다.
    # O (V+E)logV
    def dijkstra(grid, start_node):
        # 우선순위 큐를 생성하기 위한 디폴트 리스트
        pq = []
        costs = {}

        # 우선순위 큐로 구현해주고, 가중치를 앞에 둔다.
        heapq.heapify(pq)
        heapq.heappush(pq, (0, start_node))

        # 우선순위 큐가 완전히 빌때 까지 while문을 수행하고,
        # 우선선위 큐가 완전히 비어있으면 방문 노드와 가중치를 저장한 딕셔너리를 리턴한다.
        while pq:
            # 우선순위 큐에서 아이템을 제거하는 과정은 반드시 가중치가 제일 낮은 vertex부터 제거된다.
            cur_cost, cur_node = heapq.heappop(pq)

            # 우선순위 큐에 존재하는 vertex를 방문한 적이 없는경우
            if cur_node not in costs:
                # 방문 체크 및 해당 노드 까지의 value를 저장한다.
                costs[cur_node] = cur_cost

                # 해당 노드와 연결된 모든 간선 및 정점에 대한 value를 우선순위 큐에 저장
                for cost, next_node in grid[cur_node]:
                    next_cost = cost + cur_cost
                    heapq.heappush(pq, (next_cost, next_node))

        return costs

    # 딕셔너리로 인접 리스트를 구현하고 키에 대한 벨류의 값은 list로 가져간다.
    # 리스트내 아이템들의 자료 타입은 튜플이다.
    graph = defaultdict(list)
    V, E = map(int, stdin.readline().split())
    start = int(stdin.readline())

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())
        # 튜플내 가중치를 앞으로 넣어야 우선순위에 따라 정점들에 방문하게 된다.
        graph[u].append((w, v))

    result = dijkstra(graph, start)

    # 1번부터 마지막 정점의 번호까지 가중치를 저장한 결과 탐색
    # 존재할 경우 해당 값을 출력하고 해당 노드에 방문을 하지 않은 경우 INF 출력
    for i in range(1, V+1):
        if i not in result:
            print("INF")
        else:
            print(result[i])
