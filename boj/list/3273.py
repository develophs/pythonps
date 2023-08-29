if __name__ == '__main__':
    # O(NlogN)
    count = 0
    n = int(input())
    num = list(map(int, input().split()))
    target = int(input())

    num.sort() # O(NlogN)
    l, r = 0, len(num) - 1
    while l < r: #O(N)
        if num[l] + num[r] < target: #O(1)
            l += 1
        elif num[l] + num[r] > target: #O(1)
            r -= 1
        elif num[l] + num[r] == target: #O(1)
            count += 1
            l += 1
            r -= 1
        # 양끝을 더한 후 target인 경우 인덱스를 하나씩 증감시켜준다.
        # 정렬되어있기 때문에 이미 target과 동등하면
        # 해당 인덱스들로 더 이상 target을 구할 수 없다.
    print(count)


