from sys import stdin

if __name__ == '__main__':
    # O(n)
    nums = [0 for _ in range(30)]

    for _ in range(28):
        idx = int(stdin.readline())
        nums[idx-1] = 1

    for i in range(30):
        if nums[i] == 0:
            print(i+1)