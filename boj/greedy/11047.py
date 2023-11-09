from sys import stdin

if __name__ == '__main__':
    # O(n) 정렬을 안할경우
    # O(NlogN) 정렬을 할경우

    # 그리디 (탐욕법)
    n, k = map(int, stdin.readline().split())
    costs = []

    for _ in range(n):
        cost = int(stdin.readline())
        costs.append(cost)

    cnt = 0

    # 계산하기 쉽게 내림차순으로 바꾼다.
    costs.sort(reverse=True)

    for i in range(n):
        coin = k//costs[i] # 가장 큰수부터 나눈다.
        cnt += coin # 코인의 갯수를 더해주고
        k -= coin * costs[i] # 나눠준만큼 뺀다.

    print(cnt)