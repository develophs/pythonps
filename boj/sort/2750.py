from sys import stdin

if __name__ == '__main__':

    # O(NlogN)
    # 숫자를 추가하는것은 O(1)이므로 거의 무시된다.
    # 파이썬 내장 정렬알고리즘의 시간 복잡도는 O(NlogN)이다.
    n = int(stdin.readline())
    my_nums = []
    for _ in range(n):
        my_nums.append(int(stdin.readline()))

    my_nums.sort()

    for num in my_nums:
        print(num)