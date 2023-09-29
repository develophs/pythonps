from sys import stdin
import heapq

if __name__ == '__main__':
    # O(logN)
    # 테이스 케이스 T * logN(트리의 높이)
    # 테스트 케이스 t
    t = int(stdin.readline().rstrip())

    max_heap = []
    heapq.heapify(max_heap)

    for _ in range(t):
        x = int(stdin.readline().strip())

        # heapq 라이브러리는 max_heap에 대한 push 메소드가 존재하지 않는다.
        # 따라서 음수를 곱하여 value가 클수록 음수로는 가장 작은 값이 되기 때문에
        # heap안에서는 음수로 가장 작은값으로 존재하다가
        # heapq.heappop(Object)로 가장 작은 값인 아이템을 제거하고
        # 다시 음수를 곱하여 원래의 값으로 되돌린다.
        if x > 0:
            #O(logN)
            heapq.heappush(max_heap, -x)
        else :
            if max_heap:
                # O(logN)
                weight = heapq.heappop(max_heap)
                print(-weight)
            elif not max_heap:
                # O(1)
                print(0)


    # heapq 라이브러리의 기본 메소드
    # heapq.heapify(Object)
    # heapq.heappush(Object,value)
    # heapq.heappop(Object)