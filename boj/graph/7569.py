from sys import stdin
from collections import deque

if __name__ == '__main__':
    # O(n**3)

    def bfs():
        # 최대 높이
        max_z = len(graph)
        # 최대 세로
        max_x = len(graph[0])
        # 최대 가로
        max_y = len(graph[0][0])

        dirs = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

        while q:
            cur_z, cur_x, cur_y, cur_v = q.popleft()
            values.append(cur_v)

            # 토마토가 존재하는 좌표 방문체크
            visited[cur_z][cur_x][cur_y] = True

            for dz, dx, dy in dirs:
                next_z = cur_z + dz
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_z < max_z and 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if graph[next_z][next_x][next_y] == 0 and not visited[next_z][next_x][next_y]:
                        # 방문체크, 같은 좌표를 다시 탐색하지 않기 위함
                        visited[next_z][next_x][next_y] = True
                        # 방문할 좌표에 대해 토마토 숙성
                        graph[next_z][next_x][next_y] = 1
                        q.append((next_z, next_x, next_y, cur_v + 1))


    # y:가로, x: 세로 z:높이
    y, x, z = list(map(int, stdin.readline().split()))

    # 입력받은 가로, 세로, 높이의 값을 이용하여 3차원 배열을 초기화 시켜준다.
    graph = [[[0] * y for _ in range(x)] for _ in range(z)]

    # 방문을 기록할 배열
    visited = [[[False] * y for _ in range(x)] for _ in range(z)]

    # 일 수를 계산하기 위한 배열 values
    values = []

    q = deque()

    # 1 : 익은 토마토, 0: 익지 않은 토마토, -1 : 토마토 X
    for i in range(z):
        for j in range(x):
            tomatoes = list(map(int, stdin.readline().split()))
            graph[i][j] = tomatoes

    # 토마토 존재하고 방문하지 않은 좌표에 대해 enque 해준다.
    for z_ in range(z):
        for x_ in range(x):
            for y_ in range(y):
                if graph[z_][x_][y_] == 1 and not visited[z_][x_][y_]:
                    q.append((z_, x_, y_, 0))

    # 익은 토마토의 좌표가 queue에 enque되어 있으며
    # 해당 좌표들에 대해 bfs 메소드를 실행시킨다.
    bfs()

    flag = 1
    for x_tomatoes in graph:
        if flag == 0:
            break
        for y_tomatoes in x_tomatoes:
            if flag == 0:
                break
            if 0 in y_tomatoes:
                flag = 0
                break

    if flag == 1:
        print(max(values))
    else:
        print(-1)
