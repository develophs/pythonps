from collections import deque

if __name__ == '__main__':
    graph = {
        "A": ["B", "C", "D"],
        "B": ["A", "G"],
        "C": ["A", "F"],
        "D": ["A", "E"],
        "E": ["D"],
        "F": ["C", "H"],
        "G": ["B"],
        "H": ["F"]
    }

    def bfs(cur_v):
        visited = [cur_v]
        q = deque(cur_v)

        while q:
            cur = q.popleft()

            for v in graph[cur]:
                if v not in visited:
                    visited.append(v)
                    q.append(v)

        return visited


    visited = []
    def dfs(cur_v):
        visited.append(cur_v)

        for v in graph[cur_v]:
            if v not in visited:
                dfs(v)

        return visited
    #print(bfs("A"))
    print(dfs("A"))
