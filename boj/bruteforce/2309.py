from sys import stdin

if __name__ == '__main__':
    # O(n**2)
    heights = []
    for _ in range(9):
        height = int(stdin.readline())
        heights.append(height)

    sum_ = sum(heights)

    temp1 = 0
    temp2 = 0

    for i in range(8):
        if temp1 != 0 or temp2 != 0:
            break
        for j in range(i+1, 9):
            if sum_ - heights[i] - heights[j] == 100:
                temp1 = heights[i]
                temp2 = heights[j]
                break

    heights.remove(temp1)
    heights.remove(temp2)
    heights.sort()

    for h in heights:
        print(h)