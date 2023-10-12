from sys import stdin
from collections import deque

if __name__ == '__main__':
    # O (n**2)
    # 굳이 좌표에 대한 값을 설정하지 않고 queue에 존재하는 다음 좌표가 타겟과 같으면 메소드를 종료한다.
    # 주의 ! : 대각선 좌표일 경우 좀더 자세히 보기
    def bfs(grid, start_x, start_y, end_x, end_y):
        # 첫 좌표에 대해 방문 체크
        visited[start_x][start_y] = True

        # 나이트가 이동할 수 있는 대각선의 크기들
        dirs = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

        max_x = max_y = len(grid)
        count = 0
        q = deque()
        q.append((start_x, start_y, count))

        while q:
            x, y, cur_v = q.popleft()

            if x == end_x and y == end_y:
                print(cur_v)
                break

            for dx, dy in dirs:
                next_x = x + dx
                next_y = y + dy

                if 0 <= next_x < max_x and 0 <= next_y < max_y:
                    if not visited[next_x][next_y]:
                        # next_x, next_y로 이동 후 목적지에 도착하지 못하면 더이상 해당 좌표를 갈 필요가 없다.
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y, cur_v + 1))

    t = int(stdin.readline())

    for _ in range(t):
        l = int(stdin.readline())

        # 기본 그래프를 1로 초기화 한다.
        graph = [[1] * l for _ in range(l)]
        visited = [[False] * l for _ in range(l)]

        cur_x, cur_y = list(map(int, stdin.readline().split()))
        target_x, target_y = list(map(int, stdin.readline().split()))

        bfs(graph, cur_x, cur_y, target_x, target_y)
