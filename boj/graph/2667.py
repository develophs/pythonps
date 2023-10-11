from sys import stdin
from collections import deque

# stdin을 사용하여 readline().split()으로 입력하면 공백을 기준으로 나누고
# readline()만 사용하면 공백이 존재하지 않아도 1개씩 나뉘어진다.

if __name__ == '__main__':

    def bfs(grid, x, y):
        visited[x][y] = True
        val = 1
        q = deque()
        q.append((x, y))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_x = max_y = len(grid)

        while q:
            cur_x, cur_y = q.popleft()

            for dx, dy in dirs:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        val += 1
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y))

        values.append(val)

    graph = []
    n = int(stdin.readline().strip())
    for _ in range(n):
        house = list(map(int, stdin.readline().strip()))
        graph.append(house)

    visited = [[False] * n for _ in range(n)]
    values = []
    count = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(graph, i, j)
                count += 1

    values.sort()
    print(count)
    for v in values:
        print(v)