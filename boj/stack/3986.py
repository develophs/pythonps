from sys import stdin

if __name__ == '__main__':
    # O(n**2) n * n
    def count():
        cnt = 0
        n = int(stdin.readline().rstrip())

        # 입력한 n의 크기만큼 n번 반복 O(n) 1 <= n <= 100
        for _ in range(n):
            stack = []
            strs = list(stdin.readline().rstrip())

            # strs의 길이만큼 반복 O(n) 모든 단어 길이의 합은 1000000을 넘지 않는다.
            # WORST CASE : 100 * 1,000,000 = 100,000,000
            for cur_data in strs:
                # O(1)
                # stack이 비어있지 않고 현재 아이템과 스택의 Last와 같은경우 아이템 제거
                if stack and stack[-1] == cur_data:
                    stack.pop()
                # stack이 비어있거나 값이 일치하지 않는경우 stack에 아이템 추가
                else:
                    stack.append(cur_data)

            # stack이 비어있는 경우 cnt + 1
            if not stack:
                cnt += 1
        return cnt

    result = count()
    print(result)