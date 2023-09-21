from collections import deque
from sys import stdin

if __name__ == '__main__':
    # O(n**2)
    def waste(graph):
        # 인접한 1의 갯수를 파악하기 위한 배열 생성
        count_list = []

        max_r = len(graph)
        max_c = len(graph[0])

        # 남 북 동 서
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * max_c for _ in range(max_r)]

        def bfs(r, c):
            # 음식물의 default 갯수 1개
            # bfs 메소드가 실행되었다는것은 해당 좌표에 음식물이 있다는것이다.
            # 튜플이 값을 3개 가지고있도록 생성해도 된다. (행,렬,음식물 갯수)
            count = 1
            q = deque()
            q.append((r, c))
            visited[r][c] = True

            while q:
                cur_r, cur_c = q.popleft()

                for v in dir:
                    dr, dc = v

                    next_r = cur_r + dr
                    next_c = cur_c + dc

                    # 인접한 좌표에 음식물이 존재하면 1씩 증가한다.
                    # 한번 탐색한 좌표는 두번 다시 가지 않기 때문에 처음에 갔을때만 1씩 증가
                    if 0 <= next_r < max_r and 0 <= next_c < max_c:
                        if graph[next_r][next_c] == 1 and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            q.append((next_r, next_c))
                            count += 1

            # 튜플, count 리스트, 그때 그때 max()해서 값을 갱신해도 될듯
            count_list.append(count)

        for i in range(max_r):
            for j in range(max_c):
                if graph[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)

        return max(count_list)


    # 행,열,음식물 갯수 받기
    n, m, k = map(int, stdin.readline().rstrip().split())
    # 열을 기준으로 0을 생성하고 행의 갯수만큼 반복생성
    graph = [[0] * m for _ in range(n)]

    # 음식물 갯수만큼 해당 좌표에 음식물 버리기
    for _ in range(k):
        r, c = map(int, stdin.readline().rstrip().split())
        graph[r-1][c-1] = 1

    print(waste(graph))
