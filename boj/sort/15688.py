from sys import stdin

if __name__ == '__main__':
    # O(NlogN)
    # 특별한거 없이 파이썬 내장함수 sort를 사용하면 간단하게 해결된다.
    n = int(stdin.readline())

    # 파이썬 내장 함수 sort 사용
    nums = []

    for _ in range(n):
        num = int(stdin.readline())
        nums.append(num)

    nums.sort()

    for i in nums:
        print(i)