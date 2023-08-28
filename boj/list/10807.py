if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    v = int(input())
    sum = 0
    for i in range(N):
        if (nums[i] == v):
            sum += 1
    print(sum)
