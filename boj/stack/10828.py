from sys import stdin

if __name__ == '__main__':
    # O(1)의 시간복잡도를 가진 pop과 append를 입력받은 n회 반복
    # O(n)의 시간복잡도를 가진다.
    stack = []
    n = int(stdin.readline().strip())

    for i in range(n):
        cmd = list(stdin.readline().split())

        if cmd[0] == "push":
            stack.append(cmd[1])
        elif cmd[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif cmd[0] == "size":
            print(len(stack))
        elif cmd[0] == "empty":
            if not stack:
                print(1)
            else:
                print(0)
        elif cmd[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)