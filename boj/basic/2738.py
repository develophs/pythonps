from sys import stdin

if __name__ == '__main__':
    # O(n**2)
    # O(1) 연산을 n번 반복문 및 m번 반복
    n, m = map(int, stdin.readline().split())

    graph1 = []
    graph2 = []

    for _ in range(n):
        nums = list(map(int, stdin.readline().split()))
        graph1.append(nums)

    for _ in range(n):
        nums = list(map(int, stdin.readline().split()))
        graph2.append(nums)

    for i in range(n):
        for j in range(m):
            print(graph1[i][j] + graph2[i][j], end = " ")
        print()