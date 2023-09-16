from collections import deque

if __name__ == "__main__":

    # 인접 리스트, 딕셔너리를 사용하여 연결되어 있는 정점, vertex와의 관계를 나타낸다.
    graph = {
        "A": ["B", "D", "E"],
        "B": ["A", "C", "D"],
        "C": ["B"],
        "D": ["A", "B"],
        "E": ["A"]
    }


    def bfs(start_value):
        # 값을 넣어줄 list를 생성하고 default 값으로 start_value
        visited = [start_value]

        # BFS 탐색을 위한 queue생성, 루트 노드와 가까운 순서대로
        # queue에 들어가며, FIFO로 각 노드에 접근한다.
        # queue의 default값으로 start_value
        q = deque(start_value)

        # queue가 비어질 때 까지 반복문 실행
        while q:
            cur_value = q.popleft()

            # 그래프에 존재하는 해당 노드와 연결되어있는 값들을 탐색.
            for node in graph[cur_value]:

                # visited : 접근할 노드 또는 이미 접근한 값들이 담겨있다.
                # 해당 노드와 연결되어있는 값들이 visited 리스트에 존재하지 않으면 방문 예약 및 queue에 넣어준다.
                if node not in visited:
                    visited.append(node)
                    q.append(node)

        return visited

    # 시작 노드와 가까운 순서대로 queue에 enque되고 멀 수록 가장 마지막에 enque된다.
    # A, B, D, E, C
    result = bfs("A")
    print(result)