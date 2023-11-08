from sys import stdin

if __name__ == '__main__':
    # 재귀 : O(2**n) >> f(5)는 하위함수 f(4),f(3)... 함수들이 2개씩 불러온다.
    # dp : O(n)
    recursionCount = 0

    def recursion(n):
        global recursionCount

        if n == 1 or n == 2:
            recursionCount += 1
            return 1

        return recursion(n - 1) + recursion(n - 2)

    dpCount = 0
    memo = {1: 1, 2: 1}

    # 탑 다운
    # def dp(n):
    #     global dpCount
    #
    #     if n not in memo:
    #         dpCount += 1
    #         memo[n] = dp(n-1) + dp(n-2)
    #
    #     return memo[n]

    # 바텀 업 >>> 백준 Python으로 하는경우 시간초과
    def dp(n):
        for i in range(3, n + 1):
            global dpCount
            if i not in memo:
                dpCount += 1
                memo[i] = memo[i - 1] + memo[i - 2]

    target = int(stdin.readline())

    recursion(target)
    dp(target)

    print(recursionCount, dpCount)
