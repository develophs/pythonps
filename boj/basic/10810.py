from sys import stdin

if __name__ == '__main__':
    # O(n**2)
    n, m = map(int, stdin.readline().split())

    nums = [0 for _ in range(n)]

    # m번 반복
    for _ in range(m):
        i, j, k = map(int, stdin.readline().split())
        # i,j가 양끝 인덱스인 경우 m번반복
        for idx in range(i - 1, j):
            nums[idx] = k

    for num in nums:
        print(num, end=" ")