from sys import stdin
from collections import deque

if __name__ == '__main__':
    # O(n**2)
    # 여태까지 접하지 못한 새로운 방식의 BFS
    # 해당 문제 전까지는 BFS 탐색 순서가 인접한 노드로 옮겨가며 탐색하여
    # 시작노드가 여러 군데여도 신경 쓸 필요가 없었다.
    def bfs():
        # 익은 토마토가 있는 노드부터 방문 체크 및 bfs메소드를 실행하고
        # 그 이후에 익은 토마토 옆에있는 안익은 토마토를 탐색한다.
        while q:
            cur_x, cur_y, cur_v = q.popleft()
            # 현재의 날짜를 모두 days 배열에 넣어준다.
            days.append(cur_v)

            visited[cur_x][cur_y] = True

            max_x = len(graph)
            max_y = len(graph[0])

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in dirs:
                next_x = cur_x + dx
                next_y = cur_y + dy

                if 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if graph[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        graph[next_x][next_y] = 1 # 안익은 토마토를 숙성시켜야한다.
                        q.append((next_x, next_y, cur_v + 1))

    graph = []
    days = []
    # 이전까지는 queue를 bfs 메소드 안에서 지역변수로 사용하여
    # 첫 탐색위치에서의 탐색의 크기, 탐색의 시작 횟수를 구하는데 주로 사용했다.

    # 하지만, 해당 문제는 BFS 탐색 시작위치가 처음부터 동시에 queue에 저장되어야한다.
    # 시작위치가 동시에 적용되어야 하기 때문에 미리 queue에 시작위치들을 enque하고
    # 시작위치로 지정된 노드들부터 탐색 후 근처 노트를 탐색한다.

    q = deque() # queue를 전역변수로 사용하기 위함
    m, n = list(map(int, stdin.readline().split()))

    visited = [[False] * m for _ in range(n)]

    for _ in range(n):
        tomatoes = list(map(int, stdin.readline().split()))
        graph.append(tomatoes)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                # 익은 토마토가 있는 노드들을 전부 queue에 미리 enqueue한다.
                # 익은 토마토의 위치 및 day를 계산하기 위한 0
                q.append((i, j, 0))
    bfs()

    flag = 1
    for i in range(n):
        if flag == 0:
            break
        for j in range(m):
            if graph[i][j] == 0:
                flag = 0
                break

    if flag == 0:
        print(-1)
    else:
        print(max(days))
