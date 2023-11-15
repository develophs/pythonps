from sys import stdin

if __name__ == '__main__':
    # [Silver4] 해시테이블 O(n)
    dict = {}

    # n : 사용안함
    stdin.readline().rstrip()

    nums = list(map(int, stdin.readline().split()))

    for num in nums:
        if num in dict:
            dict[num] = dict[num] + 1
        else:
            dict[num] = 1

    # m : 사용안함
    stdin.readline().rstrip()

    targets = list(map(int, stdin.readline().split()))

    for target in targets:
        if target in dict:
            print(dict[target], end=" ")
        else:
            print(0, end=" ")