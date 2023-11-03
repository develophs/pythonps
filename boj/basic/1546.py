from sys import stdin

if __name__ == '__main__':
    # O(n) : n 과목의 갯수
    n = int(stdin.readline())

    scores = list(map(int, stdin.readline().split()))

    max_score = max(scores)

    for i in range(n):
        scores[i] = scores[i]/max_score * 100

    print(sum(scores)/n)