from sys import stdin

if __name__ == '__main__':
    # O(1)
    # 새로 알게된 사실
    # 파이썬의 딕셔너리는 키를 추가한 순서대로 정렬되어있다.
    waiting_list = {}
    k, waiting_count = map(int, stdin.readline().split())

    for _ in range(waiting_count):
        num = stdin.readline().rstrip()

        if num in waiting_list:
            # 해시테이블에 이미 존재하면 삭제해준다.
            del(waiting_list[num])
        # 그리고 새롭게 값을 넣어준다.
        waiting_list[num] = True

    for idx, key in enumerate(waiting_list.keys()):
        # 해당 인덱스 값이 k이면 멈춘다.
        if idx == k:
            break
        print(key)