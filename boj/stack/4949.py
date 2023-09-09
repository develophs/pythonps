from sys import stdin

if __name__ == '__main__':
    # O(n)
    # O(1)인 메소드들이 입력된 문자열 strs의 길이만큼 수행된다.
    while True:
        strs = stdin.readline().rstrip()

        if strs == '.':
            break
        stack = []

        for value in strs:
            if value == '(':
                stack.append(value)
            elif value == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(value)
                    break
            elif value == '[':
                stack.append(value)
            elif value == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(value)
                    break
        if stack:
            print('no')
        else:
            print('yes')