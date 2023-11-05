from sys import stdin

if __name__ == '__main__':
    # O(n) : O(1)인 딕셔너리 메소드들이 n번, m번 반복된다

    memo = {}
    n = int(stdin.readline())

    keys = list(stdin.readline().rstrip().split())

    for key in keys:
        memo[key] = True

    m = int(stdin.readline())

    nums = stdin.readline().rstrip().split()

    for idx in range(m):
        if nums[idx] in memo:
            print("1", end=" ")
        else:
            print("0", end=" ")