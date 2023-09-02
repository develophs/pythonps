from sys import stdin

if __name__ == '__main__':
    # O(1)인 명령어 append, pop이 명령어의 갯수인 N번 반복한다.
    # 시간 복잡도 : O(n)
    stack = []

    N = int(stdin.readline())

    for i in range(N):
        command = list(map(int, stdin.readline().split()))

        if command[0] == 1:
            stack.append(command[1])
        elif command[0] == 2:
            if not stack:
                print(-1)
            else:
                print(stack.pop())
        elif command[0] == 3:
            print(len(stack))
        elif command[0] == 4:
            if not stack:
                print(1)
            else:
                print(0)
        elif command[0] == 5:
            if not stack:
                print(-1)
            else:
                print(stack[-1])