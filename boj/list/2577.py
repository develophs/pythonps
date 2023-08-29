if __name__ == '__main__':

    A = int(input())
    B = int(input())
    C = int(input())
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    dup = A * B * C
    for i in str(dup):
        count[int(i)] += 1

    #range가 10이면 0~9까지 반복한다.
    for j in range(10):
        print(count[j])