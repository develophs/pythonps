from collections import deque
from sys import stdin

if __name__ == '__main__':
    # O(n)의 시간복잡도를 2번 수행한다. 하지만 시간복잡도는 O(n)이다.
    queue = deque()
    n = int(stdin.readline().strip())

    #O(1)인 append()를 n번 반복 > O(n)
    for i in range(n):
        queue.append(i+1)

    #O(1)인 popleft(), append()를 n-1번 반복 > O(n)
    length = len(queue)
    while length > 1:
        queue.popleft()
        sec = queue.popleft()
        queue.append(sec)

        length -= 1

    print(queue[0])
