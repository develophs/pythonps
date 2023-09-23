from sys import stdin

if __name__ == '__main__':

    # O(n)
    # Hash Table을 이용한 계산 O(1)
    # n의 수 n번 반복한다.
    # 파이썬 재귀는 1000넘어가면 에러 발생한다. stack over flow
    def fibo(n):
        memo = {
            0: 0,
            1: 1,
            2: 1
        }

        for i in range(3, n + 1):
            if i not in memo:
                memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]

    a = int(stdin.readline().strip())
    print(fibo(a))


