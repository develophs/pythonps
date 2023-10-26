from sys import stdin

if __name__ == '__main__':
    # O(1)
    hash_table = dict()

    #포켓몬의 갯수n, 맞춰야하는갯수 m
    n, m = map(int, stdin.readline().split())

    # 1번부터 N번까지 입력받는다.
    # 하나의 입력을 받고 해당 값을 key, value로 각각 사용한다.
    for i in range(1, n+1):
        name = stdin.readline().rstrip()
        hash_table[i] = name
        hash_table[name] = i

    for _ in range(m):
        value = stdin.readline().rstrip()

        # 새로 알게된 메소드 str.isdigit()
        # 문자열이 모든 숫자인지 판단한다. 0과 양수만 가능. 음수인경우 불가능하다.
        # 모든 문자열이 숫자인 경우 True, 한개라도 문자인경우 False
        if value.isdigit():
            print(hash_table[int(value)])
        else:
            print(hash_table[value])