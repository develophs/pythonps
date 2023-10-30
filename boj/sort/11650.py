from sys import stdin

if __name__ == '__main__':
    # O(NlogN)
    """
    파이썬 내장함수는 튜플을 정렬할때 0번째 인덱스로만 비교하여 정렬한다
    따라서 sort(key=lambda)문법을 사용하여 정렬 기준을 세워주어야한다. 
    """
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

