from sys import stdin

if __name__ == '__main__':
    # O(NlogN) : 파이썬 정렬 내장 함수

    # 응시자수 : n , 상을 받는 사람의 수 : k
    n, k = map(int, stdin.readline().split())

    scores = list(map(int, stdin.readline().split()))

    # 내림 차순 정렬
    scores.sort(reverse=True)

    # 커트라인에 해당하는 인덱스 접근
    print(scores[k-1])