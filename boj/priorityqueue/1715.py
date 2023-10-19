import heapq
from sys import stdin

if __name__ == '__main__':
    # 가장 작은 수부터 더해가며 값을 구해야한다.
    # 비교한 횟수들을 저장해가며 새롭게 더하고, 다시 heap에 push 해준다.
    # O(logN)
    heap = []
    heapq.heapify(heap)

    # 합계를 저장할 배열
    values = []
    t = int(stdin.readline())

    for _ in range(t):
        x = int(stdin.readline())
        heapq.heappush(heap, x)

    # heap에 숫자가 1개 남을때 까지만 반복한다.
    # heap에 남아있는 아이템이 1개인 경우 더이상 비교할 필요가 없다.
    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)

        heapq.heappush(heap, x+y)
        values.append(x+y)

    # 파이썬 내장함수 sum() : 배열에 존재하는 아이템들의 값들을 더해준다.
    print(sum(values))