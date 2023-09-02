from sys import stdin

if __name__ == '__main__':
    nums = list(map(int, stdin.readline().split()))
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    print(sum)