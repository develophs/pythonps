from sys import stdin

if __name__ == '__main__':
    # 정렬 : O(NlogN)
    graph = []
    n = int(stdin.readline())

    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        graph.append((x, y))

    # y를 기준으로 정렬 후 y값이 같으면 x를 기준으로 정렬한다.
    graph.sort(key=lambda k: (k[1], k[0]))

    for k_x, k_y in graph:
        print(k_x, k_y)

