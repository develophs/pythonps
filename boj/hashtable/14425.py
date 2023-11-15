from sys import stdin

if __name__ == '__main__':
    # [Silver4] 해시테이블 O(n)

    n, m = map(int, stdin.readline().split())
    dict = {}
    cnt = 0

    for _ in range(n):
        value = stdin.readline().rstrip()
        dict[value] = True

    for _ in range(m):
        target = stdin.readline().rstrip()

        if target in dict.keys():
            cnt += 1

    print(cnt)