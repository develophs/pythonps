from sys import stdin

if __name__ == '__main__':
    # O(1)의 시간복잡도를 가진 pop과 append를 입력받은 n회 반복
    # O(n)의 시간복잡도를 가진다.
    stack = []
    sum = 0
    k = int(stdin.readline().strip())

    for i in range(k):
        n = int(stdin.readline().strip())

        if n == 0:
            stack.pop()
        elif n != 0:
            stack.append(n)

    length = len(stack)
    for s in range(length):
        sum += stack[s]

    print(sum)