from sys import stdin
from collections import deque

if __name__ == '__main__':
    # BFS O(n**3)
    # WORST CASE : n * n * height의 최대 높이
    def bfs(x, y, h):
        visited[x][y] = True
        max_x = max_y = len(graph)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        q.append((x, y))

        while q:
            cur_x, cur_y = q.popleft()

            for dx, dy in dirs:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if graph[next_x][next_y] > h and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))

    graph = []
    n = int(stdin.readline())

    for _ in range(n):
        area = list(map(int, stdin.readline().split()))
        graph.append(area)

    # 새로 알게된 문법
    # map(min,graph) : 2차원 배열에서 최소값을 가져온다. return 값은 map이기 때문에 파싱 필요
    # map(max,graph) : 2차원 배열에서 최대값을 가져온다. return 값은 map이기 때문에 파싱 필요
    min_val, max_val = min(map(min, graph)), max(map(max, graph))
    values = []

    # 해당 높이에 대한 bfs 메소드가 몇번 실행되었나 체크해야한다.
    # 안전 지역의 갯수를 구함. 범위 X
    # 인접한 안전지역의 범위를 파악할 필요가없다.

    # range 문법 !!! 마지막 숫자의 -1 까지 수행한다.
    # 1 <= height <= 100 range 문법사용시 101까지 실행시켜야 100까지 수행

    for height in range(min_val, max_val):
        # 해당 높이에 대한 탐색이 끝날 때 마다 방문 체크에 사용하는 배열과 count의 크기를 초기화 시켜준다.
        count = 0
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j] > height and not visited[i][j]:
                    bfs(i, j, height)
                    count += 1
        values.append(count)

    if values:
        print(max(values))
    else:
        print(1)