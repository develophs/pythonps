from sys import stdin
import heapq

if __name__ == '__main__':
    # O(logN)
    # 테스트 케이스 t
    t = int(stdin.readline())

    for _ in range(t):
        heap = []
        heapq.heapify(heap)

        # 파일의 갯수 f >> 필요없다.
        f = int(stdin.readline())

        file_list = list(map(int, stdin.readline().split()))

        # 입력받은 파일의 크기들을 heap에 push해준다.
        for file in file_list:
            heapq.heappush(heap, file)

        # 비용을 저장할 배열
        values = []

        # 오버 헤드를 막기 위해 heap의 길이는 따로 변수로 선언
        length = len(heap)
        while length > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            heapq.heappush(heap, x+y)
            values.append(x+y)
            length -= 1

        print(sum(values))