from sys import stdin

if __name__ == '__main__':

    # 모든 해시테이블의 메소드들은
    # 시간복잡도 O(1)을 갖는다.
    hash_table = dict()
    t = int(stdin.readline())

    for _ in range(t):
        name, cmd = stdin.readline().split()

        if cmd == "enter":
            hash_table[name] = True
        elif cmd == "leave":
            del(hash_table[name])

    # 해시 테이블 정렬하는방법
    # 파이썬 내장함수 sorted(dict.keys())
    # 역순 정렬 sorted(dict.keys(), reverse=True)
    # 정렬된 자료구조를 리턴값으로 받아야한다!!!
    hash_table = sorted(hash_table.keys(), reverse=True)

    for name in hash_table:
        print(name)