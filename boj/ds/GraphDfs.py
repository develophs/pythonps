if __name__ == "__main__":

    # 인접 리스트, 딕셔너리를 사용하여 연결되어 있는 정점, vertex와의 관계를 나타낸다.
    graph = {
        "A": ["B", "D", "E"],
        "B": ["A", "C", "D"],
        "C": ["B"],
        "D": ["A", "B"],
        "E": ["A"]
    }

    visited = []
    # dfs는 방문한 노드에게 값의 처리를 위임한다.
    # 값의 처리를 위임하기 위해 재귀를 이용
    def dfs(start_value):
        # visited 리스트에 현재값을 넣어준다.
        visited.append(start_value)

        # 그래프의 해당 현재 값의 노드를 탐색
        for cur_v in graph[start_value]:

            # visited 리스트에 현재 노드의 값과 연결된 노드가 존재하지 않으면
            # 재귀를 이용하여 현재 노드와 연결된 노드에게 값의 처리를 위임한다.
            if cur_v not in visited:
                dfs(cur_v)

        return visited

    # A, B, C, D, E
    result = dfs("A")
    print(result)