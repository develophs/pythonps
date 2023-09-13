from sys import stdin

if __name__ == '__main__':
    # O(n**2)
    # 입력한 테이스 케이스 t * 문자열의 길이
    t = int(stdin.readline().rstrip())

    for _ in range(t):
        stack = []
        strs = list(stdin.readline().rstrip())

        for i in strs:
            if i == "(":
                stack.append("(")
            elif i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")

        if stack:
            print("NO")
        elif not stack:
            print("YES")