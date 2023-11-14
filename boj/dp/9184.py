from sys import stdin

if __name__ == '__main__':
    # O(a*b*c)
    dict = {}

    def w(a, b, c):
        if (a, b, c) not in dict.keys():
            if a <= 0 or b <= 0 or c <= 0:
                dict[(a, b, c)] = 1
            elif a > 20 or b > 20 or c > 20:
                dict[(a, b, c)] = w(20, 20, 20)
            elif a < b < c:
                dict[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            else :
                dict[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

        return dict[(a, b, c)]

    while True:
        x, y, z = map(int, stdin.readline().split())
        if x == -1 and y == -1 and z == -1:
            break
        else:
            print("w({}, {}, {}) = {}".format(x, y, z, w(x, y, z)))