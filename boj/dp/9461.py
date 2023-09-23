from sys import stdin

if __name__ == '__main__':
    # O(n)
    memo = {
        1:1,
        2:1,
        3:1,
        4:2,
        5:2
    }
    def pado(n: int):
        if n not in memo:
            memo[n] = pado(n-2) + pado(n-3)
        return memo[n]

    t = int(stdin.readline().strip())
    for i in range(t):
        a = int(stdin.readline().strip())
        print(pado(a))