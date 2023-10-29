from sys import stdin

if __name__ == '__main__':
    # 계수 정렬
    # 입력가능한 수(K)의 크기 0 부터 10000 :: 마지막 반복문이 반복 될수 있는 K번 0부터 1만까지 입력된 경우 출력을 만번한다.
    # 수를 입력하는 횟수 N :: 배열의 값을 N번 변경한다.
    # 시간복잡도 O (N+K)
    n = int(stdin.readline())

    """ 메모리 초과
    my_nums = [] 
    for _ in range(n):
       my_nums.append(int(stdin.readline()))
    
    for 문 안에서 append를 사용할 경우 메모리 재할당이 이루어져서 메모리를 효율적으로 사용하지 못한다.
    list를 미리 초기화 시켜준 후 랜덤 액세스로 값을 추가해 주는 계수 정렬로 구현한다.
    """

    # 인덱스의 크기가 입력가능한 수의 최대 크기인 10000 + 1 배열 초기화
    # 0 <= K <= 10,000
    my_nums = [0] * 10001

    # n의 수가 1000만인 경우 최대 1000만번 반복
    # 입력받은 값에 대한 인덱스의 값을 +1 해준다.
    for _ in range(n):
        idx = int(stdin.readline())
        my_nums[idx] += 1

    for i in range(10001):
        if my_nums[i] > 0:
            for j in range(my_nums[i]):
                print(i)