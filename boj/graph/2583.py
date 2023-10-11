from sys import stdin
from collections import deque

if __name__ == '__main__':
    # O(n**2)
    # M * n = 10000

    def bfs(x, y):
        # bfs 메소드를 시작하면 방문체크 중복 접근을 방지한다.
        visited[x][y] = True
        val = 1
        max_x = len(graph)
        max_y = len(graph[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque()
        q.append((x, y, val))  # bfs가 시작되었다는 뜻은 해당 좌표는 공백이다. 공백의 크기 default값 1

        while q:
            cur_x, cur_y, cur_v = q.popleft()

            for dx, dy in dirs:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        # while문 안에서는 방문체크 로직이 따로 없기 때문에 해당 로직에서 방문 체크
                        val += 1
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y, val))

        # bfs를 시작한 좌표에 더이상 인접한 공백이 존재하지 않으면 현재의 값을 values에 저장
        values.append(val)


    m, n, k = list(map(int, stdin.readline().split()))
    graph = [[1] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    # 공백의 크기를 담아줄 배열 생성
    # bfs 메소드를 실행한 횟수 = 공백의 갯수
    # bfs 메소드 내 while문을 실행한 횟수 = 공백의 크기
    values = []

    # 직사각형의 위치를 입력받는다.
    # 직사각형의 시작점 부터 끝나는 지점까지 모두 직사각형(0)으로 채워준다.
    for s in range(k):
        sx, sy, ex, ey = list(map(int, stdin.readline().split()))

        # 이중 반복문을 이용하여 입력받은값의 index로 접근해 0으로 변경
        for i in range(sy, ey):
            for j in range(sx, ex):
                graph[i][j] = 0

    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1 and not visited[x][y]:
                bfs(x, y)

    values.sort()
    print(len(values))
    for value in values:
        print(value, end=" ")