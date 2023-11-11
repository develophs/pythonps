from sys import stdin

if __name__ == '__main__':
    # O(n)
    def factorial(num):
        if num == 1 or num == 0:
            return 1
        return num * factorial(num-1)

    n = int(stdin.readline())
    print(factorial(n))