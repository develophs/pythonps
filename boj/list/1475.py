from sys import stdin

if __name__ == '__main__':
    #O(n) : 입력한 문자열의 길이만큼 반복문을 수행한다.
    count = [0] * 10
    nums = stdin.readline().strip()

    for i in nums:
        number = int(i)
        if number == 6 or number == 9: #더 작은 수에 값을 추가하기 위해 반복문 내 조건문 추가
            if count[6] <= count[9]:
                count[6] += 1 #9의 갯수가 더 많거나 같은 경우 6의 카운트를 먼저 증가시킴
            else:
                count[9] += 1 #6이 더 많은 경우 9를 추가
        else:
            count[number] += 1
    print(max(count))
