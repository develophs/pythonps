from sys import stdin

if __name__ == '__main__':
    # O(1)

    s = stdin.readline().rstrip()
    idx = int(stdin.readline())
    print(s[idx - 1])