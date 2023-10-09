from sys import stdin
import heapq

if __name__ == '__main__':
    # n*n 리스트를 만들기 위해 n의 값을 입력받는다.
    # O(logN) >> WORST CASE : n * n * logN
    n = int(stdin.readline().strip())

    # 일차원 리스트로 값을 구성하기 priority queue로 구현하기 위한 pq
    pq = []

    # heapq 라이브러리를 이용하여 일차원 배열 pq를 priority queue로 구현해준다.
    heapq.heapify(pq)

    # n번 만큼 값을 입력받고 2차원 배열을 구현한다.
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        for i in row:
            # pq의 길이가 5미만인 경우 pq에 해당 값을 넣어준다.
            if len(pq) < n:
                # O(logN)
                heapq.heappush(pq, i)
            else :
                # pq의 길이가 5일때 들어온다.
                if i > pq[0]:
                    # 현재 들어오는 값이 우선순위가 가장 높은것 보다 크면은 제거해주고 넣어준다.
                    heapq.heappop(pq)
                    heapq.heappush(pq,i)

                    # 현재 들어오는 값이 우선 순위가 가장 높은것 보다 작은 경우
                    # 큰값을 유지해야하기 때문에 연산을 해줄 필요가 없다.
                    # 해당 로직을 수행하면 가장큰 값은 자연스럽게 인덱스 가장 마지막에 존재하고
                    # min heap에 존재하는 가장 작은값만 비교하게 된다.
    print(pq[0])


