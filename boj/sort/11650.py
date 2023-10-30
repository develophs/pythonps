from sys import stdin

if __name__ == '__main__':
    # O(NlogN)
    n = int(stdin.readline())

    graph = []

    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        graph.append((x, y))

    # 벨류값이 튜플인 경우 반드시 필요
    graph.sort(key=lambda x: (x[0], x[1]))

    # 벨류가 리스트인 경우
    # graph.sort()
    for g_x, g_y in graph:
        print(g_x, g_y)

