from sys import stdin

if __name__ == '__main__':
    # O(n**2)

    myList = []
    row = 5
    for _ in range(row):
        strs = list(stdin.readline().rstrip())
        myList.append(strs)

    # 행을 먼저 증가시키고, 그 후 열의 크기를 증가시킨다.
    # 열의 최대길이는 15이고, 현재 행의 길이가 열의 크기보다 큰경우에만 출력한다.
    for i in range(15):
        for j in range(row):
            if len(myList[j]) > i :
                print(myList[j][i], end="")