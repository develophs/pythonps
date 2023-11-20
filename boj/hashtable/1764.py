from sys import stdin

if __name__ == '__main__':
    # O(n)
    dict = {}

    n, m = map(int, stdin.readline().split())

    for _ in range(n):
        firstName = stdin.readline().rstrip()
        dict[firstName] = False

    for _ in range(m):
        secondName = stdin.readline().rstrip()
        if secondName in dict:
            dict[secondName] = True

    sortDict = sorted(dict.items())

    cnt = 0
    trueList = []
    for key, value in sortDict:
        if value:
            cnt += 1
            trueList.append(key)

    print(len(trueList))
    for item in trueList:
        print(item)