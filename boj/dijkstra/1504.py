import sys
from sys import stdin
from collections import defaultdict
import heapq
INF = int(1e9)

if __name__ == '__main__':
    # 한번의 다익스트라 메소드로 필수경로를 파악하기 불가능했다.
    # 따라서 각각의 경로에 대한 값들을 구하고
    # 합계를 구한 후 min으로 최솟값을 출력한다.
    # costs를 딕셔너리로 했었을 경우 경로가 존재하지 않았을 때 결과값을 출력하기 어려웠다.
    # 따라서 구글을 통해 정답을 본 결과 costs를 배열로 선언 후 파이썬 정수의 최대값으로 초기화한다.

    # O((V+E)logV)
    # V <= 800, E <= 200000
    # 시간 복잡도 : 200800 * 10
    def dijkstra(grid, start_node, end_node):
        costs = [INF] * (V+1)
        costs[start_node] = 0
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (0, start_node))

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)

            if costs[cur_node] < cur_cost:
                continue

            # 현재 존재하는 값보다 우선순위큐에 있는 값이 더 큰경우
            # 아래 코드를 실행시키지 않고 while문 처음 다시 돌아간다.

            for cost, next_node in grid[cur_node]:
                next_cost = cur_cost + cost
                if next_cost < costs[next_node]:
                    costs[next_node] = next_cost
                    heapq.heappush(pq, (next_cost, next_node))

        return costs[end_node]


    graph = defaultdict(list)
    V, E = map(int, stdin.readline().split())

    for _ in range(E):
        # 간선의 이동 비용과 무향 그래프 설정
        a, b, c = map(int, stdin.readline().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    # 반드시 거쳐야 하는 두 정점 v1, v2
    v1, v2 = map(int, stdin.readline().split())

    result1 = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, V)  # 1 - v1 - v2 - V
    result2 = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, V)  # 1 - v2 - v1 - V

    if result1 >= INF and result2 >= INF:
        print(-1)
    else:
        print(min(result1, result2))
