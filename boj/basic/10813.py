from sys import stdin

if __name__ == '__main__':
    # O(n)
    n, m = map(int, stdin.readline().split())

    nums = [z for z in range(1, n+1)]
    temp = 0
    for _ in range(m):
        i, j = map(int, stdin.readline().split())

        temp = nums[i-1]
        nums[i-1] = nums[j-1]
        nums[j-1] = temp

    for num in nums:
        print(num, end=" ")