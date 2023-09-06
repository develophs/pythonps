from collections import deque
from sys import stdin

if __name__ == '__main__':
    #O(1)인 메소드들을 n번 반복하므오 O(n)
    n = int(stdin.readline())
    deque = deque()

    for _ in range(n):
        cmd = list(stdin.readline().split())

        if cmd[0] == "push_front":
            deque.appendleft(cmd[1])
        elif cmd[0] == "push_back":
            deque.append(cmd[1])
        elif cmd[0] == "pop_front":
            if not deque:
                print(-1)
            else:
                print(deque.popleft())
        elif cmd[0] == "pop_back":
            if not deque:
                print(-1)
            else:
                print(deque.pop())
        elif cmd[0] == "size":
            print(len(deque))
        elif cmd[0] == "empty":
            if not deque:
                print(1)
            else:
                print(0)
        elif cmd[0] == "front":
            if not deque:
                print(-1)
            else:
                print(deque[0])
        elif cmd[0] == "back":
            if not deque:
                print(-1)
            else:
                print(deque[-1])