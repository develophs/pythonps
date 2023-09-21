from collections import deque
from sys import stdin

if __name__ == '__main__':
    t = int(stdin.readline())

    for test in range(t):
        # 이제부터 x를 행으로 y를 열로 보겠다. 알고리즘 문제를 풀기에 적합한 생각 방식인거같다.
        # 세로, 가로, 지렁이 갯수 받기
        m, n, k = map(int, stdin.readline().strip().split())

        # 0을 가로(n)만큼 생성하고 m개의 행만큼 반복생성
        graph = [[0] * n for _ in range(m)]

        # 세로의 좌표 x , 가로의 좌표 y를 통해 배추 심기
        for _ in range(k):
            x, y = map(int, stdin.readline().strip().split())
            graph[x][y] = 1

        # 그래프를 파라미터로 받는 전체적인 메소드 생성
        def find_worm(graph):
            worm = 0
            max_x = len(graph)
            max_y = len(graph[0])

            # 특정 좌표에 값을 체크한 여부를 판단하기 위한 visited 그래프를 원본의 크기만큼 생성
            visited = [[False] * max_y for _ in range(max_x)]

            # 그래프를 남, 북, 동, 서 체크하기 위한 방향 튜플
            dir = [(1,0), (-1,0), (0,1), (0,-1)]

            # 너비 우선 탐색의 bfs 메소드
            def bfs(x, y):
                visited[x][y] = True
                queue = deque()

                queue.append((x, y))

                # queue에 저장된 튜플을 dequeue해주고
                # 해당 좌표를 동서남북으로 값을 체크한다.
                while queue:
                    dx, dy = queue.popleft()

                    for d in dir:
                        nx, ny = d

                        next_x = dx + nx
                        next_y = dy + ny

                        # 행렬의 최대 범위를 넘지 않고, 0 이상일 경우
                        # 해당 좌표와 동서남북의 값을 체크하고, 배추가 존재하고 아직 방문하지 않은 특정 좌표를 queue에 넣고, 방문체크를 해준다.
                        # 해당 과정을 통해 중복탐색하는 좌표가 존재하지 않고 배추가 심어져있으면 주변 동서남북 좌표도 넓게 퍼져나가 값을 체크한다.
                        if 0 <= next_x < max_x and 0 <= next_y < max_y:
                            if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                                visited[next_x][next_y] = True
                                queue.append((next_x, next_y))

            # 인접 행렬로 구현했기 때문에 O(n**2)의 시간복잡도를 가진다.
            # WORST CASE : max_x * max_y
            for i in range(max_x):
                for j in range(max_y):
                    # 해당 좌표에 애벌레가 있고, 방문하지 않았으면 bfs 메소드를 실행한다.
                    if graph[i][j] == 1 and not visited[i][j]:
                        bfs(i, j)
                        worm += 1
            return worm


        print(find_worm(graph))