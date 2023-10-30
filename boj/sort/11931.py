from sys import stdin

if __name__ == '__main__':
    # O(NlogN) N : 입력되는 수의 갯수
    n = int(stdin.readline())

    nums = []

    for _ in range(n):
        num = int(stdin.readline())
        nums.append(num)

    nums.sort(reverse=True)

    for i in nums:
        print(i)