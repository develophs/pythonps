from sys import stdin
from collections import deque

if __name__ == "__main__":
    # 시간 복잡도 O(n**2) == x*y
    def bfs(x, y):
        visited[x][y] = True  # 방문 체크

        max_x = len(graph)
        max_y = len(graph[0])

        q = deque()
        q.append((x, y, 1))  # queue를 이용하여 방문 예약, 최초 bfs 시작 step 1 디폴트값

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            cur_x, cur_y, cur_v = q.popleft()

            # queue에 저장되어있는 x와 y의 값이 최대x, 최대y의 인덱스 값인 경우
            # 해당 값을 출력하고 반복문을 정지시킨다.
            if cur_x == max_x-1 and cur_y == max_y-1:
                print(cur_v)
                break

            # max_x, max_y의 인덱스가 아닌 경우
            # for문을 이용하여 방문 예약 및 방문 체크 후
            # cur_v에 +1을 해준값들을 queue에 enque해준다.
            for d in dirs:
                dx, dy = d

                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        q.append((next_x, next_y, cur_v + 1))
                        visited[next_x][next_y] = True


    graph = []
    x, y = map(int, stdin.readline().strip().split())
    for i in range(x):
        row = list(map(int, stdin.readline().strip()))
        graph.append(row)

    visited = [[False] * y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)