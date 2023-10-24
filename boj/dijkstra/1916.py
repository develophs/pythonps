from sys import stdin
from collections import defaultdict
import heapq

if __name__ == '__main__':
    # O((V+E)logV)
    # 일반적인 다익스트라 문제
    def dijksatra(grid, start_node, end_node):
        costs = {}
        pq = []

        heapq.heapify(pq)
        heapq.heappush(pq, (0, start_node))

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)

            if cur_node not in costs:
                costs[cur_node] = cur_cost

                for cost, next_node in grid[cur_node]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_node))

        return costs[end_node]

    graph = defaultdict(list)
    v = int(stdin.readline())
    e = int(stdin.readline())

    for _ in range(e):
        s_num, e_num, c = map(int, stdin.readline().split())
        graph[s_num].append((c, e_num))

    s_node, e_node = map(int, stdin.readline().split())

    result = dijksatra(graph, s_node, e_node)
    print(result)