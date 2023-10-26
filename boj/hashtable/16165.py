from sys import stdin
from collections import defaultdict

if __name__ == '__main__':

    # 딕셔너리의 벨류가 리스트 타입이기 때문에
    # 리스트에서 멤버네임을 찾고
    # key값을 리턴해주는 메소드
    def find_group_name(mem_name):
        for key, value in memo.items():
            if value.__contains__(mem_name):
                return key

    # 해시테이블의 벨류로 리스트를 가진다.
    memo = defaultdict(list)
    n,  m = map(int, stdin.readline().split())

    # 걸그룹의 수를 n만큼 입력받는다.
    for _ in range(n):
        # 팀이름, 인원수 한줄 씩 입력받는다.
        group_name = stdin.readline().rstrip()
        group_size = int(stdin.readline())

        # 그룹의 크기만큼 멤버를 입력받는다.
        for j in range(group_size):
            member_name = stdin.readline().rstrip()
            memo[group_name].append(member_name)

    # 출력은 마지막에 한번에 해야하므로 정답을 보관할 리스트
    values = []
    for _ in range(m):
        target = stdin.readline().rstrip()
        type = int(stdin.readline())

        if type == 0:
            # 출력값이 멤버 이름일 경우 정렬이 되어서 출력되어야 하기 때문에
            # 해당로직에서 미리 정렬 후 values 배열에 추가시킨다.
            memo[target].sort()
            for name in memo[target]:
                values.append(name)
        elif type == 1:
            g_name = find_group_name(target)
            values.append(g_name)

    for item in values:
        print(item)