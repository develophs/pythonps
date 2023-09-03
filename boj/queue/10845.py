from collections import deque
from sys import stdin

if __name__ == '__main__':
    # O(1)의 시간복잡도를 가진 popleft과 append를 입력받은 n회 반복
    # O(n)의 시간복잡도를 가진다.
    queue = deque()

    n = int(stdin.readline().strip())

    for _ in range(n):
        cmd = list(stdin.readline().split())

        if cmd[0] == "push":
            queue.append(cmd[1])
        elif cmd[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif cmd[0] == "size":
            print(len(queue))
        elif cmd[0] == "empty":
            if not queue:
                print(1)
            else:
                print(0)
        elif cmd[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif cmd[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
