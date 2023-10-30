from sys import stdin

if __name__ == '__main__':
    # O(NlogN)
    # value로 숫자만을 가졌었지만, 해당 문제는 숫자, 순서, 이름을 가져야한다.
    # 튜플을 사용하면 간단하게 해결된다.
    n = int(stdin.readline())

    my_tuples = []

    for i in range(n):
        num, name = stdin.readline().rstrip().split()
        my_tuples.append((int(num), i, name))

    # 파이썬 내장함수 sort는 value가 리스트 또는 튜플일 경우
    # 인덱스 값끼리 비교. 해당 인덱스의 값이 같으면 다음 값을 비교하여 정렬한다.
    my_tuples.sort()
    
    for t_num, t_seq, t_name in my_tuples:
        print(t_num, t_name)