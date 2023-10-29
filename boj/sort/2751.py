from sys import stdin

if __name__ == '__main__':

    # 1 <= N <= 1,000,000 (2**20)
    # O(logN) >> 20
    n = int(stdin.readline())
    my_nums = []

    # n의 수가 100만인 경우 최대 100만번 반복
    for _ in range(n):
        my_nums.append(int(stdin.readline()))

    my_nums.sort()

    for num in my_nums:
        print(num)