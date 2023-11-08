from sys import stdin

if __name__ == '__main__':
    # O(NlogN)
    nums = list(map(int, stdin.readline().rstrip()))

    reverseNums = sorted(nums, reverse=True)

    for num in reverseNums:
        print(num, end="")