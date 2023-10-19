from sys import stdin
import heapq

if __name__ == '__main__':
    # heap에 튜플을 사용하여 값을 저장한다.
    # 절대값이기 때문에 음수일경우 - 를 곱해서 저장해주고, 양수일 경우 그냥 저장한다.
    # heap에 저장된 튜플의 인덱스 0의 값이 같으면 인덱스 1의 값을 비교하여
    # 우선순위 별로 정렬한다.

    # heapq.heappush(), heapq.heappop() > O(logN)
    heap = []
    heapq.heapify(heap)

    t = int(stdin.readline())

    for _ in range(t):
        x = int(stdin.readline())

        if x == 0:
            if heap:
                abs, v = heapq.heappop(heap)
                print(v)
            else:
                print(0)
        elif x < 0:
            heapq.heappush(heap, (-x, x))
        elif x > 0:
            heapq.heappush(heap, (x, x))