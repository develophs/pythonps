from sys import stdin
import heapq

if __name__ == '__main__':
    # O(logN)
    # logN의 시간복잡도를 가진 heappop(), heappush() 메소드를
    # 테스트 케이스 t번 반복한다.
    # WORST CASE : t * logN (현재 트리에 존재하는 아이템의 갯수)

    # 테스트 케이스 실행 횟수 t를 입력한다. 1 <= t <= 100,000
    t = int(stdin.readline().rstrip())

    # min heap을 구현하기 위한 default array 선언
    min_heap = []

    # default array 및 heapq 라이브러리를 이용하여 min heap을 구현
    heapq.heapify(min_heap)

    for _ in range(t):
        x = int(stdin.readline().rstrip())

        if x > 0:
            # heapq.heapush(min_heap,x) : 아이템을 추가하는 시간복잡도는 O(1)이지만
            # 트리를 재정렬 하는데 걸리는 시간복잡도는 O(logN)이다.
            # 총 시간복잡도 O(logN)
            heapq.heappush(min_heap, x)
        else:
            if min_heap:
                # heapq.heappop(min_heap) : 아이템을 제거하는 시간복잡도는 O(1)이지만
                # 트리를 재정렬 하는데 걸리는 시간복잡도는 O(logN)이다.
                # 총 시간복잡도 O(logN)
                value = heapq.heappop(min_heap)
                print(value)
            elif not min_heap:
                print(0)

