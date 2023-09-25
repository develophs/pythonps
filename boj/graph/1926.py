from sys import stdin
from collections import deque

if __name__ == '__main__':
    # O(n**2)
    def image(grid):
        cc = 0
        values = []

        max_x = len(grid)
        max_y = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * max_y for _ in range(max_x)]

        def bfs(x, y):
            # bfs가 시작했다는것을 첫 시작지점이다.
            # value 1로 초기화
            value = 1
            q = deque()

            # 첫 좌표가 queue에 enque될 때 반드시 첫좌표에 방문표시 해야한다.
            q.append((x, y))
            visited[x][y] = True

            while q:
                # bfs를 시작한 정점 및 인접해있는 정점에 대한 너비 탐색
                cur_x, cur_y = q.popleft()
                for d in directions:
                    dx, dy = d

                    next_x = cur_x + dx
                    next_y = cur_y + dy

                    if 0 <= next_x < max_x and 0 <= next_y < max_y:
                        if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                            # 인접해있는 vertex가 그림이고, 아직 방문하지 않은 경우
                            # 큐에 enque해주고 해당 vertex에 대해 bfs를 while문을 통해 반복.
                            q.append((next_x, next_y))
                            visited[next_x][next_y] = True
                            value += 1

            values.append(value)

        for w in range(max_x):
            for j in range(max_y):
                if grid[w][j] == 1 and not visited[w][j]:
                    bfs(w, j)
                    cc += 1
        print(cc)
        # 해당부분에서 valueError발생
        # 그림이 1개도 없는 경우 최대 사이즈는 0이다.
        # values 배열에 값이 하나도 없기 때문에 max를 가져올 수 없다.
        if not values:
            print(0)
        else:
            print(max(values))

    x, y = map(int, stdin.readline().strip().split())

    grid = []

    for i in range(x):
        aa = list(map(int, stdin.readline().strip().split()))
        grid.append(aa)

    image(grid)
