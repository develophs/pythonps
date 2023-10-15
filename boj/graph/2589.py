from sys import stdin
from collections import deque

if __name__ == '__main__':

    def bfs(grid, x, y):
        # O(n**2)
        max_x = len(grid)
        max_y = len(grid[0])

        # 방문체크를 하기 위한 배열
        # 전역변수로 사용하여 방문체크를 하게 되면 모든 육지에 대해서 bfs를 실행하지 못한다.
        visited = [[False] * max_y for _ in range(max_x)]
        visited[x][y] = True

        v = 0
        q = deque()
        q.append((x, y, v))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            cur_x, cur_y, cur_v = q.popleft()
            values.append(cur_v)

            for dx, dy in dirs:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if grid[next_x][next_y] == "L" and not visited[next_x][next_y]:
                        q.append((next_x, next_y, cur_v + 1))
                        visited[next_x][next_y] = True
    graph = []
    values = []
    r, c = list(map(int, stdin.readline().split()))
    for _ in range(r):
        columns = list(stdin.readline().strip())
        graph.append(columns)

    # 모든 육지 좌표에 대해서 bfs 메소드를 실행시켜야한다.
    # 각 좌표마다 가장 멀리있는 좌표까지의 거리를 구하고 values 배열에 넣어
    # 최대값을 구해준다.
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "L":
                bfs(graph, i, j)

    print(max(values))
