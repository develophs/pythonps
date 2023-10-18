import sys
from sys import stdin
from collections import defaultdict
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    # O(n) 딕셔너리, 인접 리스트로 구현되어있기 때문에 한번씩만 방문한다.
    def dfs(cur_node):
        visited.append(cur_node)

        for v in graph[cur_node]:
            if v not in visited:
                dfs(v)

    graph = defaultdict(list)
    visited = []
    count = 0
    n, m = list(map(int, stdin.readline().split()))

    for _ in range(m):
        a, b = list(map(int, stdin.readline().split()))
        graph[a].append(b)
        graph[b].append(a)

    for key in range(1, n+1):
        if key not in visited:
            # dfs 메소드를 실행할때 연결된 모든 노드들을 방문하기 때문에
            # 연결된 요소들을 전부 방문한다.
            # 따로 존재하는 요소들의 갯수만큼 해당 로직에서 bfs메소드 호출
            dfs(key)
            count += 1

    print(count)