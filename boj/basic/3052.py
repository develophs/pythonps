from sys import stdin

if __name__ == '__main__':
    # O(n)
    nums = [0 for _ in range(43)]

    for _ in range(10):
        n = int(stdin.readline())
        mod = n%42
        nums[mod] = 1

    count = 0
    for num in nums:
        if num != 0:
            count +=1

    print(count)