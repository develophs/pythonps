from sys import stdin

if __name__ == '__main__':
    # O(1)
    # 간단한 해시테이블 문제
    memo = {}
    n, m = map(int, stdin.readline().split())

    for _ in range(n):
        site, password = stdin.readline().rstrip().split()
        memo[site] = password

    for _ in range(m):
        target = stdin.readline().rstrip()
        print(memo[target])