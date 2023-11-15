from sys import stdin

if __name__ == '__main__':
    # [Silver3] 스택 O(n**2)
    # n : 필요없음
    # 문제를 제대로 읽자. 스택을 다채우고 다시 시작하는게 아닌
    # 스택에 아이템이 존재하고 타겟이면 바로바로 제거하는거다.
    int(stdin.readline())

    nums = list(map(int, stdin.readline().split()))
    stack = []

    target = 1
    while nums:
        if nums[0] == target:
            nums.pop(0)
            target += 1
        else:
            stack.append(nums.pop(0))

        while stack:
            if stack[-1] == target:
                stack.pop()
                target += 1
            else:
                break

    if stack:
        print("Sad")
    elif not stack:
        print("Nice")