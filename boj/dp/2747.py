from sys import stdin

if __name__ == '__main__':
    # 피보나치 수열을 해시테이블을 이용하여 구현하는 방법

    memo = {
        1: 1,
        2: 1,
    }


    # 하나의 큰 상위 함수로 부터 가지치면서 내려와 값을 계산한다.
    def top_down(n):
        # 해시테이블에 존재하지 않으면 재귀를 통해 값을 계산하고
        # 해시테이블에 저장한다.
        if n not in memo:
            memo[n] = top_down(n - 1) + top_down(n - 2)

        return memo[n]

    # 차근 차근 작은 단위의 함수부터 계산하며 상위 함수의 값을 도출한다.
    def bottom_up(n):
        # base case가 존재하지 않는 3부터 n+1까지 계산.
        # range 함수는 n-1까지 계산하기 떄문에 n+1을 해줘야 n까지 계산한다.

        for i in range(3, n+1):
            if i not in memo:
                memo[i] = memo[i-1] + memo[i-2]

        return memo[n]

    a = int(stdin.readline().strip())

    print(top_down(a))
    print(bottom_up(a))

    # top_down 방식은 base case에 값이 존재하지 않으면 재귀를 통해 값을 생성하여 상위 함수의 값을 도출해야한다.
    # bottom_up 방식은 반복문을 통해 하위 함수부터 단계적으로 값을 도출하고, 결국 상위 함수의 값을 도출한다.
    # 두 방식은 값이 도출되는 순서는 실행되는 함수의 순서가 다르다.