from collections import deque

if __name__ == '__main__':
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]


    def island(grid):
        count = 0
        max_row = len(grid)
        max_col = len(grid[0])

        delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = [[False] * max_col for _ in range(max_row)]

        def bfs(x,y):
            q = deque()
            q.append((x, y))
            visited[x][y] = True
            while q:
                cur_x, cur_y = q.popleft()

                for d in delta:
                    x_, y_ = d

                    next_x = cur_x + x_
                    next_y = cur_y + y_

                    if 0 <= next_x < max_row and 0 <= next_y < max_col:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))

        for x in range(max_row):
            for y in range(max_col):
                if grid[x][y] == "1" and not visited[x][y]:
                    bfs(x,y)
                    count += 1
        return count

    print(island(grid))