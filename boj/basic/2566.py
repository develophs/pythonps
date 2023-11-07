from sys import stdin

if __name__ == '__main__':
    # O(n**2)
    graph = []
    row = 0
    col = 0

    for _ in range(9):
        nums = list(map(int, stdin.readline().split()))
        graph.append(nums)

    maxNum = graph[0][0]

    # 행과 열을 구하기 위해 완전 탐색
    for i in range(9):
        for j in range(9):
            if graph[i][j] > maxNum:
                row = i
                col = j
                maxNum = graph[i][j]

    print(maxNum)
    # 인덱스 접근에서 행,열 접근
    print(row+1, col+1)