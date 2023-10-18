from collections import defaultdict
from sys import stdin

if __name__ == '__main__':
    # O(n) : 1 또는 주변 노드와 연결된 노드의 수만큼 반복
    def dfs(start_node):
        # 방문한 노드들을 전부 visited에 추가한다.
        visited.append(start_node)

        for next_node in graph[start_node]:
            if next_node not in visited:
                dfs(next_node)

    graph = defaultdict(list) # 그래프를 구성할 딕셔너리
    visited = [] # 방문체크할 visited 배열
    computers = int(stdin.readline()) # 쓸모없음 버리기
    t = int(stdin.readline())

    for _ in range(t):
        key, value = list(map(int, stdin.readline().split()))
        # 틀렸던 부분 :
        # key에 해당하는 노드에만 값을 추가하는것이 아닌
        # 연결된 노드 value에도 key에 해당하는 노드를 추가시켜줘야한다.
        graph[key].append(value)
        graph[value].append(key)

    # dfs 메소드를 통해 1과 연결된 노드 탐색
    # 1 또는 1과 연결된 노드들은 전부 visited 배열에 추가되어있다.
    dfs(1)
    # 정답으로 방문한 visited에 있는 노드들의 수만 출력하면 된다.
    # 1은 제외해야하므로 -1
    print(len(visited)-1)