from sys import stdin

if __name__ == '__main__':
    # O(n**3)
    
    n, m = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))

    max = 0
    for i in range(n-1):
        for j in range(i+1, n):
            for z in range(j+1, n):
                curValue = nums[i] + nums[j] + nums[z]
                if max < curValue <= m:
                    max = curValue
    print(max)