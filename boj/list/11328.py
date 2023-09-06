from sys import stdin

if __name__ == '__main__':
    # O(n**2)
    # 새로 알게된 문법 : sorted() => 문자로 구성된 데이터를 정렬 후 list에 담아 리턴해준다.
    n = int(stdin.readline())

    #O(n) n에 대해 입력한 수 만큼 반복문
    for _ in range(n):
        strs = list(stdin.readline().split())

        strfry_0 = sorted(strs[0])
        strfry_1 = sorted(strs[1])

        #O(n) 문자 list에 담긴 데이터의 수 (length)만큼 반복한다.
        length = len(strfry_0)
        for i in range(length):
            if strfry_0[i] == strfry_1[i]:
                is_possible = True

            if strfry_0[i] != strfry_1[i]:
                is_possible = False
                break

        if is_possible:
            print("Possible")
        else:
            print("Impossible")

